# Timperley, Herckis, Le Goues & Hilton (2021), *Understanding and improving artifact sharing in software engineering research* (EMSE)

_Page numbers are the printed "Page x of 41" numbers, identical to PDF pages._

**In one sentence:** 62.69 % of 1434 ICSE/FSE/ASE/EMSE papers (2014–2018) link an artifact,
about 14 % of those links were already dead in 2019, and only 74 of 196 FSE artifact papers
went to the AEC. A survey of 153 authors names twelve challenges (C1–C12, led by "not
worth it"), which the authors analyse with Diffusion of Innovations and turn into eight
recommendations aimed at specific actors.

**Type:** empirical, mixed methods (publication survey + qualitative author survey +
framework-based secondary analysis + recommendations).

### Unclear aspects / methodological questions

- **"Artifact = any link" (p. 3).** Companion sites, survey instruments and raw data all
  count. The 62.69 % headline therefore measures *linking something*, not *sharing
  something usable*. Compare Heumüller (week 1), who counted only runnable software.
- **"Available = link alive" (p. 11).** A live landing page with a dead download counts as
  available. The authors admit it, but the 14 % dead-link figure is then a *lower bound* on
  unavailability.
- **Age confound again (Fig. 3, p. 20).** 26.47 % dead for 2014 vs. 5.43 % for 2018, all
  checked in early 2019. As with Heumüller in week 1, this mixes *older papers had worse
  practice* with *older links had more time to break*. The text says "as one may expect",
  but then also reads Fig. 2 as a trend in practice.
- **RQ1 answered with prevalence plus quotes (pp. 11–12).** "Does the community perceive
  inherent value?" is answered yes because many papers link something and respondents say
  nice things. Respondents chose to answer an artifact survey, so a positive view is
  likely. Linking may also just be a norm reviewers expect (C9 quote: "ritualistic blanket
  argument", p. 18).
- **Thematic analysis vs. counts (p. 9 vs. pp. 18–19).** The authors say thematic
  analysis shows *range*, not *prevalence*. They then rank challenges ("first and
  third-most common") using Table 5. That is fine for Table 5 (a closed question), but the
  C1–C12 list itself has no frequencies. We don't know if C8 (double-blind) is a big or a
  rare problem.
- **Fig. 4 percentage (p. 21).** "74 papers were submitted to the AEC (26.33 %)" =
  74/281 *all* papers. Of the 196 *artifact* papers it is 37.8 %. The low-participation
  conclusion holds, but the denominator is the wrong one.
- **Only 32 reviewers (Table 2, p. 8).** RQ2.3 rests on 21 % of respondents. Hermann et al.
  asked 257 AEC members. The two papers complement each other here.
- **Small inconsistencies.** Table 5 says 81 inaccessible and 60 modified, the text says
  82 and 62 (pp. 19–20). The survey had 153 participants but Table 5 has 130 answers.
  Table 6 cites "C13", which is never defined. Minor, but notable in a paper about
  artifact quality.
- **Recommendations: from data or from literature?** Table 6 lists for each R whether it is
  "derived from results" and "supported by literature". R1 (sharing contracts, Collberg)
  and R3 (archives, Heumüller) are mostly borrowed. The genuinely new ones are R4–R6
  (reviewer rubric, lazy second evaluation, certified artifact description, best-reviewer
  award). Were any of them trialled, as IS principles would demand (p. 9)?

### Central claims to take a position on

- **"Artifacts… should be reviewed as part of the paper review process" (p. 28).** The
  authors' own belief, not a survey result. It conflicts with C8 (double-blind) and C11
  (reviewer time). How would you implement it at ICSE scale (~1000 submissions)?
- **The root cause is incentives (C1, C10, §5.4).** Yet R1–R6 ask creators and reviewers to
  do *more* work. Only R7 addresses rewards. Is the order of recommendations backwards?
- **"Count artifacts in hiring and promotion" (R7, p. 34).** The strongest lever on paper.
  How would a hiring committee measure "artifact impact" without reducing it to badges or
  GitHub stars?
- **VMs and containers as the portability answer (R2, p. 31).** The paper's own respondents
  say containers don't stop bitrot (P18, p. 22) and VMs break performance claims (P64,
  p. 22). Same tension as Collberg vs. Heumüller in week 1.
- **"Protect a Ph.D. student's ability to produce results" (P120, p. 13).** Is delayed
  sharing (embargo) a legitimate compromise or a reproducibility gap?

### Points of interest

- **Diffusion of Innovations as a lens (pp. 5, 24–28).** Treating each *artifact* as an
  innovation that must spread is unusual. The four qualities (compatibility, trialability,
  complexity, relative advantage, p. 25) form a neat checklist for a README. Does the
  framework add insight beyond §4, or relabel it?
- **An anthropologist on the team (p. 1).** Lauren Herckis is from the humanities and
  social sciences. Qualitative method expertise in an SE paper: does it show?
- **"Replicate the same mistake" (P25, p. 22).** One-click reproduction scripts make AE
  easy, but a reviewer who only runs the script re-runs any bug too. Links to Kitchenham's
  critique of lab packages (p. 35). This is an argument for 2020 *replicability*
  (independent re-implementation) over *reproducibility*.
- **Hardware gap (P64, pp. 23–24).** Fuzzers, program repair and cloud work need resources
  reviewers don't have, hence the idea of compute credits from ACM/IEEE (R7, p. 34). Will
  the gap grow with ML-heavy SE research?
- **Certified artifact description (R6, p. 33).** AE "certifies" a structured document of
  claims and limits rather than the artifact itself. A close cousin of Collberg's sharing
  contract, but checked by someone.
- **Whole research areas "dead" (P68, p. 15)** because early work had no artifacts and
  re-implementation was too costly. A strong, concrete harm of not sharing.
- **Students as AEC reviewers (P64, p. 23).** "Good… gets students involved" but
  "reinforces the idea that artifacts are not a primary thing." Matches Hermann's finding
  that most reviewers serve once.
- **Hosting (C7, p. 17; R3, p. 32).** GitHub for the living version, Zenodo or Software
  Heritage for a snapshot per paper. This answers week 1's "GitHub vs. persistent archive"
  conflict: use both, for different purposes.

### Subjective discourse / opinion prompts

- **Not worth it?** P137: improving the paper has "a clear benefit, whereas the benefit of
  releasing the artifacts is hard to quantify" (p. 14). In your own projects (thesis,
  coursework), have you ever cleaned up code just so others could use it? Was it worth it?
- **Fear of being found wrong.** P87 didn't share because they were "scared the analysis
  is incorrect" (p. 13). Isn't that exactly the reason it *should* be shared? But would you
  publish your own messy analysis scripts?
- **Is reimplementation always bad?** 28 users had to reimplement (Table 5). An
  independent reimplementation is 2020 *replicability*, the strongest form of
  confirmation. Is the failure of an artifact sometimes a scientific gain?
- **Maintenance forever?** Who should keep a tool working after the PhD student leaves:
  the advisor, the university, nobody? Is "this artifact is unmaintained" an honest
  and acceptable state?
- **Double-blind vs. open science (C8).** Which is worth more: anonymous review or easy
  sharing at submission time?
- **Would you reuse a badge-less artifact?** For a thesis baseline, would you trust GitHub
  stars, a badge, or your own trial run?

### Ethics / tone

- Constructive, non-blaming, frames creators sympathetically ("which is understandable",
  p. 19). Privacy and re-identification risk for qualitative data is taken seriously
  (pp. 17–18), and the authors themselves share only de-identified quantitative survey data
  (p. 10). They practise what they preach within ethical limits.
- Industry constraints (IP, liability, p. 17) are treated as legitimate, not as excuses.

### Terminology / link to the lecture

- The paper mostly uses "replicate" generically and doesn't fix definitions. Mapped to 2020:
  - re-running the authors' artifact (what AECs do; Krishnamurthi & Vitek's "repeatability", p. 35) = **reproducibility**
  - "conceptual replication" by a different lab with its own implementation (p. 35) = **replicability**
  - the creator re-running their own work = **repeatability**
- Keywords list replicability *and* reproducibility side by side (p. 1), without saying
  which ACM version is used. Hermann's footnote 5 shows why that matters.

### My top 3 points for the session

1. **Incentives are the diagnosed root cause, but most recommendations add work** to the
   people who lack incentives. What would a solution look like that starts from R7?
2. **"Replicate the same mistake":** should AE aim at reproducibility (run the script) or
   push toward replicability and robustness?
3. **Measurement validity:** "artifact = any link" and "available = link alive" overstate
   the situation, and the dead-link trend repeats Heumüller's time-since-publication
   confound.
