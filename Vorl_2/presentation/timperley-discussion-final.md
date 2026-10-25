# Timperley et al. (2021): Discussion Questions (Challenges, §4.2)

Generated from `Vorl_2/slides/discussion_questions_timperley.py` (single source for slides and notes).

Core questions come from my selected (green) questions, lightly reworded and anchored in the paper. Follow-ups go on the slide as sub-points. Example answers and my notes go in the speaker notes only; the notes draw on `timperley-research.md` and are not part of the questions.

## Questions, sorted by challenge (RQ1 last)

### 1. C1 Not worth it: Fear of exposing mistakes

**Context:** Creators fear shared code exposes mistakes and harms their reputation, though finding mistakes is what review is for.

**Question:** What would make you more or less willing to share your own code?

**Follow-ups:**
- Example: a bug found later only leads to a correction note, not a retraction
- You: Would you share more readily if messy, as-is code were the norm?

**Example answers:**
- More willing: proportionate consequences for honest errors; messy code accepted.
- Less willing: as long as any visible mistake can cost a paper or reputation.

**My notes:**
- Chang 2006: inherited script flipped two columns, 5 retractions, treated as honest error.
- Reinhart & Rogoff 2013: spreadsheet error found after the data was shared.
- Hermann et al.: some reviewers prefer availability over quality.

### 2. C1 Not worth it: Holding back artifacts

**Context:** Some creators hold back artifacts to protect future publications.

**Question:** Does this slow down research, and how far should researchers accept being undercut for scientific progress?

**Follow-ups:**
- Example: a tool kept private until the PhD student's next paper
- You: Would you build on a paper whose tool you can't get?

**Example answers:**
- Protect: a PhD has fixed time; being overtaken with your own tool is a real risk.
- Share: the paper already establishes priority; whole research areas died without artifacts.

**My notes:**
- Embargoes in data-heavy fields (telescope data 12-18 months); no measured scooping rate.

### 3. C2 Portability: Running untrusted artifacts

**Context:** Running untrusted artifacts is a security risk for reviewers.

**Question:** Should reviewers be allowed to refuse artifacts that need root access or invasive libraries?

**Follow-ups:**
- Example: an installer that changes system libraries on the reviewer's laptop
- You: If refusing were allowed, which research could no longer be evaluated?

**Example answers:**
- Yes: safety first; authors must package safely (VM, container).
- No: system-level research (OS, drivers, security tools) would become unevaluable.

**My notes:**
- POPL recommends VM images partly to protect reviewers' machines.

### 4. C3 Maintenance: Decay and maintenance

**Context:** Artifacts decay as dependencies age and student maintainers leave.

**Question:** Is software decay unavoidable, and what practical ways are there to limit it?

**Follow-ups:**
- Example: a 2015 thesis tool needs Python 2 and a library that no longer exists: fix it, freeze it in an image, or let it go?
- You: Who should pay for keeping your thesis tool running after you leave?

**Example answers:**
- Unavoidable: you can slow decay, not stop it.
- Limitable: a frozen image runs as long as it can be executed.
- Cost: group or university vs. nobody (archive and mark unmaintained).

**My notes:**
- Paper's own suggestions (teammate): maintenance plans, long-term archives.
- DFG: archive code and data 10 years; archived is not runnable.
- Research software engineers; short-cycle maintenance funding.
- Week 1: Docker may not exist in 40 years; source code most stable.

### 5. C4 Tacit knowledge: One-click reproduction scripts

**Context:** Scripts capture steps that would otherwise stay in the developer's head. Reviewers warn they can be a black box that re-runs the authors' mistakes.

**Question:** Is a one-click reproduction script good or bad for scientific scrutiny?

**Follow-ups:**
- Example: the script reproduces every table, but nobody reads the code behind it
- You: As a reviewer, what besides a script would help you understand why the results come out?

**Example answers:**
- Good: anyone can re-run it.
- Bad: checks the numbers, not the method.

**My notes:**
- Python file-order case (2019): scripts correct on one OS, wrong on another.

### 6. C4 Tacit knowledge: Capturing tacit knowledge

**Context:** Much know-how about a prototype stays in the developer's head.

**Question:** What practical ways are there to capture this knowledge so that others can use the artifact?

**Follow-ups:**
- Example: the order the scripts must run in, hard-coded paths, parameter values that were tried and dropped
- You: Could someone reproduce your bachelor thesis results from your repository alone?

**Example answers:**
- Mostly capturable with checklists and a run-all script.
- Not fully: some know-how only transfers by talking to the author.

**My notes:**

### 7. C4 Tacit knowledge: Reviewer effort

**Context:** Reviewers report missing instructions and needing the paper to fill gaps; deep dives can take days.

**Question:** How much effort, time and money should reviewers invest before giving up on an artifact?

**Follow-ups:**
- Example: after two hours it fails on a missing dependency: fix it, ask the authors, or reject?
- You: As an author, how much of a reviewer's goodwill would you rely on?

**Example answers:**
- Little: it should work for a stranger.
- More: reviewers are often the only ones who ever try.

**My notes:**
- Typical budget 8-20 h per artifact (SOSP 2021, APLAS 2022).

### 8. C7 Hosting: Dead links and old badges

**Context:** Many artifacts become inaccessible, older ones more often.

**Question:** Should a badge expire if the artifact link dies after publication?

**Follow-ups:**
- Example: conferences re-check links every few years and mark dead ones
- You: Would "awarded 2016, not re-checked" change how you treat a paper?

**Example answers:**
- Yes: a badge should describe the current state.
- No: it certifies what was checked at review time.

**My notes:**
- Who organises and pays for re-checks?
- Klein et al. 2014: 13-22 % of web references suffer link rot.

### 9. C7 Hosting: Very large artifacts

**Context:** Large datasets don't fit common hosting or a reviewer's disk.

**Question:** What should researchers do with artifacts too big for Zenodo or a reviewer's laptop?

**Follow-ups:**
- Example: several terabytes of mined repository data
- You: What would you publish if your thesis data were that large?

**Example answers:**
- A representative subset plus scripts to regenerate the rest.
- Institutional repositories; share the generator, not the data.

**My notes:**
- Zenodo: 50 GB per record, up to 200 GB on request.
- Overlaps with the paper's proof-of-concept recommendation (teammate).

### 10. C9 External constraints: Unshareable industry data

**Context:** Industry partners often forbid sharing data.

**Question:** Should reviewers criticise a paper for not sharing data its industry partner won't release?

**Follow-ups:**
- Example: a study of a company's bug reports, with the data under NDA
- You: If you built on a study whose data is under NDA, would you trust it less than one whose artifact simply disappeared?

**Example answers:**
- Yes: readers cannot check the claims either way.
- No: it punishes industry collaboration.

**My notes:**
- ICSE: sharing not required for acceptance, only a statement of why not.

### 11. C9 External constraints: Formal exceptions

**Context:** ACM separates "evaluated" from "publicly available".

**Question:** Should artifact evaluation have formal exceptions for artifacts like industry data?

**Follow-ups:**
- Example: reviewers get temporary access under NDA, but readers never see the artifact
- You: Would a badge saying "evaluated privately" convince you as a reader?

**Example answers:**
- Yes: someone independent has checked it.
- No: a check nobody can repeat adds little.

**My notes:**
- ACM: Evaluated badges with reviewer-only access; Available needs a public archive. Proxies allowed for proprietary data.

### 12. C9 External constraints: Open by default

**Context:** IP, privacy and commercial tools limit what can be shared.

**Question:** How open should research software be, and where are the legitimate limits?

**Follow-ups:**
- Example: a company co-authored the tool and wants to sell it later
- You: Which part of your own thesis work would you not want to make public, and why?

**Example answers:**
- Fully open: publicly funded research belongs to the public.
- Limits: personal data, partner contracts, commercial plans.

**My notes:**
- Horizon Europe: open data mandatory, exceptions justified in a data management plan.

### 13. C9 External constraints: Licensed software

**Context:** Some artifacts need paid licences reviewers don't have.

**Question:** Should research tools that depend on paid commercial software be accepted as artifacts at all?

**Follow-ups:**
- Example: your artifact needs MATLAB, and the reviewer has no licence: whose problem is that?
- You: As a reviewer, would you pay for a licence yourself to evaluate someone else's artifact?

**Example answers:**
- Accept: much real-world SE runs on commercial platforms.
- Restrict: if others cannot run it, it misses its purpose.

**My notes:**
- ACM policy is silent on reviewer licences; each AEC decides. CAV/FORMATS/QEST: case by case, e.g. MATLAB Online.

### 14. C10 Lack of reviewer incentives: Students as reviewers

**Context:** Artifact review is poorly rewarded and often left to students.

**Question:** Is leaving artifact evaluation to students a good training opportunity, or does it undermine how rigorous and seriously taken the badges are?

**Follow-ups:**
- Example: a first-year PhD student judges an experienced group's artifact
- You: Would you trust a badge more if you knew a senior researcher rather than a student had awarded it?

**Example answers:**
- Meaningful: checking that it runs needs no seniority.
- Weak: students may not judge methods or dare to reject.

**My notes:**
- Students chosen deliberately from ECOOP/OOPSLA 2013; most AEC members serve once (Hermann et al.).

### 15. C11 Technical obstacles: Fixed time limits

**Context:** Some artifacts need more than the roughly one day a reviewer has.

**Question:** Is it fair to fail an artifact after a fixed time limit, e.g. a 30-minute setup?

**Follow-ups:**
- Example: a fuzzing experiment that runs for three days
- You: Could your own thesis project be set up in 30 minutes?

**Example answers:**
- Fair: future users won't invest more either.
- Unfair: penalises inherently heavy research.

**My notes:**
- ICSE 2026: setup over 30 min makes acceptance unlikely; MobiSys allows a reduced representative scope.

### 16. C11 Technical obstacles: Hardware reviewers don't have

**Context:** Reviewers often lack the hardware to run an artifact.

**Question:** Should conferences provide compute and storage for reviewers, e.g. remote servers with containers?

**Follow-ups:**
- Example: an experiment needs eight GPUs for a week, and the reviewer has a laptop
- You: Would you trust a badge from a reviewer who only ran a scaled-down version?

**Example answers:**
- Yes: otherwise resource-rich labs are favoured.
- No: costly; authors should provide access or a smaller run.

**My notes:**
- Paper recommends compute funding (teammate's section): keep it short and hand over.
- SOSP 2019 Azure credits proved hard to use; IISWC has authors provide remote access.

### 17. C12 Limited communication: One-shot or iterative review

**Context:** Reviewers value responsive authors; single-round reviews frustrate both sides.

**Question:** Should artifact evaluation be a one-shot review or a dialogue with the authors?

**Follow-ups:**
- Example: the artifact fails on a typo in the install instructions: reject, or ask the authors?
- You: Later users won't have the authors' help: should reviewers?

**Example answers:**
- Dialogue: fixes help every later user.
- One-shot: a badge should mean it works without the authors.

**My notes:**
- Most venues have a 'kick the tires' phase; ICSE 2026: answers within 72 h.

### 18. C12 Limited communication: Support after publication

**Context:** Users value authors who help fix problems.

**Question:** Is that support sustainable, given it can't last forever?

**Follow-ups:**
- Example: the student who built the tool graduated two years ago, and a user's bug report goes unanswered
- You: Would you answer emails about your thesis code in three years?

**Example answers:**
- Yes, for a stated period.
- No: archive it and say it is unsupported.

**My notes:**
- Overlaps with C3.

### 19. RQ1: Rewards

**Context:** Respondents want sharing encouraged and rewarded.

**Question:** Which reward would actually make researchers invest more in artifacts?

**Follow-ups:**
- Example: a best-artifact award at the conference vs. your artifacts counting in your next job application
- You: What would make you spend an extra week on your thesis artifact?

**Example answers:**
- Career credit.
- Direct benefit: users, collaborations.

**My notes:**
- JOSS; possible overlap with the teammate's recommendations.

