# Olszewski, Lu, Stillman, Warren, Kitroser, Pascual, Ukirde, Butler & Traynor (2023): Condensed Notes

_Page numbers are printed proceedings pages (3433–3459 = PDF pages 1–27). The body ends on
p. 3444; pp. 3445–3459 are references and the paper list (Appendix A.1)._

## Core claims
- Security research could easily be computationally reproducible, but nobody has measured whether it is (pp. 3433–3434).
- In ML security papers at the four Tier 1 venues, 2013–2022: **60 % provide no code**, and **56 % of provided artifacts do not run**; only **20 %** reproduce the claimed results (p. 3434, p. 3439).
- **No statistically significant difference** in code availability before vs. after AECs were introduced (2020); p = 0.068 (p. 3441). The authors conclude AECs "have yet to achieve their intended goals" (p. 3434).
- Yet artifacts submitted to USENIX's AEC appear to work more often (anecdotal, Fig. 8, p. 3441).
- "Just make code available" is not enough; five common problems must be fixed (p. 3444).

## Key definitions (§2.1, p. 3434)
- The paper uses the **National Academies (NAS 2019)** definitions, not ACM's 2020 ones.
  - **Computational reproducibility:** an independent team gets consistent results with the same data, environment and code. **Bit-wise reproducibility** = exact numbers; relaxed for ML.
  - **Replicability:** same research question, different methods and new data.
  - **Generalizability:** do the trends hold in other environments?
- **Mapping to the lecture's 2020 ACM terms:** NAS reproducibility (independent team, authors' code and data) = ACM 2020 **reproducibility**. NAS replicability (new data/method) ≈ ACM 2020 **replicability**. Generalizability has no ACM badge.
- **Indirect study:** checks whether method, data and code are *available*. **Direct study:** runs the code to recreate results (p. 3434).
- Footnote 1 (p. 3434): bugs in the code propagate; correctness is not checked.
- **USENIX badges (2023):** Available, Functional, Reproduced (p. 3435).
- **AECs in security:** WiSec and ACSAC 2017; **USENIX Security 2020**; **CCS 2023**; NDSS and IEEE S&P none at writing time (p. 3435).

## Null hypothesis (§3, p. 3435)
- H0: "There is no difference in whether code from published papers is available before vs after the introduction of AECs to Tier 1 Security Conferences (2020)."
- The paper adopts the "post p < 0.05" view: 0.005 < p < 0.05 is only "suggestive", p < 0.005 "begins to indicate" significance.

## Study method
- **Sample (§4.1, p. 3435):** every main-track paper at CCS, IEEE S&P, NDSS and USENIX Security 2013–2022 that (1) mentions ML in a main section, (2) trains a model on data, and (3) reports a new ML metric. Two reviewers per year; **union** of their lists → **744 papers**.
- **Indirect study (§4.2, pp. 3435–3436, Table 1):** each paper coded twice; Cohen's κ = 0.83.
  - Method: model named; hyperparameters and training each rated 0/1/2.
  - Data: available / not available (with reason) / public data only; deterministic split.
  - Experiment: code available (also searched via search engines and author websites).
- **Direct study (§4.3, p. 3436):** 298 artifacts downloaded and run following the README.
  - At most **1 hour** of debugging and setup (compared with Collberg et al.).
  - Training capped at **10 hours**, then evaluation run.
  - **CPU** unless the authors specify special hardware.
  - Reproduced = within **5 %** of the claimed metric (following Raff).
  - Second reviewer checks; re-run if a workaround is seen; **the most positive result counts**.
  - Effort: about 8 person-years and more than 10 000 hours of computation (p. 3434).

## Findings
- **RQ1 method (p. 3437, Figs. 2–3):** hyperparameters described fully in 312, partly in 165, not at all in 267 papers. Training: 410 / 166 / 168 (23 % not described).
- **RQ2 data (p. 3438, Fig. 4):** 36 % collected data and did not share it; 36 % shared it; 28 % used public data only. Of those not sharing, **~90 % give no reason** (7 % sensitive data, 3 % proprietary).
- **RQ3 code (p. 3439, Fig. 5):** 446 of 744 (60 %) no code; 298 (39–40 %) code; ~1 % "request access", some unanswered for months. 95 % on GitHub, 4 % Google Sites/Drive, 1 % university pages. One artifact was only found through a Twitter thread.
- **RQ4 running (pp. 3439–3440, Figs. 6–7):** 56 % do not run; 20 % same results; 4 % different results; 18 % run but miss parameters, files or outputs.
  - Over half do not run at every venue.
  - README with instructions 57 %; 13 % only a title.
  - Out of the box 28 %; output matches the paper 43%; deterministic split 22 %; trained model included 17 %.
  - Example: code claiming a speed-up only prints "DONE!" (p. 3440).
- **Permutation test (p. 3441):** per-year share of papers with code, years < 2020 vs. ≥ 2020, 10 000 permutations, **p = 0.068** → "we accept the null hypothesis".
- **USENIX AE (pp. 3441–3442, Figs. 8–9):**
  - AE submissions: 40 (2020, 38 passed), 37 (2021, 34 passed), 114 (2022: Available 107, Functional 98, Reproduced 65).
  - Re-checked 19 of 21 overlapping 2022 papers using the artifact appendices: **15 badges re-created**, 4 not. The causes were permissions (data or commands only the AEC could access) and package problems.
  - "No real incentive for any code to be maintained once it is accepted" (p. 3441).
- **Industry (§6.4, p. 3442):** only 6 % of papers, so no claims; calls for a discussion on legitimately unpublished artifacts (IP, sensitive data).

## Five recommendations (§7, pp. 3442–3443)
1. **Packaging and dependencies:** the most common problem; unpinned versions, deprecated TensorFlow 1 still used in 2022 → pinned `requirements.txt`, Docker images or VMs.
2. **Incomplete files or data:** missing functions, labels, preprocessing, pre-trained models → keep everything in one place; more AE would guarantee one complete instance.
3. **Incomplete instructions:** hard-coded absolute paths, missing steps → step-by-step exact commands with examples; test that a **non-expert** can run it.
4. **Complex hardware:** e.g. data collection needing a $1 000 oscilloscope → share the collected data.
5. **Not designed for reproducibility:** demos and libraries instead of experiment scripts → every claim reproducible; outputs should be the paper's tables and figures; "reproducible by design".

## Limitations and open challenges (§8, pp. 3443–3444)
- **Reproducing this study:** would take similar effort. The 298 repositories cannot be shared (licences, size limits); a CSV with every paper, link and coding, plus figure scripts, is on GitHub.
- **Bias:** selection may miss papers or repositories; coding is partly subjective (graded scales); negative-result bias countered by taking the most positive result; 1 h / 10 h caps.
- **Open challenges:**
  - Funding ends and students leave, so maintenance stops. Funders could spot artifacts early (e.g. NSF "Transition to Practice").
  - Don't resurrect the failed papers; spend effort on future work instead.
  - Replicability, generalizability and correctness were not studied.

## Related work (§9, p. 3444)
- **Computer science:** 9 % code in 2004 (IEEE TSP); 28 % in 2019 (ICIS); 32 % compiled within 30 min in 2014 (Collberg et al.).
- **Machine learning:** 8 % of 45 papers discuss randomness; 11 of 12 recommender systems beaten by simpler baselines; 25 % of AAAI/IJCAI papers describe their method reproducibly; Raff reproduced 62 % of 255 papers.
- **Security:** only two earlier studies, both indirect: "Van et al." [633], 50 systems papers from 2010 and 2015, benchmarking flaws, about 1 in 4 papers names no platform or software version (probably van der Kouwe et al.'s "benchmarking crimes" work; from memory, not checked); Hamm et al. [215], 61 user studies 2013–2018, 51 % share the questionnaire, none the full responses.
