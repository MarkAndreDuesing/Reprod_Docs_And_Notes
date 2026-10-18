# Paper Reading & Discussion Guide

A time-boxed version of Keshav's three-pass method, with a structured middle pass,
plus a discussion template. Based on Keshav, *How to Read a Paper*, and role-based
seminar formats (Raffel & Jacobson; presenter/advocate/critic).

## Core idea for Pass 2

Don't read front to back. Read **claim → evidence → doubt**:

1. Write down what the paper *claims* (from abstract, intro, RQs, conclusion).
2. Go find the *evidence* for each claim (methods, tables, figures).
3. Note where the evidence is weaker than the claim. Those gaps are your
   discussion points.

Keep one notes sheet with three columns while reading:

| Claim / RQ | Evidence (page, table, fig) | Doubt / question |
|------------|-----------------------------|------------------|

Margin codes help you scan back quickly: `?` don't understand, `!` key result,
`✗` disagree or weak, `→` connects to lecture or other paper.

## 4-hour plan: Heumüller et al. (32 pages, body ≈ pp. 1–27)

| Block | Time | Pages | What to do | Output |
|-------|------|-------|------------|--------|
| 1. Survey (Pass 1) | 15 min | Abstract, §1 (pp. 1–3), §8 (p. 27), headings, all figure/table captions | Find the 3 RQs and headline numbers (789 papers, 604 SAPs, 58.5 % available in 2017, small positive citation correlation) | RQs copied into the claims column; five Cs, one line each |
| 2. Background | 25 min | §2 Artifact Publishing Guidelines (pp. 4–7), Table 1 | Skim. Capture what the guidelines recommend (persistence, licensing, archives) | 3–5 bullets: "what good artifact publishing looks like" |
| 3. Method (slow) | 60 min | §3 Methodology (pp. 8–12), Table 2 | Read carefully. How were papers collected? How is a "software artifact paper" defined? Who classified, how was agreement checked? What is the community clustering for? | For each RQ, how it was measured; list of judgement calls in the method |
| — Break | 10 min | | | |
| 4. Results | 50 min | §4 Evaluation (pp. 13–20), Table 3, Figs. 1–8 | For each figure, write one sentence on what it shows *before* reading the text, then check. Map every result back to RQ1–3. Check the correlation: how strong? Controlled for what? | Evidence column filled; `✗` marks on results that seem over-interpreted |
| 5. Discussion & threats | 35 min | §5 (pp. 21–24) incl. Table 4, §6 Threats (pp. 24–25) | Compare the authors' own threats with your doubts list. What did they miss? Are the lessons learned supported by the results? | Doubt column completed |
| 6. Related work | 10 min | §7 (pp. 25–27) | Skim only. Note any link to Collberg & Proebsting or the lecture | `→` connections |
| 7. Synthesis | 35 min | — | Fill in the discussion template below. Pick your 3 best points | One-page discussion sheet |

Total: 240 min. References (pp. 28–32) can be skipped.

If you're behind schedule, cut from blocks 2 and 6 first, never from 3 or 7.

### Questions to ask while reading this paper

- **Definitions:** how is "artifact available" decided? Does a dead link or
  "available on request" count?
- **Sample:** ICSE research track 2007–2017 only. Does that generalise to SE or CS?
- **Correlation vs causation:** do linked artifacts get cited more, or do
  already-strong groups both share artifacts *and* get cited more?
  What does the clustering do about this?
- **Reproducibility of the study itself:** could you repeat this study from the
  paper? Is their own data published?
- **Practice:** which lesson learned would actually change researcher behaviour?

## 1.5-hour plan: Collberg & Proebsting (8 pages, argument piece)

| Block | Time | What to do |
|-------|------|------------|
| Survey | 10 min | Abstract, headings, sidebars, conclusion. What is the central argument? |
| Read | 50 min | Follow the argument: their study of building others' code, the obstacles found, the proposed fixes. Note which claims rest on data vs opinion |
| Synthesis | 30 min | Fill in the template; compare with Heumüller et al. |

## Discussion template (one page per paper)

1. **Summary (3 sentences):** problem, approach, main finding.
2. **Five Cs:** category, context, correctness, contributions, clarity.
3. **Strongest point** of the paper, with evidence.
4. **Weakest point** (gap between claim and evidence), with page reference.
5. **Reproducibility check:** are data/tools available? Could the study be repeated
   from the text? Are key terms precisely defined?
6. **Connection:** to the other paper and to the lecture.
7. **2–3 open questions** for the group.

## Discussion roles (no prior materials needed)

Pick roles that only need the paper itself:

- **Presenter:** gives the 3-minute summary.
- **Advocate:** argues why the paper is convincing and important.
- **Critic / reviewer:** argues the weaknesses, as in a conference review
  (accept or reject, and why).
- **Practitioner:** what should researchers or the community actually do
  differently because of this paper?
