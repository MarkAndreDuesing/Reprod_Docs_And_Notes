"""Appends a 'CITED SOURCES' block to the speaker notes of every visible slide that cites [n]
(in slide text or notes), explaining what each source says and why it matters here."""
import re, sys
from pptx import Presentation

BG = {
 1: "ACM Artifact Review and Badging v1.1 (2020): ACM defines five independent badges: Evaluated-Functional (documented, consistent, complete, exercisable), Evaluated-Reusable (also well structured for reuse), Available (on a public archival repository with DOI; personal pages or GitHub alone are not enough), Results Reproduced (other team, authors' artifacts) and Results Replicated (other team, own artifacts). The 'Complete' criterion lets authors leave out proprietary parts if they document how to obtain them and include proxy data. ACM defines only the badges; each conference runs its own evaluation process.",
 2: "Introductory lecture (Winter & Beyer): slide 9 groups the badges into 'Does the artifact work? / Is it permanently available? / Can the results be confirmed?' and notes the 2017 ACM task force and the 2020 revision for NISO RP-31-2021.",
 3: "ICSE 2026 artifact evaluation call: awards Available, Functional and Reusable; if installation and configuration take more than 30 minutes, acceptance is unlikely (the whole review takes several hours); Docker/VM images strongly encouraged; artifacts must be on an archival repository (Zenodo, Figshare, Software Heritage; GitHub only via a Zenodo DOI); proprietary data may be replaced by proxies; authors must answer reviewer questions within 72 hours.",
 4: "Zenodo (run by CERN): free, gives a DOI per upload, 50 GB per record (one-time increase up to 200 GB on request), can archive each GitHub release automatically. Records are kept 'for the lifetime of the repository', i.e. of CERN, whose programme is planned for at least 20 more years. Only bit-level preservation: files stay intact, but nothing guarantees they still run.",
 5: "Heumüller et al. (2020, last week): of ICSE papers 2007-2017, 76.6 % built software, but only 47.8 % linked it and many links were dead by 2019. Counted runnable software only, so its numbers are lower than Timperley's 'any linked material'.",
 6: "Hermann, Winter & Siegmund (2020, Paper 1 today): survey of artifact evaluation committee members. Found no shared quality threshold, badges meaning different things per conference, most reviewers serving only once, and some reviewers preferring availability over quality ('enforcing quality criteria only means that some authors will not publish their code').",
 7: "Collberg & Proebsting (2016, last week): tried to obtain and build the code of 601 systems papers; only about a third to a half could be built ('weak repeatability'). Proposed sharing contracts and funding for repeatability engineering.",
 8: "Felter et al. (IBM, 2014): containers matched or beat virtual machines in almost all benchmarks, with negligible CPU/memory overhead compared to bare metal; both need tuning for heavy I/O. Implication: performance measured in a VM is not representative; in a container it is close to native.",
 9: "DFG Code of Conduct (Germany): research data and the software behind a publication should be archived for at least ten years; universities make this binding (e.g. Potsdam, Max Planck). Archiving keeps the files, not their ability to run.",
 10: "Anonymous GitHub (anonymous.4open.science): mirrors a repository with author and organisation names replaced, so reviewers can browse code during double-blind review. Links expire after the review period, so it is not an archive; authors remain responsible for leaks such as commit history.",
 11: "History of artifact committees: from ECOOP and OOPSLA 2013, AECs were deliberately filled with senior PhD students, because they know current tools and so the next generation learns about artifact evaluation (organisers' nomination letter; Krishnamurthi's memo on artifact evaluation, which started at FSE 2011).",
 12: "Reviewer time budgets: SOSP 2021 estimated 10-20 hours per artifact with 2-4 artifacts per member; APLAS 2022 about 8 hours with 3-4 per member. So a reviewer typically has about one working day per artifact.",
 13: "SLE 2025 artifact evaluation: a 'kick the tires' phase first checks that the artifact runs at all, followed by a 5-day window in which reviewers and authors can talk and fix setup problems; only then the full review. Most PL/SE venues have a similar phase.",
 14: "Chang case (Science news, 2006): a lab-inherited analysis program flipped two data columns, inverting protein structures; this led to five retractions (three in Science) over five years of work. Treated as an honest error; found because another group's results contradicted it.",
 15: "Reinhart & Rogoff (2013): a student, Herndon, asked for the spreadsheet behind an influential austerity paper after failing to replicate it; a range error left out five countries, and corrected, average growth for high-debt countries changed from -0.1 % to 2.2 %.",
 16: "NMR script bug (2019): Python's glob returns files in an operating-system-dependent order; widely used chemistry scripts gave correct results on Windows and older macOS but wrong ones on newer macOS and Ubuntu, possibly affecting about 150 studies. Fixed by sorting the file list.",
 17: "POPL 2023 artifact evaluation call: recommends packaging artifacts as VM images, partly because VMs 'protect reviewers from malfunctioning artifacts damaging their computer'.",
 18: "ICSE open science policy: sharing data is not required for submission or acceptance; authors who cannot share (e.g. confidential industry data) state why in a data availability section and the submission form.",
 19: "Horizon Europe (EU research funding): open access to research data is mandatory under 'as open as possible, as closed as necessary'; exceptions (commercial exploitation, data protection, confidentiality, security, IP) must be justified in a mandatory data management plan.",
 20: "Formal-methods conferences CAV, FORMATS and QEST: no blanket rule for licensed software; authors who need e.g. MATLAB contact the AE chairs for a case-by-case solution; FORMATS 2022 accepted a shared folder runnable in MATLAB Online.",
 21: "MobiSys 2026: for experiments with heavy computation or data, reviewers and authors may agree on a reduced but representative set of experiments. IISWC 2026: most artifacts should run on a laptop; otherwise authors must provide (anonymised) remote access to suitable machines.",
 22: "SOSP 2019 (reported for OSDI 2020): Microsoft donated Azure cloud credits for artifact evaluation, but organisers found them hard to use for exactly the artifacts that needed them most; later calls let authors pay for cloud use.",
 23: "Journal of Open Source Software (JOSS): publishes short papers about research software with a DOI, reviewed openly on GitHub (docs, tests, licence), so software work becomes citable and counts for careers.",
 24: "Embargo norms: data-heavy fields let the producing team publish first, e.g. telescope data 12-18 months exclusive, UK NERC up to 2 years after collection. No study measures how often scooping actually happens; it is a perceived risk.",
 25: "Research software engineers (RSEs): permanent staff (e.g. Princeton, Aalto) who maintain research code so knowledge stays when students leave. Maintenance funding (e.g. CZI open-source grants, DFG calls) runs in short cycles.",
}

src, dst = sys.argv[1], sys.argv[2]
p = Presentation(src)
for i, s in enumerate(p.slides, 1):
    if s._element.get("show") == "0": continue
    if not (11 <= i <= 42): continue
    text = " ".join(sh.text_frame.text for sh in s.shapes if sh.has_text_frame)
    tf = s.notes_slide.notes_text_frame
    t = tf.text.split("\n\nCITED SOURCES\n")[0]
    nums = sorted({int(n) for grp in re.findall(r"\[(\d+(?:,\s*\d+)*)\]", text + " " + t) for n in grp.split(",")})
    if not nums: continue
    tf.text = t + "\n\nCITED SOURCES\n" + "\n".join(f"[{n}] {BG[n]}" for n in nums)
    print(i, nums)
p.save(dst)
