# Broneske, Kittan & Krüger (2024), *Sharing Software-Evolution Datasets: Practices, Challenges, and Recommendations* (Proc. ACM Softw. Eng. / FSE 2024)

_Page numbers: printed "91:x" = PDF page x (1–24)._

**In one sentence:** A meta study of 200 papers around 41 datasets from the MSR conference
(2017–2021), plus one expert interview, finds that datasets built from version-control
histories are shared mostly on Zenodo and GitHub as spreadsheets, that 10 of 41 contain
personal data without any privacy discussion, that reusers mostly hit technical problems
(too small, missing or redundant data, outdated), and recommends minimising personal data,
checking licence compatibility and standardising formats.

**Type:** empirical, qualitative (literature meta study + single semi-structured interview).

### Unclear aspects / methodological questions

- **One expert (pp. 8, 18).** The recommendations are "refined and enriched" by a single
  interview. The justification, that data regulations are similar between countries,
  covers the legal basics but not judgement calls like the "gray area" of consent. What
  would a second expert from another country, or a developer whose data is mined, add?
- **One coder (pp. 7–8).** The second author extracted all data alone "to ensure
  consistency"; a cross-check found "no errors". Card sorting was collaborative, so no
  agreement was computed (p. 9). How much of the problem catalogue is interpretation?
- **Most-cited filter (p. 6).** Only the 10 most-cited citing papers per dataset were
  snowballed. Papers that tried and failed to use a dataset are probably cited less, so
  the problem picture may be too rosy.
- **Counts don't line up.** p. 7: 136 snowballed papers = 112 use + 24 problem papers;
  p. 12: "158 snowballed papers that used (133) or analyzed (24)". The text also refers to
  "Table 8" for the reuse problems, which are in Table 7 (p. 14).
- **One conference as source (pp. 6, 18).** Datasets come only from MSR; the authors argue
  snowballing broadens it. But the *sharing practices* (RO1) are MSR-only by design.
- **"Temporary sharing practices" (pp. 3, 7).** Probably "contemporary"; small, but it
  shows how little the term "practice" is defined: what is shared, or how well?

### Central claims to take a position on

- **"Sharing a SED is subject to several ethical and legal problems that researchers have
  to assess in advance" (p. 14).** Agree in principle. But who checks it? The paper aims at
  researchers "without access to authorities" (p. 3); is self-assessment enough?
- **"If it's truly anonymous, GDPR does not apply" (p. 17).** True legally, but commit
  histories are notoriously re-identifiable (writing style, timestamps, project). Is
  "truly anonymous" achievable for version-control data at all?
- **"Provide only a dataset of weblinks" (p. 17).** Solves licences and privacy, and the
  expert likes that it lets others test theories "at another point in time". But it gives
  up exactly what week 1 called repeatability: Heumüller et al. showed links rot.
- **Insights would "not change strongly when interviewing multiple experts" (p. 18).** A
  claim about saturation made without being able to check saturation.

### Points of interest

- **Data about others (pp. 1–2).** Weeks 1–3 discussed artifacts researchers make
  themselves. Here the researcher republishes other people's work and identities. The
  usual "share everything" norm runs into privacy law.
- **GitHub's acceptable-use policy (pp. 13–14).** Research use of public data is allowed
  only if resulting publications are open access. A platform's terms set an open-science
  requirement that venues don't.
- **Three SEDs already offline (p. 11),** all on personal or university websites, matching
  week 1 (Heumüller) and week 3 (Winter: hosting platform drives availability).
- **Topicality (p. 15).** A dataset of evolving software is outdated the day it is
  published. Should datasets be frozen snapshots (replicability) or living datasets
  (usefulness)? GHTorrent was updated periodically and then stopped.
- **Faulty data by design (p. 15).** Git lets developers rewrite history and dates; a
  "ground truth" mined from it may never have been true.
- **Scale (p. 15).** Software Heritage needs about 850 TiB: an artifact nobody can
  download is available but not reusable.

### Subjective discourse / opinion prompts

- **Did open-source contributors consent?** By using GitHub, did they agree to being
  studied? Would you mind your commit history being in a public research dataset?
- **Privacy vs. reproducibility.** If anonymisation and minimisation remove what other
  researchers need, which should win, and who decides?
- **Ethics boards for mining studies.** Should every repository-mining paper need ethics
  approval, as human-subject studies do? What would that cost the field?
- **One interview as evidence.** Would you accept "we asked one expert" in a paper you
  review? Does it change if the expert is an authority on the regulation itself?
- **Platform power.** GitHub's terms effectively set research rules. Is it acceptable that
  a company decides what research may do with public code?

### Ethics / tone

- The paper is careful: ethics approval for the interview, minimal data about the expert,
  dataset on Zenodo (pp. 8, 20). It cites the 2021 University of Minnesota case (Linux
  kernel ban) as a reminder that developer trust can be lost (p. 20).
- It names specific datasets as having privacy issues (Table 6, p. 13), including
  GHTorrent, without contacting their authors. Fair, or should they have been asked?

### Terminology / link to the lecture

- No definitions of reproducibility or replicability; only "replicability" as a goal.
- Reusing a shared SED for the same analysis = **reproducibility** (2020: different team,
  same artifacts). Re-mining with the authors' published method at a later time (the
  "weblinks" recommendation) = closer to **replicability** (different data).
- Week links: Heumüller (availability, link rot), Hermann and Timperley (cited, p. 18),
  Winter et al. 2022 (cited as guideline work, p. 18).

### My top 3 points for the session

1. Mining public repositories without consent: legal (GitHub terms) is not the same as ethical.
2. "Share links, not data" trades replicability for privacy and licences.
3. Recommendations based on one expert and one coder: how much weight can they carry?
