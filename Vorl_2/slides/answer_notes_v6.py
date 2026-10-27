"""Rewrites the speaker notes of the visible Paper 2 question slides with a fuller answer plan:
what the question is about, possible answers with reasoning, a follow-up ladder, then the
existing background (kept from the current notes)."""
import sys
from pptx import Presentation

N = {
"C4 Tacit knowledge: One-click reproduction scripts": dict(
 question="Is a one-click reproduction script good or bad for scientific scrutiny and evaluation? Does the idea help or harm more?",
 about="A script that rebuilds all results with one command makes an artifact easy to run. The question is whether easy re-running also means the results are properly checked.",
 answers=[
  "HELPS - lowers the barrier: without a script, many artifacts never run at all because steps are missing; a script at least proves the pipeline works end to end and the published numbers come out of the published code.",
  "HELPS - removes tacit knowledge: the order of steps, paths and parameters are written down in code instead of living in the author's head; a new student can start from it.",
  "HELPS - makes checking cheap: reviewers with one day can re-run everything and spend their time on looking at results instead of fixing setup.",
  "HARMS - false confidence: 'the numbers come out' only shows the code is deterministic, not that the method is right. If the analysis has a bug, the script reproduces the bug perfectly (the paper's reviewer quote: AECs 'likely to replicate the same mistake').",
  "HARMS - black box: a reviewer who only presses the button never looks at what happens inside, e.g. whether test data leaked into training data or a filter silently drops inconvenient cases.",
  "HARMS - narrow reuse: a script reproduces exactly the paper's experiment; changing the input or adding a case study can be harder than with a documented step-by-step setup (paper: 'easy to reproduce, difficult to understand where to add more case studies').",
  "MIDDLE - a script is necessary but not sufficient: combine it with a short description of what each step does, small example inputs, and reviewers who change one input to see if results behave plausibly."],
 ladder=[
  "What exactly does a reviewer know after the script finished successfully?",
  "Imagine the script produces every table, but one table depends on a wrongly chosen threshold in the code: who would ever notice?",
  "As a reviewer, what would you want next to the script (comments, a walkthrough, small examples)?",
  "Could someone reproduce your bachelor thesis results from your repository alone?"]),
"C4 Tacit knowledge: Reviewer effort": dict(
 about="Reviewers report missing instructions and gaps they had to fill themselves. How far should they go, in time, computing resources and their own money, before they may reject?",
 answers=[
  "TIME - little: the artifact must work for a stranger; if it fails after the setup time, that is the result. A reviewer who fixes it hides problems later users will face.",
  "TIME - more: reviewers are often the only people who ever seriously try the artifact; an hour of fixing a missing dependency and reporting it back helps every later user.",
  "TIME - by stage: a short 'does it start' check first, then the authors get a chance to fix, then the full review; effort grows only once basics work.",
  "COMPUTE - reviewer's laptop only: anything that needs more is the authors' job to provide (remote access, a smaller run).",
  "COMPUTE - shared resources: departments or conferences could offer machines, otherwise only well-equipped reviewers can evaluate heavy work.",
  "MONEY - never the reviewer's: reviewers are unpaid volunteers, so paying for cloud time or licences out of pocket is unreasonable; the authors (or the conference) pay.",
  "MONEY - authors pay: if an artifact needs a paid cloud GPU, the authors provide the account; this keeps reviewing fair but favours well-funded groups.",
  "LIMIT - a clear rule (e.g. a fixed number of hours) protects reviewers and makes reviews comparable; no rule means some reviewers deep-dive for days while others stop after ten minutes."],
 ladder=[
  "After two hours it fails on a missing library you could install yourself: fix, ask the authors, or reject?",
  "Would you spend 20 euros of your own money on cloud time to review someone else's artifact? 200?",
  "As an author, how much of a reviewer's goodwill would you rely on?",
  "Who should be responsible for the cost: reviewer, authors or conference?"]),
"C9 External constraints: Open by default": dict(
 about="IP, privacy and commercial interests limit what can be shared. Should openness be the default, with closed parts needing a reason, and where are reasonable limits?",
 answers=[
  "FULLY OPEN - publicly funded research should be public; closed code means results can't be checked.",
  "OPEN BY DEFAULT, EXCEPTIONS EXPLAINED - share everything unless there is a concrete reason (personal data, partner contract), and state that reason in the paper.",
  "LIMITS - personal data: interview transcripts or user logs can identify people even after anonymising; sharing them can harm participants.",
  "LIMITS - industry partners: if a company provides data or co-develops a tool, forcing openness means they stop collaborating with academia.",
  "LIMITS - commercial plans: a tool may be the basis of a start-up; publishing it fully removes that option for the student.",
  "PARTIAL OPENNESS - share the method and analysis scripts but not raw data; share binaries but not source; share with reviewers only."],
 ladder=[
  "A company co-authored the tool and wants to sell it later: open or not?",
  "Which part of your own thesis work would you not want to make public, and why?",
  "Is 'we can't share it' acceptable if the paper explains why?"]),
"C9 External constraints: Licensed software": dict(
 about="Some artifacts depend on paid software (e.g. MATLAB, Windows, a commercial IDE) that reviewers or users don't have. Should such artifacts count, and who carries the cost?",
 answers=[
  "ACCEPT - much real software engineering happens on commercial platforms; refusing such artifacts pushes research toward only open tools and away from practice.",
  "ACCEPT, AUTHORS ORGANISE ACCESS - authors must provide a way to run it (online version, remote machine, trial licence), otherwise no 'functional' badge.",
  "RESTRICT - an artifact others can't run doesn't do its job; it should at most get an 'available' badge.",
  "DEPENDS ON ROLE - if the commercial tool is the subject of the research (studying a commercial IDE), accept it; if it is a replaceable helper (plotting in MATLAB), authors should port it to free tools.",
  "COST - reviewers shouldn't pay; universities often have campus licences, so in practice access depends on where a reviewer works, which is unfair."],
 ladder=[
  "Your artifact needs MATLAB and the reviewer has no licence: whose problem is that?",
  "As a reviewer, would you pay for a licence yourself?",
  "Is rejecting such artifacts fair, or does it punish industry-relevant research?"]),
"C10 Lack of reviewer incentives: Students as reviewers": dict(
 about="Artifact review is time-consuming and less rewarded than paper review, so it is often given to PhD students. Does that make badges less trustworthy, or is it a sensible choice?",
 answers=[
  "GOOD CHOICE - students know current tools well, have time to try things, and are exactly the typical future users of artifacts; if they can run it, others can too.",
  "GOOD CHOICE - training: students learn what makes a good artifact and will build better ones themselves.",
  "WEAKER BADGES - students may lack the experience to judge whether the method or experiment design is sound; they check 'it runs', not 'it is right'.",
  "WEAKER BADGES - power imbalance: a first-year PhD student may not dare to reject the artifact of a famous group.",
  "SIGNAL - giving the job to students tells everyone artifacts are second-class, so authors put less effort in.",
  "MIDDLE - mixed committees: students run the artifacts, an experienced reviewer checks the judgement and handles disputes."],
 ladder=[
  "Would you trust a badge more if a senior researcher awarded it?",
  "What would a badge need to certify for you to rely on it in your thesis?",
  "Would you volunteer for an artifact evaluation committee? What would you get out of it?"]),
"C2 Portability: Running untrusted artifacts": dict(
 about="Some artifacts need administrator (root) rights or change system libraries. Reviewers protect themselves with VMs. Should they be allowed to refuse such artifacts?",
 answers=[
  "YES, REFUSE - reviewers are volunteers; nobody should risk their own machine. Authors must package it safely (VM, container) or provide a machine.",
  "YES, BUT ONLY IF NO SAFE PACKAGE - refusing is fine when authors didn't even try to isolate it.",
  "NO - some research genuinely needs deep system access (operating systems, drivers, security tools, performance tools); refusing would make whole fields unevaluable.",
  "SHIFT RESPONSIBILITY - instead of refusing, the conference provides isolated test machines, or authors give remote access to a machine they own.",
  "TRUST QUESTION - running code from strangers is normal in open source; why should research be stricter?"],
 ladder=[
  "If refusing were allowed, which research could no longer be evaluated?",
  "Would you run a stranger's install script with administrator rights on your own laptop?",
  "Who should provide a safe machine: reviewer, authors or conference?"]),
"C3 Maintenance: Decay and maintenance": dict(
 about="Artifacts stop working as libraries, compilers and operating systems change and the student who built them leaves. Can this be prevented, and how?",
 answers=[
  "UNAVOIDABLE - the software world keeps changing; you can delay decay, not stop it. Accept that artifacts document a point in time.",
  "LIMIT IT - freeze the environment (container or VM image that includes everything), pin exact library versions, keep dependencies few, prefer plain and well-known tools.",
  "LIMIT IT - plain source code plus a clear description is the most durable form: even if it doesn't run, others can understand and re-implement it.",
  "ORGANISE IT - hand over to a group member or a permanent research software engineer when the student leaves; plan this from the start.",
  "COST - maintenance takes time nobody is paid for; the group, the university or funders would have to pay, or the artifact is archived and marked 'unmaintained'.",
  "EXPECTATION - an artifact only needs to work at publication and review time; afterwards it is a record, not a product."],
 ladder=[
  "A tool only runs on Python 2, which has had no updates since 2020: fix it, freeze it in an image, or let it go?",
  "Should your thesis tool still run when the next student picks it up three years later?",
  "Is a frozen image a solution, or does the image itself decay (e.g. if the hosting service deletes it)?"]),
"C7 Hosting / C11 Technical obstacles: Unreviewable artifacts": dict(
 about="Some artifacts are so large or need such special hardware that no reviewer can run them. What should a badge mean then?",
 answers=[
  "NO BADGE - a check nobody can perform certifies nothing; better honest 'not evaluated' than a misleading badge.",
  "BADGE FOR WHAT WAS CHECKED - review a reduced but representative version (subset of data, shorter run) and say so on the badge.",
  "AUTHORS PROVIDE ACCESS - authors give reviewers remote access to their own hardware or pay for cloud time; then normal review is possible.",
  "DIFFERENT KIND OF CHECK - inspect code, logs and raw outputs instead of re-running; weaker, but better than nothing.",
  "FAIRNESS - if large-scale work can never get badges, badges reward small, cheap studies; if it gets badges anyway, badges mean less."],
 ladder=[
  "Several terabytes of data, or a week on eight GPUs: what could a reviewer realistically check?",
  "Would you trust a badge awarded after only a scaled-down run?",
  "Should the badge say what was and wasn't checked?"]),
"C9 External constraints: Unshareable industry data": dict(
 about="Industry partners often forbid sharing data. Should top venues still publish results that nobody outside can ever verify?",
 answers=[
  "ACCEPT - industry data shows how software is really built; excluding it makes SE research less relevant to practice.",
  "ACCEPT WITH CONDITIONS - the paper explains why data can't be shared, shares the analysis code, and offers proxy or synthetic data with the same structure.",
  "REVIEWER-ONLY ACCESS - reviewers see the data under an NDA, the public doesn't; at least one independent check happens.",
  "REFUSE / LOWER STATUS - results nobody can check are weaker evidence; publish them in industry tracks rather than as full research results.",
  "CONSEQUENCE - strict rules would push companies to publish internally or not at all, so less industry knowledge reaches research."],
 ladder=[
  "A study of a company's bug reports, data under NDA: what would make you trust it anyway?",
  "If your thesis were done with a company and its data couldn't be shared, would you still want to publish at a top venue?",
  "Should such papers be marked differently?"]),
"C11 Technical obstacles: Fixed time limits": dict(
 about="Many venues expect artifacts to be set up within about 30 minutes and reviewed within roughly a day. Is one fixed limit fair for very different artifacts?",
 answers=[
  "FLAT LIMIT IS FAIR - simple, predictable, same rules for everyone; future users won't spend more time either.",
  "FLAT LIMIT IS UNFAIR - a small library and a three-day experiment are not comparable; heavy research is penalised for its nature, not its quality.",
  "BY TYPE - different limits for tools, datasets, large experiments, declared up front by the authors.",
  "SEPARATE SETUP AND RUNTIME - the setup must be quick (that is about documentation and packaging), but long runtimes are fine if the steps are automated.",
  "REDUCED RUN - long experiments provide a short representative version for review; the full run is optional."],
 ladder=[
  "A small library and a three-day fuzzing experiment under the same 30-minute setup rule: fair?",
  "Could your own thesis project be set up in 30 minutes?",
  "Who should decide the limit for an artifact: authors, reviewers or the conference?"]),
"C12 Limited communication: Purpose of artifact review": dict(
 about="Is artifact review a one-time check that the paper's results come out (like a second look at the evidence), or a guarantee that the artifact can be used by others as a foundation? The other paper found reviewers care about the first, users about the second.",
 answers=[
  "REPRODUCED ONCE - that is what peer review needs: the evidence behind the claims exists and works. Reuse is a separate, much bigger task.",
  "FOUNDATION - readers see the badge and assume they can build on the tool; if it only worked once with the authors' help, the badge misleads them.",
  "TWO BADGES - one for 'results reproduced', one for 'reusable'; ACM already separates functional and reusable, but readers don't know the difference.",
  "AUTHOR HELP - if reviewers needed three emails, the fixes should go into the artifact before the badge is given; otherwise later users hit the same wall.",
  "LIMITS OF SUPPORT - authors can't support a tool forever; a badge can only describe the state at review time."],
 ladder=[
  "The artifact only runs after three emails with the authors: badge or not?",
  "If you started a thesis on a badged tool, what would you expect the badge to guarantee?",
  "Should evaluation be a one-shot test or a dialogue with the authors?",
  "Would you still answer emails about your thesis code in three years?"]),
"RQ1: Rewards": dict(
 about="Respondents value artifacts and want sharing rewarded. The four reasons they share are supporting evidence, community norm, reuse and understanding. What reward would make the effort worth it?",
 answers=[
  "CAREER CREDIT - artifacts counted in hiring and promotion, like papers; strongest lever, but needs a way to judge artifact quality.",
  "CITATIONS - artifacts get their own DOI and are cited separately; visible credit in the currency researchers already use.",
  "VISIBILITY - badges on the paper, best-artifact awards; cheap, but unclear if anyone hiring cares.",
  "FUNDING - grants require and pay for artifact work; turns it into part of the job instead of extra work.",
  "NORM INSTEAD OF REWARD - if sharing is simply expected (like writing a related-work section), no reward is needed; not sharing becomes the exception that needs explaining."],
 ladder=[
  "What would make you spend an extra week on your thesis artifact?",
  "Which of the four reasons (evidence, norm, reuse, understanding) would a reward strengthen most?",
  "Hand-over: the paper itself makes recommendations on this; Minh Thi presents them next."]),
}

src, dst = sys.argv[1], sys.argv[2]
p = Presentation(src)
done = set()
for s in p.slides:
    if s._element.get("show") == "0": continue
    subs = [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text in N]
    if not subs: continue
    key = subs[0].text_frame.text; d = N[key]; done.add(key)
    if d.get("question"):
        order = [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip() and sh.text_frame.text != "‹#›"]
        q = order[order.index(subs[0]) + 2]
        runs = q.text_frame.paragraphs[0].runs; runs[0].text = d["question"]
        for r in runs[1:]: r.text = ""
    old = s.notes_slide.notes_text_frame.text
    bg = ""
    for marker in ("BACKGROUND (sources named inline; not on slide)\n", "MY NOTES (background, not on slide)\n"):
        if marker in old: bg = old.split(marker, 1)[1].split("\n\nCITED SOURCES")[0]
    cited = ("\n\nCITED SOURCES" + old.split("\n\nCITED SOURCES", 1)[1]) if "\n\nCITED SOURCES" in old else ""
    s.notes_slide.notes_text_frame.text = (
        "WHAT THIS IS ABOUT\n" + d["about"] +
        "\n\nPOSSIBLE ANSWERS\n" + "\n".join("- " + a for a in d["answers"]) +
        "\n\nIF THE ROOM IS QUIET (ask in this order)\n" + "\n".join(f"{i}. {x}" for i, x in enumerate(d["ladder"], 1)) +
        ("\n\nBACKGROUND\n" + bg.strip() if bg.strip() else "") + cited)
print("missing:", set(N) - done)
p.save(dst)
