# Timperley et al. (2021): Final Discussion Questions (Challenges, §4.2)

Eight core questions of about 3 minutes each, plus spares. All are based on the challenges
(C1–C12) in the paper's Results section. Secondary analysis and recommendations are left to
my teammate.

Each question has:
- **Paper context:** what the paper says, so the question makes sense on a first read
- **Core question:** for the slide
- **Starters:** concrete examples or options to give if nobody bites
- **Follow-ups:** to deepen or redirect
- **Example answers:** both sides, so I can prompt if the room is quiet
- **My notes:** background from `timperley-research.md`, for me only, not for the slides

Teammate feedback taken into account:
- liked C3 decay, C9 licensed software, C10 students and C12 author support
- C1 and C9 risk being too open or having one obvious answer, so they get more examples and
  follow-ups
- C3 should include the costs
- C2 performance moved to the spares (research time)

---

## 1. C1: fear of mistakes being discovered

**Paper context:** creators list risks that outweigh the rewards of sharing, among them that
poor code quality harms their reputation and the "fear of mistakes in the analysis being
discovered".

**Core question:** Is the fear that mistakes will be discovered a legitimate reason to hold
back an artifact, given that finding mistakes is what scientific review is for?

**Starters (positions to choose from):**
- (a) Not legitimate: if the analysis is wrong, the community needs to know, full stop.
- (b) Legitimate, because the consequences are out of proportion: an honest bug can end in
  retraction and lasting reputation damage.
- (c) Legitimate only as a sign of poor practice: the fix is better code and tests, not
  hiding it.

**Follow-ups:**
- How much personal accountability should a researcher carry for errors found in their
  shared code years later?
- Should an honest bug be treated differently from a careless or misleading result? Does
  today's system make that distinction?
- Does this fear hit PhD students hardest, since their prototype code is the least polished?

**Example answers:**
- *Pro sharing:* errors found early are cheaper than errors found after others have built on
  them.
- *Understanding the fear:* incentives punish visible mistakes, while unshared mistakes cost
  the author nothing.

**My notes:**
- Chang 2006: an inherited script flipped two columns, leading to 5 retractions. It was
  treated as an honest error.
- Hermann et al. (this week): artifact evaluation caught hard-coded outputs, and the paper
  was withdrawn.
- Reinhart & Rogoff: a student's request for the spreadsheet revealed a range error.

## 2. C1: holding back artifacts with "untapped publication value"

**Paper context:**
- some creators won't share artifacts that still have untapped publication value, or fear
  being scooped ("sometimes, one needs to protect a Ph.D. student's abilities to produce
  sufficient results")
- others assume a limited audience
- in contrast, one respondent says whole research areas died because early work had no
  artifacts

**Core question:** Where should the line be between protecting your own (or your student's)
next publication and letting others build on your work?

**Starters (options):**
- share everything at publication
- share after the follow-up paper is out
- share only on request
- share the paper's analysis but keep the tool private

**Follow-ups:**
- Does the "dead research areas" quote change your answer?
- Is a researcher who withholds an artifact slowing down the field, or just being
  rational?
- "Nobody else works on this topic, so nobody will use it": is that a valid reason not to
  share?

**Example answers:**
- *Protect:* a PhD has a fixed time; being overtaken with your own tool is a real career
  risk.
- *Share:* the paper already establishes priority, and holding back hides the evidence for
  its claims.

**My notes:** data-heavy fields use embargoes (telescope data 12–18 months; NERC up to 2
years). There is no measured rate of how often scooping happens. Week 1: Collberg listed
"competitors' advantage" too.

## 3. C3: software decay, and the cost of fighting it

**Paper context:**
- sharing needs an upfront investment and an "ongoing investment to continually maintain
  the artifact" as bugs appear, use cases evolve and "inevitable bit rot" sets in
- students usually maintain artifacts and then graduate
- users struggle with unmaintained artifacts that need old library versions
- respondents note that only well-funded groups manage maintenance

**Core question:** Is software decay unavoidable as technology moves on? What practical ways
are there to limit it, and who should pay for the extra cost?

**Starters (ways to limit decay):**
- archive a built container or VM image
- pin exact dependency versions
- keep the code simple, with few dependencies
- add an automated test that rebuilds it regularly
- accept decay and mark the artifact "unmaintained"

**Follow-ups:**
- How long should an artifact be expected to keep working: only at publication and review
  time, or for a stated period?
- When the student graduates, who is responsible: the student, the advisor, the group, or
  nobody?
- If only well-funded groups can afford maintenance, is that a problem for fairness in
  research?

**Example answers:**
- *Unavoidable:* dependencies, compilers and operating systems change; you can slow decay,
  not stop it.
- *Mostly avoidable:* a frozen image keeps working as long as it can still be run, so decay
  is mainly a packaging choice.

**My notes:**
- The DFG expects code and data behind a publication to be archived for at least 10 years.
  Archived ≠ runnable.
- Research software engineers are permanent staff who keep code alive (Princeton, Aalto).
- Maintenance funding (CZI's open-source fund, DFG calls) runs in short cycles.
- Week 1: maintenance is costly; Docker may not exist in 40 years; source code may be the
  most stable format.

## 4. C4: one-click reproduction scripts

**Paper context:**
- tacit knowledge, "buried in developers' heads", makes artifacts hard to use
- some reviewers suggest automated scripts as a remedy
- others warn that a script can be a black box that produces the expected results "with no
  insight into whether the process… is sound", and that AECs asking for scripts are "likely
  to replicate the same mistake (if any) the original authors made"

**Core question:** Does a one-click reproduction script help or hurt the scrutiny of a
paper's results?

**Starters:**
- *Helps:* anyone can re-run it; no setup knowledge needed.
- *Hurts:* the reviewer checks that the numbers come out, not whether the method behind them
  is right.

**Follow-ups:**
- If scripts don't help a reviewer understand *why* the results come out, what would? Code
  comments, a walkthrough, small examples, a description of the steps?
- How much effort should a reviewer put in beyond pressing the button?
- One reviewer found it "easy to reproduce, but difficult to understand where to add more
  case studies". Is reuse a separate goal that scripts don't serve?

**Example answers:**
- *Help:* a script is the minimum, and without it many artifacts wouldn't run at all.
- *Hurt:* it creates false confidence; a badge then certifies repeatability, not
  correctness.

**My notes:** the Python file-order case (2019): a script that worked was wrong on another
OS. "Push-button replication" is an established first step, followed by an independent
re-implementation.

## 5. C9: unshareable industry data

**Paper context:**
- IP, contracts and liability fears prevent sharing industry data
- one creator was "once criticised for not sharing data for an industry track paper…
  Artifact should not be used as ritualistic blanket argument to judge papers"

**Core question:** Should paper reviewers be allowed to criticise a paper for not sharing
data that its industry partner won't release?

**Starters (options):**
- yes, unshared data weakens the evidence regardless of the reason
- no, as long as the paper states why
- formal exception rules
- partial substitutes: proxy or synthetic data, access for reviewers only

**Follow-ups:**
- Should there be formal exceptions, and what should a paper have to provide instead?
- How would you stop "legal reasons" becoming a convenient excuse?
- Would strict sharing rules push industry collaborations out of top venues?

**Example answers:**
- *Allow criticism:* readers can't check the claims, so the evidence is weaker either way.
- *Don't:* it punishes valuable industry collaboration for something the authors can't
  control.

**My notes:**
- ICSE doesn't require data sharing, only a statement of why not.
- ACM's "Complete" criterion allows proxies for proprietary data.
- The Evaluated badges can be earned with private, reviewer-only access; Available needs
  public access.

## 6. C9: artifacts that depend on licensed software

**Paper context:**
- users report artifacts that "require a paid commercial license [for the] auxiliary tools"
  and had to decompile tools to extend them
- reviewers may not have the licences, and there is "no obvious pathway for what to do if
  the software artifact requires a proprietary component (Windows, a commercial IDE)"

**Core question:** Should research tools that depend on paid commercial software be accepted
as artifacts at all?

**Starters (concrete cases to compare):**
- (a) A tool written in MATLAB.
- (b) A plugin whose whole purpose is to study a commercial IDE.
- (c) A Windows-only build.
- (d) An analysis that calls a paid cloud API.

Which of these should be accepted, and does the answer differ by case?

**Follow-ups:**
- Your artifact needs MATLAB and the reviewer has no licence. Whose problem is that?
- Is automatically rejecting such an artifact fair, or should reviewers or conferences
  arrange access?
- Does it matter whether the commercial tool is the *subject* of the research or just a
  *helper* that could be replaced?

**Example answers:**
- *Accept:* much real-world SE happens on commercial platforms; excluding them biases
  research toward open tools.
- *Restrict:* if others can't run or check it, the artifact doesn't serve its purpose.

**My notes:** CAV, FORMATS and QEST handle it case by case: authors contact the chairs, and
FORMATS 2022 accepted MATLAB Online. Reviewers aren't expected to buy licences.

## 7. C10: students as artifact reviewers

**Paper context:**
- reviewing is time-consuming and "not recognized and rewarded to the same extent as paper
  reviewing"
- "We usually just make students do AEC. This is good in some ways because it gets students
  involved… But it also reinforces the idea that artifacts are not a primary thing"
- lack of incentives "may lead to inconsistent and low-quality reviews"

**Core question:** If artifact evaluation is left largely to comparatively inexperienced
students, how rigorous and meaningful are the resulting badges, and how seriously are they
taken?

**Starters:**
- *For students:* they are close to the code, have time, and are the typical future users.
- *Against:* they lack experience to judge methodology or spot subtle problems; they may not
  dare to reject.

**Follow-ups:**
- What would a badge need to certify for you to trust it when picking a tool for your own
  work?
- Is it a good training opportunity for the students themselves?
- Would mixed committees (students plus experienced reviewers) fix it, or just move the
  workload around?

**Example answers:**
- *Meaningful:* checking that an artifact runs and matches the paper doesn't need seniority.
- *Weak:* without experience and time, badges certify "it ran once", not that the results
  hold.

**My notes:**
- Students were chosen deliberately from ECOOP and OOPSLA 2013: familiarity with current
  tools, and training the next generation.
- Time budget: about 8–20 hours per artifact.
- Hermann et al.: most AEC members serve only once.

## 8. C12: artifacts that only work with the authors' help

**Paper context:**
- reviewers complain of single-round reviews where "a minor glitch in the installation
  instructions should not be grounds for rejection"
- it matters that owners are "willing to help the users resolve outstanding issues"
- unresponsive authors can leave reviewers waiting for days

**Core question:** If an artifact only works with active help from its authors, does it
deserve a badge, or should there be a separate badge category for "doesn't work on its own,
but is actively supported"?

**Starters:**
- (a) Same badge, because the review fixed the problems, so later users benefit too.
- (b) No badge, because a badge should mean "works for a stranger".
- (c) A separate "supported" badge.

**Follow-ups:**
- Would a separate badge create an incentive to rely on support rather than fix the
  documentation?
- How long can authors realistically promise support: until review, a year, as long as
  they're in the group?
- Should evaluation be iterative (dialogue with the authors) or a one-shot test?

**Example answers:**
- *Separate badge:* it's honest and rewards responsive authors.
- *No:* support disappears when the student graduates, so the badge would outlive its
  meaning.

**My notes:** most venues already have a "kick the tires" phase and response windows (e.g.
SLE: 5 days); ICSE 2026 requires answers within 72 h.

---

## Spares

- **S1 (C2, performance; research incomplete):** Reviewers say performance claims can't be
  assessed accurately in a VM, and containers don't stop decay. How should artifact
  evaluation handle papers whose main claim is about performance?
  - Follow-up: "your paper claims a 3× speedup and the reviewer runs it in a VM on a laptop.
    What counts as reproduced?"
  - My notes: SPLASH says check trends, not exact numbers; containers run at almost native
    speed, VMs are slower.
- **S2 (C11):** Reviewers report VM images that don't fit on their disk and experiments
  (fuzzers, program repair) needing hardware they don't have. Should such artifacts still get
  a badge, and what would it mean? Avoid "who provides compute" (teammate's
  recommendations).
- **S3 (C2):** Running untrusted artifacts is a security risk, and some need root access or
  invasive libraries. Should reviewers be allowed to refuse them?
- **S4 (C7):** About 14 % of artifact links were already dead, more for older papers. Should
  conferences re-check artifacts years after publication, and what should happen to dead
  ones? Follow-up: who would organise and pay for it?
- **S5 (RQ1):** Respondents want sharing "encouraged and rewarded". Which reward would
  actually change researchers' behaviour? Possible overlap with the teammate's
  recommendations.
