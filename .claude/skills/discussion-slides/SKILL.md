---
name: discussion-slides
description: Build the seminar's paper-discussion slide deck (two papers, about 90 minutes) in the user's agreed structure and house style, as a .pptx that imports into Google Slides. Use whenever the user asks for slides, a deck or a presentation for a lecture week (Vorl_N).
---

# Discussion Slides (house style)

The agreed format from lecture 2 (`Vorl_2/slides/lecture2-style-B.pptx` is the reference
deck). Follow it exactly; the user has rejected anything added beyond it.

## Hard rules

- **Headers are plain section names only:** "General Summary", "Methodology", and so on.
  **Never invent titles, taglines, subheadlines or slogans** (e.g. "Who decides what a good
  artifact is?"). Anything explanatory goes into the body, a table foot or the speaker notes.
- **No footer text.** Slide numbers only.
- **No extra sections or activities the user didn't ask for** (no "one change each",
  no agenda timings, no learning goals, no group-work slides) unless requested.
- Title slide title is factual: "Lecture N: Paper Discussion".
- Close with "Open Floor", then "Thank you for your attention". Nothing else.
- Page numbers on every claim from a paper; say whether they are printed or PDF pages.

## Structure (in this order)

1. **Title page:** "Lecture N: Paper Discussion"; the two papers (authors, venue, year); seminar name and date.
2. **Index:** the seven parts below, numbered 01–07.
3. **Paper 1:** section slide (title "Paper 1", subtitle = full reference), then six summary slides:
   - General Summary
   - Terminology / Definitions (table: setting, the paper's term, our lecture's 2020 term; foot with definitions and pages)
   - Research Questions
   - Methodology (optional row of three key numbers)
   - Results
   - Validity / Discussion
4. **Paper 1 · Discussion:** 2–3 question slides. Include at least one open point of your own.
5. **Paper 2:** same as Paper 1.
6. **Paper 2 · Discussion:** same as Paper 1.
7. **Cross Comparison:** section slide; a differences table; a similarities slide.
8. **Discussion: What Do You Agree With?:** 1–2 question slides on the comparison.
9. **Criticism:** section slide; one slide per paper (counterpoint in the notes).
10. **Open Floor:** for audience points prepared in advance (criticisms, ideas, approaches).
11. **Thank you for your attention.**

Question slides: header (e.g. "Paper 1 · Discussion"), the question in bold in the body, a
grey box with the hook from the paper (quote or number with page), and two boxes with
opposing positions. The follow-up "if it stalls" goes in the speaker notes. Question quality
follows `templates/moderation-template.md` (not obvious, not unanswerable, two defensible answers).

## Style

| Element | Setting |
|---|---|
| Font | Arial throughout (one sans-serif family) |
| Accent | LMU-like green `00883A` (approximation, not LMU's official template) |
| Text | near-black `1A1A1A`; muted grey `5F6368` for notes, feet and stat labels |
| Title, section and closing slides | green background, white text, left-aligned |
| Content slides | white background |
| Headers | 40pt bold green, top left |
| Body bullets | 22pt (20pt when a stat row is present), max 5 per slide |
| Question text | 26pt bold; hook 18pt; positions 20pt (labels 22pt bold) |
| Tables | 20pt; green header row, alternating light grey rows |
| Panels | rounded, light grey `F1F3F2`; position A light green `E3F1E8`, position B grey `ECECEC` |
| Layout | 16:9 wide (13.33" × 7.5"), 0.7" side margins |

Basis: academic slide guides (assertion-evidence checklists from Penn State/UNM/Aalto, Brown
Sheridan Center): sans-serif, body ≥ 18–24pt, minimal text, strong contrast, two font
families at most. The user overrode the "sentence headline" advice: headers stay plain
section names.

## How to build

1. Copy `content-template.js` from this folder to `Vorl_N/slides/content.js` and fill it
   from `Vorl_N/notes/`, `Vorl_N/discussion/` and `Vorl_N/moderation.md`.
2. Render:
   ```
   NODE_PATH=<folder containing node_modules/pptxgenjs> \
   node .claude/skills/discussion-slides/render.js Vorl_N/slides/content.js Vorl_N/slides/lectureN-discussion.pptx [<pptx skill>/scripts/apply_theme.js]
   ```
   If `pptxgenjs` is missing, `npm install pptxgenjs` in a scratch folder and point
   `NODE_PATH` there. The optional third argument writes the colours into the file's theme.
3. Check: validate the file (pptx skill `scripts/office/validate.py`), render to images and
   look at every slide for overflow or overlap.
4. Commit the content file and the .pptx, and send the .pptx to the user. To open it in
   Google Slides: upload to Drive, then Open with → Google Slides.
