# Hermann, Winter & Siegmund (2020): Condensed Notes

_Page numbers are printed proceedings pages (469–480 = PDF pages 1–12)._
_Co-author Stefan Winter is the seminar lecturer._

## Core claims
- AE (artifact evaluation) has spread since its FSE 2011 pilot, but there is **no evidence yet that it leads to better artifacts** (p. 469).
- There are no clear, shared quality criteria. Calls for artifacts (CfAs) and the ACM guidelines don't set thresholds, so a badge only means something in the context of one conference and year (pp. 470, 478).
- The perceived purpose has grown from "check the paper's claims" to **replicability and reusability**. Reviewers stress replicability, users stress reusability (p. 479).
- The terminology for AE's central purpose is used inconsistently (pp. 471, 474).

## Key definitions
- **Artifact:** Méndez et al.'s definition: "a self-contained work result, having a context-specific purpose…" (p. 470).
- **ACM terms as used in the paper (pre-2020 version, p. 471):**
  - repeatability = same team, same setup
  - replicability = different team, **same setup**, the declared target of AE
  - reproducibility = different team, different setup, the "ultimate goal"
- **Footnote 5 (p. 471):** ACM swapped replicability and reproducibility after the paper was accepted. The paper keeps the old meanings.
- **Mapping to the lecture's 2020 definitions:** the paper's *replicability* = 2020 **reproducibility** (author's artifacts, different team). The paper's *reproducibility* = 2020 **replicability** (independent artifacts).
- ASA definition (p. 471): reproducible = same analysis on the same data. A third, again different, usage.
- **Badges (p. 471):** Available, Evaluated–Functional (documented, consistent, complete, exercisable), Evaluated–Reusable, and two result badges.

## Study method
- **Pre-study (§3, p. 471):** 79 CfAs from SE and PL conferences, 2011–2019, plus the ACM guidelines. One researcher coded them and a second confirmed. A plagiarism checker was used to spot copied passages.
- **Survey (§4.1, p. 472):** sent to **1034** AEC members from 2011–2019 with open questions, piloted with 6 people.
  - 257 responded and 124 completed. Two responses were excluded.
  - 152 named their AEC: 125 PL, 36 SE, 9 both. The response rate is about 25 %.
- **Analysis:** open card sorting (Hudson). One author labelled the answers and a second checked. Counts are given as total (PL/SE).
- **Not checked:** any actual artifact; whether badges predict quality; authors' or non-reviewers' views.

## Findings
- **CfAs (pp. 471–472):**
  - 61 of 79 calls state a purpose: reuse 32, reproducibility 24, comparison 17, replicability 6, repeatability 4. PL calls favour reproducibility.
  - 14 calls give no evaluation criteria and 22 give no submission criteria.
  - The most common criteria are documentation (46), consistency (45), completeness (39) and reusability (36). Eight calls copy the ACM text verbatim.
  - The **only real threshold** anywhere is "setup and basic test in < 30 min" (10 calls).
  - Calls list artifact types (code 49, data 43, proofs 25) but almost never give type-specific evaluation criteria (2 calls).
- **Purpose (RQ1, pp. 473–474):** 147 answers.
  - Fostering: reproducibility 34, reusability 26.
  - Checking: validating claims 28, results 23.
  - The authors assume that "reproducibility" means replicability (p. 473).
- **Reviewer view (pp. 474–476):**
  - Minimum requirements: replicability of results 45, good documentation 43, easy setup 37. For SE alone, replicability is only third.
  - Code: documentation and "compiles and runs". Code quality is disputed: 19 want it, 12 don't.
  - Proofs: understandability and completeness.
  - Data: format description, raw data, and scripts to get from raw data to the paper's plots.
  - Some reviewers favour availability over quality (id 96).
  - ICSE/FSE dropped the Functional badge (FSE since 2018) and award only Reusable or Available.
- **User view (pp. 476–477):**
  - Mostly satisfied: code 45/12, proofs 10/2, data 25/7.
  - 20 see a difference between evaluated and unevaluated artifacts, 34 don't.
  - Only 76 respondents have reused an artifact at all.
  - Users name reusability (14) more often than replicability (6).
- **Further insights (pp. 477–478):**
  - Effort is seen as justified; one reviewer caught a fraudulent artifact with hard-coded outputs.
  - Only half are satisfied with the process. 13 of 66 complain about the missing quality standard.
  - Only 8 of 16 conferences in 2019 had a "kick the tires" phase.
  - 13 want AE coupled more tightly to paper acceptance, unprompted.
  - 76 of 115 (66.1 %) reviewers have submitted an artifact themselves, so a third have never built one.
  - Most reviewers serve only once (Fig. 2).

## Recommendations (p. 479)
- Define the purpose of AE per community, with a committee that monitors change.
- Agree quality standards per community and per artifact type, and write them **into the CfAs**, not into the discipline-wide ACM guidelines.
- Chairs should brief one-time reviewers on acceptance levels.
- Recruit reviewers who have created artifacts themselves.
- Couple AE more tightly to paper acceptance; tool tracks (CAV, TACAS) can lead.
- State the terminology explicitly in every CfA (p. 471).

## Critique (tightened)
- The survey only reached reviewers, mostly PL. The "user" perspective comes from the same people, so it is reviewers looking at their own reuse.
- Counts from open card sorting look precise but depend on one labeller's choices. Small PL/SE differences (e.g. 7 vs 9) mean little.
- PL/SE totals differ between sections: 125/36 on p. 472 vs 131/43 on p. 474.
- Counterpoint: the paper is explicit that it is qualitative and a "first step". The CfA analysis is a solid, reproducible document study, and its data is published [12].

## Discussion points (merged)
- Terminology: the paper "corrects" respondents who said reproducibility. Under the 2020 definitions the respondents were right.
- Is a 30-minute setup limit a quality standard or just a convenience rule?
- Availability over quality (id 96): a low bar for more sharing vs. a high bar for meaningful badges.
- Should AE decide paper acceptance?
- Junior, one-time reviewers: who checks the checkers?
