# Moderation Plan – Lecture 2 (Oct 27)

Papers: Hermann, Winter & Siegmund (2020, FSE, printed pp. 469–480) and Timperley et al.
(2021, EMSE, pp. 1–41). Details are in `discussion/`. This file is for live use.

## 1. Opening (2–3 min)

- **Hermann et al.:** asked the *reviewers* (257 AEC members, mostly PL) what artifact
  evaluation is for and what a good artifact is. Answer: no agreed threshold, and
  inconsistent words.
- **Timperley et al.:** asked the *authors* (153) and counted links in 1434 papers. Answer:
  most papers link something, few go to AE, sharing feels "not worth it".
- **Shared theme:** artifact evaluation exists, but nobody agrees what it should check,
  and nobody is rewarded for doing it.
- **Terminology check (1 min):** Hermann uses the *old* ACM terms (footnote 5, p. 471). Their
  "replicability" (other team, same artifacts) = our 2020 **reproducibility**. Ask the room:
  *"Which of the three does an AEC actually test?"* (Answer: 2020 reproducibility, at best.)

## 2. Warm-up

**"Would you sign up for an artifact evaluation committee next year? Why or why not?"**
- Hook: most AEC members serve only once (Hermann Fig. 2, p. 473); "We usually just make
  students do AEC" (Timperley P64, p. 23).
- Easy to enter, because everyone is a student, and it leads directly into incentives.

## 3. Core questions

### Q1. Low bar or high bar?
- **Question:** Should AE badges be easy to get (more sharing) or hard to get (meaningful badges)?
- **Hook:** id 96: "Enforcing quality criteria only means that some authors will not
  publish their code" (Hermann p. 475). ICSE/FSE dropped the Functional badge to raise the
  bar (p. 476). FSE: 86 % of submitted artifacts accepted (Timperley Fig. 4, p. 21).
- **Positions:** (a) low bar: availability is the bottleneck, any code beats none;
  (b) high bar: an 86 % pass rate means a badge signals little.
- **If it stalls:** "Hermann: 34 users saw *no* difference between evaluated and unevaluated
  artifacts, 20 did (p. 477). Does that support (a) or (b)?"

### Q2. Should the artifact decide whether the paper is accepted?
- **Question:** Should a failed artifact evaluation be able to reject a paper?
- **Hook:** Both papers lean yes (Hermann pp. 478–479, 13 unprompted respondents;
  Timperley p. 28). CAV/TACAS already require it for tool papers. "The evaluations do not
  determine if the paper is accepted… so I didn't [pay] much attention" (id 79, Hermann p. 478).
- **Positions:** (a) yes, otherwise AE is optional decoration and reviewers don't care;
  (b) no, it would put junior one-time reviewers in charge of careers, clash with
  double-blind review (Timperley C8), and penalise industry papers with legal constraints (C9).
- **If it stalls:** "What about a middle way, like Hermann's 'conditional acceptance' (id
  214, p. 478)?"

### Q3. Reproduce the script, or replicate the idea?
- **Question:** Should artifact reviewers just run the authors' scripts, or try to break them?
- **Hook:** "AECs, by asking for replicable scripts, are likely to replicate the same
  mistake" (Timperley P25, p. 22). Hermann: some reviewers modify experiments to test
  robustness, and 24 calls encourage it (p. 475). One reviewer found hard-coded outputs
  only by looking (p. 477).
- **Positions:** (a) run the scripts: cheap, scalable, clear pass/fail, which is what 2020
  *reproducibility* means; (b) probe: otherwise a badge certifies that a bug is
  repeatable.
- **If it stalls:** "How much time would you need to spend to find hard-coded outputs?
  Who pays for that time?"

### Q4. Fix the definitions or fix the incentives?
- **Question:** If you could change one thing, would it be clear standards (Hermann's
  diagnosis) or rewards for artifact work (Timperley's diagnosis)?
- **Hook:** Hermann's implications are mostly about purpose, criteria and terminology
  (p. 479). Timperley names "not worth it" as C1 and puts hiring, promotion and grants in R7
  (p. 34). Most of R1–R6 still ask creators and reviewers for more work.
- **Positions:** (a) standards first: you can't reward what you can't measure; (b)
  incentives first: perfect criteria change nothing if nobody bothers to submit.
- **If it stalls:** "Timperley P31 stopped submitting to AE because of 'wildly different
  reviewer expectations' (p. 26). Is that a standards problem or an incentive problem?"

### Q5. Who keeps an artifact alive after the PhD?
- **Question:** After the student graduates, who is responsible for a research tool?
- **Hook:** C3 maintenance (Timperley p. 16); 26 % of 2014 links dead by 2019 (Fig. 3,
  p. 20); R3 asks advisors for transition plans and a Zenodo snapshot (p. 32).
- **Positions:** (a) nobody: archive a snapshot, mark it unmaintained, done; (b) the group
  or university: research software is infrastructure and needs funding (P102, p. 19).
- **If it stalls:** "Week 1: we said Docker might not exist in 40 years. Is a frozen
  snapshot enough?"

## 4. Outside-the-box questions

- **"If artifacts counted exactly like papers for your PhD and hiring, what would go
  wrong?"** Expected answers: salami-sliced artifacts, gamed GitHub stars, badges as
  metrics (Goodhart). Leads to: how should artifact *impact* be measured?
- **"Imagine AE run by an AI agent that builds and runs every artifact automatically. What
  would it catch, and what would it miss?"** Connects to the 30-minute setup rule
  (Hermann p. 472), CI checks (Timperley R2, p. 31) and "replicate the same mistake".
  Questions what human reviewers are *for*.
- (Spare) **"Should artifacts be reviewed *before* the paper, like a registered report?"**

## 5. Wrap-up

- Each person: *one* change to AE they would make, and who has to make it (author, advisor,
  AEC chair, steering committee, funder).
- Collect on the board. Check which ones neither paper proposed.
- Optional question for the lecturer: what has changed in AE since the 2020 paper?

## Quality check (two opposing answers each)

| Question | Side A | Side B |
|---|---|---|
| Warm-up | yes, it's learning | no, unpaid work |
| Q1 | low bar | high bar |
| Q2 | couple to acceptance | keep separate |
| Q3 | run scripts | probe/replicate |
| Q4 | standards first | incentives first |
| Q5 | snapshot and done | ongoing funded maintenance |

## Background to have ready

_From memory, not verified by web search in this session; check before stating as fact._

- **ACM badges v1.1 (Aug 2020):** swapped "replicated" and "reproduced". Now "Results
  Reproduced" = other team with the author's artifacts, and "Results Replicated" = other
  team, independent artifacts. This matches the lecture's slide 3/24.
- **Artifact evaluation history:** first at ESEC/FSE 2011; ICSE from 2019 (Timperley p. 4);
  many PL and SE conferences now use a "kick the tires" phase. The site
  artifact-evaluation.org (Krishnamurthi and others) collects calls and guidelines.
- **Mandatory AE:** CAV and TACAS require artifacts for tool papers (Hermann p. 469).
- **Hosting basics:** Zenodo (CERN) gives DOIs and snapshots, and can archive a GitHub
  release automatically. Software Heritage archives public source code with intrinsic
  identifiers (SWHIDs). GitHub is a living repository, not an archive.
- **Containers vs. VMs:** a container shares the host kernel (lighter, near-native speed,
  but depends on the host and its runtime). A VM emulates a whole machine (heavier, more
  isolated, distorts performance). Neither freezes the internet resources a build
  downloads, so an image must be saved, not just its Dockerfile.
- **Double-blind sharing:** anonymous hosting such as anonymous.4open.science is commonly
  used for SE submissions (Timperley C8, p. 17).
- **Funders:** NSF requires a 2-page data management plan (Timperley p. 34). Horizon Europe
  (successor of Horizon 2020) expects open-science practices and data management plans.
  The DFG (Germany) has guidelines on research software (from memory).
