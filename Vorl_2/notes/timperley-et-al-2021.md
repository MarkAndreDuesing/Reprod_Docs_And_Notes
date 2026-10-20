# Timperley, Herckis, Le Goues & Hilton (2021): Condensed Notes

_Page numbers are the printed "Page x of 41" numbers, identical to PDF pages._

## Core claims
- Artifact sharing is an established and growing norm in SE: 62.69 % of research papers at ICSE, FSE, ASE and EMSE in 2014–2018 link an artifact, rising from 50.56 % to 69.47 % (p. 11).
- The community values artifacts, but **creators and reviewers get little reward**, so artifacts are of low quality and AE is under-used (pp. 2–3, 27–28).
- The problems come from communication, the social system, time ("bitrot") and the artifacts' own properties, analysed with Diffusion of Innovations (p. 3).
- AECs are well placed to fix much of this (p. 3).

## Key definitions
- **Artifact:** "any external materials or information provided in conjunction with a research paper via a link" (p. 3). This is very broad: it includes companion sites and survey instruments.
- **Available:** the link is still alive at inspection time (Jan/Feb 2019). Content and usability were not checked (p. 11).
- **ACM badge criteria** (pp. 4–5): documented, consistent, complete, exercisable.
- **DoI** (p. 5): innovation (= an artifact), communication channels (links, AECs, badges), time, social system (the research community).
- **IS** (p. 6): Implementation Science, iterative evidence-based change from medicine. Recommendations should be scalable, sustainable, trialable and observable (p. 9).
- **Terminology:** mostly "replicate/replication". Krishnamurthi & Vitek's "repeatability" (re-running the artifact, p. 35) = 2020 **reproducibility**. Their "conceptual replication" = 2020 **replicability**.

## Study method
- **Publication survey (§3.1, p. 7):**
  - All technical-track papers from ICSE, FSE, ASE and EMSE 2014–2018 (DBLP).
  - URLs were extracted with regex and checked by hand: 899 artifacts in 1434 papers.
  - Availability was checked once in Jan–Feb 2019.
  - The AEC chairs of FSE 2015–2018 were asked for submission and acceptance numbers.
- **Author survey (§3.2, pp. 7–8):**
  - 744 authors of 2018 papers were emailed; 698 emails arrived and 153 responded (22 %). Respondents were not paid.
  - 28 questions with branching logic (Table 1).
  - Respondents: 91 % academic. Subpopulations: creators 137, users 129, **reviewers only 32** (Table 2).
- **Analysis:** descriptive coding, then axial coding, by three domain experts and one methodologist (an anthropologist). The authors stress that this shows the range of themes, **not their prevalence** (p. 9).
- **Not checked:** artifact contents, whether they build, or results; authors were not contacted about missing links (p. 10).

## Findings
- **Motivations for sharing (Table 3, p. 12):** supporting evidence, community norms, reuse, understanding.
- **Twelve challenges (Table 4, pp. 14–15):**
  - creators: C1 not worth it, C2 portability, C3 maintenance, C4 tacit knowledge, C6 lack of standards, C7 hosting, C8 double-blind review, C9 external constraints (IP, privacy, liability)
  - users: C2, C3, C4, C5 artifact doesn't fit purpose, C7, C9
  - reviewers: C2, C4, C6, C9, C10 no reviewer incentives, C11 technical obstacles (compute, time), C12 limited communication
- **User problems (Table 5, p. 19, 130 answers):** no usage instructions 103, artifact no longer accessible 81, no build instructions 79, unavailable dependency 69, missing dependency at run time 66, modified source 60, run-time error 55, had to reimplement 28. Only 10 never failed.
- **Link decay (Fig. 3, p. 20):** about 14 % of all links are dead, from 26.47 % for 2014 papers to 5.43 % for 2018.
- **FSE AE funnel (Fig. 4, p. 21):** 281 papers, 196 with artifacts, **74 submitted**, 64 accepted (86.49 %). OOPSLA'14 had 42 % participation (p. 37).
- **Risks named by creators (p. 13):**
  - reputation (poor code)
  - being scooped, i.e. "protect a Ph.D. student's ability to produce results"
  - mistakes being found
  - maintenance burden
  - nobody using the artifact
- **Reviewer quotes worth remembering:**
  - "We usually just make students do AEC" (p. 23).
  - "AECs… are likely to replicate the same mistake" if they only run scripts (p. 22).
  - A VM can't assess performance (p. 22).
  - Containers don't stop bitrot: "something that compiles today is probably not to compile in five years" (p. 22).
  - Fuzzers and program repair need hardware reviewers don't have (pp. 23–24).

## Secondary analysis (DoI, §5)
- **Artifact qualities (p. 25):** compatibility, trialability (README with claims and limits), complexity, relative advantage.
- **Channels (Fig. 5, p. 26):** AE/paper review (creator ↔ reviewer), links (creator → user), badges (reviewer → user). Each is weakened by unclear standards.
- **Time (p. 27):** hosting fails when students leave; bitrot; VMs and containers made after the fact may not match the original environment.
- **Social system (pp. 27–28):** lack of incentives for creators and reviewers → low quality → problems for users downstream.

## Recommendations (§6, Table 6, pp. 28–35)
- **R1 Describe** contents, structure, purpose and claims; add citation guidelines and a licence that ensures credit. Builds on Collberg's sharing contract. *(creators)*
- **R2 Self-contained artifact:** install instructions checked by CI, standard build tools, VM or container, small proof-of-concept for expensive experiments. *(creators)*
- **R3 Plan from the project start:** time for documentation, a maintenance plan (how long, by whom), transition plans when students leave, Zenodo/Figshare/Software Heritage plus GitHub for the working version. *(creators, advisors)*
- **R4 Use a clear rubric** and ask organisers for one before agreeing to review. *(reviewers)*
- **R5 Align expectations:** publish evaluation guidelines with the call for papers, add artifact deadlines to it, hand over knowledge between AEC "generations", hold retrospectives. *(organisers)*
- **R6 Reduce reviewing cost:** compute credits, a "lazy second evaluation", a certified artifact description document, two-way anonymous communication, a "best artifact reviewer" award. *(organisers)*
- **R7 Recognise and fund:** count artifacts in hiring and promotion (CRA guidance), require artifact plans in grants (like NSF's data management plans), fund hosting, maintenance and compute. *(community leaders)*
- **R8 Long-term strategy** by steering committees; a standard artifact description format; periodic systematic review of AE. *(community leaders)*
- The authors believe artifacts **should be reviewed as part of paper review** (p. 28).

## Critique (tightened)
- "Artifact = any link" inflates prevalence, and "available = link alive" overstates availability. The authors admit both (pp. 10–11).
- RQ1 ("does the community value artifacts?") is answered with prevalence and supportive quotes from people who chose to answer a survey about artifacts.
- Fig. 4: 26.33 % = 74/281 *papers*. As a share of the 196 *artifact* papers, participation is 37.8 %. The low-participation message holds, but the percentage is computed against the wrong base.
- Small internal inconsistencies: Table 5 says 81 inaccessible and 60 modified, the text says 82 and 62 (pp. 19–20). The text says 153 participants, Table 5 has 130 answers. Table 6 cites a "C13" that is never defined.
- Counterpoint: the paper is careful about what thematic analysis can show, publishes its data on Zenodo, and its recommendations are concrete and assigned to named actors. That is more actionable than most papers in this genre.

## Discussion points (merged)
- Incentives (C1, C10) are the root cause; most recommendations still ask creators and reviewers to do more work.
- Should AE be part of paper acceptance? (p. 28; compare Hermann et al. §5.3)
- Double-blind review vs. sharing at submission (C8).
- Students as reviewers: training opportunity or devaluation?
- Dead links fall with age (26 % → 5 %): the same "time since publication" effect as Heumüller et al. in week 1.
