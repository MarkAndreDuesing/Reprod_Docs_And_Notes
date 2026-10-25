# TTS Runbook: Making Paper MP3s Without Claude Code

Everything needed to continue the text-to-speech work on any computer (or
with any assistant) using only this repository. The plan and conventions are
in `tts-plan-template.md`; this file is the hands-on part.

## 1. Set up (once)

```bash
# system tools
sudo apt install ffmpeg poppler-utils        # macOS: brew install ffmpeg poppler
# python packages (Python 3.13 was used)
python3 -m venv .venv && source .venv/bin/activate
pip install -r templates/tools/requirements.txt
# voice models (not stored in git: 60–115 MB each), into a folder of your choice
mkdir -p ~/piper-voices && cd ~/piper-voices
python3 -m piper.download_voices en_GB-alba-medium en_GB-jenny_dioco-medium \
  en_GB-northern_english_male-medium en_GB-semaine-medium en_GB-vctk-medium
# German, for later: de_DE-thorsten-high
```

Models come from Hugging Face (`rhasspy/piper-voices`). The voice lists name
the model each voice needs (`model` column); multi-speaker models (`vctk`,
`aru`, `semaine`) also need the `speaker` column.

## 2. Make the listening script

1. Extract text page by page:
   `for p in $(seq 1 N); do echo "@@PAGE $p"; pdftotext -f $p -l $p paper.pdf -; done > raw.txt`
2. First-pass clean-up:
   `python3 templates/tools/clean_pdf_text.py raw.txt clean.txt --header-regex '^Page \d+ of \d+'`
3. Manual pass, following `tts-plan-template.md` (steps 2–5):
   - order and split into tracks as in the week's `reading-guide.md`;
   - add a `### NN | file-stem | title | pages` header per track;
   - spoken signposts at the start and end of each track, every skip announced;
   - replace tables, figures and formulas with a short description plus page;
   - spell out abbreviations (e.g. "I C S E"), "per cent", participant numbers.
   `templates/tools/examples/build_script_timperley_2021.py` shows how this
   was scripted for one paper. Finished scripts: `Vorl_*/audio/scripts/*.txt`.

## 3. Generate MP3s

```bash
cd Vorl_N/audio
# one voice (final listening version)
python3 ../../templates/tools/tts_generate.py scripts/<paper>.txt out \
  --voice en_GB-alba-medium --models ~/piper-voices --album Vorl_N
# a speaker of a multi-speaker model, with its calibration factor from the voice list
python3 ../../templates/tools/tts_generate.py scripts/<paper>.txt out \
  --voice en_GB-vctk-medium --speaker p240 --voice-scale <length_scale> --models ~/piper-voices
# voice test: spread the paper over a voice list (writes segments.csv)
python3 ../../templates/tools/tts_generate.py scripts/<paper>.txt voice-test-roundN \
  --voices voices-roundN.csv --models ~/piper-voices
```

- `--speed 1.0` is the preferred pace (0.9× Piper's normal rate, `BASE_PACE`
  in `tts_generate.py`). Any value works, e.g. `--speed 1.05`.
- Even out a voice list: `calibrate_voices.py voices.csv` before the first run;
  after a run, `refine_calibration.py voices.csv out/segments.csv`, then generate again.
- One merged file: `ls out/*.mp3 | sed "s/^/file '/;s/$/'/" > list.txt && ffmpeg -f concat -safe 0 -i list.txt -c copy full.mp3`

## 4. Rating sheets

`Vorl_*/audio/voice-test*/index.html` are self-contained pages that play the
MP3s next to them. They work when the folder is opened locally in a browser or
served by any static host (e.g. GitHub Pages, `python3 -m http.server`). Ratings
are kept in the browser only: use the export button and save the result as
`ratings-roundN.csv` in the repo. A new round's page is made by copying the last
one and replacing `TRACKS`, `SEG` (from `segments.csv` + voice list), `ROUND1`
(previous ratings) and the storage key.

The published copies on claude.ai are listed in each week's `audio/tts-plan.md`;
they are conveniences, the repo holds the sources.

## 5. Where the state is

| What | File |
|------|------|
| All voices with sex/accent and calibration | `Vorl_1/audio/voice-test/voices.csv` |
| Ratings per round | `Vorl_1/audio/voice-test/ratings-round1.csv`, `Vorl_1/audio/voice-test-round2/ratings-round2.csv` (round 3: export still to be added) |
| Current shortlist (refined calibration) | `Vorl_2/audio/voices-round4.csv` (same voices as round 3) |
| Plans, track lists, sheet links | `Vorl_1/audio/tts-plan.md`, `Vorl_2/audio/tts-plan.md` |
| Scripts, MP3s, timestamps | `Vorl_*/audio/scripts/`, `Vorl_*/audio/voice-test*/` |
