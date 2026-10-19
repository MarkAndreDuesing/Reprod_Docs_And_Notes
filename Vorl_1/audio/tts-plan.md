# TTS Plan – Vorl_1

Follows `templates/tts-plan-template.md`. Script: `scripts/collberg-proebsting-2016.txt`.

## Paper 1: Collberg & Proebsting (2016) – voice test

Read in full by **110 voices in turn** (all British-English Piper voices,
American-accent VCTK speakers excluded), about 14 s each, split at sentence
boundaries only. No spoken voice labels; use the timestamps in
`voice-test/segments.csv` or the rating sheet.

- Rating sheet: https://claude.ai/artifact/VK6CpHNqtLzefAe5mkxyFc (private) – source `voice-test/index.html`
- Voice list: `voice-test/voices.csv` (accent labels are approximate)

| Track | File | Block | Pages (journal) | Content / skips | Non-audio items |
|-------|------|-------|-----------------|-----------------|-----------------|
| 01 | `collberg-01-survey.mp3` | Survey | 62–63, 69 | Standfirst, key insights, **jump to Discussion** | – |
| 02 | `collberg-02-introduction-and-study.mp3` | Full read | 62–65 | Anecdote, definitions, study, background, study process | Table 1 (p. 64) |
| 03 | `collberg-03-results.mp3` | Results | 65–68 | Rates A/B/C, funding, industry, versions, author quotes | Formulas (p. 65), summary figure + Table 2 (p. 67) |
| 04 | `collberg-04-recommendations.mp3` | Recommendations | 68–69 | Funding, sharing contracts, licensing; Discussion skipped (heard in 01); references and bios skipped | Table 3 (p. 68), example contract (p. 69) |

Total about 26 min.

## Paper 2: Heumüller et al. (2020) – voice test round 2

Read in full by the **61 voices rated good or medium in round 1**
(`voice-test/ratings-round1.csv` → `voices-round2.csv`), in the reading-guide order.
Snippets are balanced by speaking time (61–80 s per voice, median 68 s) and
speaking rates were re-calibrated on this paper (`refine_calibration.py`).

- Rating sheet: https://claude.ai/artifact/6dpKMadUVpXQMumpyYnyQs (private) – source `voice-test-round2/index.html`, starts from round-1 ratings

| Track | File | Block | PDF pages | Content / skips | Non-audio items (page) |
|-------|------|-------|-----------|-----------------|------------------------|
| 01 | `heumueller-01-survey.mp3` | Survey | 1–4, 27 | Abstract, §1, **jump to §8**, list of figures/tables | – |
| 02 | `heumueller-02-background.mp3` | Guidelines | 4–8 | §2 | Table 1 (5) |
| 03 | `heumueller-03-method.mp3` | Method | 8–13 | §3; formulas spoken in words | ARC formula (9), Jaccard (10), Table 2 (11), example URLs (12–13) |
| 04 | `heumueller-04-results.mp3` | Results | 13–21 | §4; statistics simplified | Figs. 1–2 (14), Table 3 (15), Fig. 3 (16), Fig. 4 (17), Fig. 5 (18), Figs. 6–8 (19–20), Cliff's δ (20), Table 4 (21) |
| 05 | `heumueller-05-discussion-and-threats.mp3` | Discussion & threats | 21–25 | §5, §6 | – |
| 06 | `heumueller-06-related-work.mp3` | Related work | 25–27 | §7; §8 skipped (heard in 01); references, licence, author details skipped | – |

Total about 69 min.
