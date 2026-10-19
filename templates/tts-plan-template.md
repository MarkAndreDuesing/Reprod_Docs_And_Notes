# Text-to-Speech (TTS) Plan (Template)

How to turn lecture papers into MP3s you can listen to, to lighten the reading load.
Copy this file to `Vorl_N/audio/tts-plan.md`, fill in the per-week section and
generate the audio from it.

## Requirements

- **Language/accent:** British English for English papers; German voice for
  German material.
- **Format:** MP3.
- **Order:** follow the time plan in the week's `reading-guide.md`, not the
  paper's page order.
- **Skips announced:** whenever the audio jumps or leaves something out, say so
  (e.g. "Skipping section 2.3, related work, pages 25 to 27. Continuing with…").
- **Non-audio content** (tables, figures, formulas, code, long lists of numbers):
  don't read it raw. Give a short spoken description and **always cite the page**
  so you can look it up in the PDF
  (e.g. "Table 3 on page 15 lists linked and available artifacts per year; in
  short, …").

## Tooling

| Item | Choice | Notes |
|------|--------|-------|
| Engine | [Piper](https://github.com/OHF-Voice/piper1-gpl) (`pip install piper-tts`) | Free, offline, runs in the cloud session. Clear but noticeably synthetic voice |
| British English voice | `en_GB-cori-high` (default), alternative `en_GB-alba-medium` | Download: `python3 -m piper.download_voices <voice>` |
| German voice | `de_DE-thorsten-high` | For future German material |
| Conversion | `ffmpeg` (WAV → MP3, ~64 kbit/s mono is enough for speech) | Also joins chunks and adds short pauses |
| Speed | Piper `--length-scale` (1.0 = normal, 0.9 ≈ 10 % faster) | Pick after a test clip |

## Steps

1. **Extract text** from the PDF (`pdftotext`, page by page so page numbers
   stay known).
2. **Clean the text** for listening:
   - remove running headers/footers, page numbers, journal banners, line-break
     hyphenation
   - remove or shorten in-text citations, e.g. "(Wohlin et al. 2012)" → dropped,
     reference numbers like "¹⁹" → dropped
   - drop footnote markers; read important footnotes inline ("Footnote: …")
   - expand symbols and abbreviations that TTS reads badly: "%" → "per cent",
     "e.g." → "for example", "i.e." → "that is", "RQ1" → "research question one",
     "≈" → "about", "δ" → "delta", URLs → "a link given in the paper"
   - keep British spelling as in the source; don't rewrite content
3. **Replace non-audio content** with a spoken description plus page number.
   Rule: one or two sentences on what it shows and the key takeaway.
4. **Order and split into tracks** following the reading guide. One MP3 per
   reading block; name files so they sort correctly:
   `<paper-short>-<NN>-<block>.mp3`, e.g. `heumueller-03-method.mp3`.
5. **Add spoken signposts** at the start of each track:
   - paper, block name, pages covered ("Heumüller et al., block 3, methodology,
     pages 8 to 12")
   - announce every skip or reordering
   - end of track: "End of block 3. Next: results."
6. **Generate** WAV per track with Piper, convert to MP3 with ffmpeg, set ID3
   tags (title, album = `Vorl_N`, track number).
7. **Spot-check** each track: listen to the start, one description of a
   table/figure and the end. Fix pronunciation issues in the cleaned text and
   regenerate.
8. **Save** to `Vorl_N/audio/` together with the cleaned scripts
   (`scripts/<track>.txt`) so the audio can be regenerated or corrected.
   Commit and push.

## Script format and generator

Cleaned scripts are plain text, one paragraph per line, with a header line per track:

```
### 01 | collberg-01-survey | Survey: standfirst, key insights and discussion | pp. 62–63, 69
Track one: survey. …
```

Generate with `templates/tools/tts_generate.py`:

```
python3 templates/tools/tts_generate.py <script.txt> Vorl_N/audio --voice en_GB-alba-medium --album Vorl_N
```

## Voice test (optional, to pick voices)

Spread one paper over many voices to compare them on real content:

- Use all candidate voices from a `voices.csv` (`no,model,speaker,sex,accent`);
  leave out accents you don't want (e.g. American VCTK speakers).
- Split at **sentence boundaries only**, about equal text per voice.
- **No spoken voice labels**; the generator writes `segments.csv` with start/end
  timestamps per voice and track.
- Rate on the rating sheet page (audio player, highlighted current voice,
  bad/medium/good per voice, keys 1/2/3, export as Markdown or CSV).
  First used in `Vorl_1/audio/voice-test/`.
- `--voices voices.csv` switches the generator to this mode.
- Round 2: read the next paper only with the shortlisted voices.

## Content options (choose per paper)

- **Full text:** everything in the reading-guide order (default for papers you
  must discuss in depth).
- **Selected sections:** abstract, method, results, discussion only.
- **Spoken summary:** a short narrated summary instead of the full text.
- **Discussion notes:** audio version of `discussion/*.md` to listen to before
  the seminar.

Always skip: references, acknowledgements, author addresses, licence text.

## Limitations

- Synthetic voice: understandable, not audiobook quality.
- PDF extraction can garble multi-column layouts and tables, so cleaning
  needs a manual check.
- Formulas and statistics get simplified in speech; the PDF stays the
  reference.

## Per-week plan (fill in)

| Track | Paper | Reading-guide block | Pages | Content / skips | Non-audio items (page) |
|-------|-------|---------------------|-------|-----------------|------------------------|
| 01 | | | | | |

Voice: `en_GB-cori-high` · Speed: 1.0 · Output: `Vorl_N/audio/`

---

## Notes for the future (not used yet)

**Claude plugins (Anthropic directory):**
- **Potion:** private podcast feed. Subscribe once in any podcast app; the
  generated MP3s show up as episodes (resume position, offline on phone).
- **read-aloud** (community): reads Claude's *replies* aloud with system voices
  or premium voices (ElevenLabs, OpenAI, Speechify; own API key). Needs a
  local Claude Code session, not the cloud one.

**Outside Claude:**
- **ElevenLabs Reader**, **Speechify**, **NaturalReader**: apps that read PDFs
  directly, with more natural voices.
- **Microsoft Edge "Read aloud":** free, good neural voices, reads PDFs.
- **NotebookLM "Audio Overview":** podcast-style two-voice discussion of
  uploaded papers (a summary, not the full text).
