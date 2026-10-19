#!/usr/bin/env python3
"""Generate MP3 tracks from a cleaned TTS script with Piper.

Script format (see templates/tts-plan-template.md):
    ### <track no> | <file stem> | <title> | <pages>
    paragraph text ...

Usage:
    # one voice for everything
    tts_generate.py SCRIPT OUTDIR --voice en_GB-alba-medium [--speaker ID]
    # spread the text over a list of voices (voice test), sentence boundaries only
    tts_generate.py SCRIPT OUTDIR --voices voices.csv

Speed: voices.csv may carry a per-voice `length_scale` (from calibrate_voices.py) so all
voices speak at about the same rate; --speed then sets the overall pace in fine steps.

Needs: pip install piper-tts; ffmpeg; voice models in --models (downloaded with
`python3 -m piper.download_voices <model>`).
Writes OUTDIR/<file stem>.mp3 per track and, with --voices, OUTDIR/segments.csv
(voice no, model, speaker, track, start/end in seconds, first words).
"""
import argparse
import csv
import json
import re
import subprocess
import tempfile
import wave
from pathlib import Path

from piper import PiperVoice, SynthesisConfig

RATE = 22050
SENTENCE_GAP = 0.35   # seconds between sentences
PARAGRAPH_GAP = 0.8   # seconds between paragraphs


def parse_script(path):
    tracks = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            no, stem, title, pages = [p.strip() for p in line[4:].split("|")]
            tracks.append({"no": no, "stem": stem, "title": title, "pages": pages, "paras": []})
        elif line.strip():
            tracks[-1]["paras"].append(line.strip())
    return tracks


def split_sentences(para):
    # split after . ? ! or : followed by a space and a capital letter or digit
    parts = re.split(r"(?<=[.?!])\s+(?=[A-Z0-9])", para)
    return [p for p in parts if p]


class Voices:
    def __init__(self, models_dir):
        self.dir = Path(models_dir)
        self.cache = {}

    def get(self, model):
        if model not in self.cache:
            onnx = self.dir / f"{model}.onnx"
            if not onnx.exists():
                subprocess.run(["python3", "-m", "piper.download_voices", model,
                                "--data-dir", str(self.dir)], check=True)
            self.cache[model] = PiperVoice.load(str(onnx))
        return self.cache[model]

    def speaker_id(self, model, speaker):
        if not speaker:
            return None
        meta = json.loads((self.dir / f"{model}.onnx.json").read_text())
        return meta["speaker_id_map"][speaker]


def synth(voices, model, speaker, text, length_scale, tmp):
    """Return mono 16-bit PCM bytes at RATE for one sentence."""
    voice = voices.get(model)
    raw = Path(tmp) / "s.wav"
    with wave.open(str(raw), "wb") as w:
        voice.synthesize_wav(text, w, syn_config=SynthesisConfig(
            speaker_id=voices.speaker_id(model, speaker), length_scale=length_scale))
    out = Path(tmp) / "r.raw"
    subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(raw),
                    "-ar", str(RATE), "-ac", "1", "-f", "s16le", str(out)], check=True)
    return out.read_bytes()


def silence(sec):
    return b"\x00\x00" * int(RATE * sec)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("outdir")
    ap.add_argument("--voice", default="en_GB-alba-medium")
    ap.add_argument("--speaker", default="")
    ap.add_argument("--voice-scale", type=float, default=1.0,
                    help="calibration length_scale for --voice (from voices.csv)")
    ap.add_argument("--voices", help="CSV with columns no,model,speaker (voice test)")
    ap.add_argument("--models", default="/tmp/piper-voices")
    ap.add_argument("--speed", type=float, default=1.0,
                    help="overall speed, any value, e.g. 1.08 = 8 %% faster, 0.95 = 5 %% slower")
    ap.add_argument("--album", default="")
    ap.add_argument("--bitrate", default="48k")
    a = ap.parse_args()

    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    Path(a.models).mkdir(parents=True, exist_ok=True)
    voices = Voices(a.models)
    tracks = parse_script(a.script)

    # sentence list: (track index, paragraph end?, text)
    sents = []
    for ti, t in enumerate(tracks):
        for para in t["paras"]:
            s = split_sentences(para)
            for i, x in enumerate(s):
                sents.append((ti, i == len(s) - 1, x))

    # assign a voice to every sentence
    if a.voices:
        with open(a.voices) as f:
            vlist = list(csv.DictReader(f))
        words = [len(x.split()) for _, _, x in sents]
        total = sum(words)
        per = total / len(vlist)
        assign, cum = [], 0
        for w in words:
            assign.append(min(int(cum / per), len(vlist) - 1))
            cum += w
    else:
        vlist = [{"no": "1", "model": a.voice, "speaker": a.speaker,
                  "length_scale": a.voice_scale}]
        assign = [0] * len(sents)

    segments = []
    with tempfile.TemporaryDirectory() as tmp:
        for ti, t in enumerate(tracks):
            pcm = bytearray()
            cur = None
            for (sti, para_end, text), vi in zip(sents, assign):
                if sti != ti:
                    continue
                if vi != cur:
                    if segments and segments[-1]["track"] == t["stem"] and cur is not None:
                        segments[-1]["end"] = len(pcm) / 2 / RATE
                    v = vlist[vi]
                    segments.append({"voice_no": v["no"], "model": v["model"],
                                     "speaker": v.get("speaker", ""), "track": t["stem"],
                                     "start": len(pcm) / 2 / RATE, "end": None,
                                     "first_words": " ".join(text.split()[:8])})
                    cur = vi
                v = vlist[vi]
                # per-voice calibration (voices.csv column length_scale) evens out speaking rates
                ls = float(v.get("length_scale") or 1.0) / a.speed
                pcm += synth(voices, v["model"], v.get("speaker", ""), text, ls, tmp)
                pcm += silence(PARAGRAPH_GAP if para_end else SENTENCE_GAP)
            segments[-1]["end"] = len(pcm) / 2 / RATE
            raw = Path(tmp) / "track.raw"
            raw.write_bytes(bytes(pcm))
            mp3 = out / f"{t['stem']}.mp3"
            subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y",
                            "-f", "s16le", "-ar", str(RATE), "-ac", "1", "-i", str(raw),
                            "-b:a", a.bitrate,
                            "-metadata", f"title={t['no']} {t['title']} ({t['pages']})",
                            "-metadata", f"album={a.album}",
                            "-metadata", f"track={int(t['no'])}", str(mp3)], check=True)
            print(f"{mp3}  {len(pcm) / 2 / RATE / 60:.1f} min")

    if a.voices:
        with open(out / "segments.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(segments[0]))
            w.writeheader()
            for s in segments:
                s["start"], s["end"] = round(s["start"], 1), round(s["end"], 1)
                w.writerow(s)


if __name__ == "__main__":
    main()
