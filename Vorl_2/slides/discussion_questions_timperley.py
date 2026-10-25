"""Paper 2 (Timperley) discussion questions: single source for the notes file and the slides.

Usage: python3 discussion_questions_timperley.py <in.pptx> <out.pptx> <out.md>
Inserts the question slides, sorted by challenge, after the slide titled
"Paper 2 · Discussion (Kevin)". The existing idea-dump slides follow and are hidden.
"""
import sys, copy
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Each item: (title, question, example, perspective, paper context, example answers, my notes)
Q = [
 ("C1: Fear of exposing mistakes",
  "Creators fear that shared code exposes mistakes and harms their reputation: what would make you more or less willing to share your own code?",
  "a mistake found later through your artifact only leads to a correction note, not a retraction",
  "Would you share more readily if releasing research code as is, messy and undocumented, were the accepted norm?",
  "Creators fear that sharing exposes mistakes in their analysis and that poor code quality harms their reputation.",
  ["More willing: if consequences for honest errors are proportionate (correction, erratum) and messy code is normal.",
   "Less willing: as long as any visible mistake can cost a paper or a reputation, keeping code private is the safer choice.",
   "Releasing as is: something checkable beats nothing vs. it wastes users' time and signals sloppiness."],
  ["Chang 2006: inherited script flipped two columns, 5 retractions, treated as an honest error.",
   "Reinhart & Rogoff 2013: a spreadsheet range error found after the data was shared.",
   "Hermann et al.: some reviewers prefer availability over quality; an AEC found hard-coded outputs (misconduct, not error)."]),
 ("C3: Decay and maintenance",
  "Is software decay unavoidable as technology moves on, and who should carry the cost of limiting it?",
  "a 2015 thesis tool needs Python 2 and a library that no longer exists: fix it, freeze it in an image, or let it go?",
  "If you inherited a ten-year-old tool for your thesis, what would you want its authors to have left you?",
  "Artifacts need ongoing maintenance (bugs, changing use cases, bit rot), usually by students who later leave; only well-funded groups manage it.",
  ["Unavoidable: you can slow decay (archived images, pinned versions, few dependencies), not stop it.",
   "Cost: the group or university, since it is research infrastructure, vs. nobody (archive and mark unmaintained).",
   "Expected lifetime: only at publication and review, or a stated period?"],
  ["DFG: code and data behind a publication archived for at least 10 years; archived is not runnable.",
   "Research software engineers keep code alive inside institutions (Princeton, Aalto).",
   "Maintenance funding runs in short cycles (CZI, DFG calls).",
   "Week 1: costly constant maintenance; Docker may not exist in 40 years; source code most stable."]),
 ("C4: One-click reproduction scripts",
  "Is a one-click reproduction script good or bad for scientific scrutiny?",
  "the script regenerates every table in the paper, but nobody reads the code that produces them: what has actually been checked?",
  "As a reviewer with one day per artifact, would you rather get a script or a documented step-by-step procedure?",
  "Reviewers suggest scripts against tacit knowledge, but warn they act as a black box that can re-run the authors' mistakes.",
  ["Good: anyone can re-run it; without scripts many artifacts would not run at all.",
   "Bad: checks that numbers come out, not that the method is sound; false confidence.",
   "Understanding why results come out needs documentation of the steps, not just the button."],
  ["Python file-order case (2019): scripts correct on one OS, wrong on another; ~150 studies possibly affected.",
   "Push-button replication is an established first step before independent re-implementation."]),
 ("C9: Unshareable industry data",
  "Should a paper be criticised for not sharing data that its industry partner won't release?",
  "an empirical study of a company's ten years of bug reports, with the data under NDA",
  "If you built on a study whose data is under NDA, would you trust it less than one whose artifact simply disappeared?",
  "IP, contracts, privacy and liability fears prevent sharing; authors feel reviewers use missing artifacts as a blanket argument.",
  ["Yes: readers cannot check the claims, whatever the reason.",
   "No: it punishes valuable industry collaboration for something authors cannot control.",
   "Middle: state the reason, offer proxy data or reviewer-only access."],
  ["ICSE: data sharing not required for acceptance, only a statement of why not.",
   "ACM 'Complete' allows proxies for proprietary data."]),
 ("C9: Licensed software",
  "Should research tools that depend on paid commercial software be accepted as artifacts at all?",
  "your artifact needs MATLAB, and the reviewer has no licence: whose problem is that?",
  "As a reviewer, would you pay for a licence yourself to evaluate someone else's artifact?",
  "Users and reviewers report artifacts needing paid licences or proprietary components (Windows, a commercial IDE); reviewers see no clear pathway.",
  ["Accept: much real-world SE runs on commercial platforms; excluding them biases research to open tools.",
   "Restrict: if others cannot run or check it, the artifact misses its purpose.",
   "Depends whether the commercial tool is the subject of the research or a replaceable helper."],
  ["CAV, FORMATS, QEST: case by case via the chairs; FORMATS 2022 accepted MATLAB Online.",
   "ACM policy is silent on reviewer licences; each AEC decides. Reviewers are not expected to pay."]),
 ("C10: Students as reviewers",
  "Is leaving artifact evaluation to students a good training opportunity, or does it undermine how rigorous and seriously taken the badges are?",
  "a first-year PhD student has to judge the artifact of an experienced professor's group",
  "Would you trust a badge more if you knew a senior researcher rather than a student had awarded it?",
  "Artifact review is time-consuming and less rewarded than paper review, so it is often left to students; this may lead to inconsistent, low-quality reviews.",
  ["Meaningful: checking that an artifact runs and matches the paper needs no seniority; students are typical future users.",
   "Weak: students may not judge methodology or dare to reject."],
  ["Students chosen deliberately from ECOOP/OOPSLA 2013 (current tools, training).",
   "Time budget about 8-20 h per artifact; Hermann et al.: most AEC members serve once."]),
 ("C11: Fixed time limits",
  "Is it fair to have a fixed time limit (e.g. a 30-minute setup) after which an artifact fails?",
  "a fuzzing experiment that by nature runs for three days",
  "How long would you give an artifact before giving up, if you were reviewing it unpaid?",
  "Reviewers report long execution times and artifacts that need more than the roughly one day they can give each.",
  ["Fair: forces authors to make artifacts usable; future users won't invest more either.",
   "Unfair: penalises inherently heavy research; a reduced representative run could replace the full one."],
  ["ICSE 2026: setup over 30 min makes acceptance unlikely; whole review ~8-20 h.",
   "MobiSys: reviewers and authors agree a reduced but representative scope."]),
 ("C12: One-shot or iterative review",
  "Should artifact evaluation be a one-shot review or an iterative dialogue with the authors?",
  "the artifact fails because of a typo in the install instructions: reject, or ask the authors?",
  "Later users won't have the authors on call: should the review simulate that?",
  "Reviewers find single-round reviews frustrating and value authors willing to help, but unresponsive authors leave them waiting.",
  ["Iterative: glitches are inevitable; the fixes help every later user.",
   "One-shot: the badge should certify that it works without the authors.",
   "Hybrid: a short check-in phase for setup, then a final test without help."],
  ["Most venues have a 'kick the tires' phase (SLE: 5-day response); ICSE 2026: answers within 72 h."]),
]
SPARES = [
 ("C1: Unreleased tools",
  "Should a paper whose results rest on a tool the authors keep private be treated as a full result or as preliminary until the tool is released?",
  "a new testing technique evaluated with a tool held back for the PhD student's next paper",
  "Would you cite and build on such a paper in your own thesis?",
  "Creators hold back artifacts with untapped publication value or fear of being scooped; a limited audience is another reason.",
  ["Full result: peer review judged the paper; the tool is the authors' property.",
   "Preliminary: claims that nobody can check are weaker evidence."],
  ["Embargoes exist in data-heavy fields (telescope data 12-18 months); no measured scooping rate."]),
 ("C4: Tacit knowledge",
  "What knowledge about a research prototype typically stays in the developer's head, and could documentation ever capture it?",
  "the order the scripts must run in, hard-coded paths, parameter values that were tried and dropped",
  "Could someone reproduce your bachelor thesis results from your repository alone?",
  "Tacit knowledge, buried in developers' heads, makes artifacts hard to understand, extend and reuse.",
  ["Mostly capturable: checklists, a run-everything script, a short walkthrough video.",
   "Not fully: some know-how only transfers by talking to the author."],
  []),
 ("C4: Reviewer effort",
  "How much effort should an artifact reviewer invest before giving up on an artifact?",
  "after two hours the artifact fails on a missing dependency: fix it yourself, contact the authors, or reject?",
  "As an author, how much of a reviewer's goodwill would you be comfortable relying on?",
  "Reviewers report missing instructions and needing the paper to fill gaps; deep dives can take days.",
  ["Little: the artifact should work for a stranger.",
   "More: reviewers are the only ones who will ever try; one fix helps everyone after."],
  ["Overlaps with the C11 time-limit question; use as its follow-up if needed."]),
 ("C9: Formal exceptions",
  "Should artifact evaluation have formal exceptions for unshareable artifacts, e.g. evaluating them privately without publishing them?",
  "reviewers get temporary access under NDA, but readers never see the artifact",
  "Would a badge saying evaluated privately convince you as a reader?",
  "Some artifacts cannot be shared for legal or privacy reasons; reviewers lack guidance for such cases.",
  ["Yes: at least someone independent has checked it.",
   "No: a check that nobody else can repeat adds little."],
  ["ACM already separates Evaluated (reviewer access suffices) from Available (public archive)."]),
 ("C9: Open by default",
  "Should research software be open source by default, with closed artifacts needing a justification?",
  "a company co-authored the tool and wants to sell it later",
  "If your thesis tool had commercial potential, would you open-source it?",
  "IP restrictions, licences and privacy concerns keep some artifacts closed.",
  ["Yes: publicly funded research should be open.",
   "No: it drives industry collaboration away from research."],
  ["Horizon Europe: open research data mandatory, 'as open as possible, as closed as necessary', exceptions justified in a data management plan."]),
 ("C7: Very large artifacts",
  "How should researchers share artifacts that are too big for archives like Zenodo and for a reviewer's laptop?",
  "several terabytes of mined repository data",
  "If your thesis data were that large, what would you publish?",
  "Creators struggle to find hosting for large datasets; GitHub, Dropbox and Google Drive are not long-term archives.",
  ["A representative subset plus scripts to regenerate the rest.",
   "Institutional repositories; share the generator, not the data."],
  ["Zenodo: 50 GB per record, up to 200 GB on request.",
   "Overlaps with the paper's recommendation on proof-of-concept artifacts (teammate's section)."]),
 ("C11: Hardware reviewers don't have",
  "Should artifacts that need more hardware than reviewers have still be eligible for a badge?",
  "an experiment that needs eight GPUs or a 500 GB VM image",
  "If your thesis needed a GPU cluster, how would you want it evaluated?",
  "Some experiments (cloud systems, fuzzers, program repair) are practically infeasible to re-run for reviewers.",
  ["Yes, with a badge that states what was checked.",
   "No: an unrepeatable check certifies little."],
  ["Avoid 'who provides compute' (paper's recommendation, teammate's section).",
   "SOSP 2019 Azure credits proved hard to use; IISWC has authors provide remote access."]),
 ("C2: Portability",
  "Does an artifact count as portable if it only runs inside the authors' container image?",
  "the Docker image works, but nobody could rebuild the tool from source",
  "Would you build your own research on a tool you can only run inside a black-box image?",
  "Artifacts often fail on other machines (missing information, outdated dependencies); VMs and containers are the usual fix.",
  ["Yes: it runs anywhere Docker runs.",
   "No: the image hides how the environment was set up and decays too."],
  ["Rebuilding from an unpinned Dockerfile can silently change the result; archive the built image."]),
 ("C7: Dead links and old badges",
  "Should a badge expire if the artifact link dies a few years after publication?",
  "a 2016 badge on a paper whose artifact link now returns 404",
  "Would a label like awarded 2016, not re-checked change how you treat the paper?",
  "Many artifacts are no longer accessible, older ones more often.",
  ["Yes: a badge should describe the current state.",
   "No: it certifies what was checked at review time."],
  ["Klein et al. 2014: 13-22 % of web references in articles suffer link rot."]),
 ("C12: Support after publication",
  "Can authors be expected to support their artifacts after publication, and for how long?",
  "the PhD student who built the tool has graduated and changed jobs",
  "Would you still answer emails about your thesis code three years from now?",
  "Users value authors who help fix problems, but creators move on and support stops.",
  ["Yes, for a stated period.", "No: archive it and say it is unsupported."],
  ["Overlaps with C3; use as its follow-up if needed."]),
 ("RQ1: Rewards",
  "Which reward would actually make researchers invest more in their artifacts?",
  "a citable DOI, a best-artifact award, or counting artifacts in hiring",
  "What would make you spend an extra week on your thesis artifact?",
  "Respondents want sharing encouraged and rewarded.",
  ["Career credit (hiring, citations).", "Direct benefit (users, collaborations)."],
  ["JOSS: citable software papers. Possible overlap with the teammate's recommendations."]),
]

ORDER = ["C1: Fear of exposing mistakes", "C1: Unreleased tools", "C2: Portability", "C3: Decay and maintenance",
         "C4: One-click reproduction scripts", "C4: Tacit knowledge", "C4: Reviewer effort",
         "C7: Very large artifacts", "C7: Dead links and old badges",
         "C9: Unshareable industry data", "C9: Formal exceptions", "C9: Open by default", "C9: Licensed software",
         "C10: Students as reviewers", "C11: Fixed time limits", "C11: Hardware reviewers don't have",
         "C12: One-shot or iterative review", "C12: Support after publication", "RQ1: Rewards"]

def ordered():
    items = {x[0]: x for x in Q + SPARES}
    assert set(items) == set(ORDER), set(items) ^ set(ORDER)
    return [items[t] for t in ORDER]

def markdown():
    out = ["# Timperley et al. (2021): Discussion Questions (Challenges, §4.2)", "",
           "Generated from `Vorl_2/slides/discussion_questions_timperley.py` (single source for slides and notes).", "",
           "Core questions come from my selected (green) questions, lightly reworded and anchored in the paper. "
           "Follow-ups go on the slide as sub-points. Example answers and my notes go in the speaker notes only; "
           "the notes draw on `timperley-research.md` and are not part of the questions.", ""]
    def block(items, hdr):
        out.append(f"## {hdr}"); out.append("")
        for i, (t, q, ex, me, ctx, a, n) in enumerate(items, 1):
            out.extend([f"### {i}. {t}", "", f"**Question:** {q}", "",
                        "**Follow-ups:**", f"- Example: {ex}", f"- You: {me}", "",
                        f"**Paper context:** {ctx}", ""])
            out.extend(["**Example answers:**"] + [f"- {x}" for x in a] + [""])
            out.extend(["**My notes:**"] + [f"- {x}" for x in n] + [""])
    block(ordered(), "Questions, sorted by challenge (RQ1 last)")
    return "\n".join(out)

def build(src, dst):
    G = RGBColor(0x00, 0x88, 0x3A); K = RGBColor(0x1A, 0x1A, 0x1A); M = RGBColor(0x5F, 0x63, 0x68)
    p = Presentation(src)
    slides = list(p.slides)
    def ttl(s): return next((sh.text_frame.text for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()), "")
    anchor = next(s for s in slides if ttl(s).startswith("Paper 2 · Discussion (Kevin)"))
    dumps = [s for s in slides[slides.index(anchor) + 1:slides.index(anchor) + 4] if ttl(s) == "Paper 2 · Discussion"]
    ref = next(s for s in slides if ttl(s) == "General Summary" and slides.index(s) > 10)
    title_el = next(sh for sh in ref.shapes if sh.has_text_frame and sh.text_frame.text == "General Summary")._element
    num_el = next(sh for sh in ref.shapes if sh.is_placeholder)._element
    def add(item, hidden):
        t, q, ex, me, ctx, a, n = item
        f = ["Example: " + ex, "You: " + me]
        s = p.slides.add_slide(ref.slide_layout)
        for ph in list(s.placeholders): ph._element.getparent().remove(ph._element)
        s.shapes._spTree.append(copy.deepcopy(title_el)); s.shapes[-1].text_frame.paragraphs[0].runs[0].text = "Paper 2 · Discussion"
        s.shapes._spTree.append(copy.deepcopy(num_el))
        def para(tf, first, text, size, bold=False, color=K, space=8, prefix=None):
            pa = tf.paragraphs[0] if first else tf.add_paragraph(); pa.space_after = Pt(space)
            if prefix:
                r = pa.add_run(); r.text = prefix; r.font.size = Pt(size); r.font.bold = True; r.font.color.rgb = G; r.font.name = "Arial"
            r = pa.add_run(); r.text = text; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Arial"
        box = s.shapes.add_textbox(Inches(.7), Inches(1.45), Inches(11.93), Inches(1.0)); tf = box.text_frame; tf.word_wrap = True
        para(tf, True, t, 28, True, G, 4)
        box = s.shapes.add_textbox(Inches(.7), Inches(2.25), Inches(11.93), Inches(2.4)); tf = box.text_frame; tf.word_wrap = True
        para(tf, True, q, 28, True, K, 4)
        if f:
            h = 0.55 + 0.65 * len(f)
            pn = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(.7), Inches(7.0 - h), Inches(11.93), Inches(h - .2))
            pn.adjustments[0] = 0.08; pn.fill.solid(); pn.fill.fore_color.rgb = RGBColor(0xF1, 0xF3, 0xF2); pn.line.fill.background(); pn.shadow.inherit = False
            box = s.shapes.add_textbox(Inches(.9), Inches(7.0 - h + .1), Inches(11.5), Inches(h - .4)); tf = box.text_frame; tf.word_wrap = True
            for i, x in enumerate(f):
                lab, rest = x.split(": ", 1)
                para(tf, i == 0, rest, 20, False, K, 8, "↳ " + lab + ": ")
        s.notes_slide.notes_text_frame.text = ("PAPER CONTEXT\n" + ctx + "\n\nEXAMPLE ANSWERS\n" + "\n".join("- " + x for x in a) +
                                               "\n\nMY NOTES (background, not on slide)\n" + ("\n".join("- " + x for x in n) or "-"))
        if hidden: s._element.set("show", "0")
        return s
    new = [add(x, False) for x in ordered()]
    for d in dumps: d._element.set("show", "0")
    lst = p.slides._sldIdLst
    def eid(sl): return next(e for e in lst if p.part.rels[e.rId]._target is sl.part)
    prev = eid(anchor)
    for s in new:
        e = eid(s); lst.remove(e); prev.addnext(e); prev = e
    p.save(dst)
    print("slides", len(p.slides), "dumps hidden", len(dumps))

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
    open(sys.argv[3], "w").write(markdown() + "\n")
