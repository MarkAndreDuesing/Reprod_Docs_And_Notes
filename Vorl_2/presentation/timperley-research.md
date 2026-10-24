# Research Notes for the Timperley Discussion (Open Questions from My Annotations)

Background for the discussion-question file. Each item starts with my handwritten note and
where it sits in the paper.

**Source status:**
- acm.org blocks direct access from this environment, so ACM policy content comes from
  search results, conference calls that quote the policy, and the lecture slides.
- Anything I couldn't confirm is marked _(unverified)_.

---

## 1. How the ACM initiative operates (lecture slides 5–10/24; my notes on pp. 18 and 23)

### Where it comes from
- **ACM Task Force on Data, Software, and Reproducibility in Publication** (lecture slide 9:
  "ACM initiative 2017").
  - It grew out of the ACM Digital Library Standing Committee, set up after a 2013 strategic
    retreat, and was led by Michael Lesk (Rutgers) and Alex Wade (Microsoft Research).
  - **Aims:**
    - make software and data first-class objects in the ACM Digital Library
    - adopt or define standard metadata for software, data and methods
    - support artifact evaluation processes
  - **Output:** the **Artifact Review and Badging** policy, adopted by the ACM Publications
    Board. Version 1.0 dates from 2016–17; **version 1.1 from August 2020**.
- **2020 revision (slide 9):** a "minor revision… for compliance with **NISO RP-31-2021**"
  (*Reproducibility Badging and Definitions*, approved Jan 2021).
  - NISO is the US standards body for libraries and publishers. Its recommended practice
    gives publishers one shared set of badges and terms across disciplines.
  - To match it, ACM **swapped the meanings of "Results Replicated" and "Results
    Reproduced"**. This is the switch Hermann et al. mention in their footnote 5.

### The badges (slide 9 groups them into three questions)
Badges are **independent**: a paper can get any combination. Only one of the two Evaluated
levels is awarded.

| Question on slide 9 | Badge | What it requires |
|---|---|---|
| *Does the artifact work?* | **Artifacts Evaluated – Functional** | Documented, consistent, complete, exercisable, with appropriate evidence of verification and validation |
| | **Artifacts Evaluated – Reusable** | Functional, plus quality that "significantly exceeds minimal functionality"; documented and structured well enough for reuse and repurposing |
| *Is the artifact permanently available?* | **Artifacts Available** | Placed on a **publicly accessible archival repository** with a DOI or persistent link. Personal web pages or GitHub/GitLab alone are **not** enough; typical choices are Zenodo, Figshare, Dryad or Software Heritage. No formal evaluation needed |
| *Can the results be confirmed?* | **Results Reproduced** | (since 2020) A different team obtains the main results **using the authors' artifacts** |
| | **Results Replicated** | (since 2020) A different team obtains the main results **without the authors' artifacts** |

These match the lecture's 2020 definitions (slide 3/24).

### How it operates in practice
- **ACM defines the badges, not the process.** The interpretation and the evaluation
  process are left to each conference or community. ACM itself said it is "too early to
  establish more specific guidelines… may not be desirable at all" (the passage I marked
  pink on Timperley p. 5).
- **Typical conference process (slide 10/24; ICSE 2026 call):**
  - **Standard model:** the paper goes through peer review and is accepted; then
    the authors *optionally* submit the artifact to a separate AEC, which awards badges.
    The artifact can't affect paper acceptance.
  - **TACAS model** (slide 10; OOPSLA and ECOOP are struck through on the slide): artifact
    review runs **in parallel with paper review** and feeds into it. This is the "tighter
    coupling" that both Hermann et al. and Timperley et al. ask for.
  - **ICSE 2026:**
    - awards Available, Functional and Reusable
    - Reproduced/Replicated only for *earlier* papers, via a 2-page abstract
    - installation over **30 minutes** makes acceptance unlikely
    - Docker/VirtualBox images strongly encouraged
    - iterative author–reviewer communication via HotCRP, authors must answer within 72 h
    - no compute provided; authors must document hardware needs
- **Origins (slide 7):** artifact evaluation was pioneered at FSE 2011 and OOPSLA 2013.
  The initial criteria were: consistent with the paper, as complete as possible, well
  documented, easy to reuse. Slide 7 flags the problem: *prototypes may not be easy to
  reuse but are still useful for reproducibility*.
- **Why separate badges (slide 8, "separation of concerns"):** reusability and availability
  are orthogonal. Availability can be blocked by **IP/licensing, security and privacy**
  (citing Collberg & Proebsting). So a working artifact doesn't have to be public, and a
  public one doesn't have to work.
- **Adoption (slide 11):** from FSE alone in 2011 to about 20 SE/PL conferences by 2023,
  including ICSE from 2019. The slide asks: "Everybody does AE. Have we reached the peak of
  research excellence?"

### What this means for my notes
- **p. 18, "Should there be exceptions to AEC, like the ACM initiative, for this?"** (the
  industry paper criticised for not sharing data):
  - The ACM scheme already *is* the exception mechanism, in two ways:
    1. Evaluation is **optional and badge-based**, so a paper without a shareable artifact
       is not penalised by the process. Badges are only a bonus.
    2. Evaluated and Available are **separate**: an artifact can be evaluated, but not
       badged Available, if it can't be published.
  - Plus the "Complete" criterion: proprietary parts "need not be included" if documented
    with instructions to obtain them, and **proxy data** should demonstrate the analysis.
    ICSE 2026 also exempts raw qualitative data (share anonymised data only).
  - So P22's problem isn't the badge rules. It comes from **paper reviewers** treating
    missing artifacts as a reason to criticise, which no ACM rule covers. Discussion angle:
    should calls for papers state explicitly that missing artifacts for legal reasons must
    not count against a paper?
- **p. 23, "How does the ACM badge system rule on this?"** (reviewers without licences for
  proprietary components): no explicit rule. The policy only covers documenting proprietary
  parts. Whether a reviewer who can't run it may reject is left to each AEC. That is
  exactly the gap P65 describes, and Timperley's C6 (no standards).
- **Badge meaning differs by venue** (Hermann's finding) because ACM only defines labels.
  Slide 11's question fits here.

## 2. "Isn't this a solved problem with Zenodo?" (C7, p. 17)

**Mostly yes for normal artifacts, no for large or living ones.**
- **Zenodo** (run by CERN, funded by OpenAIRE/EU):
  - free, DOI per upload, **50 GB per record (max. 100 files)**
  - a one-time increase **up to 200 GB** for datasets, granted case by case
  - splitting one dataset across many records to dodge the limit is not allowed
  - each upload is immutable; updates become new versions with their own DOI, so the
    version cited in a paper never changes
  - GitHub releases can be archived to Zenodo automatically _(widely documented; not
    re-checked here)_
  - Zenodo promises only **bit-level preservation**: files stay intact, but old formats may
    become unreadable, so open formats are recommended
  - I found **no** formal retention period. The often quoted "20 years" refers to CERN's
    experimental programme, not a Zenodo guarantee.
- **Software Heritage:** archives public source code (with intrinsic IDs, SWHIDs). Accepted
  for the Available badge (ICSE 2025/2026), but source only, no data.
- **What Zenodo doesn't solve:**
  - data over 50–200 GB
  - **living** artifacts (use GitHub for development, Zenodo snapshots per paper; this is
    Timperley's Rec 3)
  - **runnability**: an archived artifact can still rot (C2/C3)
  - **anonymity for double-blind review** (C8). Anonymous hosts such as
    anonymous.4open.science are used for that _(from memory)_.
- **Paper context:** data collected Jan–Feb 2019. One respondent (P19) already said Zenodo
  solved the double-blind hosting problem for them. Since then, ICSE has made archival hosting a
  condition for the Available badge, so the problem is now largely solved *by rule* for
  badged artifacts.

## 3. "What if your artifact is a few terabytes?" (C7, p. 17) and "what if it exceeds a normal PC's disk? → unreviewable" (C11, p. 23)

Common options (general practice; partly from the sources below):
- **Institutional or domain repositories** with larger quotas (university research data
  services, national infrastructures). Zenodo stops at about 200 GB.
- **Share a representative subset** plus the scripts to regenerate or download the rest.
  Timperley's own Rec 2: a "representative proof-of-concept… on a smaller dataset".
- **Share the generator, not the data:** e.g. a mining script plus the exact query and date,
  when the data is public (mining studies).
- **Cloud-hosted evaluation:** the reviewer gets access to an environment where the data
  already lives, rather than downloading it. See item 4.
- So "unreviewable" mostly means "not reviewable on a laptop". AEs can review a subset, or
  review remotely, but both reduce what the badge certifies.

## 4. "Remote servers and containerisation for compute, disk and consistency? Realistic?" (C11, p. 23)

**Realistic and in use, with limits.**
- Shared research testbeds such as **Chameleon** and **CloudLab** are used for AE in systems
  research:
  - the evaluator gets the **same hardware** the authors used, including bare-metal nodes
    with A100/H100 GPUs and FPGAs
  - authors can snapshot their environment for reviewers to restore
  - Chameleon's guidance: authors flag special hardware early; reviewers get onboarding; a
    shared environment per artifact with short 1–2 day leases
- **Limits** (2025 report on systems/HPC reproducibility):
  - access is by advance reservation, so reviewers may wait **weeks**
  - learning the platform takes time
  - some venues assign 3 reviewers per artifact (ICPP), which multiplies compute use
- **Not standard in SE:** ICSE 2026 provides no compute; authors only document hardware
  needs. Timperley's Rec 7 (ACM/IEEE funding cloud credits) has not been implemented
  there, as far as I can find.
- **Containers vs. consistency:** containers fix the *software* environment, not the
  *hardware*. Combined with a shared testbed they address both, which supports my p. 22 note
  that P18's complaint is not really about containers (see item 5).

## 5. "How do we accurately verify performance claims?" (C2, p. 22) and "That's not really a problem with containers then though" (after P18)

- **VMs:** add virtualisation overhead and share the host with other loads, so absolute
  timings aren't comparable (P64; Collberg & Proebsting made the same point in week 1).
- **Containers:** run at near-native speed on the host kernel, so the VM performance
  problem largely disappears. P18's complaint is different: *build rot*. An image whose
  Dockerfile downloads packages at build time can stop building, but a **saved image**
  keeps working as long as the container runtime and CPU architecture are supported. So my
  note is fair in part: the problem is rebuilding from a recipe, not containers as such.
- **Ways AECs can handle performance claims** _(general practice; I found no source that
  covers this specifically, so treat these as reasoned options)_:
  - check **relative** claims (A is faster than B on the same machine) rather than absolute
    numbers
  - use **identical hardware** via shared testbeds (item 4)
  - authors provide raw measurement logs and scripts, so reviewers can check the analysis
    even without re-running
  - repeated runs with variance reported
  - otherwise award Functional for correctness and say explicitly that performance wasn't
    checked
- Mostly a systems/PL concern, less so for SE tools whose claims are about accuracy rather
  than speed.

## 6. "Isn't 62.69 % way more than the other studies state?" (§4.1, p. 11) and "compare [Fig. 3] with the Vorl 1 papers" (p. 20)

The numbers measure different things, so they can't be compared directly:

| Study | Sample | Counts as "artifact" | Headline |
|---|---|---|---|
| Collberg & Proebsting 2016 | 601 systems papers, 2011–12 | Code behind the paper's results (402 papers) | 32–54 % **weakly repeatable**, i.e. code obtainable *and builds* |
| Heumüller et al. 2020 | 789 ICSE papers, 2007–2017 | Runnable software only, incl. scripts (not datasets) | 76.6 % *build* software; 47.8 % of those **link** it; 27 % still downloadable in 2019 (58.5 % for 2017 papers) |
| Timperley et al. 2021 | 1434 ICSE/FSE/ASE/EMSE papers, 2014–2018 | **Any link** to external material, incl. companion sites, data, survey instruments | 62.69 % link one; ~86 % of links alive in 2019 (73.5 % for 2014, 94.6 % for 2018) |

- **Why 62.69 % is high:** the definition is the broadest (any link, not runnable code), the
  period is more recent (2014–2018 vs. 2007–2017), and the venues include EMSE. It is close
  to Heumüller's 58.5 % for 2017 alone.
- **Availability:** Heumüller's *available* rate counts only linked artifacts that can be
  downloaded. Timperley's ~86 % counts *links that still load*, without checking the content.
  Both show the same age effect, checked once in 2019: older papers have more dead links,
  which mixes "practice got better" with "older links had more time to break".
- **What none of the three checks:** whether the results can be reproduced. Collberg
  went furthest (does it build?).

## 7. "meaning?" → parallel-convergent mixed-methods design (§3.5, p. 10)

- Quantitative and qualitative data are **collected in the same phase**, **analysed
  separately**, then **merged** in one interpretation to see where the results agree or
  diverge (triangulation). Both strands carry equal weight.
- Here: the publication survey (quantitative) and the author survey (mostly qualitative)
  ran in parallel and were integrated in §4 and with DoI in §5.
- Hardest part: the integration step. Creswell and Plano Clark's standard textbook calls it
  the "convergent design" (secondary sources; I didn't consult the book).
- Already added to the Definitions section of the summary.

## 8. "How open source should research be? How feasible is this?" (C9 users, p. 20)

Background for the discussion:
- The ACM scheme deliberately separates "works" from "public" (slide 8), so full openness is
  not a precondition for evaluation.
- Funders increasingly push openness: NSF requires data management plans (Timperley p. 34),
  and EU Horizon Europe expects open science and data management plans _(from memory)_.
- Feasibility limits named in the paper: IP and contracts (C9), privacy and
  re-identification of qualitative data (p. 18), commercial tool licences (p. 20).

---

## Sources

- Lecture slides: `Vorl_1/IntroductoryLecture.pdf`, slides 3, 6–11/24
- [ACM Artifact Review and Badging, current](https://www.acm.org/publications/policies/artifact-review-and-badging-current) (cited on slides 3, 6; blocked here, content via search results)
- [ACM Task Force on Data, Software, and Reproducibility in Publication](https://www.acm.org/publications/task-force-on-data-software-and-reproducibility) (slide 9; blocked here)
- [ACM: New Changes to Badging Terminology](https://www.acm.org/publications/badging-terms)
- [Artifact Review and Badging v1.0 (not current)](https://www.acm.org/publications/policies/artifact-review-badging/)
- [CACM: Incentivizing reproducibility (2016)](https://cacmb4.acm.org/magazines/2016/10/207757-incentivizing-reproducibility)
- [Rous, STM 2017 slides on the ACM reproducibility initiative](https://stm-assoc.org/wp-content/uploads/2024/08/2017_04_26_Annual_Conference_Rous_Reproducibility-1.pdf)
- [NISO RP-31-2021 Reproducibility Badging and Definitions](https://www.niso.org/publications/rp-31-2021-badging) and [press release](https://www.niso.org/press-releases/2021/01/nisos-recommended-practice-reproducibility-badging-and-definitions-now)
- [ICSE 2026 Artifact Evaluation call](https://conf.researchr.org/track/icse-2026/icse-2026-artifact-evaluation), [ICSE 2025 call](https://conf.researchr.org/track/icse-2025/icse-2025-artifact-evaluation)
- [MICRO 2024 AE reviewing guidelines](https://ctuning.org/ae/reviewing-micro24.html)
- [Zenodo size limitations](https://support.zenodo.org/help/en-gb/1-upload-deposit/80-what-are-the-size-limitations-of-zenodo), [Zenodo quota increase](https://help.zenodo.org/docs/deposit/manage-files/quota-increase), [Zenodo general policies](https://about.zenodo.org/policies), [Zenodo records help](https://help.zenodo.org/docs/deposit/about-records/)
- [Chameleon: Using Chameleon for artifact evaluation](https://blog.chameleoncloud.org/posts/using-chameleon-for-artifact-evaluation), [Running artifact evaluations on Chameleon](https://blog.chameleoncloud.org/posts/running-artifact-evaluations-on-chameleon)
- [Report on Challenges of Practical Reproducibility for Systems and HPC CS (2025)](https://arxiv.org/pdf/2505.01671)
- [ATLAS.ti guide: convergent parallel design](https://atlasti.com/guides/the-guide-to-mixed-methods-research/convergent-parallel-design)
- Week-1 numbers: `Vorl_1/discussion/cross-paper.md`
