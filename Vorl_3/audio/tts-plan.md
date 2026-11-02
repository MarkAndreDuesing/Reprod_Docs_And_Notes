# TTS Plan – Vorl_3

Follows `templates/tts-plan-template.md`. No reading guide exists yet for these
papers, so tracks follow the usual order: survey (abstract, introduction, jump to
the conclusion, figure and table overview), then the paper's sections in order,
with skips announced. Both PDFs are two-column; text was extracted column by
column (`pdftotext -x/-y/-W/-H`), see `templates/tools/examples/build_*.py`.

Both rounds use the **22 voices from round 3** (`voices-round5.csv` /
`voices-round6.csv`, each re-refined on its paper), in a **mixed order** (models
spread, sex and accent alternating) with a **3-second pause** at every voice
change. Pace 1.0 = preferred pace. Ratings start from round-3 ratings.

## Round 5: Olszewski et al. (2023), `3576915.3623130.pdf`

Rating sheet: https://claude.ai/artifact/KxtPttGLgBYWJM6CZsnnW1 (private), source `voice-test-round5/index.html`.
About 2.7 min per voice, 62 min audio plus pauses (about 21 MB).

| Track | Block | Pages | Notes |
|---|---|---|---|
| 01 | Survey | 1–2, 12 | Abstract, §1, **jump to §10**, figure/table overview |
| 02 | Background | 2–3 | §2 (NAS definitions), §3 null hypothesis; Fig. 1 (3) |
| 03 | Method | 3–5 | §4; Table 1 (4) |
| 04 | Indirect study | 5–7 | §5; Figs. 2–3 (5), 4–5 (6) |
| 05 | Direct study | 7–10 | §6; Figs. 6 (7), 7 (8), 8 (9), 9 (10) |
| 06 | Recommendations & limitations | 10–12 | §7, §8 |
| 07 | Related work | 12 | §9; §10 skipped (heard in 01); references and appendix pp. 13–27 skipped |

## Round 6: Winter et al. (2022), `3540250.3549172.pdf`

Rating sheet: https://claude.ai/artifact/R7agbVYyToo2jNPmZnXpQx (private), source `voice-test-round6/index.html`.
About 2.6 min per voice, 59 min audio plus pauses (about 20 MB).

| Track | Block | Pages | Notes |
|---|---|---|---|
| 01 | Survey | 1–2 | Abstract, §1, the five boxed findings, figure/table overview (no conclusion section; §10 discussion read in 06) |
| 02 | Background & subjects | 1–4 | §2, §3; Figs. 1–2 (2), 3 (4) |
| 03 | RQ1 visibility | 4–5 | §4; Tables 1–2 (5) |
| 04 | RQ2 availability | 5–8 | §5; Table 3 (6), Table 4 + Fig. 4 (7) |
| 05 | RQ3–RQ5 | 8–10 | §6–8; Tables 5 (8), 6 (9), 7 (10) |
| 06 | Threats & discussion | 10–11 | §9, §10; references skipped |
