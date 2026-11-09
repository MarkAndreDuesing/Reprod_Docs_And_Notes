# Guevara-Vega, Bernárdez, Cruz, Durán, Ruiz-Cortés & Solari (2024), *Research artifacts for human-oriented experiments in software engineering: An ACM badges-driven structure proposal* (Journal of Systems and Software 218)

_Page numbers are PDF pages (1–16)._

**In one sentence:** A review of 267 human-oriented experiments in four SE journals
(2000–2022) finds only 39.7 % with fully accessible artifacts, and those mostly lack design,
protocol and structure; the authors propose a sectioned artifact outline with items marked
mandatory or recommended per ACM badge, which covers on average about 86 % of 12 awarded
conference artifacts.

**Type:** empirical survey + design science research (artifact structure proposal with
internal validation).

### Unclear aspects / methodological questions

- **Circular validation (pp. 9–12).** Mandatory items come partly from what awarded
  artifacts contain; the outline is then "validated" by showing awarded artifacts contain
  them. A real test would apply it before submission and compare outcomes.
- **Self-validation (pp. 9, 13).** The second validation uses two of the authors' own
  experiments; the authors acknowledge researcher bias.
- **Numbers that don't work (p. 9).** Coverage of "55.5 %" of 6 mandatory items is not a
  possible share (possible values are 16.7 %, 33.3 %, 50 %, 66.7 %, 83.3 %). Decimal commas
  and points are mixed (39,70 % vs. 33.96 %).
- **Search string "experiment" (pp. 5, 13).** High recall, but one researcher screened 1426
  hits; a second researcher only "in case of doubt" (p. 6). No agreement measure.
- **"Missing" design and protocol (p. 8).** 91.5 % and 88.8 % of artifacts lack them, but
  the authors note these are usually in the paper. Is that a defect of the artifact, or of
  the definition of artifact?
- **The paper's own artifact (pp. 13–14).** "The research artifact of this work is
  available at the Zenodo repository" vs. "Data will be made available on request". A
  paper about artifact completeness should be unambiguous here.

### Central claims to take a position on

- **"The ESE community is making a big effort in standardization … Nevertheless, the
  research artifacts … do not usually follow these guidelines" (p. 13).** Agree that
  guidelines exist and are not followed. But week 2 (Hermann) and week 3 (Winter) showed
  the guidelines themselves are vague. Can authors follow vague guidelines?
- **A structure makes artifacts "well-structured" and "carefully documented" for the
  Reusable badge (p. 9).** A table of contents is not documentation quality. Does filling
  in a dictionary make an artifact reusable?
- **"The public repository alone is not sufficient to achieve the available badge"
  (p. 10).** Matches ACM: Available means persistent, DOI. This is useful clarity for
  authors who think GitHub is enough.

### Points of interest

- **Human-oriented experiments are different (pp. 1–2).** Consent forms, demographic
  surveys, training material, measuring instruments: none of this exists in the
  computational artifacts the earlier weeks discussed.
- **Maturity levels (p. 4).** Solari & Vegas' ladder from "Article" to "Decision-making"
  makes clear that sharing data is only the second rung; explaining *why* decisions were
  made is the top. Links to Timperley's "tacit knowledge" challenge.
- **The 2020 jump (pp. 6–7).** From about 5 to 35 artifacts per year, around the time ACM
  badges and journal open-science policies arrived. Correlation, but a striking one.
- **Optional replication section (Tables 4, 6).** The outline has a place to record later
  replications, close to Heumüller et al.'s "living badges" idea (week 1) and to Solari's
  Evolution module.
- **Datasets are almost always there (Table 3, p. 8):** only 6.6 % lack data. For human
  experiments the problem is not data, it's context.

### Subjective discourse / opinion prompts

- **Checklists for artifacts.** Would a mandatory template help you, or turn artifact
  creation into box-ticking? Compare with structured abstracts or the ACM Empirical
  Standards.
- **Effort vs. reward.** About 40 items in the outline (Table 4). Who has time for that
  on an unrewarded artifact (Timperley's "not worth it")?
- **Badges as the target.** The outline optimises for badges. Should artifacts be built
  for badges, or for the next researcher who wants to replicate?
- **"Data on request".** Is it acceptable at all in 2024 for an open-science paper? What
  if the data is about human participants?
- **Human data and openness.** Participant data can't always be shared (privacy, consent).
  Where would you draw the line between open material and protected data?

### Ethics / tone

- Constructive and practical; the authors present their framework as a proposal needing
  external validation (p. 13).
- Naming specific awarded artifacts A–L with their missing items (Table 7, p. 12) is
  transparent, but turns other authors' work into negative examples.

### Terminology / link to the lecture

- Uses the ACM **2020** badge meanings (Reproduced = independent study using the original
  artifacts in part; Replicated = own setup, p. 4), consistent with the lecture.
- Also uses "reproducibility and replicability" together throughout without
  distinguishing them in the survey.
- Week links: a survey of AE committee members on missing uniform criteria (p. 2, Hermann
  et al. 2020); the challenges list on p. 2 (lack of standards, hosting, "not worth it")
  matches Timperley et al. 2021; Heumüller et al. 2020 is cited for "replication package" (p. 4).

### My top 3 points for the session

1. Validation against awarded artifacts and own experiments is partly circular.
2. For human experiments the missing piece is context (design, protocol, decisions), not data.
3. A paper on artifact completeness with "data on request": what does that say about norms?
