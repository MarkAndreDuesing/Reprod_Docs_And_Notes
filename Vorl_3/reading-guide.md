# Reading Guide – Lecture 3

Two **measurement studies of artifacts after artifact evaluation (AE) exists**, one in SE/PL and
one in security. Both ask whether AE has made a difference, and both answer "less than hoped".
Winter et al. is again co-authored by our lecturer (Stefan Winter) and by authors from week 2
(Hermann, Timperley, Hilton). There are no new slides this week; the reference point is still
`Vorl_1/IntroductoryLecture.pdf` (2020 definitions on slide 3/24).

| | Paper A | Paper B |
|---|---|---|
| File | `3540250.3549172.pdf` | `3576915.3623130.pdf` |
| Title | *A Retrospective Study of One Decade of Artifact Evaluations* | *"Get in Researchers; We're Measuring Reproducibility": A Reproducibility Study of Machine Learning Papers in Tier 1 Security Conferences* |
| Authors | Stefan Winter, Christopher S. Timperley, Ben Hermann, Jürgen Cito, Jonathan Bell, Michael Hilton, Dirk Beyer | Daniel Olszewski, Allison Lu, Carson Stillman, Kevin Warren, Cole Kitroser, Alejandro Pascual, Divyajyoti Ukirde, Kevin Butler, Patrick Traynor (all University of Florida) |
| Venue | ESEC/FSE 2022 (conference) | ACM CCS 2023 (conference) |
| Length | 12 pages (two-column) | 27 pages, but the body is **12 pages**; pp. 13–27 are 784 references and the paper list |
| Type | Empirical, **quantitative**, observational: 3 650 articles from 64 ACM venues (2011–2020), five RQs on visibility, availability, maintenance, reuse, documentation | Empirical, **quantitative**: indirect study (availability) of 744 ML papers + direct study (running the code) of 298 artifacts |
| Page numbers | Printed proceedings pages **145–156** (= PDF pages 1–12). This guide uses printed pages. | Printed proceedings pages **3433–3459** (= PDF pages 1–27). This guide uses printed pages. |

## Structure maps

### Winter et al. 2022 (printed pp. 145–156)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction (central question, RQ1–5 in prose) | 145–146 | — |
| §2 Background: definitions, badges, related studies, data collections | 146–147 | **Fig. 1** first OOPSLA badge 2013 (p. 146); **Fig. 2** ACM badges (p. 146); footnote 6: is "Reproduced" possible inside AE? (p. 146) |
| §3 RQs and study subjects (venue selection, exclusions, 3 650 articles) | 147–148 | **Fig. 3** article categories AE / Av. / NoB / NoA per venue (p. 148) |
| §4 RQ1 visibility (citations, KS tests, stratification) | 148–149 | **Table 1** confounders per venue (p. 149); **Table 2** significant results, only 2 of 64 venues (p. 149) |
| §5 RQ2 availability (references, HTTP checks, host platforms) | 149–152 | **Table 3** accessibility by badge (p. 150); **Table 4** links by host platform (p. 151); **Fig. 4** total and broken links per year (p. 151) |
| §6 RQ3 maintenance (GitHub activity) | 152 | **Table 5** KS results for GitHub measures (p. 152) |
| §7 RQ4 reuse (artifact URLs cited by other articles) | 152–153 | **Table 6** referenced / referencing articles (p. 153) |
| §8 RQ5 documentation (sample of 100 + 100) | 153–154 | **Table 7** file-name patterns and word counts (p. 154) |
| §9 Threats to validity | 154–155 | — |
| §10 Discussion and recommendations; declarations | 155 | footnote 18: the publisher already adopted one recommendation (p. 155) |
| References | 156 | skip |

No formulas. Findings 1–5 are boxed at the end of each RQ section (pp. 149, 152, 152, 153, 154).

### Olszewski et al. 2023 (printed pp. 3433–3459)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction (contributions, "8 person-years") | 3433–3434 | — |
| §2 Background: NAS definitions, indirect vs. direct study, AECs in security | 3434–3435 | — |
| §3 Null hypothesis H0 | 3435 | — |
| §4 Methodology: RQ1–4, paper selection, indirect and direct study rules | 3435–3436 | **Fig. 1** pipeline (p. 3435); **Table 1** factors and variables (p. 3436) |
| §5 Indirect study: method, data, experiment availability | 3437–3439 | **Fig. 2** hyperparameters, **Fig. 3** training (p. 3437); **Fig. 4** data, **Fig. 5** code availability (p. 3438) |
| §6.1 Direct study results | 3439–3440 | **Fig. 6** run outcomes per venue (p. 3439); **Fig. 7** five factors (p. 3440) |
| §6.2 Statistical analysis (permutation test, p = 0.068) | 3440–3441 | **Fig. 8** USENIX AE vs. non-AE 2020–22 (p. 3441) |
| §6.3 USENIX 2022 badges re-checked (15 of 19 agree); §6.4 academia vs. industry | 3441–3442 | **Fig. 9** results per year and venue (p. 3442) |
| §7 Five recommendations | 3442–3443 | — |
| §8 Limitations and open challenges (reproducing this study, funding) | 3443–3444 | — |
| §9 Related work, §10 Conclusion | 3444 | — |
| References, Appendix A.1 list of the 744 papers | 3445–3459 | skip |

No formulas (only the permutation test and Cohen's κ = 0.83 in prose, p. 3436). The
Coxcomb plots (Figs. 2–5) are polar bar charts; the numbers in the text are easier to read.

## 2.5-hour plan: Winter et al. (12 dense pages, quantitative)

Two columns of FSE text, five RQs, each with its own method. Read each RQ's method slowly:
every RQ uses a different proxy (citations, HTTP status, commits, URL mentions, file names).

| Block | Time | Pages | What to do | Output |
|-------|------|-------|------------|--------|
| 1. Survey | 10 min | Abstract, §1 (145–146), Findings 1–5, §10 (155) | Central question, the five RQs, the five findings | Claims column |
| 2. Background | 10 min | §2 (146–147) | Badge categories (a)–(c); footnote 6. Note the link to Hermann 2020 and Heumüller 2020 (p. 147) | — |
| 3. Subjects + threats | 20 min | §3 (147–148), Fig. 3, **§9 (154–155) now** | Four categories AE / Av. / NoB / NoA. Where do failed AE submissions go? | Judgement calls |
| 4. RQ1 + RQ2 (slow) | 40 min | §4–5 (148–152), Tables 1–4, Fig. 4 | Per-venue KS tests: how many papers per stratum? In Table 3, compare AE vs. NonAE **within** "No Av. badge" | Evidence column; `✗` where a proxy is weak |
| — Break | 10 min | | | |
| 5. RQ3–RQ5 | 30 min | §6–8 (152–154), Tables 5–7 | For each: what is the proxy, and what else could explain the difference? | One line per RQ: proxy → doubt |
| 6. Recommendations | 10 min | §10 (155) | Rewards, Available badge, community standards. Which follow from the data? | — |
| 7. Synthesis | 20 min | — | Discussion template; top 3 points | One-page sheet |

Total: 150 min. If behind schedule, cut block 2, never 4 or 7.

### Questions to ask while reading Winter et al.

- **What is "AE"?** Only articles with a badge. Rejected artifacts sit in NonAE together with
  never-submitted ones (p. 149, §9 p. 154). Does that blur the comparison?
- **Power of the citation test:** 64 venues tested separately, each split into four
  categories and then into strata. "Not significant" with 20–50 papers per stratum says
  little. The authors call it "conservative" (p. 155). Is Finding 1 worded too strongly?
- **Table 3:** without an Available badge, 91.1 % (AE) vs. 89.9 % (NonAE) of found references
  work (p. 150). Is it the evaluation, or the archival host, that keeps links alive?
- **Selection:** do tool-building groups submit to AE *and* keep committing anyway (RQ3)?
- **Reuse proxy (RQ4):** artifact URLs found in other articles of the same 3 650-article
  dataset. People usually cite the paper, not the URL. Is the 0.05 % meaningful?
- **Insiders:** the authors are AE organisers and Hermann/Timperley wrote the week-2 papers.
  This is the community evaluating its own process.

## 2.5-hour plan: Olszewski et al. (12-page body, quantitative)

| Block | Time | Pages | What to do | Output |
|-------|------|-------|------------|--------|
| 1. Survey | 10 min | Abstract, §1 (3433–3434), §10 (3444), figure captions | Headline numbers: 744 papers, 60 % no code, 56 % of artifacts don't run, 20 % same results, p = 0.068 | Claims column |
| 2. Definitions + H0 | 15 min | §2–3 (3434–3435) | Map NAS terms to the 2020 ACM terms. Read H0 closely: which conferences had an AEC before 2023? | Terminology mapping |
| 3. Method (slow) | 35 min | §4 (3435–3436), Table 1, **§8.2 limitations (3443) now** | Selection criteria, union of two reviewers, 1 h debugging, 10 h training, CPU, 5 % rule, "most positive result" | List of judgement calls |
| — Break | 10 min | | | |
| 4. Indirect study | 20 min | §5 (3437–3439), Figs. 2–5 | Method / data / code availability; 90 % give no reason for withheld data | Evidence column |
| 5. Direct study + statistics | 35 min | §6 (3439–3442), Figs. 6–9 | What exactly is permuted (per-year proportions → 10 points)? Fig. 8: who chooses to submit to AE? | `✗` on the H0 conclusion if warranted |
| 6. Recommendations | 15 min | §7–8 (3442–3444) | Five problems: who must act, what does it cost? Do the authors follow their own advice (§8.1)? | R table "who / cost" |
| 7. Synthesis | 10 min | — | Template; top 3 points | One-page sheet |

Total: 150 min. Skip the references and appendix (pp. 3445–3459) entirely. If behind
schedule, shorten block 4, never 3, 5 or 7.

### Questions to ask while reading Olszewski et al.

- **The H0 design:** "before vs. after AECs were introduced to Tier 1 conferences (2020)"
  (p. 3435), but only USENIX had an AEC in 2020–2022; CCS started in 2023 and NDSS and S&P had
  none (p. 3435). What does a before/after test across all four venues measure?
- **"We accept the null hypothesis" (p. 3441):** can a test ever do that? And does p = 0.068
  support "AECs have yet to achieve their intended goals" (p. 3434)?
- **Time limits:** 1 h of debugging and 10 h of training, compared with Collberg &
  Proebsting's 30 min (week 1). Does "does not run" mean "not reproducible"?
- **5 % rule (p. 3436):** within 5 % of the claimed metric: relative or absolute? With
  99 % accuracy claims, 5 percentage points is a large window.
- **USENIX badge check (p. 3441):** 15 of 19 badges re-created a year or two later. The
  four failures were permissions and package drift. What does a badge certify, and for how long?
- **Their own artifact (§8.1):** CSV and figure scripts, no code archive (licences, size).
  Is that enough for a paper that measures others' reproducibility?

## Discussion roles (paper only)

Same four as weeks 1–2: **presenter**, **advocate**, **critic/reviewer**, **practitioner**.
