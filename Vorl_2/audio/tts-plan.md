# TTS Plan – Vorl_2

Follows `templates/tts-plan-template.md`. Script: `scripts/timperley-et-al-2021.txt`.

## Timperley et al. (2021) – voice test round 3

Read in full by the **28 voices rated good or medium in round 2**
(`voices-round3.csv`, copied from `Vorl_1/audio/` and refined on this paper),
in the reading-guide order of `Vorl_2/reading-guide.md`.

- **Speed:** the user's preferred pace (previously 0.9× in the player) is now
  the baseline 1.0×; generated with that pace (`BASE_PACE = 0.9` in
  `templates/tools/tts_generate.py`).
- **Balance:** 3.3–3.8 min per voice (median 3.5 min), sentence boundaries only;
  speaking rates refined on this paper (spread before refinement 0.85–1.13).
- Rating sheet: https://claude.ai/artifact/Mi2N2Lnt5dYyjRVZkeecBv (private) – source
  `voice-test-round3/index.html`, starts from round-2 ratings.

| Track | File | Block | Pages | Content / skips | Non-audio items (page) |
|-------|------|-------|-------|-----------------|------------------------|
| 01 | `timperley-01-survey.mp3` | Survey | 1–3, 37–38 | Abstract, §1, **jump to §8**, list of figures/tables | – |
| 02 | `timperley-02-background.mp3` | Background | 3–6 | §2 (artifacts, ACM badges, DoI, IS) | – |
| 03 | `timperley-03-method.mp3` | Method | 6–11 | §3 incl. threats to validity §3.5 | Fig. 1 (7), Tables 1–2 (8) |
| 04 | `timperley-04-results.mp3` | Results | 11–24 | §4, challenges C1–C12 | Fig. 2, Table 3 (12), Table 4 (14–15), Table 5 (19), Fig. 3 (20), Fig. 4 (21, with the 26.33 % note) |
| 05 | `timperley-05-secondary-analysis.mp3` | Secondary analysis | 24–28 | §5 | Fig. 5 (26) |
| 06 | `timperley-06-recommendations.mp3` | Recommendations | 28–35 | §6, R1–R8 | Table 6 (29–30) |
| 07 | `timperley-07-related-work.mp3` | Related work | 35–37 | §7; §8 skipped (heard in 01); ethics declaration, references, author details skipped | – |

Total about 99 min.

Not yet done: Hermann et al. (2020), `3368089.3409767.pdf`.
