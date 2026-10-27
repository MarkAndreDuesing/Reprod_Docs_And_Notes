"""Clean speaker notes for my section (slides 11-30) of deck v9, matched to the current slide content,
plus a .docx export of those notes. Sources are named inline; only on-slide citations use [n].

Usage: python3 notes_v9.py in.pptx out.pptx out.docx
"""
import sys
from pptx import Presentation
from docx import Document
from docx.shared import Pt

def plan(about, answers, ladder, background=(), remarks=()):
    out = []
    if remarks: out += ["MY REMARKS"] + list(remarks) + [""]
    out += ["WHAT THIS IS ABOUT", about, "", "POSSIBLE ANSWERS"] + ["- " + a for a in answers]
    out += ["", "IF THE ROOM IS QUIET (ask in this order)"] + [f"{i}. {x}" for i, x in enumerate(ladder, 1)]
    if background: out += ["", "BACKGROUND (for you; sources named)"] + ["- " + b for b in background]
    return "\n".join(out)

NOTES = {
11: """SPEAKING PROTOCOL (about 30 seconds)
1. Link to last week: "Last week's papers asked why so few working artifacts exist. This paper asks why making good artifacts is hard, and what could be done about it."
2. Paper: "Timperley and colleagues from Carnegie Mellon, published in Empirical Software Engineering in 2021."
3. Did: "They did two studies in parallel: a publication survey, checking how many papers at top SE venues link an artifact and whether those links still work, and an author survey asking researchers about their experiences as creators, users and reviewers of artifacts."
4. Found: "First, the community does value artifacts, and sharing has become a norm. Second, they found 12 challenges in creating, sharing, using and reviewing artifacts. We'll go through them in a moment."
5. Analysed: "In a secondary analysis they look at why these challenges persist and how they connect."
6. Then: "From that they derive 8 recommendations for creators, reviewers, process organisers and community leaders; Minh Thi will present those later."
Hand-over: "First, the research questions."

TARGET GROUPS IF ASKED (paper §3.4)
- Creators: primary researchers (often students and postdocs) and their advisors and mentors
- Reviewers: AEC members, journal reviewers, programme committee members
- Process organisers: AEC chairs, conference chairs, journal editors
- Community leaders: steering committees, professional organisations, hiring and promotion committees, funding agencies

BACKGROUND IF ASKED
- Publication survey: technical-track papers at ICSE, FSE, ASE and EMSE, 2014-2018; artifact = any linked material; available = the link still works.
- Author survey: authors of 2018 papers at those venues; open answers coded into themes.""",

12: """MY REMARKS
RQ1 establishes a baseline for RQ2.
Don't take too long on RQ1 in general, since I don't discuss it!

SPEAKING PROTOCOL (~30 s)
- "Two research questions. RQ1 is the baseline: does the SE community see value in artifacts at all? Only if yes is it worth asking RQ2: what gets in the way?"
- "RQ2 is split by perspective: creators who make artifacts, users who try to run or build on someone else's, and reviewers on artifact evaluation committees."
- The same person can be all three; most respondents were creators and users, only about a fifth had reviewed artifacts.
- Hand-over: "Let's start with RQ1." (RQs on p. 6)""",

13: """SPEAKING PROTOCOL (~30 s, keep short)
- "Short answer to RQ1: yes. Respondents see artifacts as valuable, say not every paper needs one, but that sharing should be encouraged and rewarded."
- "Their main argument: without the artifact, replicating a study is hard and unreliable."
- Tiles in one sentence each: supporting evidence (readers trust the claims more), community norm ("good practice"), reuse (tools and data others extend), understanding (details that don't fit in a paper).
- Bridge: "So people value artifacts. Why are they still often missing or unusable? That's RQ2."

BACKGROUND IF ASKED
- 62.69 % of papers at ASE, EMSE, FSE and ICSE 2014-2018 contain an artifact, rising from 50.56 % (2014) to 69.47 % (2018) (Fig. 2, pp. 11-12).
- "Artifact" here means any linked material, which is why the share is higher than in last week's Heumüller et al. paper (48 % of ICSE papers linked runnable software).""",

14: """SPEAKING PROTOCOL (~40 s)
- "These are the 12 challenges they found, from a thematic analysis of the open survey answers. So this shows which problems exist, not how often each occurs." (p. 9)
- Explain the symbols: square = creators mention it, triangle = users, star = reviewers.
- Pattern: portability, tacit knowledge and external constraints hit all three groups; the last three (incentives, technical obstacles, communication) are reviewer-only; 'not worth it' and double-blind review are creator-only.
- "I'll go through them in groups of three, focusing on what's new or surprising."
- Optional framing from the paper: the problems come down to communication, reward (social system), time ('bit rot') and the technical side of the artifacts.""",

15: """MY REMARKS
Don't have to say everything on the slides.
Skipped the counterpoint "whole research areas died for lack of artifacts" and trimmed the "Not worth it" ideas.
Left "hard-wired paths, root access needed" out of the user point.
VMs can be used to mitigate these portability challenges and to avoid the security risks associated with executing untrusted code on the reviewer's host machine (p. 21)!

SPEAKING PROTOCOL (~60 s)
C1 Not worth it
- "Biggest creator issue: preparing an artifact takes time that could go into the next paper, does little for your career, and maybe few people will use it."
- Concerns: reputation damage from messy code, mistakes being found, being scooped, so artifacts with untapped publication value are held back.
C2 Portability
- Creators can't foresee every environment; making it accessible means refactoring or building a VM/container afterwards.
- Users: builds and runs fail. Reviewers: installing dependencies and invasive libraries is the biggest hurdle; VMs are safer, but large, can cause problems across operating systems, and distort performance measurements.
C3 Maintenance
- "Artifacts need ongoing care: bugs, changing use cases, bit rot. Usually a student maintains it, then graduates."
- Users then need outdated, hard-to-find libraries.

BIT ROT, IF ASKED
Software slowly stops working over time even though its code is unchanged, because everything around it changes:
- Dependencies change or disappear (new versions break things, old versions removed; Python 2 reached end of life in 2020).
- The environment changes (new operating systems behave differently; e.g. chemistry analysis scripts that ran correctly for years gave wrong results on newer systems because the order of files changed).
- External services vanish (download links, APIs, hosted images).
- Knowledge fades (the person who knew how to set it up has left; C4).

BACKGROUND IF ASKED
- Containers run at close to native speed, VMs are slower, which matters for performance claims (Felter et al., IBM 2014).
- C1 detail: opportunity cost is highest when submitting to an AEC (p. 13).
- C2 numbers (Table 5): no build instructions 79, unavailable dependency 69, missing dependency 66, modified source 60, run-time error 55, re-implemented 28.""",

16: """MY REMARKS
C5 less interesting, skim over.

SPEAKING PROTOCOL (~45 s)
C4 Tacit knowledge
- "Know-how that only lives in the developer's head: which order to run the scripts, which paths to change, which parameters matter. Documenting it is a burden."
- Users struggle to understand artifacts and miss usage and build instructions (the most and third-most common user problems).
- Reviewers: automated scripts help, but are no universal solution; they give no insight into the process and may replicate the authors' mistakes.
C5 Doesn't fit purpose (skim)
- The artifact doesn't do what the paper says, or only works for a narrow case.
C6 No standards / guidelines
- Creators don't know what is expected: packaging, contents, quality, setup instructions, documentation.
- Reviewers find the criteria for a good artifact ambiguous and hard to apply, and it is unclear what review is for: just running the script, or a thorough investigation?

BACKGROUND IF ASKED
- ACM only defines the badges (Functional, Reusable, Available, Reproduced, Replicated); each conference's committee sets its own concrete rules, which is why standards differ (ACM badging policy v1.1; Hermann et al. 2020).""",

17: """MY REMARKS
C8 less interesting, skim over.

SPEAKING PROTOCOL (~45 s)
C7 Hosting
- "Where do you put an artifact so it's still there in ten years, can hold large data, and is free? GitHub, Dropbox or Google Drive are not meant as long-term archives."
- Users often can't access artifacts because links are dead: about 14 % of links in the publication survey were dead in 2019, about a quarter for 2014 papers (Fig. 3).
C8 Double-blind review (skim)
- The artifact must be anonymised for review, and anonymous hosting is more complicated.
C9 External constraints
- Things authors can't control: intellectual property, contracts, liability, privacy.
- Users find it harder to build on such artifacts. Reviewers may lack licences or proprietary tools to run them, and there are no guidelines for this case.

BACKGROUND IF ASKED
- Zenodo (run by CERN) is free, gives a DOI, holds 50 GB per record (200 GB on request) and can archive GitHub releases automatically (Zenodo documentation). ICSE now requires such an archive for the "Available" badge (ICSE 2026 artifact call).
- ACM allows proxy data in place of proprietary data (ACM badging policy v1.1).""",

18: """SPEAKING PROTOCOL (~45 s)
C10 No reviewer incentives
- Reviewing artifacts takes a lot of time and counts less than paper reviewing, which can lead to inconsistent, low-quality reviews. Students often do it as training, which signals that artifacts are secondary.
C11 Technical obstacles
- Long runtimes, too little computing power or disk space; some experiments (cloud systems, fuzzing, program repair) are practically impossible to re-run.
C12 Limited communication
- No good channel between authors and reviewers; a minor install glitch shouldn't mean rejection if authors could quickly help; responsive vs. unresponsive authors decide whether reviewers wait for days.
Wrap-up: "Reviewers face the same problems as users (portability, documentation) and as creators (no guidelines, no reward). That's the end of the results; next, the discussion."

BACKGROUND IF ASKED (not on the slide)
- At FSE 2015-2018 only about a third of papers with artifacts were submitted to artifact evaluation, and 86 % of those passed (Fig. 4, p. 21).
- Artifact committees were deliberately staffed with senior PhD students from ECOOP/OOPSLA 2013 on (organisers' calls).
- Typical review budget is about 8-20 hours per artifact (SOSP 2021, APLAS 2022 committee calls).
- Most venues have a "kick the tires" phase in which reviewers and authors fix setup problems (e.g. SLE 2025).""",

19: plan(
 "Some artifact committees review in one round, others let reviewers and authors talk and fix problems. Which is better, and what does that say about what a badge should mean?",
 ["ITERATIVE - small glitches (a typo in the install instructions) are inevitable; fixing them during review improves the artifact for everyone later.",
  "ONE-SHOT - later users won't have the authors on call; the review should test whether it works on its own, as it will for them.",
  "HYBRID - a short 'does it start' phase with author help, then a final test without help; all fixes must go into the artifact itself.",
  "WHAT IS REVIEW FOR - confirming the paper's results once (checking the evidence) vs. certifying a tool others can build on. Paper 1 (Hermann et al.) found: reviewers want reproducible results, users want reusable tools.",
  "SUSTAINABILITY - authors can't support a tool forever; students graduate, emails go unanswered; a badge can only describe the state at review time."],
 ["The artifact fails on a typo in the install instructions: reject, or ask the authors?",
  "Later users won't have the authors' help: should reviewers?",
  "If you started a thesis on a badged tool, what would you expect the badge to guarantee?",
  "Would you still answer emails about your thesis code in three years?"],
 ["Most venues have a 'kick the tires' phase with author responses (SLE 2025: 5 days; ICSE 2026: answers within 72 h).",
  "Hermann et al. 2020, p. 479: 'Reviewers want replicability, users want reusability' (old ACM terms; their 'replicability' is today's reproducibility)."]),

20: plan(
 "A script that rebuilds all results with one command makes an artifact easy to run. The question is whether easy re-running also means the results are properly checked, i.e. its pros and cons.",
 ["PRO - lowers the barrier: without a script, many artifacts never run because steps are missing; a script proves the pipeline works end to end and the published numbers come from the published code.",
  "PRO - captures tacit knowledge: the order of steps, paths and parameters are written down in code instead of living in the author's head; a new student can start from it.",
  "PRO - makes checking cheap: reviewers with limited time can re-run everything and spend their time on the results instead of the setup.",
  "CON - false confidence: 'the numbers come out' only shows the code runs the same way again, not that the method is right. If the analysis has a bug, the script reproduces the bug perfectly (reviewers in the paper: AECs are 'likely to replicate the same mistake').",
  "CON - black box: a reviewer who only presses the button never sees what happens inside, e.g. whether test data leaked into training data or a filter silently drops inconvenient cases.",
  "CON - hard to tell what went wrong: if results differ, it is unclear whether the artifact is faulty or the reviewer used it wrongly (P74).",
  "CON - narrow reuse: a script reproduces exactly the paper's experiment; adding a case study can be harder than with a documented step-by-step setup (a reviewer: 'easy to reproduce, difficult to understand where to add more case studies').",
  "MIDDLE - a script is necessary but not sufficient: add a short description of what each step does, small example inputs, and let reviewers change one input to see whether results behave plausibly."],
 ["What exactly does a reviewer know once the script finished successfully?",
  "Imagine the script produces the required data, but one result depends on a wrongly chosen threshold in the code: who would ever notice?",
  "As a reviewer, what would you want next to the script (comments, a walkthrough, small examples)?",
  "Could someone reproduce your bachelor thesis results from your repository alone?"],
 ["Chemistry analysis scripts (2019) gave correct results on some operating systems and wrong ones on others, because the order of files differed; a script that 'works' can still be wrong (The Register, 2019).",
  "In other fields, 'push-button replication' is only a first check, followed by an independent re-implementation."],
 ["From the paper (p. 22): some reviewers suggest automated scripts to mitigate the tacit knowledge problem; others stress they are not a panacea. P74: 'it is often difficult to know whether the submitted device is faulty, or if [you don't know how to] use it.' A script may behave as a black box that gives no insight into whether the process is sound."]),

21: plan(
 "Reviewers may face missing instructions and gaps they have to fill themselves, or experiments that run for days. How much time and effort should they invest before they may give up, and what is fair to both reviewers and authors?",
 ["LITTLE - the artifact must work for a stranger; if it fails after the expected setup time, that is the result. A reviewer who fixes it hides problems later users will face.",
  "MORE - reviewers are often the only people who ever seriously try the artifact; an hour of fixing a missing dependency and reporting it back helps every later user.",
  "BY STAGE - a short 'does it start' check first, then the authors get a chance to fix things, then the full review; effort grows only once basics work.",
  "FIXED LIMIT - a clear rule (e.g. setup within 30 minutes, review within a day) protects volunteer reviewers and makes reviews comparable.",
  "FLEXIBLE LIMIT - long-running experiments (fuzzing for three days) are penalised by a flat limit for their nature, not their quality; authors could declare the expected runtime and provide a short representative run.",
  "SEPARATE SETUP FROM RUNTIME - setup must be quick (that is about packaging and documentation), but long runtimes are acceptable if they run unattended.",
  "BALANCE - authors want a fair chance and not be rejected for a typo; reviewers are unpaid and have several artifacts; both sides benefit from clear expectations stated up front."],
 ["After two hours it fails on a missing library you could install yourself: fix it, ask the authors, or reject?",
  "A fuzzing experiment runs for three days: should the reviewer wait, or review a shorter run?",
  "As the author, would a 30-minute setup limit feel fair for your project?",
  "Who should decide the time budget: the conference, the authors or the reviewers?"],
 ["Typical budget: about 8-20 hours per artifact (SOSP 2021 committee call: 10-20 h, 2-4 artifacts per member; APLAS 2022: about 8 h, 3-4 per member).",
  "Setup is usually expected within about 30 minutes as a guideline (OSDI, OOPSLA; ICSE 2026: more than 30 minutes makes acceptance unlikely); NDSS 2027 asks full experiments to take at most 1 day on a desktop. No venue found that varies limits by artifact type."]),

22: plan(
 "Some artifacts need administrator (root) rights or change system libraries, and outdated dependencies can carry security holes. Reviewers protect themselves with VMs. Should they be allowed to refuse such artifacts?",
 ["YES, REFUSE - reviewers are volunteers; nobody should risk their own machine. Authors must package it safely (VM, container) or provide a machine.",
  "YES, BUT ONLY IF NO SAFE PACKAGE - refusing is fine when authors didn't even try to isolate it.",
  "NO - some research genuinely needs deep system access (operating systems, drivers, security tools, performance tools); refusing would make whole fields unevaluable.",
  "SHIFT RESPONSIBILITY - instead of refusing, the conference provides isolated test machines, or authors give remote access to a machine they own.",
  "TRUST - running other people's code is normal in open source; why should research be stricter, or should it be stricter because reviewers can't inspect everything?"],
 ["If refusing were allowed, which research could no longer be evaluated?",
  "Would you run a stranger's install script with administrator rights on your own laptop?",
  "Who should provide a safe machine: reviewer, authors or conference?"],
 ["From the paper: users report artifacts that 'require the user to be root' (p. 18); reviewers cite the 'requirement to install complex and invasive program/system libraries' and use VMs 'to avoid the security risks associated with executing untrusted code on the reviewer's host machine' (p. 21).",
  "POPL's artifact call recommends VM images partly because they 'protect reviewers from malfunctioning artifacts damaging their computer'."]),

23: plan(
 "Some datasets or artifacts are too big for common archives and for a reviewer's laptop. How can they still be shared, and how can the work still be reviewed?",
 ["SUBSET - share a small, representative sample plus the scripts that produced the full data; reviewers check the pipeline on the sample.",
  "SHARE THE RECIPE, NOT THE DATA - if the data comes from public sources (e.g. mined repositories), publish the exact scripts, queries and dates so others can regenerate it.",
  "OTHER HOSTING - university or national research data repositories, or well-documented split archives; storage costs may need to be in the project budget.",
  "REVIEWER ACCESS - authors keep the data on their own server and give reviewers temporary remote access; readers later get only the subset.",
  "ACCEPT LIMITS - some artifacts can't be fully reviewed; the badge or paper should say what was actually checked.",
  "WIDER POINT - does size make an artifact effectively unreviewable, and should that change how much we trust the paper?"],
 ["Several terabytes of mined repository data: what would you publish?",
  "What would you publish if your thesis data were that large?",
  "What workarounds would still let a reviewer check your work?",
  "If reviewers can only check a sample, should the badge say so?"],
 ["[1] Zenodo: 50 GB per record, one-time increase to 200 GB on request; free, DOI per version, run by CERN (Zenodo documentation).",
  "Some venues let reviewers and authors agree on a reduced but representative scope for heavy experiments (MobiSys 2026)."]),

24: plan(
 "Building on the last question: some experiments need hardware reviewers don't have (many GPUs, clusters, special devices). Who should make the resources available, and what does a review still mean otherwise?",
 ["CONFERENCE PROVIDES - conferences or ACM/IEEE fund shared machines or cloud credits, so reviewing doesn't depend on where a reviewer works. (This is also one of the paper's recommendations: keep it short, Minh Thi covers it.)",
  "AUTHORS PROVIDE - authors give reviewers remote access to their own hardware or pay for cloud time; this is what most venues ask for today.",
  "SCALED-DOWN RUN - authors provide a smaller version that runs on a normal machine and shows the same trend; weaker, but practical.",
  "NO BADGE - if nobody can run it, nobody can certify it; better to say 'not evaluated'.",
  "FAIRNESS - if authors must pay, well-funded groups get badges more easily; if conferences pay, someone has to fund it (conference fees, sponsors).",
  "TRUST - is a badge after a scaled-down run still meaningful to readers?"],
 ["An experiment needs eight GPUs for a week, and the reviewer has a laptop: what now?",
  "Would you trust a badge from a reviewer who only ran a scaled-down version?",
  "As an author, would you pay for reviewers' cloud time to get a badge?"],
 ["Current practice: authors give reviewers anonymous remote (SSH) access to special hardware (SenSys 2024, SACMAT 2026, IEEE S&P 2026, MICRO 2026). MICRO 2026 may decline to evaluate artifacts if no reviewer can access the hardware.",
  "Donated cloud credits were tried (Azure credits for SOSP 2019) but proved hard to use for exactly the artifacts that needed them.",
  "The paper recommends that ACM/IEEE fund compute for reviewers (Rec 6/7): hand over to Minh Thi here."]),

25: plan(
 "Intellectual property, privacy and commercial interests limit what can be shared. Should openness be the default, where are legitimate limits, and should a paper be criticised when its industry partner won't release the data?",
 ["FULLY OPEN - publicly funded research should be public; closed code or data means results can't be checked.",
  "OPEN BY DEFAULT, EXCEPTIONS EXPLAINED - share everything unless there is a concrete reason (personal data, partner contract), and state that reason in the paper.",
  "LIMITS - personal data: interview transcripts or user logs can identify people even after anonymising.",
  "LIMITS - industry partners: forcing openness means companies stop collaborating with academia; partners in the paper refused even anonymised data, fearing liability lawsuits.",
  "LIMITS - commercial plans: a tool may be the basis of a start-up; publishing it fully removes that option.",
  "INDUSTRY DATA - criticise: readers can't check the claims, so the evidence is weaker whatever the reason.",
  "INDUSTRY DATA - don't criticise: it punishes collaboration for something the authors can't control; one author in the paper called this a 'ritualistic blanket argument' (pp. 17-18).",
  "PARTIAL OPENNESS - share the method and analysis scripts but not raw data, provide proxy or synthetic data with the same structure, or give reviewers access under an NDA."],
 ["A company co-authored the tool and wants to sell it later: open or not?",
  "Would you consider the artifact open enough if it won't be accessible in the future?",
  "If you were building on a study whose data is under NDA, would you trust it less?",
  "Is 'we can't share it' acceptable if the paper explains why?"],
 ["ICSE's open science policy: sharing data is not required for acceptance; authors explain why they can't share in a data availability section.",
  "ACM's badge policy allows proxy data in place of proprietary data; the 'Evaluated' badges can be earned with reviewer-only access, 'Available' needs public access.",
  "EU research funding (Horizon Europe) follows 'as open as possible, as closed as necessary': open data is the default, exceptions must be justified."],
 ["IP := Intellectual Property"]),

26: plan(
 "Building on the last question: here openness is limited not by choice but by a licence. Some artifacts depend on paid software (e.g. MATLAB, Windows, a commercial IDE) that reviewers or users don't have. Should such artifacts count, and who carries the cost?",
 ["ACCEPT - much real software engineering happens on commercial platforms; refusing such artifacts pushes research toward open tools only and away from practice.",
  "ACCEPT, AUTHORS ORGANISE ACCESS - authors must provide a way to run it (online version, remote machine, trial licence), otherwise no 'Functional' badge.",
  "RESTRICT - an artifact others can't run doesn't do its job; at most an 'Available' badge.",
  "DEPENDS ON ROLE - if the commercial tool is the subject of the research (studying a commercial IDE), accept it; if it is a replaceable helper (plotting in MATLAB), authors should port it to free tools.",
  "WHO PAYS - not the reviewer (unpaid volunteer); the authors, since they chose the tool; or the conference. In practice access often depends on whether the reviewer's university has a campus licence, which is unfair."],
 ["Your artifact needs MATLAB and the reviewer has no licence: whose problem is that?",
  "As a reviewer, would you pay for a licence yourself? Who should instead?",
  "Is rejecting such artifacts fair, or does it punish industry-relevant research?"],
 ["No conference states a budget for artifact evaluation; committees are unpaid volunteers set up by the organisers (no source found that says otherwise).",
  "CAV asks authors who can't ship licensed software such as MATLAB in a VM or Docker image to contact the chairs for a case-by-case solution; FORMATS 2022 accepted a MATLAB Drive folder runnable in MATLAB Online.",
  "ACM's badge policy says nothing about reviewer licences; each committee decides."]),

27: plan(
 "Artifact review is time-consuming and less rewarded than paper review, so it is often given to PhD students. Does that make badges less trustworthy, or is it a sensible choice?",
 ["GOOD CHOICE - students know current tools well, have time to try things, and are the typical future users of artifacts; if they can run it, others can too.",
  "GOOD CHOICE - training: students learn what makes a good artifact and will build better ones themselves.",
  "WEAKER BADGES - students may lack the experience to judge whether the method or experiment design is sound; they check 'it runs', not 'it is right'.",
  "WEAKER BADGES - power imbalance: a first-year PhD student may not dare to reject the artifact of a well-known group.",
  "SIGNAL - giving the job to students tells everyone artifacts are second-class, so authors put in less effort.",
  "MIDDLE - mixed committees: students run the artifacts, an experienced reviewer checks the judgement and handles disputes."],
 ["Would you trust a badge more if a senior researcher had awarded it?",
  "What would a badge need to certify for you to rely on it in your thesis?",
  "Would you volunteer for an artifact evaluation committee? What would you get out of it?"],
 ["Artifact committees were deliberately filled with senior PhD students from ECOOP and OOPSLA 2013 on, because they know current tools and so the next generation learns about artifacts (organisers' calls).",
  "Hermann et al. (Paper 1): most committee members serve only once, and about a third have never submitted an artifact themselves."]),

29: plan(
 "Artifacts stop working as libraries, compilers and operating systems change and the student who built them leaves. Can this be prevented, how, and who should keep it running?",
 ["UNAVOIDABLE - the software world keeps changing; you can delay decay, not stop it. Accept that an artifact documents a point in time.",
  "LIMIT IT - freeze the environment (a container or VM image with everything included), pin exact library versions, keep dependencies few, prefer well-known tools.",
  "LIMIT IT - plain source code plus a clear description is the most durable form: even if it doesn't run, others can understand and re-implement it.",
  "WHO KEEPS IT RUNNING - hand over to a group member or a permanent research software engineer when the student leaves; plan this from the start.",
  "COST - maintenance takes time nobody is paid for; the group, the university or funders would have to pay, or the artifact is archived and marked 'unmaintained'.",
  "EXPECTATION - an artifact only needs to work at publication and review time; afterwards it is a record, not a product."],
 ["A 2015 thesis tool needs Python 2 and a library that no longer exists: fix it, freeze it in an image, or let it go?",
  "Who should continue keeping your thesis tool running after you leave?",
  "Is a frozen image a solution, or does the image itself decay (e.g. if the hosting service deletes it)?"],
 ["Python 2 reached end of life on 1 Jan 2020 and Linux distributions removed it; the research tool OBITools (Python 2) is no longer maintainable and is kept runnable only through a Docker image its maintainers provide.",
  "Docker Hub announced in 2020 that unused images of free accounts would be deleted after 6 months; enforcement was paused after protests. Even 'frozen' images depend on a company's policy.",
  "Germany's DFG expects code and data behind a publication to be archived for 10 years; archived is not the same as runnable.",
  "Research software engineers (e.g. at Princeton, Aalto) are permanent staff who keep research code alive when students leave."]),

30: plan(
 "Respondents value artifacts and want sharing rewarded. The four reasons they share are supporting evidence, community norm, reuse and understanding. What reward would make the effort worth it?",
 ["CAREER CREDIT - artifacts counted in hiring and promotion, like papers; strongest lever, but needs a way to judge artifact quality.",
  "CITATIONS - artifacts get their own DOI and are cited separately; credit in the currency researchers already use.",
  "VISIBILITY - badges on the paper, best-artifact awards; cheap, but unclear whether anyone hiring cares.",
  "FUNDING - grants require and pay for artifact work; it becomes part of the job instead of extra work.",
  "NORM INSTEAD OF REWARD - if sharing is simply expected, no reward is needed; not sharing becomes the exception that needs explaining."],
 ["What would make you spend an extra week on your thesis artifact?",
  "Which of the four reasons (evidence, norm, reuse, understanding) would a reward strengthen most?",
  "Hand-over: 'The paper itself makes recommendations on this; Minh Thi presents them next.'"],
 ["Journal of Open Source Software (JOSS): publishes short, citable papers about research software, so software work counts for careers."]),
}

src, dst, docx_out = sys.argv[1], sys.argv[2], sys.argv[3]
p = Presentation(src)
slides = list(p.slides)
def title(s):
    texts = [sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip() and sh.text_frame.text != "‹#›"]
    if not texts: return ""
    if texts[0].startswith("Paper 2 · Discussion") and len(texts) > 1: return texts[1]
    return texts[0] + (" · " + texts[1].split("\n")[0] if texts[0] == "Results" and len(texts) > 1 else "")
for n, text in NOTES.items():
    s = slides[n - 1]
    assert s._element.get("show") != "0", n
    s.notes_slide.notes_text_frame.text = text
# on-slide citation: Zenodo [4] -> [1]; References slide lists only it
for sh in slides[22].shapes:
    if sh.has_text_frame:
        for pa in sh.text_frame.paragraphs:
            for r in pa.runs:
                if "[4]" in r.text: r.text = r.text.replace("[4]", "[1]")
for s in slides:
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.startswith("[1] ACM"):
            tf = sh.text_frame
            for pa in list(tf.paragraphs)[1:]: pa._p.getparent().remove(pa._p)
            runs = tf.paragraphs[0].runs
            runs[0].text = "[1] Zenodo: size limitations and general policies. help.zenodo.org; about.zenodo.org/policies"
            for r in runs[1:]: r.text = ""
p.save(dst)

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(10.5)
doc.add_heading("Paper 2 (Timperley et al. 2021): Presenter Notes", 0)
doc.add_paragraph("Slides 11-30 of the team deck (lecture 2). Hidden slides are not included.")
SECTIONS = ("MY REMARKS", "WHAT THIS IS ABOUT", "POSSIBLE ANSWERS", "IF THE ROOM IS QUIET", "BACKGROUND", "SPEAKING PROTOCOL", "TARGET GROUPS", "BIT ROT")
for n in sorted(NOTES):
    s = slides[n - 1]
    doc.add_heading(f"Slide {n}: {title(s)}", 1)
    for line in NOTES[n].split("\n"):
        if not line.strip(): continue
        if line.startswith(SECTIONS) or line.startswith("C") and len(line) < 40 and line[1].isdigit():
            doc.add_heading(line, 3)
        elif line.startswith("- "):
            doc.add_paragraph(line[2:], style="List Bullet")
        elif line[:2].rstrip(".").isdigit() and line[1:3] in (". ", "0."):
            doc.add_paragraph(line.split(". ", 1)[1], style="List Number")
        else:
            doc.add_paragraph(line)
doc.save(docx_out)
print("ok")
