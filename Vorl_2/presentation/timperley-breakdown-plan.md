# Plan: Breaking Down Timperley et al. (2021), Abstract to §4 Results

My part in the discussion round: summarise the paper from the Abstract to the end of
§4 Results (pp. 1–24). Section 5 onward is excluded; my handwritten note "split here"
on p. 24 marks the cut. This file merges my plan notes with what is actually in my
annotated copy (`s10664-021-09973-5_annotated.pdf`). The annotation inventory is at the
end, so the summary and question steps can work from it directly.

_Page numbers are the paper's "Page x of 41" = PDF pages._

## Colour code (from p. 1 of the annotated copy)

| Colour | Meaning | Where it goes |
|---|---|---|
| Green | Material to summarise | Bullet points under the matching section header |
| Yellow | Background definitions | Dedicated **Definitions** section |
| Pink | Potential discussion point | Noted now, used in the question step |
| Bar on the left edge | The whole paragraph to the right counts as highlighted in that colour | Same as above |
| Blue handwriting | Comments; arrows show which passage they refer to | Instruction (how to summarise), discussion seed, or open research question (see inventory) |

## Output document structure

Target file: `Vorl_2/presentation/timperley-summary.md` (summary only; the discussion
questions go in a separate file, see below). Keep the paper's order, with one
header per section or subsection and exhaustive but non-redundant bullets.

1. **General summary** (from the Abstract, green). Problem, goal, method (publication
   survey + survey of 153 researchers), main findings (challenges incl. mismatched
   expectations and missing reward), DoI analysis, recommendations.
   - My p. 1 header note frames it: *"So the past 2 papers were: why there are so few
     working artifacts, and potential solutions. Now we have: why making good artifacts
     is hard (+ a bit of overlap)."* Use this as the one-line framing at the top.
2. **Definitions** (all yellow, collected in one place, one bullet group per term):
   - Artifact: tools, benchmarks, datasets (§1, p. 2); the paper's own definition, "any
     external material… via a link", and its examples (§2.1, pp. 3–4); the ACM definition
     (edge bar, p. 4); motivations for sharing (replicate, reproduce, build upon)
   - AEC (my note on p. 4: "Artifact Evaluation Committee")
   - ACM badges: Available / Evaluated (Functional, Reusable) / Results Validated; FSE and
     ICSE participate since July 2020; badges shown on the paper's front page (p. 4)
   - Artifact quality criteria: documented, consistent, complete, exercisable (pp. 4–5)
   - Diffusion of Innovations and its four elements: innovation, communication channels,
     time, social system (pp. 5–6)
   - Implementation Science (p. 6)
   - Descriptive coding, axial coding, thematic analysis (pp. 8–9)
   - Secondary analysis (p. 9)
3. **§1 Introduction.** My notes on p. 2 say the introduction is "basically just a
   long-winded reiteration of the abstract". So: *no separate block*. Merge each
   green point into the later section that covers it in more detail (badging → §2.2
   definitions; the four problem areas, communication / social system / time /
   technical, and "AECs are well positioned" → general summary; contributions list →
   method overview). Points mentioned **only** here get their own short "Introduction"
   bullets:
   - recent work (Collberg et al.) shows many artifacts can't be reused, extended or
     replicated (missing documentation, unstated dependencies), and the controversy around
     it shows there are no clear community standards (p. 2)
   - badging processes assess claims, uncover usability issues and signal quality, but
     their implementation has met "both praise and criticism" (p. 2)
4. **§3 Methodology** (green), with subheaders:
   - RQ1, RQ2, RQ2.1–2.3 (p. 6). My note on p. 6 says the mixed-methods / secondary
     analysis paragraphs are "once again duplicate with intro", so state them once.
   - Fig. 1 study overview (p. 7). My note: *"see if explaining these terms is in scope
     too, or too much detail"*. Decision: name the terms in one line here and define them
     only in Definitions (axial/thematic coding are already yellow on p. 9).
   - §3.1 Publication survey: technical-track papers 2014–2018; 899 artifacts in 1434
     papers; availability = URL reachable at inspection time (p. 7)
   - §3.2 Author survey: online questionnaire, 28 questions, branching logic by
     subpopulation (p. 7); response rate paragraph (edge bar, p. 8: 744 emails, 46 bounced,
     153 of 698 = 22 %); Table 2 roles/subpopulations (p. 8)
   - **Table 1** (p. 8). My note: *"summarise and sort these by research question"*. Make a
     compact list grouped as RQ1 (Q5, Q10, Q12), RQ2.1 (Q3, Q4, Q6–Q9), RQ2.2 (Q11),
     RQ2.3 (Q13–Q15), all RQs (Q16), demographics (Q1, Q2).
   - §3.4 Recommendations: assessed against IS principles; target subgroups (creators =
     primary researchers + mentors/advisors, reviewers, process organisers, community
     leaders) (pp. 9–10). My note on p. 9: *"see how important this info actually is to
     keep, considering limited space"*. Decision: one line per subgroup, no more.
   - §3.5 Threats to validity: replicability, construct, internal, external, each in one
     or two bullets (pp. 10–11). My note "meaning?" on p. 10 points to the
     "parallel-convergent design / subsequent integrated analysis" sentence, so add a
     plain-language explanation (see research list).
5. **§4.1 RQ1** (green): 62.69 % of papers contain an artifact; positive sentiment;
   sharing should be encouraged and rewarded; replication difficult without artifacts;
   **Table 3** motivations (supporting evidence, community norms, reuse, understanding).
   Close with the "Insights for RQ1" box. My note on p. 13 calls it a *"good
   repetition/summary"*, so use it as the section's summary line rather than repeating
   the bullets.
6. **§4.2 RQ2, merged by challenge C1–C12** (see the format decision below). Kept
   strictly apart from §4.1 RQ1: nothing from the RQ1 results is repeated here.

## Format decision for §4.2 (from my open question)

> "have to think about how to merge results segments, maybe a table with a column for
> each of the 3 perspectives? or is that a waste of space? Or just do Table 4 but drop
> the representative quote column…"

**Recommendation: both, in two layers.**

- **Layer 1, overview table (replaces Table 4).** Columns: `C | Challenge | Creator |
  User | Reviewer | Merged description`. Tick marks (■ ▲ ★ as in the paper) instead of
  text in the three perspective columns. A text column per perspective *would* waste
  space: the matrix is sparse (C1 and C8 are creator-only, C5 is user-only, C10–C12 are
  reviewer-only), so most cells would be empty. The description column holds the merged
  one-to-two-line summary. No quotes.
- **Layer 2, one header per challenge** (`### C2 Portability (■ ▲ ★)`) with merged
  bullets. The general problem is stated once. Points that only one perspective raised
  get a short tag, e.g. **[user]** "hard-wired paths to the author's home directory,
  requires root" or **[reviewer]** "VMs make performance claims unverifiable". This
  keeps every highlighted idea without repeating the shared core three times.
- Numbers from **Table 5** (user challenges, p. 19), **Fig. 3** (14 % inaccessible,
  26.47 % for 2014 vs. 5.43 % for 2018, p. 20) and **Fig. 4** (FSE: 281 papers, 196 with
  artifacts, 74 submitted, 64 accepted, p. 21) go under the challenge they belong to (C2,
  C4, C5, C7), not in a separate block.
- The three "Insights for RQ2.x" boxes become a final 3-line "Insights" summary per
  perspective, the same way the RQ1 box is used.

### Which perspective contributes what (from the green highlights)

| C | Creator (§4.2.1) | User (§4.2.2) | Reviewer (§4.2.3) |
|---|---|---|---|
| C1 Not worth it | ✔ cost, career, opportunity cost; risks (reputation, scooping, mistakes found, maintenance, no users); untapped publication value; limited audience; counter-quote "whole research areas dead" (p. 15) | | |
| C2 Portability | ✔ anticipating environments; retroactive refactoring / VM / container; test in several environments; VM images too big; no time to document | ✔ hard-wired paths, root; Table 5 counts | ✔ installing dependencies; invasive libraries; VMs for security, but huge, cross-OS problems, no performance assessment; containers don't stop degradation |
| C3 Maintenance | ✔ ongoing investment; bugs, evolving use cases, bitrot; students responsible, then leave | ✔ hard-to-find old libraries, unmaintained | |
| C4 Tacit knowledge | ✔ documentation burden; knowledge "in developers' heads"; prototypes evolve fast; automate usage | ✔ lack of documentation and poor code quality; "guidance… takes time" | ✔ couldn't reproduce from instructions alone; automation not a panacea (black box, replicates the same mistake); documentation still needed |
| C5 Doesn't fit purpose | | ✔ doesn't serve the purpose stated in paper; very limited use cases | |
| C6 Standards and guidelines | ✔ unclear packaging, contents, quality; how to handle existing datasets; community lacks guidelines (setup, contribution guides) | | ✔ ambiguous review guidelines and criteria; ACM badge text "confusing", "too general"; unclear purpose (run scripts vs. deep investigation); unclear link to paper shepherding |
| C7 Hosting | ✔ long-term, large, affordable; GitHub/Dropbox/Drive not archives | ✔ unable to access (2nd most common); 14 % dead links, older more likely | |
| C8 Double-blind | ✔ anonymise artifact; anonymous hosting | | |
| C9 External constraints | ✔ IP, privacy, larger ecosystem; liability; re-identification risk of qualitative data | ✔ licensing; decompiling; paid licences for auxiliary tools | ✔ reviewers lack licences; no pathway for proprietary components |
| C10 Reviewer incentives | | | ✔ time and effort not rewarded like paper review; "just make students do AEC"; inconsistent, low-quality reviews |
| C11 Technical obstacles | | | ✔ long execution times; compute; > 1 day artifacts; disk space; some experiments practically infeasible (cloud, fuzzers, program repair) |
| C12 Limited communication | | | ✔ single-round reviews; minor glitches shouldn't reject; owners willing to help; unresponsive authors, waiting days |

Plus the reviewer-section intro (p. 21): few artifact papers are submitted for evaluation
even when possible; some reviewers are happy with the current process.

## Next step after the summary: discussion questions

Target file: `Vorl_2/presentation/timperley-discussion-questions.md`, **separate from the
summary file**, with the same headers as the summary so each block of questions sits
under the section it belongs to.

Rules:

- **3 questions** per unit, **5 questions** if the unit contains a **pink** block.
- **Units:** §1, §2.1–2.4, §3.1–3.5, §4.1 (RQ1), and **each challenge C1–C12 on its own**
  under §4.2 (RQ2). §4.1 and §4.2 stay strictly separate: RQ1 is about *whether the
  community values artifacts*; RQ2 is about *the challenges*. No RQ1 material goes under a
  challenge and vice versa.
- Questions build mainly on the **exact pink-marked lines** (list below) and on my
  handwritten comments (inventory, types D and R).
- **Research first** for notes that are really open questions (type R), then turn the
  answers into background facts and follow-up questions.
- Keep the paper's own **recommendations** in mind (§6, called Rec 1–Rec 8 here so
  they aren't confused with RQ1/RQ2). A good question can ask whether the matching
  recommendation would actually fix a challenge: C1 ↔ Rec 7 (hiring/promotion credit),
  C2 ↔ Rec 2 (CI, containers), C3 ↔ Rec 3 (maintenance and transition plans), C6 ↔
  Rec 4/Rec 5 (rubric, published criteria), C7 ↔ Rec 3 (Zenodo/Software Heritage), C10 ↔
  Rec 6/Rec 7, C11 ↔ Rec 6/Rec 7 (compute credits), C12 ↔ Rec 6 (two-way anonymous
  communication).
- Same quality test as in `moderation.md`: each question needs a hook in the text and two
  defensible opposing answers.

### Exact pink-marked lines per unit

Line ranges were measured from the annotation layer: the lines next to each pink edge
bar, or under an inline pink highlight. Quotes are shortened to the start and end of the
marked lines.

**§2 Background → 5 questions for §2.2; 3 for §2.1, §2.3, §2.4**
- §2.2, p. 5 (3 lines): ACM: "We believe that it is still too early to establish more
  specific guidelines for artifact and replicability review… sufficient diversity among
  the various communities… may not be desirable at all."

**§3 Methodology → 5 questions for §3.1, §3.2, §3.4, §3.5; 3 for §1 and §3.3**
- §3.1, p. 7 (3 lines): "we identified 899 artifacts across 1434 papers. Finally, we
  determined the availability of each artifact by manually checking that its associated
  URL could be accessed at the time of inspection (Jan 29th – Feb 6th, 2019)."
- §3.2, p. 9 (3 lines): "A thematic analysis does not tell us how prevalent each of the
  experiences… might be, only that they are present in the social context."
- §3.4, p. 9 (inline, 1½ lines): "ensure that it does not exacerbate any known
  challenges, is compatible with existing practices, and is likely to be scalable,
  sustainable, trialable, and observable."
- §3.4, p. 9 (3 lines): "Each of these recommendations can be implemented, trialed,
  observed, and evaluated to determine whether it has achieved its intended outcome."
- §3.5, p. 10: the **heading "3.5 Threats to Validity"** itself is marked pink, so the
  whole section is a discussion area. Plus:
  - replicability (inline, 2 lines): "as much of our materials available as possible,
    while still preserving the confidentiality of the survey respondents"
  - construct (3 lines): "papers could have artifacts that are not documented in the
    paper, which could potentially be found only by searching, or contacting the authors
    of the paper. We did not contact authors for practical reasons…"
  - internal (2 lines): "Did we skew the accuracy of our results with how we collected
    and analyzed information? Surveys can be affected by intentional and unintentional
    bias…"
  - p. 11 (4 lines): "we define an artifact as being available if the link is still
    alive… completely unusable, or… links to a download that is no longer available…
    evaluating the quality of artifacts is beyond the scope of this work"
  - external, p. 11 (2 lines): "Because of the nature of surveys, we cannot generalize
    our results beyond our survey population. Perhaps if we had chosen a different…"

**§4.1 RQ1 → 5 questions**
- p. 11 (3 lines): "almost two thirds (62.69 %) of papers published at ASE, EMSE, FSE,
  and ICSE between 2014 and 2018 (inclusive) contain an artifact. Furthermore, across
  all venues… the proportion…"

**§4.2 RQ2, per challenge**

| C | Questions | Pink-marked lines (page, length) |
|---|---|---|
| C1 Not worth it | 5 | p. 13 (4 lines): "risks that outweigh the potential rewards… poor code quality may harm their reputation, a fear of being 'scooped', a fear of mistakes in the analysis being discovered, the burden of maintaining the artifact, and the possibility that the artifact may be used by no one." · p. 13 (3 lines): "reluctant to share artifacts that still have some untapped publication value, or may wish to avoid being 'scooped'… 'sometimes, one needs to protect a Ph.D. students abilities to…'" |
| C2 Portability | 5 | p. 21 (3 lines, reviewers): "VMs can be used to mitigate these portability challenges and to avoid the security risks of executing untrusted code… However, VMs are not without their own problems." · p. 22 (9 lines, reviewers): from "running across different OSes leads to problems and sizes are huge" through P64 "not really possible to accurately assess performance, nor should the authors be penalised…" and "containers… to address performance and size concerns" to P18 "Something that compiles today is probably not to compile in five years… having containers does not always solve this problem." |
| C3 Maintenance | 5 | p. 16 (4 lines, creators): "Sharing an artifact not only requires an upfront investment… but also an ongoing investment to continually maintain the artifact. As bugs are uncovered, use cases evolve, and inevitable bit rot occurs, there is a need to update the artifact." |
| C4 Tacit knowledge | 5 | p. 16 (3 lines, creators): "tacit knowledge remains a major obstacle to artifact creators… 'the main difficulty is to provide a highly automated way to utilize the artifact. A lot of knowledge is typically buried in developers' heads.'" · p. 22 (10 lines, reviewers): "Some reviewers suggest that automation… may be used to mitigate the tacit knowledge problem. However… not a panacea" → P74 "difficult to know whether the submitted device is faulty, or if [you don't know how to] use it" → script as "a blackbox… no insight into whether the process… is sound" → P25 "likely to replicate the same mistake (if any) the original authors made." |
| C5 Doesn't fit purpose | 3 | none |
| C6 Standards and guidelines | 5 | p. 22 (4 lines, reviewers): "The purpose of the artifact review process itself is often unclear… running a set of automated scripts to replicate a result, or… a more thorough investigation of the assumptions, limitations, and generality of the artifact." · p. 23 (3 lines): end of P6 quote, "deep-dive into the code and occasionally uncover severe problems… extremely time-intensive… multiple days of work. But if the AEC doesn't do it, will anybody ever? Probably not." · p. 23 (8 lines): from "[an improperly] implemented benchmark should be grounds for paper rejection" through P11 (evaluate as part of paper), P124 / P146 (artifacts mandatory) to P143 "rubber stamping… less [of] a burden to get an artifact 'stamp'. Often, many papers…" |
| C7 Hosting | 5 | p. 17 (4 lines, creators): P12 "share a large dataset that does not fit into a GitHub repo or Dropbox… Google Drive, GitHub, and Dropbox… not intended as a long-term archive, and are ill-suited to large datasets." · p. 20 (Fig. 3 caption, users): availability over time, checked once in Jan/Feb 2019 |
| C8 Double-blind | 3 | none |
| C9 External constraints | 5 | pp. 17–18 (inline, creators): P22 "once criticised for not sharing data for an industry track paper coauthored with practitioners. Artifact should not be used as ritualistic blanket argument to judge papers." · p. 20 (6 lines, users): whole C9 user paragraph: licensing, P35 decompiler and no replication package, P9 paid commercial licence for auxiliary tools · p. 23 (4 lines, reviewers): "reviewers may not possess the necessary licenses… P65 'no obvious pathway… proprietary component (Windows, a commercial IDE). Some legal clarity…'" |
| C10 Reviewer incentives | 5 | p. 23 (4 lines): "gets students involved in the reviewing process. But it also reinforces the idea that artifacts are not a primary thing… may lead to inconsistent and low-quality reviews due to reviewers that are not fully invested." |
| C11 Technical obstacles | 5 | p. 23 (5 lines): from the C11 heading, "long execution times and a lack of adequate compute resources… P50 'what to do for artifacts that by nature take more time than one can devote to evaluating a single artifact (~ one day)'… significant disk space, such as virtual machine…" · pp. 23–24 (5 lines): "practically infeasible to replicate an experiment via an artifact… P64 'reviewers do not often have the capabilities to actually run the artifact… cloud-based contributions, fuzzers, automated program repair, require significant hardware…'" |
| C12 Limited communication | 5 | p. 24 (5 lines): "takes a considerable amount of time to build an artifact and a minor glitch in the installation instructions should not be grounds for rejection… P133 'understandable that an artifact from a researcher is not perfect. An important thing is that the owners of the artifact are willing to help the users resolve outstanding issues'" |

Also marked pink, attached to the challenges it lists: **Table 5** (p. 19, whole table,
users). Questions about it go under C4 (instructions, 103 and 79), C7 (no longer
accessible, 81) and C2/C5 (build, run, modify, reimplement), not as a separate unit.

## Open research questions (to look up before writing questions)

From my handwritten notes that ask for facts rather than opinions:

1. **"Isn't this a solved problem with Zenodo?"** (C7, p. 17). Zenodo's size limits,
   longevity guarantees, DOIs, GitHub integration; Software Heritage; what is *not* solved
   (very large data, living versions).
2. **"What would you do if your artifact was a few terabytes large?"** (C7, p. 17) and
   **"what if the artifact exceeds the disk space of a conventional PC? → unreviewable
   with this approach"** (C11, p. 23). Options for very large artifacts (institutional
   repositories, data subsets, cloud-hosted evaluation).
3. **"Isn't 62.69 % way more than the other studies state?"** (§4.1, p. 11). Compare with
   Heumüller (week 1: 76.6 % *build* software, 47.8 % *link* it) and Collberg; explain
   that the definitions differ ("any link" vs. runnable code).
4. **"Compare [Fig. 3 availability] with those from Vorl 1 papers"** (p. 20). Line up the
   availability / link-rot numbers of Collberg, Heumüller and Timperley.
5. **"How does the ACM badge system rule on this?"** (proprietary components, C9
   reviewers, p. 23). What ACM policy says about proprietary data and software (the
   "Complete" criterion allows proxies, p. 5).
6. **"What about using remote servers and containerisation to avoid the compute, disk
   space and consistency issues? Realistic?"** (C11, p. 23). Do AECs offer cloud
   resources today (e.g. compute credits, Chameleon, CloudLab)?
7. **"How do we accurately verify performance claims?"** (C2 reviewers, p. 22). How AECs
   handle performance artifacts (bare-metal access, relative rather than absolute
   numbers).
8. **"meaning?"** → "mixed-methods parallel-convergent design … subsequent integrated
   analysis" (§3.5, p. 10). Plain-language definition, for the Definitions section.
9. **"Do you think there should be exceptions to AEC like the ACM initiative to account
   for this?"** (C9, p. 18; industry papers). Do venues have exemptions or industry-track
   rules for artifact sharing?

## Annotation inventory

Types: **I** = instruction for summarising, **D** = discussion seed, **R** = research
question. "Edge" = bar on the left margin.

| Page | Where (arrow target) | Highlight | Handwritten note | Type |
|---|---|---|---|---|
| 1 | Top of page, general | — | "So the past 2 papers were: why there are so few working artifacts and potential solutions. Now we have: why making good artifacts is hard (+ a bit of overlap)" | I (framing) |
| 1 | Legend | green / yellow / pink | "summary", "definitions", "potential discussion" | I |
| 2 | Edge blocks: para 2 (from "for an artifact to be useable…"), "In this paper…", "We find that…" continuing to p. 3 contributions list | green edge | "basically just a long-winded reiteration of the abstract. Merge into bullet-point notes along with the actual full [content] section" (the last word is hard to read; possibly "conclusion") | I |
| 2 | Para 1–2 | yellow words/edge | Artifacts, tools, benchmarks, datasets | definitions |
| 4 | "AEC" in §2.2 | — | "Artifact Evaluation Committee" | I (definition) |
| 4 | ACM artifact definition; Documented/Consistent | yellow edge | — | definitions |
| 5 | ACM quote "too early to establish more specific guidelines… may not be desirable at all" | pink edge | — | D |
| 6 | Mixed-methods paragraph and secondary-analysis paragraph | green edge | "once again duplicate with intro" | I |
| 7 | Fig. 1 (axial/thematic analysis terms) | green caption | "see if explaining these terms is in scope too, or too much detail" | I |
| 7 | "identified 899 artifacts across 1434 papers… availability… URL" | pink edge | — | D |
| 8 | Table 1 | green caption | "summarise and sort these by research question" | I |
| 8 | Response-rate paragraph | green edge | — | summary |
| 9 | "thematic analysis does not tell us how prevalent…" | pink edge | — | D |
| 9 | IS criteria "does not exacerbate… scalable, sustainable, trialable, observable" | pink | — | D |
| 9 | "Each of these recommendations can be implemented, trialed…" | pink edge | — | D |
| 9 | Subgroup list (creators … community leaders) | green edge | "see how important this info actually is to keep, considering limited space" | I |
| 10 | §3.5 heading | pink | — | D (whole threats section) |
| 10 | "as much of our materials available as possible, while still preserving confidentiality" | pink | — | D |
| 10 | Construct: "artifacts that are not documented in the paper…" | pink edge | — | D |
| 10 | "parallel-convergent design … subsequent integrated analysis" | — | "meaning?" | R |
| 10 | Internal validity | pink edge | — | D |
| 11 | "available if the link is still alive…" | pink edge | — | D |
| 11 | External validity | pink edge | — | D |
| 11 | "almost two thirds (62.69 %)…" | pink edge | "isn't that way more than the other studies state?" | R + D |
| 13 | "Insights for RQ1" box | — | "good repetition/summary" | I |
| 13 | Perceived risks (fear of mistakes being discovered) | pink edge | "that's the point of review though" | D |
| 13 | Perceived risks (poor code, scooping, mistakes) | pink edge | "How much personal accountability should you expect?" | D |
| 13 | "reluctant to share artifacts that still have untapped publication value… scooped" | pink edge | "halting research progress?" | D |
| 16 | C3 Maintenance opening | pink edge | "unavoidable with development of technology? Ways to mitigate this?" | D |
| 16 | C4 "tacit knowledge… highly automated way" | pink edge | "implicit human problem. What are ways to tackle this?" | D |
| 17 | C7 hosting paragraph (arrow loops round to "not intended as a long-term archive") | green | "Isn't this a solved problem with Zenodo?" | R |
| 17 | "share a large dataset that does not fit into a GitHub repo or Dropbox" | pink edge | "What would you do if your artifact was a few terabytes large?" | R + D |
| 17–18 | P22 "once criticised for not sharing data for an industry track paper… ritualistic blanket argument" | pink | "Do you think there should be exceptions to AEC like the ACM initiative to account for this?" | D (+R) |
| 19 | Table 5 | pink edge, green counts | — | D |
| 20 | C9 users: licensing, decompiler, paid licences | pink edge | "How open source should research be? How feasible is this?" | D |
| 20 | Fig. 3 | pink edge | "compare with those from Vorl 1 papers" | R |
| 21 | "Virtual machines can be used… However, VMs are not without their own problems" | pink edge | — | D |
| 22 | VM/performance passage (P64) | pink edge | "how do we accurately verify performance claims?" | R + D |
| 22 | After P18 "containers does not always solve this problem" | — | "That's not really a problem with containers then though" | D (my counterpoint) |
| 22 | Reviewers' C4 (could not reproduce from instructions) | — | "how much effort/resources/finances should reviewers be expected to invest?" | D |
| 22 | Automation "not a panacea" passage | pink edge | "scripts can't help gain this understanding" | D |
| 22 | C6 heading (reviewers) | — | "Isn't that what an AEC does, set guidelines? Look into these in detail to find discussion questions? → how would you rewrite these?" | D |
| 22 | "purpose of artifact review is unclear… run scripts or thorough investigation" | pink edge | — | D |
| 23 | Rest of P6 quote ("But if the AEC doesn't do it, will anybody ever?") | pink edge | — | D |
| 23 | Shepherding / AE as precondition / rubber stamping passage | pink edge | "what is the point of review if you're just rubber stamping anyway?" | D |
| 23 | C9 reviewers: licences, proprietary components | pink edge | "→ how does the ACM badge system rule on this?" / "once again, whose responsibility is this, should financial investment be expected from reviewers? or is automatic badge rejection fair for using inaccessible tools/libraries?" | R + D |
| 23 | C10 "just make students do AEC… not a primary thing" | pink edge | — | D |
| 23 | Between C10 and C11 | — | "should be provided? → what about using remote servers and containerisation to avoid the compute, disk space and consistency issues? Realistic?" | R + D |
| 23 | C11 "more time than one can devote… (~ one day)" | pink edge | "Is it fair to have a flat time cutoff for rejection?" | D |
| 23 | After P52 large VM / slow downloads | — | "very amateurish, what if the artifact exceeds the disk space of a conventional PC? → unreviewable with this approach" | D + R |
| 23–24 | "practically infeasible to replicate… cloud-based, fuzzers, program repair" | pink edge | "damaging to the scientific process if we can't reproduce!" | D |
| 24 | C12 "minor glitch… not grounds for rejection"; "owners willing to help" | pink edge | "is this actually sustainable though? Support can't be there forever" | D |
| 24 | Above §5 heading | — | "split here" | I (scope end) |

Note: the `.sdocx` file is the Samsung Notes source of the same annotations. The exported
PDF contains everything, so only the PDF is kept in the repo.
