# Winter, Timperley, Hermann, Cito, Bell, Hilton & Beyer (2022), *A Retrospective Study of One Decade of Artifact Evaluations* (ESEC/FSE 2022)

_Page numbers are printed proceedings pages (145–156 = PDF pages 1–12)._

**In one sentence:** Across 3 650 articles from 64 ACM SE/PL venues (2011–2020), articles with
artifacts get no more citations (significant in only 2 of 64 venues), Available badges go with
far fewer dead links (no working reference: 0.4 % vs. 9.7 %), evaluated artifacts show slightly
more GitHub activity (D ≤ 0.15), and reuse and documentation show no clear advantage. Many
artifacts, evaluated or not, lack a licence (50 / 46 of 100).

**Type:** empirical, quantitative, observational (metadata, link checks, GitHub API, file-name
search; no artifact is run).

**Note:** first author Stefan Winter is our lecturer, and the paper picks up the open question
from week 2 (Hermann et al. 2020: "no evidence AE leads to better artifacts"). It is the AE
community evaluating its own process, with insider access (AEC chairs filled data gaps, p. 155).

### Unclear aspects / methodological questions

- **Rejected artifacts are counted as NonAE (pp. 149–150, §9 p. 154).** The comparison is
  "badged" vs. "everything else", which mixes never-submitted, rejected, and unknown artifacts.
  The authors assume artifacts that benefited from AE without a badge are negligible, based on
  five open-review venues. If rejected ones were improved by reviewer feedback, the NonAE
  group would look better and hide part of the AE effect.
- **"Not significant" with small strata (RQ1, pp. 148–149).** 64 venues tested separately,
  each split into four categories and partly into page-length / access strata. A venue has
  20–160 articles (Fig. 3), so some cells hold a handful of papers. The authors call the
  results "conservative" (p. 155), yet Finding 1 reads "Artifacts do not significantly improve
  citation counts" (p. 149). Absence of evidence or evidence of absence? A pooled model across
  venues (e.g. with venue as a factor) would have more power.
- **Citation window.** The per-venue tests remove age differences *between* groups, but 2019–2020
  papers had only one or two years to collect citations (data collected 2021–22). Many venue
  tests therefore compare very small counts.
- **The 16 tests "(2 + 3!) · 2" (p. 149).** The arithmetic of the test count is not obvious from
  the text. A minor point, but it is the basis of the multiple-testing correction.
- **Table 3 hides a striking number (p. 150).** Without an Available badge, references of AE
  articles work in 91.1 % and of NonAE articles in 89.9 % of cases. Evaluation itself barely
  changes link survival; the **archival host** behind the Available badge does. That is what
  Finding 2 says, but the headline "evaluated vs. not evaluated" framing invites misreading.
- **"Is accessible" = HTTP status (p. 150).** HEAD requests check that a URL answers, not that
  the artifact is there (2.5 % false positives, 5.6 % false negatives on a sample). Step 3
  (is it the artifact?) is delegated to the AEC or to URLBrowser tagging.
- **Selection in RQ3 (p. 152).** Groups that build real tools both submit to AE and keep
  committing. The higher activity of AE repositories may come from *who* submits, not from AE.
  Also, commits for AE preparation itself may fall after the publication date.
- **Reuse proxy (RQ4, pp. 152–153).** Only artifact URLs inside the same 3 650 articles count.
  Reuse is normally cited through the paper, not the URL, and most reusing papers are at
  other venues. With ≤ 0.11 % hits, the authors rightly draw no conclusion. Why keep the RQ?
- **Documentation by file name (RQ5, p. 153).** Patterns were chosen "according to our
  experience", and word count stands in for quality. A long README can still be useless; a
  short one with one Docker command can be ideal.

### Central claims to take a position on

- **"Creating and publishing research artifacts does not generally have beneficial effects
  on citation counts" (p. 149).** Contradicts Heumüller et al. (week 1). Winter et al. explain
  this by Heumüller's ICSE-only sample in years without AE (p. 147). Which result would you
  quote to a PhD student deciding whether to invest in an artifact?
- **Available badge should move to the paper review (p. 155).** Many NoB papers would qualify
  at no extra cost; separating it from AE removes the impression that "available" requires an
  evaluation. One of the few recommendations already adopted (ESEC/FSE 2022, footnote 18).
- **Alternative rewards (p. 155):** attribution rules, counts of evaluated artifacts, R+
  index, test-of-time artifact awards. Would any of them change hiring decisions?
- **Community standards for documentation and packaging (pp. 154–155).** A standard makes
  automated checks possible, but artifacts range from proofs to fuzzers to datasets
  (Hermann 2020 found no consensus on thresholds). One standard or one per artifact type?
- **Licence files in the artifact, not just the metadata (p. 154).** Small, cheap, and clearly
  supported by the data (4 of 26 metadata-licensed artifacts also appeared elsewhere without one).

### Points of interest

- **Badge detection by pixel colour (p. 148).** Old monochrome badges are not in the DL
  metadata, so the authors read the PDF corners. Shows how poorly badge information is recorded.
- **Data errors reported to ACM and fixed (p. 155).** A side effect: the study improved the
  infrastructure it measured.
- **Host platforms (Table 4, p. 151).** Institutional websites break in 23 % of cases, public
  VCS (GitHub) in 4 %, DOI/handle and publisher material in 1 %. Matches the week-1 link-rot
  theme and gives numbers for "use Zenodo, not your university page".
- **ICSE 2020 open review on GitHub (p. 150).** Artifacts were available, but the link sat only
  on a submission-info page, not in the paper. Available ≠ findable.
- **Reproduction vs. reuse documentation (p. 154).** AE artifacts have longer READMEs, some NonAE
  artifacts have large doc folders. The authors link this to Hermann's finding that reviewers
  want reproducibility and users want reusability. AE may train authors for the reviewer, not
  the user.
- **The paper practises what it preaches:** data, scripts and URLBrowser on Zenodo (p. 155).

### Subjective discourse / opinion prompts

- **Are citations the right measure of "visibility"?** The authors don't endorse them (p. 148)
  but test them because institutions use them. If artifacts don't raise citations, is that a
  failure of artifacts or of citations? (Week-1 seminar note: "maybe citations are not a
  good measure of impact".)
- **Would you rather have an evaluated artifact or an archived one?** The data says the
  archive (Available badge) makes the bigger difference to availability. Is evaluation then
  worth its reviewer cost, or is its value elsewhere (feedback, trust)?
- **Your own projects:** where would your thesis code live in five years: university GitLab,
  GitHub, Zenodo? Which of Table 4's categories is it in?
- **Insiders evaluating their own process.** The authors run AEs and found modest effects.
  Does that make the result more or less credible to you?

### Terminology (link to the lecture)

- The paper uses the **2020 ACM terms** consistently (badge (c): results *reproduced* with the
  artifact, *replicated* without, p. 146). No mapping needed.
- Footnote 6 (p. 146): whether "Results Reproduced" can be earned *within* AE is debated.
  Compare Olszewski et al.: USENIX gives "Artifact Reproduced" inside AE (65 of 114 in 2022).
- Note that the RQs never measure reproducibility; "reproducibility" appears only as AE's
  goal. The study measures preconditions (availability, documentation) and proxies (activity).
