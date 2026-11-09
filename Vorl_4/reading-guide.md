# Reading Guide – Vorl_4

Two empirical papers on **how artifacts are packaged and shared**, from two angles:
one on datasets built from *other people's* data (version-control histories), one on
artifacts of experiments *with human participants*. Both build on week 1–3 papers
(Heumüller, Hermann, Timperley, Winter). No slides this week; the reference point for
terminology is still `Vorl_1/IntroductoryLecture.pdf` (2020 definitions).

| | Paper A | Paper B |
|---|---|---|
| File | `3660798.pdf` | `1-s2.0-S0164121224002310-main.pdf` |
| Title | *Sharing Software-Evolution Datasets: Practices, Challenges, and Recommendations* | *Research artifacts for human-oriented experiments in software engineering: An ACM badges-driven structure proposal* |
| Authors | David Broneske, Sebastian Kittan, Jacob Krüger | Cathy Guevara-Vega, Beatriz Bernárdez, Margarita Cruz, Amador Durán, Antonio Ruiz-Cortés, Martin Solari |
| Venue | Proc. ACM Softw. Eng. (FSE) 1, Article 91, 2024 | Journal of Systems and Software 218, 112187, 2024 |
| Length | 24 pages (single column; body pp. 1–20) | 16 pages (two-column; body pp. 1–13) |
| Type | Empirical, **qualitative meta study**: 200 papers (43 dataset papers from MSR 2017–2021 + snowballing) and **one** expert interview | Empirical + **design science**: survey of 106 artifacts from 4 journals (2000–2022), then a proposed artifact structure validated on 12 conference artifacts and 2 own experiments |
| Page numbers | Printed "91:x" = PDF page x | PDF pages 1–16 (journal uses an article number, no printed page range) |

## Structure maps

### Broneske et al. 2024 (pp. 1–24)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction (contributions p. 3) | 1–3 | — |
| §2 Methodology: ROs (p. 4–5), literature review, snowballing, data extraction, expert discussion, analysis | 3–9 | **Fig. 1** method overview (p. 4); **Table 1** MSR papers per year/track (p. 7); **Table 2** interview questions (p. 8) |
| §3 RO1 sharing practices | 9–12 | **Table 3** 41 SEDs by type (p. 9); **Table 4** data sources (p. 10); **Table 5** storage formats (p. 11); insight box I1–I5 (p. 12) |
| §4.1 RO2 problems of sharing and using | 12–16 | **Table 6** privacy status of the 41 SEDs (p. 13); **Table 7** problems when reusing (p. 14); insight box I6–I7 (p. 16) |
| §4.2 RO3 recommendations | 16–17 | recommendation box (p. 17) |
| §5 Threats to validity | 18 | — |
| §6 Related work | 18–20 | **Table 8** related work vs. this study (p. 19) |
| §7 Conclusion, data availability | 20 | — |
| References | 21–24 | skip |

### Guevara-Vega et al. 2024 (pp. 1–16)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction (DSR phases I–IV) | 1–3 | **Fig. 1** BPMN of the DSR process (p. 3); **Table 1** open-science policies of EMSE, TSE, IST, JSS (p. 3) |
| §2 Background: open science, ACM badges, artifact taxonomies (Solari maturity levels, seven modules) | 3–5 | — |
| §3 Survey method (RQ1.1–1.4, RQ2.1–2.2; WoS query) | 5–6 | **Fig. 2** selection funnel 1426 → 267 → 106 (p. 5) |
| §4 Results | 6–9 | **Fig. 3** availability per journal (p. 6); **Fig. 4** trend 2000–2022 (p. 7); **Fig. 5** repositories (p. 7); **Table 2** journal guidelines (p. 8); **Table 3** top-ten problems (p. 8); **Fig. 6** Solari modules (p. 9) |
| §5 Proposed structure and validation | 9–12 | **Table 4** structure (p. 10); **Table 5** mapping to Functional/Reusable/Available (p. 11); **Table 6** Reproduced/Replicated (p. 11); **Table 7** check against 12 awarded artifacts (p. 12) |
| §6 Threats to validity | 13 | — |
| §7 Conclusions and future work | 13 | — |
| Declarations, references | 13–16 | skip; but note "Data availability: on request" (p. 14) |

No formulas in either paper.

## 4-hour plan: Broneske et al. (24 pages, dense prose)

| Block | Time | Pages | What to do | Output |
|-------|------|-------|------------|--------|
| 1. Survey | 15 min | Abstract, §1 (pp. 1–3), §7 (p. 20), insight boxes (pp. 12, 16, 17) | RO1–RO3 and the boxed insights I1–I7 | Claims column; five Cs |
| 2. Method (slow) | 60 min | §2 (pp. 3–9), Tables 1–2, **§5 threats (p. 18) now** | Why MSR only? How were 200 papers coded (one person)? What does one expert interview support? | List of judgement calls |
| — Break | 10 min | | | |
| 3. RO1 practices | 30 min | §3 (pp. 9–12), Tables 3–5 | Where and how are SEDs shared; which went offline? | 3–5 bullets |
| 4. RO2 problems | 45 min | §4.1 (pp. 12–16), Tables 6–7 | Privacy vs. technical problems; the GitHub terms quote; check the counts | Evidence column; `✗` on numbers |
| 5. RO3 recommendations | 25 min | §4.2 (pp. 16–17) | For each recommendation: who acts, what it costs, is it new? | Table "who / cost / new?" |
| 6. Related work | 15 min | §6 (pp. 18–20), Table 8 | Links to Heumüller, Hermann, Timperley, Winter; Gold & Krinke | `→` links |
| 7. Synthesis | 40 min | — | Discussion template; top 3 | One-page sheet |

If behind schedule, cut blocks 3 and 6, never 2 or 7.

### Questions to ask while reading Broneske et al.

- **One expert (pp. 8, 18):** the recommendations are "refined" by a single interview. Is
  the argument "regulations are similar everywhere" enough to justify n = 1?
- **Sample:** 43 dataset papers from one conference, plus the 10 most-cited citing papers
  each. Does the most-cited filter hide failed reuse attempts?
- **Counting:** "136 relevant papers, 112 use, 24 analyse" (p. 7) vs. "158 snowballed
  papers that used (133) or analyzed (24)" (p. 12). Which is right?
- **Consent (p. 13):** the expert calls mining public repositories a "gray area". Does
  GitHub's acceptable-use policy settle the ethics, or only the legal side?
- **Recommendations (p. 17):** "anonymize, don't collect what you don't need, share links
  instead of code". How do these trade off against replicability?

## 2.5-hour plan: Guevara-Vega et al. (16 dense pages)

| Block | Time | Pages | What to do |
|-------|------|-------|------------|
| Survey | 10 min | Abstract, §1 (pp. 1–3), §7 (p. 13), Fig. 1 | The four DSR phases and the RQs |
| Background | 15 min | §2 (pp. 3–5) | ACM badge groups; Solari's five maturity levels and seven modules (needed for Tables 5–7) |
| Method + threats | 20 min | §3 (pp. 5–6), Fig. 2, **§6 (p. 13)** | Search string "experiment" only; one person screening; 106 of 267 |
| Results | 35 min | §4 (pp. 6–9), Figs. 3–6, Tables 2–3 | Availability, repositories, top-ten problems |
| Proposal + validation | 40 min | §5 (pp. 9–12), Tables 4–7 | Which items are mandatory and why; is the validation independent? Check the coverage percentages |
| Synthesis | 30 min | — | Template; compare with Broneske et al. |

### Questions to ask while reading Guevara-Vega et al.

- **Validation (pp. 9–12):** mandatory items are partly derived from awarded artifacts and
  then "validated" against awarded artifacts, plus two of the authors' own experiments.
  How independent is that?
- **Numbers:** "55.5 % of the 6 mandatory items" (p. 9) is not a possible share of six
  items. What happened?
- **Own artifact:** the paper's data availability statement says "on request" (p. 14),
  while p. 13 points to a Zenodo artifact. Does the paper meet its own standard?
- **HOE vs. computational experiments:** what actually differs for artifacts with human
  participants (consent forms, training material, surveys)?

## Discussion roles (paper only)

- **Presenter:** 3-minute summary of each paper.
- **Advocate:** why a structure (Guevara-Vega) or a set of rules (Broneske) would help.
- **Critic / reviewer:** n = 1 interview; self-validation; numbers that don't add up.
- **Practitioner:** what you would change in your own next dataset or experiment package.
