# Timperley et al. (2021): Discussion Questions (Challenges, §4.2)

Generated from `Vorl_2/slides/discussion_questions_timperley.py` (single source for slides and notes).

Core questions come from my selected (green) questions, lightly reworded and anchored in the paper. Follow-ups go on the slide as sub-points. Example answers and my notes go in the speaker notes only; the notes draw on `timperley-research.md` and are not part of the questions.

## Questions, sorted by challenge (RQ1 last)

### 1. C1: Fear of exposing mistakes

**Question:** Creators fear that shared code exposes mistakes and harms their reputation: what would make you more or less willing to share your own code?

**Follow-ups:**
- Example: a mistake found later through your artifact only leads to a correction note, not a retraction
- You: Would you share more readily if releasing research code as is, messy and undocumented, were the accepted norm?

**Paper context:** Creators fear that sharing exposes mistakes in their analysis and that poor code quality harms their reputation.

**Example answers:**
- More willing: if consequences for honest errors are proportionate (correction, erratum) and messy code is normal.
- Less willing: as long as any visible mistake can cost a paper or a reputation, keeping code private is the safer choice.
- Releasing as is: something checkable beats nothing vs. it wastes users' time and signals sloppiness.

**My notes:**
- Chang 2006: inherited script flipped two columns, 5 retractions, treated as an honest error.
- Reinhart & Rogoff 2013: a spreadsheet range error found after the data was shared.
- Hermann et al.: some reviewers prefer availability over quality; an AEC found hard-coded outputs (misconduct, not error).

### 2. C1: Unreleased tools

**Question:** Should a paper whose results rest on a tool the authors keep private be treated as a full result or as preliminary until the tool is released?

**Follow-ups:**
- Example: a new testing technique evaluated with a tool held back for the PhD student's next paper
- You: Would you cite and build on such a paper in your own thesis?

**Paper context:** Creators hold back artifacts with untapped publication value or fear of being scooped; a limited audience is another reason.

**Example answers:**
- Full result: peer review judged the paper; the tool is the authors' property.
- Preliminary: claims that nobody can check are weaker evidence.

**My notes:**
- Embargoes exist in data-heavy fields (telescope data 12-18 months); no measured scooping rate.

### 3. C2: Portability

**Question:** Does an artifact count as portable if it only runs inside the authors' container image?

**Follow-ups:**
- Example: the Docker image works, but nobody could rebuild the tool from source
- You: Would you build your own research on a tool you can only run inside a black-box image?

**Paper context:** Artifacts often fail on other machines (missing information, outdated dependencies); VMs and containers are the usual fix.

**Example answers:**
- Yes: it runs anywhere Docker runs.
- No: the image hides how the environment was set up and decays too.

**My notes:**
- Rebuilding from an unpinned Dockerfile can silently change the result; archive the built image.

### 4. C3: Decay and maintenance

**Question:** Is software decay unavoidable as technology moves on, and who should carry the cost of limiting it?

**Follow-ups:**
- Example: a 2015 thesis tool needs Python 2 and a library that no longer exists: fix it, freeze it in an image, or let it go?
- You: If you inherited a ten-year-old tool for your thesis, what would you want its authors to have left you?

**Paper context:** Artifacts need ongoing maintenance (bugs, changing use cases, bit rot), usually by students who later leave; only well-funded groups manage it.

**Example answers:**
- Unavoidable: you can slow decay (archived images, pinned versions, few dependencies), not stop it.
- Cost: the group or university, since it is research infrastructure, vs. nobody (archive and mark unmaintained).
- Expected lifetime: only at publication and review, or a stated period?

**My notes:**
- DFG: code and data behind a publication archived for at least 10 years; archived is not runnable.
- Research software engineers keep code alive inside institutions (Princeton, Aalto).
- Maintenance funding runs in short cycles (CZI, DFG calls).
- Week 1: costly constant maintenance; Docker may not exist in 40 years; source code most stable.

### 5. C4: One-click reproduction scripts

**Question:** Is a one-click reproduction script good or bad for scientific scrutiny?

**Follow-ups:**
- Example: the script regenerates every table in the paper, but nobody reads the code that produces them: what has actually been checked?
- You: As a reviewer with one day per artifact, would you rather get a script or a documented step-by-step procedure?

**Paper context:** Reviewers suggest scripts against tacit knowledge, but warn they act as a black box that can re-run the authors' mistakes.

**Example answers:**
- Good: anyone can re-run it; without scripts many artifacts would not run at all.
- Bad: checks that numbers come out, not that the method is sound; false confidence.
- Understanding why results come out needs documentation of the steps, not just the button.

**My notes:**
- Python file-order case (2019): scripts correct on one OS, wrong on another; ~150 studies possibly affected.
- Push-button replication is an established first step before independent re-implementation.

### 6. C4: Tacit knowledge

**Question:** What knowledge about a research prototype typically stays in the developer's head, and could documentation ever capture it?

**Follow-ups:**
- Example: the order the scripts must run in, hard-coded paths, parameter values that were tried and dropped
- You: Could someone reproduce your bachelor thesis results from your repository alone?

**Paper context:** Tacit knowledge, buried in developers' heads, makes artifacts hard to understand, extend and reuse.

**Example answers:**
- Mostly capturable: checklists, a run-everything script, a short walkthrough video.
- Not fully: some know-how only transfers by talking to the author.

**My notes:**

### 7. C4: Reviewer effort

**Question:** How much effort should an artifact reviewer invest before giving up on an artifact?

**Follow-ups:**
- Example: after two hours the artifact fails on a missing dependency: fix it yourself, contact the authors, or reject?
- You: As an author, how much of a reviewer's goodwill would you be comfortable relying on?

**Paper context:** Reviewers report missing instructions and needing the paper to fill gaps; deep dives can take days.

**Example answers:**
- Little: the artifact should work for a stranger.
- More: reviewers are the only ones who will ever try; one fix helps everyone after.

**My notes:**
- Overlaps with the C11 time-limit question; use as its follow-up if needed.

### 8. C7: Very large artifacts

**Question:** How should researchers share artifacts that are too big for archives like Zenodo and for a reviewer's laptop?

**Follow-ups:**
- Example: several terabytes of mined repository data
- You: If your thesis data were that large, what would you publish?

**Paper context:** Creators struggle to find hosting for large datasets; GitHub, Dropbox and Google Drive are not long-term archives.

**Example answers:**
- A representative subset plus scripts to regenerate the rest.
- Institutional repositories; share the generator, not the data.

**My notes:**
- Zenodo: 50 GB per record, up to 200 GB on request.
- Overlaps with the paper's recommendation on proof-of-concept artifacts (teammate's section).

### 9. C7: Dead links and old badges

**Question:** Should a badge expire if the artifact link dies a few years after publication?

**Follow-ups:**
- Example: a 2016 badge on a paper whose artifact link now returns 404
- You: Would a label like awarded 2016, not re-checked change how you treat the paper?

**Paper context:** Many artifacts are no longer accessible, older ones more often.

**Example answers:**
- Yes: a badge should describe the current state.
- No: it certifies what was checked at review time.

**My notes:**
- Klein et al. 2014: 13-22 % of web references in articles suffer link rot.

### 10. C9: Unshareable industry data

**Question:** Should a paper be criticised for not sharing data that its industry partner won't release?

**Follow-ups:**
- Example: an empirical study of a company's ten years of bug reports, with the data under NDA
- You: If you built on a study whose data is under NDA, would you trust it less than one whose artifact simply disappeared?

**Paper context:** IP, contracts, privacy and liability fears prevent sharing; authors feel reviewers use missing artifacts as a blanket argument.

**Example answers:**
- Yes: readers cannot check the claims, whatever the reason.
- No: it punishes valuable industry collaboration for something authors cannot control.
- Middle: state the reason, offer proxy data or reviewer-only access.

**My notes:**
- ICSE: data sharing not required for acceptance, only a statement of why not.
- ACM 'Complete' allows proxies for proprietary data.

### 11. C9: Formal exceptions

**Question:** Should artifact evaluation have formal exceptions for unshareable artifacts, e.g. evaluating them privately without publishing them?

**Follow-ups:**
- Example: reviewers get temporary access under NDA, but readers never see the artifact
- You: Would a badge saying evaluated privately convince you as a reader?

**Paper context:** Some artifacts cannot be shared for legal or privacy reasons; reviewers lack guidance for such cases.

**Example answers:**
- Yes: at least someone independent has checked it.
- No: a check that nobody else can repeat adds little.

**My notes:**
- ACM already separates Evaluated (reviewer access suffices) from Available (public archive).

### 12. C9: Open by default

**Question:** Should research software be open source by default, with closed artifacts needing a justification?

**Follow-ups:**
- Example: a company co-authored the tool and wants to sell it later
- You: If your thesis tool had commercial potential, would you open-source it?

**Paper context:** IP restrictions, licences and privacy concerns keep some artifacts closed.

**Example answers:**
- Yes: publicly funded research should be open.
- No: it drives industry collaboration away from research.

**My notes:**
- Horizon Europe: open research data mandatory, 'as open as possible, as closed as necessary', exceptions justified in a data management plan.

### 13. C9: Licensed software

**Question:** Should research tools that depend on paid commercial software be accepted as artifacts at all?

**Follow-ups:**
- Example: your artifact needs MATLAB, and the reviewer has no licence: whose problem is that?
- You: As a reviewer, would you pay for a licence yourself to evaluate someone else's artifact?

**Paper context:** Users and reviewers report artifacts needing paid licences or proprietary components (Windows, a commercial IDE); reviewers see no clear pathway.

**Example answers:**
- Accept: much real-world SE runs on commercial platforms; excluding them biases research to open tools.
- Restrict: if others cannot run or check it, the artifact misses its purpose.
- Depends whether the commercial tool is the subject of the research or a replaceable helper.

**My notes:**
- CAV, FORMATS, QEST: case by case via the chairs; FORMATS 2022 accepted MATLAB Online.
- ACM policy is silent on reviewer licences; each AEC decides. Reviewers are not expected to pay.

### 14. C10: Students as reviewers

**Question:** Is leaving artifact evaluation to students a good training opportunity, or does it undermine how rigorous and seriously taken the badges are?

**Follow-ups:**
- Example: a first-year PhD student has to judge the artifact of an experienced professor's group
- You: Would you trust a badge more if you knew a senior researcher rather than a student had awarded it?

**Paper context:** Artifact review is time-consuming and less rewarded than paper review, so it is often left to students; this may lead to inconsistent, low-quality reviews.

**Example answers:**
- Meaningful: checking that an artifact runs and matches the paper needs no seniority; students are typical future users.
- Weak: students may not judge methodology or dare to reject.

**My notes:**
- Students chosen deliberately from ECOOP/OOPSLA 2013 (current tools, training).
- Time budget about 8-20 h per artifact; Hermann et al.: most AEC members serve once.

### 15. C11: Fixed time limits

**Question:** Is it fair to have a fixed time limit (e.g. a 30-minute setup) after which an artifact fails?

**Follow-ups:**
- Example: a fuzzing experiment that by nature runs for three days
- You: How long would you give an artifact before giving up, if you were reviewing it unpaid?

**Paper context:** Reviewers report long execution times and artifacts that need more than the roughly one day they can give each.

**Example answers:**
- Fair: forces authors to make artifacts usable; future users won't invest more either.
- Unfair: penalises inherently heavy research; a reduced representative run could replace the full one.

**My notes:**
- ICSE 2026: setup over 30 min makes acceptance unlikely; whole review ~8-20 h.
- MobiSys: reviewers and authors agree a reduced but representative scope.

### 16. C11: Hardware reviewers don't have

**Question:** Should artifacts that need more hardware than reviewers have still be eligible for a badge?

**Follow-ups:**
- Example: an experiment that needs eight GPUs or a 500 GB VM image
- You: If your thesis needed a GPU cluster, how would you want it evaluated?

**Paper context:** Some experiments (cloud systems, fuzzers, program repair) are practically infeasible to re-run for reviewers.

**Example answers:**
- Yes, with a badge that states what was checked.
- No: an unrepeatable check certifies little.

**My notes:**
- Avoid 'who provides compute' (paper's recommendation, teammate's section).
- SOSP 2019 Azure credits proved hard to use; IISWC has authors provide remote access.

### 17. C12: One-shot or iterative review

**Question:** Should artifact evaluation be a one-shot review or an iterative dialogue with the authors?

**Follow-ups:**
- Example: the artifact fails because of a typo in the install instructions: reject, or ask the authors?
- You: Later users won't have the authors on call: should the review simulate that?

**Paper context:** Reviewers find single-round reviews frustrating and value authors willing to help, but unresponsive authors leave them waiting.

**Example answers:**
- Iterative: glitches are inevitable; the fixes help every later user.
- One-shot: the badge should certify that it works without the authors.
- Hybrid: a short check-in phase for setup, then a final test without help.

**My notes:**
- Most venues have a 'kick the tires' phase (SLE: 5-day response); ICSE 2026: answers within 72 h.

### 18. C12: Support after publication

**Question:** Can authors be expected to support their artifacts after publication, and for how long?

**Follow-ups:**
- Example: the PhD student who built the tool has graduated and changed jobs
- You: Would you still answer emails about your thesis code three years from now?

**Paper context:** Users value authors who help fix problems, but creators move on and support stops.

**Example answers:**
- Yes, for a stated period.
- No: archive it and say it is unsupported.

**My notes:**
- Overlaps with C3; use as its follow-up if needed.

### 19. RQ1: Rewards

**Question:** Which reward would actually make researchers invest more in their artifacts?

**Follow-ups:**
- Example: a citable DOI, a best-artifact award, or counting artifacts in hiring
- You: What would make you spend an extra week on your thesis artifact?

**Paper context:** Respondents want sharing encouraged and rewarded.

**Example answers:**
- Career credit (hiring, citations).
- Direct benefit (users, collaborations).

**My notes:**
- JOSS: citable software papers. Possible overlap with the teammate's recommendations.

