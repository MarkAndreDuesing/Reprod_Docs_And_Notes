# Cross-Paper Discussion: Hermann et al. (2020) × Timperley et al. (2021)

## Quick comparison

| | Hermann, Winter & Siegmund | Timperley, Herckis, Le Goues & Hilton |
|---|---|---|
| Field / venues | SE **and PL** AECs, 2011–2019 (PL-dominated) | SE only: ICSE, FSE, ASE, EMSE, 2014–2018 |
| Sample | 79 calls for artifacts; 1034 AEC members invited, 257 responses | 1434 papers; 744 authors invited, 153 responses |
| Who is asked | **Reviewers** (AEC members) | **Authors** (creators 137, users 129, reviewers 32) |
| What is measured | Stated purposes and quality criteria | Link prevalence, link liveness, challenges |
| Method | Document analysis + open card sorting | Regex + manual URL check + descriptive/axial coding + DoI |
| Headline | No consensus on thresholds; reviewers want reproducibility (2020 sense), users want reusability; inconsistent terms | 62.69 % link an artifact, ~14 % dead; few submit to AE; "not worth it" |
| Diagnosis | Unclear purpose and standards; inexperienced, one-time reviewers | Misaligned incentives, poor communication, bitrot |
| Proposals | Per-community purpose and standards in CfAs; experienced reviewers; couple AE to acceptance | R1–R8: describe, self-contain, plan, rubric, align, cut review cost, fund and reward, long-term strategy |
| Tone | Insider, constructive | Sympathetic, sociotechnical |
| Shares its own data? | Yes (survey, data, scripts [12]) | Yes (Zenodo, de-identified quantitative data only) |
| Terminology | Old ACM (pre-2020), stated explicitly | Not fixed |

## Discussion questions

1. **Same picture from two sides.** Reviewers (Hermann) and authors (Timperley) both say:
   no clear standard (Hermann p. 478; Timperley C6, p. 16). Each side partly blames the
   missing guidance from the other. Who should write the standard: organisers, ACM, or the
   community?
2. **Competing diagnoses.** Hermann: the problem is *definitional* (purpose, criteria,
   terms). Timperley: the problem is *incentives*. If we had perfect criteria tomorrow,
   would participation in AE go up?
3. **What neither paper measures.** Neither opens an artifact. Neither checks whether
   badged artifacts are actually better than unbadged ones. Hermann's 20 vs. 34 (p. 477)
   is the only hint, and it is negative. What would a study look like that tests whether
   AE works?
4. **Both want AE coupled to paper acceptance** (Hermann pp. 478–479; Timperley p. 28). Both
   also report overworked, junior, one-time reviewers. Can those two findings coexist?
5. **Reuse vs. reproduction.** Hermann: reviewers check reproduction, users want reuse.
   Timperley: creators share mainly as "supporting evidence" (Table 3). Which purpose
   should AE optimise for? Week 1: Collberg's repeatability vs. benefaction and Heumüller's
   containers-for-replicating vs. source-for-building-on are the same split.
6. **Containers again.** Timperley recommends VMs and containers (R2) while quoting
   reviewers who say they don't stop bitrot or break performance claims (p. 22). Hermann
   finds calls asking for Docker/VMs as formats (p. 472). Same tension as Collberg vs.
   Heumüller.

## Broader / subjective discussion

- **Who checks the checkers?** If AE badges are given by students on their first
  committee, with no shared rubric, what does a badge tell *you* as a reader?
- **Then vs. now (2020 → today).** ACM swapped its terms in 2020; ICSE has run AE since
  2019. Has participation or badge meaning improved? A good question for the lecturer, who
  co-wrote one of the papers.
- **Is a culture change or a rule change faster?** Timperley argues for culture (R3:
  advisors valuing artifacts) and for rules (R7: hiring, grants). Which would change *your*
  behaviour first?
- **Meta-research genre.** Week 1 and week 2 are four papers about SE research itself,
  and they agree on almost everything. What is the next useful study, rather than another
  survey?

## Links to week 1

| Week 1 | Week 2 |
|---|---|
| Collberg's sharing contract | Timperley R1 / R6 "certified artifact description" (explicitly inspired, p. 28) |
| Heumüller: links decay with age | Timperley Fig. 3: 26 % dead (2014) → 5 % (2018); same confound |
| Heumüller: GitHub vs. persistent archives | Timperley R3: GitHub for the working version + Zenodo snapshot |
| Collberg: VMs distort timing | Timperley P64 (p. 22): same complaint from a reviewer |
| Collberg/Heumüller: reasons for not sharing | Timperley C1, C3, C7, C9; nearly the same list five years later |
| 2011 terminology | Hermann uses pre-2020 ACM terms; Timperley none fixed |
