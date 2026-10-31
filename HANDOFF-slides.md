# Handoff: Discussion Slides

Use this to continue the **discussion slide deck** work in a new chat. The
text-to-speech (MP3) work stays in the original chat; don't touch it here
(`Vorl_*/audio/`, `templates/tools/tts_*`, `templates/tts-plan-template.md`).
For the general project context (course, repo, workflow, user preferences) read
`HANDOFF.md` first.

## Where things stand

- **Final deck for lecture 2:** `Vorl_2/slides/lecture2-style-B.pptx` (32 slides).
  The user approved it. Content is in `Vorl_2/slides/content.js`.
- **Skill:** `.claude/skills/discussion-slides/` holds everything needed to make the
  next deck in the same format:
  - `SKILL.md`: the rules, structure and style (read it before any slide work)
  - `render.js`: renders the house style from a content file
  - `content-template.js`: a blank deck in the agreed structure
- `templates/README.md` (step 11) and `HANDOFF.md` point to the skill.
- Older decks kept for reference only: `lecture2-discussion.pptx` (first attempt,
  rejected), `lecture2-style-A.pptx` (clean academic) and `lecture2-style-C.pptx`
  (minimal dark), which were alternatives to B.

## How we got here (decisions in order)

1. **Request:** a Google Slides deck for the lecture-2 discussion, about 90 minutes
   including paper summaries and plenty of group discussion. No Google connector is
   available, so decks are made as .pptx. To open one in Google Slides: upload it to
   Drive, then Open with → Google Slides.
2. **First deck** (`lecture2-discussion.pptx`): built from `Vorl_2/moderation.md` with an
   agenda, goals, terminology, summaries, warm-up, core questions, a break, group work,
   outside-the-box questions and a wrap-up. **Rejected:** the user disliked the
   formatting and fonts (serif Cambria headings, small text).
3. **Style research** (web search): academic slide guides (assertion-evidence checklists
   from Penn State, UNM and Aalto; Brown Sheridan Center) recommend one sans-serif family,
   body text of at least 18–24pt, minimal text and strong contrast. LMU Munich's house
   style is green, black, white and grey with the typeface Compatil; no official LMU slide
   template was found.
4. **Three styles** with a new structure the user specified: A clean academic, B LMU
   green, C minimal dark. **The user chose B.**
5. **Corrections to B** (keep these, they are now hard rules in the skill):
   - no invented titles, taglines or subheadlines (e.g. "Who decides what a good
     artifact is?", "The paper uses the old ACM terms, which ACM swapped in 2020"):
     headers are plain section names, and explanatory text goes into the body
   - larger headers (40pt), e.g. "Methodology"
   - no "One change each" slide; close with "Thank you for your attention"
   - no footer text (the "Lecture 2 · Artifact evaluation" footer was removed)
   - add an "Open Floor" slide before the closing, for audience points prepared in
     advance (further discussion, criticisms, ideas or approaches)
6. **Skill created** from the final B deck. Re-rendering the lecture-2 content with the
   skill gives the same slide text as the approved deck.

## The agreed structure (also in `SKILL.md`)

Title page → Index → Paper 1 (section slide; General Summary, Terminology / Definitions,
Research Questions, Methodology, Results, Validity / Discussion) → Paper 1 · Discussion
(2–3 questions, at least one of Claude's own) → Paper 2 (same) → Paper 2 · Discussion →
Cross Comparison (differences table, similarities) → Discussion: What Do You Agree With? →
Criticism (one slide per paper) → Open Floor → Thank you for your attention.

## What the user wants (from this thread)

- Only what was asked. Don't add sections, activities, slogans or footers of your own;
  suggest them in chat instead.
- Plain, factual headers; content in the body; detail and follow-ups in speaker notes.
- Page numbers on claims from the papers.
- Show the result as a file the user can download, and say how to open it in Google Slides.

## Building a deck in this environment

```
# pptxgenjs is not installed globally; install it once in the scratchpad
cd <scratchpad> && npm install pptxgenjs
NODE_PATH=<scratchpad>/node_modules node .claude/skills/discussion-slides/render.js \
  Vorl_N/slides/content.js Vorl_N/slides/lectureN-discussion.pptx \
  <pptx skill dir>/scripts/apply_theme.js
python3 <pptx skill dir>/scripts/office/validate.py Vorl_N/slides/lectureN-discussion.pptx
```

The pptx skill (`anthropic-skills:pptx`) provides `apply_theme.js`, `validate.py` and
`scripts/office/soffice.py` (for rendering to PDF, then `pdftoppm` to images for a visual
check of every slide).

## Possible next steps

- Small edits to the lecture-2 deck if the user asks (edit `Vorl_2/slides/content.js`,
  re-render with the skill to `lecture2-style-B.pptx`).
- Decks for later lecture weeks with the same skill.

## Prompt to start the new chat

> Please read `HANDOFF.md` and `HANDOFF-slides.md`, then
> `.claude/skills/discussion-slides/SKILL.md`. We're continuing the discussion-slides
> work from there.
