# Hermann, Winter & Siegmund (2020), *Community Expectations for Research Artifacts and Evaluation Processes* (ESEC/FSE 2020)

_Page numbers are printed proceedings pages (469–480 = PDF pages 1–12)._

**In one sentence:** An analysis of 79 calls for artifacts (2011–2019) and a survey of
1034 AEC members (257 responses, mostly PL) finds that AE is meant to foster both
replicability and reusability. Yet no one agrees on quality thresholds (the only explicit
threshold is "set up in < 30 min"), reviewers prioritise replicability while users want
reusability, and the key terms are used inconsistently.

**Type:** empirical, qualitative (document analysis + open-question survey with card sorting).

**Note:** co-author Stefan Winter is our lecturer. That makes it a good chance to ask what
has changed since 2020, but critique should stay about the paper, as for any other.

### Unclear aspects / methodological questions

- **Who is "the community"? (pp. 472, 478)** Only AEC members were asked, and of those
  mostly PL people (125 PL vs. 36 SE who named their AEC). The title promises
  *community* expectations, but authors who never submit, and readers who never serve on
  an AEC, are missing. The authors chose this on purpose (p. 479: "preference to the risk
  of selection bias over the risk of our questions being misunderstood"). Fair trade-off?
- **Half-finished surveys.** 257 started, 124 finished, and partial answers were used
  for RQ2/RQ3 (p. 472). People who drop out may differ from those who finish (e.g. less
  engaged reviewers). Each question therefore has a different, unknown sample.
- **Counts from open card sorting.** Numbers like "45 (39/7)" look quantitative, but
  one author assigned labels and another checked them (p. 473), with no agreement measure.
  The SE/PL comparison (RQ3) rests on small SE counts (often single digits). The authors
  themselves say they "could neither confirm nor refute" the SE-values-reuse idea (p. 474).
- **Inconsistent totals.** p. 472: 125 PL / 36 SE / 9 both. p. 474: 131 PL / 43 SE /
  12 both. Probably different subsets, but it is not explained.
- **The "user" view comes from reviewers.** Only 76 respondents had reused an artifact
  (p. 477), and they are the same people. "Users want reusability" therefore means
  "reviewers, when they act as users, want reusability". Is that a real second perspective?
- **Satisfaction ≠ AE works.** Users were mostly satisfied, but 34 saw *no* difference
  between evaluated and unevaluated artifacts vs. 20 who did (p. 477). This is the paper's
  most important number for its own motivation ("no evidence AE leads to better
  artifacts", p. 469), and it gets one sentence.
- **"A large group … has no experience" (p. 478).** 76 of 115 (66 %) *have* submitted an
  artifact. So a third have not. Is a third "a large group"? It depends on whether you
  expect all reviewers to be artifact authors.
- **Terminology correction.** The authors "assume most participants actually mean
  replicability" when they write reproducibility (p. 473) and merge the two counts (p. 474).
  ACM itself then swapped the terms (footnote 5, p. 471). The merge may be right, but it
  is the authors' interpretation, not the respondents' words.

### Central claims to take a position on

- **"There is no consensus on quality thresholds" (p. 476).** Is that a problem to fix,
  or the natural state for very different artifacts (proofs vs. fuzzers vs. datasets)? ACM
  itself said it is "too early… and may not be desirable at all" (quoted in Timperley p. 5).
- **Criteria belong in CfAs per community, not in the ACM guidelines (p. 479).** Keeps
  flexibility, but then a badge still means different things at different venues, which is
  exactly the problem the paper names (p. 478). Can both be true?
- **Tighter coupling of AE to paper acceptance (pp. 478–479).** 13 respondents raised it
  unprompted. Compare: "The evaluations do not determine if the paper is accepted… I
  didn't [pay] much attention to these reviews" (id 79, p. 478). Does coupling fix
  reviewer motivation, or just add pressure on junior reviewers deciding someone's paper?
- **Recruit reviewers who are artifact creators (p. 479).** Sensible, but AECs are
  staffed by juniors *because* seniors don't volunteer. Where would these reviewers come
  from?

### Points of interest

- **The 30-minute rule (p. 472).** The only explicit threshold in 79 calls is "setup and
  basic test within 30 min". One reviewer allows 2 hours (p. 475). This sets a usability
  standard, not a scientific one. Is it a good minimum?
- **Purpose vs. practice mismatch (p. 472).** Calls name *reuse* as the most common
  purpose, but the most common submission criterion is *documentation for replication*,
  and consistency is asked for more than reusability. What calls say vs. what reviewers do.
- **Badge inflation in reverse (p. 476).** ICSE and FSE stopped awarding "Functional"
  and give only "Reusable" or "Available". Raising the bar: does it push quality up, or
  push authors to "Available" only?
- **Availability over quality (id 96, p. 475).** "Enforcing quality criteria only means
  that some authors will not publish their code… but the paper is still published." A
  strong argument for a low bar. Links to week 1: Collberg's "weak repeatability".
- **Type-specific expectations (pp. 475–476).** Code: documentation and runs. Proofs:
  understandability (the proof checker passing is not enough!). Data: raw data plus the
  scripts that produce the paper's plots (id 156: "plotting can contain bugs"). This is a
  concrete checklist the calls lack.
- **Fraud detection (p. 477).** An artifact had hard-coded outputs; the paper was
  withdrawn. A rare example where AE does what peer review alone cannot. How often does
  this go undetected?
- **Reviewers manipulate experiments (pp. 474–475).** Some reviewers change inputs to
  test robustness, and 24 calls encourage it. This moves AE from 2020 reproducibility
  toward a small robustness study. Should that be the norm?

### Subjective discourse / opinion prompts

- **Would you volunteer for an AEC?** Most reviewers serve once (Fig. 2, p. 473). As a
  student: is it a learning opportunity, a CV line, or unpaid work for others' papers?
- **Is a badge you can't interpret worth anything?** If "Reusable" at PLDI 2015 ≠
  "Reusable" at ICSE 2019 (p. 478), would you trust a badge when picking a baseline tool
  for your thesis?
- **Low bar or high bar?** Would you rather have 80 % of papers with a rough artifact or
  30 % with a polished one? Who benefits from each?
- **Should a reviewer read the code?** "No time to inspect code quality" (p. 475) vs.
  hard-coded outputs only found by looking (p. 477). What is the minimum a reviewer
  should check?
- **Terminology fatigue.** Three incompatible definitions (old ACM, new ACM, ASA, p. 471).
  Does the word choice matter in practice, or only in papers about reproducibility?

### Ethics / tone

- Constructive and non-blaming, similar to Heumüller et al. in week 1. The authors are
  insiders improving their own process. The quotes are anonymised with IDs and AEC counts.
- Respondents' worry about the "perceived value of their work" is addressed only through
  anonymisation (pp. 478–479).

### Terminology / link to the lecture

| Paper (old ACM, p. 471) | Meaning | Lecture (2020 ACM, slide 3/24) |
|---|---|---|
| repeatability | same team, same setup | **repeatability** (unchanged) |
| replicability | different team, same setup/artifacts | **reproducibility** |
| reproducibility | different team, different setup | **replicability** |

- So the paper's central sentence "AE's most important purpose – replicability" reads in
  2020 terms as "AE's purpose is **reproducibility**", which matches the 2020 ACM badge name
  "Results Reproduced".
- Respondents who wrote "reproducibility" (p. 473) were, by today's definitions, using
  the right word.
- Collberg & Proebsting (week 1) used the 2011 terms. Their "repeatability" (someone
  else re-running the code) is again closer to 2020 reproducibility.

### My top 3 points for the session

1. **The terminology flip:** the paper corrects respondents who, under the 2020
   definitions, were right. Even the experts can't agree on words, which is the paper's
   own finding at work.
2. **20 vs. 34:** most users saw no difference between evaluated and unevaluated
   artifacts. What does AE add, then?
3. **No threshold except 30 minutes:** should the community set quality standards per
   artifact type, and who would enforce them?
