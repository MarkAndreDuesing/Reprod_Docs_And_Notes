# Research Notes for the Timperley Discussion (Open Questions from My Annotations)

Background for the discussion-question file. Each item starts with my handwritten note and
where it sits in the paper.

**Source status:**
- acm.org blocks direct access from this environment, so the ACM policy wording was
  verified via pages that quote it verbatim (ACM SIGIR, ESEC/FSE 2021, ICSE 2026 calls)
  and the lecture slides.
- Every point below was checked with a web search. Where no source exists, the point is
  marked _(my reasoning)_.

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
| *Can the results be confirmed?* | **Results Reproduced** | (v1.1, 2020) "The main results of the paper have been obtained in a subsequent study by a person or team other than the authors, using, in part, artifacts provided by the author" |
| | **Results Replicated** | (v1.1, 2020) The same, but obtained **without relying on** the author-supplied artifacts |

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
  - **GitHub integration:** once a repository is switched on in Zenodo, each new GitHub
    release is archived automatically with a DOI per version plus a "concept DOI" for all
    versions. Releases made before switching it on aren't archived. ICSE 2026 accepts
    "GitHub linked to a Zenodo DOI" for the Available badge.
  - Zenodo promises only **bit-level preservation**: files stay intact, but old formats may
    become unreadable, so open formats are recommended
  - **Retention policy:** "Items will be retained for the lifetime of the repository. This
    is currently the lifetime of the host laboratory CERN, which currently has an
    experimental programme defined for the next 20 years at least." Metadata is stored
    separately and stays available even if the data doesn't. Zenodo makes "no promises of
    usability and understandability" over time.
  - For comparison: most funder data-retention requirements are 10–20 years.
- **Software Heritage:** archives public source code. Each archived object gets a
  **SWHID**, a cryptographic hash of its content, so the same code always has the same ID,
  standardised as ISO/IEC 18670. ICSE 2026 names it as an archival option for the Available
  badge. Source code only, no data.
- **What Zenodo doesn't solve:**
  - data over 50–200 GB
  - **living** artifacts (use GitHub for development, Zenodo snapshots per paper; this is
    Timperley's Rec 3)
  - **runnability**: an archived artifact can still rot (C2/C3)
  - **anonymity for double-blind review** (C8). That is covered by **Anonymous GitHub**
    (anonymous.4open.science), a proxy that mirrors a repository and replaces identifying
    terms and the owner name with placeholders. Some venues recommend it, but the authors
    remain responsible for leaks (e.g. commit history). Links **expire** after the review
    period: a 2026 reproducibility study found artifacts hosted there had "repository
    expired". So it suits review, not archiving.
- **Paper context:** data collected Jan–Feb 2019. One respondent (P19) already said Zenodo
  solved the double-blind hosting problem for them. Since then, ICSE has made archival hosting a
  condition for the Available badge, so the problem is now largely solved *by rule* for
  badged artifacts.

## 3. "What if your artifact is a few terabytes?" (C7, p. 17) and "what if it exceeds a normal PC's disk? → unreviewable" (C11, p. 23)

What venues actually do:
- **Agreed reduced scope:** MobiSys 2026's AE call says that for experiments with large
  computation, data collection or transmission, reviewers and authors "could communicate
  to decide a reduced but still representative scope of experiments".
- **Remote access provided by the authors:** IISWC 2026 expects most artifacts to run on a
  desktop or laptop; where that isn't enough, **authors must provide remote access** (e.g.
  SSH, anonymised) to a capable system.
- A study of AE in distributed systems recommends stating the time experiments need up
  front, and validating a large parameter sweep by emulating only a subset.

Further options _(my reasoning)_:
- **Institutional or domain repositories** with larger quotas (university research data
  services, national infrastructures). Zenodo stops at about 200 GB.
- **Share a representative subset** plus the scripts to regenerate or download the rest.
  Timperley's own Rec 2: a "representative proof-of-concept… on a smaller dataset".
- **Share the generator, not the data:** e.g. a mining script plus the exact query and date,
  when the data is public (mining studies).
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
- **Cloud credits have been tried, with mixed results:** for SOSP 2019 Microsoft donated
  Azure credits, but the organisers found them "hard to leverage for the artifacts for
  which they would have been most useful". SOSP 2023 allows commercial clouds only when
  strictly necessary and when the **authors pay**, warning that budget may limit
  evaluation. IISWC 2024 stated it could not provide compute.
- **Not standard in SE:** ICSE 2026 provides no compute; authors only document hardware
  needs. I found no SE venue (ICSE, FSE, ASE, ISSTA) offering reviewer cloud credits, so
  Timperley's Rec 7 (ACM/IEEE-funded compute credits) has not been implemented there.
- **Containers vs. consistency:** containers fix the *software* environment, not the
  *hardware*. Combined with a shared testbed they address both, which supports my p. 22 note
  that P18's complaint is not really about containers (see item 5).

## 5. "How do we accurately verify performance claims?" (C2, p. 22) and "That's not really a problem with containers then though" (after P18)

- **VMs:** add virtualisation overhead and share the host with other loads, so absolute
  timings aren't comparable (P64; Collberg & Proebsting made the same point in week 1).
- **Containers:** run at near-native speed on the host kernel, so the VM performance
  problem largely disappears. P18's complaint is different: *build rot*.
  - A Dockerfile with unpinned base images (tags like `latest`) or unpinned `apt-get`/pip
    installs silently pulls newer versions on rebuild, so the same Dockerfile gives a
    different image, or none (paper "Docker Does Not Guarantee Reproducibility", 2026).
  - The fix: archive the **saved image** (`docker save` tarball with its digest), e.g. on
    Zenodo as the Carpentries lesson recommends, plus a Dockerfile with base images and
    dependencies pinned by digest/version as a best-effort rebuild path.
- So my note is largely right: the problem is rebuilding from an unpinned recipe, not
  containers as such. A saved image still needs a compatible container runtime and CPU
  architecture in the future _(my reasoning)_.
- **What venues actually ask for:** SPLASH 2026's AE criteria say that when results are
  performance data, exact numbers depend on the hardware. Artifacts must therefore explain
  how reviewers on other hardware can recognise that the **high-level results** still hold,
  e.g. a trend, or one tool beating another on a class of inputs. Individual artifact guides
  (an ICSE 2023 artifact, a 2025 Zenodo artifact guide) say the same: expect different
  absolute numbers, check **trends, ratios and speedups**. There is no single formal
  standard; the wording varies by venue.
- **Further options** _(my reasoning, building on the above)_:
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
  and **Horizon Europe** (EU) makes open access to research data mandatory under "as open
  as possible, as closed as necessary". Exceptions (commercial exploitation, data
  protection, confidentiality, security, IP) must be justified in the **mandatory data
  management plan**; metadata should be open even when data is closed. Open-source licences
  for software are strongly recommended, not required. This mirrors the ACM idea: openness
  by default, documented exceptions.
- Feasibility limits named in the paper: IP and contracts (C9), privacy and
  re-identification of qualitative data (p. 18), commercial tool licences (p. 20).

---

## Part 2: Research for refining the discussion questions

Gathered for the second round of question selection (slides 26–28 of the team deck). Each
item gives facts students can build on without background research of their own.

### 9. Real cases where errors were found because code or data was available (C1: "fear of mistakes being found")

- **Chang, 2006 (structural biology):** a home-made analysis program, inherited from a
  neighbouring lab, flipped two data columns. This inverted the protein structures and led
  to **five retractions**, three of them highly cited *Science* papers spanning five years.
  The error was found when another group's results contradicted the structure.
- **Willoughby–Hoye NMR scripts, 2019 (chemistry):** Python's `glob` returns files in an
  OS-dependent order. The scripts gave correct values on Windows and older macOS but wrong
  ones on newer macOS and Ubuntu, potentially affecting ~150 studies. Found because
  researchers ran the shared scripts on a different OS. The fix was one line (sort the file
  list).
- **Reinhart & Rogoff, 2013 (economics):** a graduate student (Herndon) asked for the
  original spreadsheet after failing to replicate an influential austerity paper. A range
  error left out five countries; corrected, the headline growth figure changed from −0.1 %
  to 2.2 %.
- **Fraud found in artifact evaluation:** an AEC member found outputs hard-coded in the
  source; the paper was withdrawn (Hermann et al. 2020, p. 477, this week's other paper).
- **Use:** these show both sides of C1. The fear is real, since errors do get found and
  can be costly, but finding them is the point of sharing, and honest bugs were treated as
  mistakes, not misconduct.

### 10. Scooping and embargoes (C1: "untapped publication value", "protect a PhD student")

- Embargoes are an established compromise in data-heavy fields:
  - telescope data typically has a 12–18-month exclusive period for the observing team
  - NERC (UK) treats up to 2 years after data collection as reasonable
  - OSF allows embargoing preregistrations for up to 4 years
- I found **no measurement of how often scooping actually happens**. Sources describe it as
  a "powerful disincentive", i.e. a perceived risk.
- Week-1 tie-in: Collberg & Proebsting listed "competitors' advantage" among the reasons not
  to share.

### 11. Performance claims, VMs and containers (C2)

- **Overhead:** IBM's Felter et al. (2014) found containers matched or beat KVM virtual
  machines in almost all cases, with negligible CPU and memory overhead versus bare metal.
  Both need tuning for I/O-heavy workloads. Containers *inside* a VM inherit the VM's
  overhead. A later independent study agrees: bare metal fastest, containers close behind,
  VMs last.
- **How venues handle it:** SPLASH 2026 tells authors to explain how reviewers on other
  hardware can recognise that the *high-level* results still hold (trends, one tool beating
  another), since exact numbers depend on the hardware. Individual artifacts state "expect
  different absolute numbers, check ratios and speedups". See item 5.
- **Build rot vs. image:** rebuilding from an unpinned Dockerfile can silently produce a
  different image. Archiving the built image plus a pinned Dockerfile is the recommended
  fix. See item 5.

### 12. How long should an artifact work, and who looks after it? (C3)

- **Retention rules:** the DFG Code of Conduct (Germany) expects research data, *and the
  software* underlying a publication, to be archived for **at least ten years**, typically
  implemented in university statutes (e.g. Potsdam, Jena, Max Planck). Archiving ≠ keeping
  it runnable.
- **Funding for maintenance exists, but is short-term:**
  - Chan Zuckerberg Initiative's Essential Open Source Software for Science: up to
    $200k/year for 2 years, for widely used tools
  - DFG "Research Software Sustainability" calls
  - NSF CSSI "transition to sustainability"
  - an overview notes funding follows short cycles, not long-term maintenance needs
- **After the author leaves:** Research Software Engineers (RSEs) are permanent staff who
  keep codebases alive inside an institution. Princeton and Aalto run RSE teams, Aalto partly
  after a departed student's code stalled a project. A Research Software Succession Planning
  task force (Oct 2025) is building a handover checklist; a 2025 paper gives "10 quick tips
  for making your software outlive your job".
- **Week-1 tie-in (`Vorl_1/seminar-notes.md`):** last week concluded that good archiving
  needs constant, costly maintenance and further funding, that formats will change (Docker
  may not exist in 40 years), and that source code may be the most stable format.

### 13. One-click reproduction scripts (C4)

- "Push-button replication" is an established term (3ie, development economics): first
  check that the authors' data and code reproduce the published numbers, then do a
  "pure replication" by writing new code. In one audit, only 14 of 69 articles with
  archived data could be reproduced at all.
- I found no study measuring whether scripts hide errors. The argument comes from the
  paper's reviewers (P25: AECs "likely to replicate the same mistake"; P52: "easy to
  reproduce, difficult to understand where to add case studies"). The NMR `glob` case
  (item 9) is a concrete example: a script that "works" can still be wrong on another
  machine.

### 14. Industry data and unshareable artifacts (C9)

- **ICSE open science policy:** sharing data is *not* mandatory for submission or
  acceptance; authors who can't share should say why in a data availability statement.
  ICSE 2027's Q&A on industry research says the same, stated in both the submission form
  and the paper.
- **Artifact evaluation:** artifacts can get the *Evaluated* badges with private access for
  reviewers only; *Available* requires public archival access. Proxy data for proprietary
  data and anonymised qualitative data are accepted (ICSE 2026/2027).
- So the formal rules already allow exceptions. P22's complaint is about paper reviewers'
  attitudes, which no policy controls.

### 15. Proprietary tools and licences (C9)

- No blanket rule. Formal-methods venues handle it case by case:
  - **CAV:** authors who can't provide a VM with licensed software (e.g. MATLAB) contact the
    chairs to arrange an alternative
  - **FORMATS 2022:** accepted a shared MATLAB Drive folder runnable in MATLAB Online
  - **QEST 2022/2023:** explicit exemption process for restrictively licensed software
- Reviewers have reported trouble getting access to proprietary operating systems (ROSE
  guidance). Reviewers aren't expected to buy licences.

### 16. Running untrusted artifacts (C2: security)

- POPL recommends VM images partly because they "protect reviewers from malfunctioning
  artifacts damaging their computer"; ACSAC recommends Docker or VirtualBox.
- A 2026 paper ("Beyond Reproducibility") proposes a security checklist for artifacts and
  asks reviewers to do basic security checks. I found no guidance specifically on refusing
  root access.

### 17. Who reviews, and how much time they get (C10, C11)

- **Students on purpose:** from ECOOP 2013 and OOPSLA 2013, AECs were deliberately filled
  with **senior PhD students**, for two stated reasons: they know current tools, and it
  gets the next generation thinking about artifacts (organisers' calls; Krishnamurthi's
  memo).
- **Time budget per artifact:** SOSP 2021 estimated **10–20 hours**, with 2–4 artifacts per
  member; APLAS 2022 about **8 hours**, with 3–4 per member. ICSE 2026: setup over 30
  minutes makes acceptance unlikely. So the 30 minutes is a *setup* limit within an
  evaluation of several hours.

### 18. Communication during review (C12)

- "Kick the tires" is an early check that the artifact runs at all, followed by a short
  author response window (SLE 2025: 5 days; OOPSLA 2021: about a week), with further rounds
  allowed at some venues (OOPSLA 2021, Programming journal). ICSE 2026 runs an iterative
  cycle with a 72-hour response time.
- So most venues are already iterative. The open question is how much author help is
  acceptable before a badge stops meaning "works for a stranger".

### 19. Link rot and re-checking (C7)

- Klein et al. (2014): across 3.5 million articles (1997–2012), **13–22 %** of web
  references suffered link rot ("one in five articles"), more with content drift.
- Timperley's 26 % dead for 2014 vs. 5 % for 2018 fits this general decay pattern.

### 20. Current state: newer numbers (for "then vs. now")

- A 2024 study of ASE, FSE, ICSE and ISSTA papers (2017–2022) found the share of papers with
  artifacts rose from **60.1 % to 81.1 %**. It also looked at maintenance, popularity and
  quality.

### 21. Rewards for artifact work (non-RQ2 idea: "which reward would motivate you?")

- **JOSS (Journal of Open Source Software):** short, citable papers about research software
  with a DOI, reviewed openly on GitHub (code, docs, tests, licence). Built explicitly
  because citations and papers are what count for hiring and promotion. Other options
  students may know: artifact awards, badges, citations of the artifact's DOI.

### 22. Qualitative data sharing (C9: re-identification)

- Repositories such as the Qualitative Data Repository offer de-identification plus
  **access controls** (approved researchers only, data use agreements). Consent forms must
  say up front who may see the data. Risk is highest in small communities, e.g. a single
  company's developers.

## Part 3: Research for the third question revision

### 23. Who pays for artifact evaluation and licences (C9 licensed software)
- No source states an artifact-evaluation budget. AECs are volunteer committees set up by
  the conference organisers (SIGMOBILE guidance); some SIGs run a standing AEC (SIGIR).
  Conferences have sponsors (e.g. MobiSys 2026: Huawei, ACM SIGMOBILE), but nothing ties
  them to artifact evaluation. Treat "AE has no dedicated budget" as likely, not verified.
- Licences: CAV asks authors who cannot provide a VM or Docker image with licensed software
  (e.g. MATLAB) to contact the chairs for a case-by-case solution; FORMATS 2022 accepted a
  shared MATLAB Drive folder runnable in MATLAB Online. No source says who pays for a
  reviewer's licence; in practice reviewers rely on their own university's campus licences
  (unverified).
- Cloud and hardware cost: the Programming journal notes one option is that authors pay
  for a cloud instance reviewers can use; SOSP 2023 allows public cloud only if authors pay.

### 24. Actual time limits (C11 fixed time limits)
- Setup ("getting started") is usually about 30 minutes, phrased as a guideline, not a
  cutoff: OSDI 2021/2023 ("e.g., within 30 minutes"), OOPSLA 2023 ("roughly 30 minutes"),
  ICSE 2026 (over 30 minutes makes acceptance unlikely).
- Full experiments: NDSS 2027 asks that they take at most 1 day on a commodity desktop.
- Reviewer budget: about 8-20 hours per artifact (SOSP 2021, APLAS 2022).
- Response windows: ECOOP and MODELS 2023 give authors 4 days to answer kick-the-tires
  reports; SLE 2025 5 days; ICSE 2026 72 h.
- No venue found that varies limits by artifact type; heavy artifacts are handled by
  negotiated reduced scope (MobiSys) or remote access instead.

### 25. How hardware for reviewers is handled today (C11 hardware, C7/C11 unreviewable)
- Common rule: authors provide anonymous remote access to special hardware (SSH with
  reviewers' keys; no forms asking for reviewer identity):
  SenSys 2024, SACMAT 2026 (HPC, cloud, SGX, GPU, TPU), IEEE S&P 2026, MICRO 2026.
- MICRO 2026 may decline to evaluate artifacts when no reviewer has access to the required
  hardware, i.e. such artifacts become unreviewable in practice.
- Testbeds (Chameleon, CloudLab) are used in systems research; donated cloud credits (SOSP
  2019) proved hard to use.
- Relation to the paper: Timperley's Rec 6/7 suggest providing compute resources / cloud
  credits funded by ACM and IEEE (teammate's section). Current practice instead shifts the
  burden to authors, which is the hand-over point.

### 26. Concrete decay examples (C3)
- Python 2 reached end of life on 1 Jan 2020; Arch Linux removed it from its repositories.
  The metabarcoding tool OBITools (Python 2) is no longer maintainable; its maintainers
  provide a Docker image so it can still be run for reproducibility.
- Docker Hub announced in August 2020 that images of free accounts not pulled for 6 months
  would be deleted (from Nov 2020); after protests the enforcement was paused. Shows that
  even "frozen" images depend on a commercial host's policy.
- NMR script bug (item 9): code that ran correctly for years gave wrong results on newer
  operating systems.

### 27. Hermann et al. wording (C12)
- Conclusion (p. 479): "Reviewers want replicability, users want reusability." Note that
  "replicability" is the old ACM term, i.e. today's reproducibility (re-running the authors'
  artifact).
- Also relevant: 34 users saw no difference between evaluated and unevaluated artifacts,
  20 did (p. 477).

### 28. Lecturer's own work (context)
- Beyer & Winter (LMU) gave an FSE 2025 tutorial "Artifact Evaluations for Stronger
  Research Results" on how AE works, its pitfalls and best practices; materials at
  stefan-winter.net/ae-materials.html. Good to know since the lecturer co-wrote Paper 1.

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
- [ACM SIGIR artifact badging (quotes ACM v1.1 definitions)](https://sigir.org/general-information/acm-sigir-artifact-badging/), [ESEC/FSE 2021 artifacts track](https://2021.esec-fse.org/track/fse-2021-artifacts)
- [SPLASH 2026 artifact evaluation](https://2026.splashcon.org/track/splash-2026-artifact-evaluation), [ICSE 2023 artifact example](https://github.com/Generative-Program-Analysis/icse23-artifact-evaluation)
- [Zenodo principles/preservation](https://about.zenodo.org/principles/), [GitHub–Zenodo integration guide](https://rue-a.github.io/github-zenodo-integration/documentation/), [Lattice QFT open science paper (retention 10–20 years)](https://arxiv.org/pdf/2502.03593)
- [Anonymous GitHub](https://github.com/tdurieux/anonymous_github), [USENIX SAIS '27 call](https://www.usenix.org/conference/sais27/call-for-papers), [reproducibility study noting expired links](https://arxiv.org/pdf/2608.09567)
- [Docker Does Not Guarantee Reproducibility (2026)](https://arxiv.org/pdf/2601.12811), [Carpentries: containers and reproducibility](https://carpentries-incubator.github.io/docker-introduction/reproduciblity.html)
- [Software Heritage SWHID docs](https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html)
- [Aalto: Horizon Europe open science requirements](https://www.aalto.fi/en/open-science-and-research/eu-horizon-europe-open-science-requirements)
- [MobiSys 2026 artefact evaluation](https://www.sigmobile.org/mobisys/2026/artifact_evaluation/), [IISWC 2026 AE](https://iiswc.org/iiswc2026/ae.html), [IISWC 2024 AE](https://iiswc.org/iiswc2024/ae.html), [AE for distributed systems study](https://www.researchgate.net/publication/381580238_Artifact_Evaluation_for_Distributed_Systems_Current_Practices_and_Beyond)
- [OSDI 2020 AE report (SOSP'19 Azure credits)](https://sysartifacts.github.io/osdi2020/report), [SOSP 2023 call for artifacts](https://sysartifacts.github.io/sosp2023/artifacts-call), [SOSP 2023 evaluator guide](https://sysartifacts.github.io/sosp2023/guide)
- [ATLAS.ti guide: convergent parallel design](https://atlasti.com/guides/the-guide-to-mixed-methods-research/convergent-parallel-design)
- Week-1 numbers: `Vorl_1/discussion/cross-paper.md`
- [Retraction Watch-style coverage of the Chang retractions (The Scientist)](https://www.the-scientist.com/retractions-unsettle-structural-bio-46891), [A Scientist's Nightmare summary](https://acawiki.org/A_Scientist%27s_Nightmare:_Software_Problem_Leads_to_Five_Retractions)
- [The Register: Python glob bug in NMR scripts](https://www.theregister.com/2019/10/15/bug_python_scripts/), [ACM TechNews](https://cacmb4.acm.org/news/240221-bug-in-python-script-may-have-affected-hundreds-of-studies)
- [Monkey Cage: Reinhart & Rogoff](https://themonkeycage.org/2013/04/what-the-reinhart-rogoff-debacle-really-shows-verifying-empirical-results-needs-to-be-routine/), [Reinhart & Rogoff response](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/rogoff/files/reinhart_rogoff_responding_to_our_critics.pdf)
- [EIDC embargo FAQ (NERC)](https://eidc.ac.uk/help/faq/embargos), [OSF on fear of scooping](https://help.osf.io/article/634-addressing-fear-of-scooping-on-osf-preregistrations), [Biosignatures workshop report](https://arxiv.org/pdf/2210.14293)
- [Felter et al. 2014, containers vs. VMs](https://people.computing.clemson.edu/~jmarty/projects/lowLatencyNetworking/papers/NFVandContainers/AnupdatedPerfAnalysisofContainersandVMs.pdf), [IJEECS Docker/VM/bare-metal study](https://www.doi.org/10.11591/IJEECS.V7.I1.PP205-213)
- [Uni Potsdam research data policy (DFG 10 years)](https://www.uni-potsdam.de/en/forschungsdaten/policies/university/policy), [MPG rules of conduct](https://rdm.mpdl.mpg.de/2022/12/12/rules-of-conduct-for-good-scientific-practice-by-the-mpg/), [DFG research software principles](https://www.dfg.de/en/basics-topics/digital-topics/research-software/principles)
- [CZI EOSS](https://chanzuckerberg.com/eoss/proposals/), [Research software funding landscape](https://www.researchsoft.org/blog/2022-02-24/)
- [Princeton: what's an RSE](https://picscie.princeton.edu/news/2018/%E2%80%9Cwhat%E2%80%99s-rse%E2%80%9D), [Aalto RSE](https://hackmd.io/@AaltoSciComp/r1N03G8FO), [Succession planning task force](https://www.researchsoft.org/tf-succession-planning), [10 quick tips for software to outlive your job](https://arxiv.org/abs/2505.06484v1)
- [Push-button replication (3ie)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6303036/)
- [ICSE 2027 artifact evaluation](https://conf.researchr.org/track/icse-2027/icse-2027-artifact-evaluation), [ICSE 2023 technical track (open science policy)](https://conf.researchr.org/track/icse-2023/icse-2023-technical-track)
- [CAV 2025 artifact evaluation](https://conferences.i-cav.org/2025/artifact/), [FORMATS 2022 AE](https://ce.ncl.ac.uk/formats2022/artifactevaluation), [QEST 2023 artifacts](https://www.qest.org/qest2023/artifacts.html), [ROSE guidance](https://github.com/researchart/rose/blob/master/guidance.md)
- [POPL 2023 AE](https://popl23.sigplan.org/track/POPL-2023-artifact-evaluation), [ACSAC artifacts](https://acsac.org/2020/submissions/papers/artifacts), [Beyond Reproducibility (2026)](https://arxiv.org/pdf/2605.06508)
- [OOPSLA 2013 AEC nomination letter](https://evaluate.inf.usi.ch/artifacts/aea/announcements/nomination1.html), [Krishnamurthi: AE memo](https://cs.brown.edu/~sk/Memos/Conference-Artifact-Evaluation/), [SOSP 2021 AEC call](https://www.sigops.org/2021/sosp-2021-aec-call/), [APLAS 2022 AEC call](https://mailman.haskell.org/archives/list/haskell-cafe@haskell.org/thread/R5FS4TTAMQ44EI2D36636SQT7OAGNOOU)
- [SLE 2025 AE](https://www.sleconf.org/2025/ArtifactEvaluation.html), [OOPSLA 2021 artifacts](https://2021.splashcon.org/track/splash-2021-Artifacts), [Programming journal AE](https://programming-journal.org/artifact-evaluation)
- [Klein et al. 2014, reference rot](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4277367/)
- [Research Artifacts in SE Publications: Status and Trends (2024)](https://arxiv.org/abs/2404.06852)
- [JOSS design and first-year review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7340488/)
- [QDR practice paper (CODATA)](https://datascience.codata.org/articles/674), [PRIMR: qualitative data sharing and IRBs](https://blog.primr.org/at-the-dawn-of-qualitative-data-sharing-questions-irbs-may-want-to-ask-during-protocol-review)
- [SIGMOBILE artifact guidelines](https://www.sigmobile.org/grav/about/artifact-guidelines), [SIGIR artifact badging](https://sigir.org/general-information/acm-sigir-artifact-badging/), [MobiSys 2026](https://www.sigmobile.org/mobisys/2026/artifact_evaluation/)
- [OSDI '23 call for artifacts](https://www.usenix.org/conference/osdi23/call-for-artifacts), [OOPSLA 2023 artifacts](https://2023.splashcon.org/track/splash-2023-Artifacts), [NDSS 2027 call](https://secartifacts.github.io/ndss2027/call), [MODELS 2023 AE](https://conf.researchr.org/track/models-2023/models-2023-artifact-evaluation), [ECOOP 2023 AE](https://2023.ecoop.org/track/ecoop-2023-artifacts)
- [SenSys 2024 AE](http://sensys.acm.org/2024/art/), [SACMAT 2026 call](https://www.sacmat.org/2026/call-for-artifacts.php), [IEEE S&P 2026 AE](https://sp2026.ieee-security.org/artifact_instructions.html), [MICRO 2026 AE](https://micro2026ae.hotcrp.com/), [SysArtifacts packaging guide](https://sysartifacts.github.io/packaging-guide), [Programming journal AE](https://programming-journal.org/artifact-evaluation/)
- [Arch Linux: removing python2](https://archlinux.org/news/removing-python2-from-the-repositories/), [OBITools legacy](https://forge.metabarcoding.org/obitools/obitools), [InfoQ: Docker image expiration](https://www.infoq.com/news/2020/11/docker-image-expiration-plans/), [Docker: retention policy delayed](https://www.docker.com/blog/docker-hub-image-retention-policy-delayed-and-subscription-updates/)
- [Beyer & Winter FSE 2025 tutorial](https://www.sosy-lab.org/research/pub/2025-FSE.Artifact_Evaluations_for_Stronger_Research_Results.pdf)
