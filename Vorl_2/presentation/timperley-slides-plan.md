# Plan: Timperley Summary → Team Deck Slides

**Target:** the uploaded team deck, slides 11–17 ("Paper 2", Abstract to Results), plus
added slides where needed.

**Source:** `timperley-summary.md`.

**Style:** house style from `.claude/skills/discussion-slides/SKILL.md`:
- Arial, green `00883A`
- 40pt plain section-name headers, no invented titles or taglines
- page numbers on claims; detail in the speaker notes

**Focus:** approaches, results and ideas rather than numbers. Numbers appear only where
they support a result.

**Left untouched:**
- the teammates' slides (Paper 1, Secondary Analysis, Recommendations, slide 19)
- the reference half (slides 32–66)

Repeated headers get no "(1/2)" or invented subtitles. When a section spans several
slides, the header stays the plain section name. The body opens with a small grey
label, e.g. "RQ2 · C1–C3", so the audience knows where they are.

## Slides

| # | Header | Content | Format |
|---|---|---|---|
| 12 | General Summary | Problem (artifacts fall short of their potential) → goal (understand creating, sharing, using, reviewing) → approach (publication survey + author survey; creator / user / reviewer view) → main result (mismatched expectations, too little reward for creators and reviewers) → output (recommendations) | Green side callout with the framing (week 1: why working artifacts are rare; this paper: why good artifacts are hard to make), plus 4–5 bold-label bullets |
| 13 | Terminology / Definitions | Artifact: the paper's link-based definition vs. ACM's · AEC (opt-in, after acceptance; can't reject a paper) · ACM quality criteria (documented, consistent, complete, exercisable) | Label–definition rows |
| 13b | Terminology / Definitions | ACM badges: rows grouped by slide 9's three questions (works? / permanently available? / results confirmed?), badge name, short "required" bullets. Foot: ACM defines the badges, each conference's AEC sets the concrete rules | Table |
| 13c | Terminology / Definitions | Diffusion of Innovations (how new ideas spread) with its 4 elements mapped to this paper (innovation = artifact · channels = links, AECs, badges · time · social system = SE community) · Implementation Science (iterative, evidence-based change, from medicine) | Four tiles for DoI, one line for IS. Coding terms in the notes |
| 14 | Research Questions | Already filled. Only add a visual split: RQ1 = value, RQ2 = challenges from 3 angles | Small tweak |
| 15 | Methodology | Overall design: a mixed-methods, parallel-convergent study (two studies at once, then merged). Two components side by side | Two-column diagram: §3.1 Publication survey ‖ §3.2 Author survey → merged analysis |
| 15b | Methodology | **§3.1 Publication survey:** all technical-track papers at ICSE / FSE / ASE / EMSE, 2014–2018 · URLs extracted and checked by hand · artifact = any linked material · available = link still works · AEC chairs asked for submission/acceptance data. **§3.2 Author survey:** 2018 authors of those venues · open + closed questions · branching by role · descriptive then axial coding (themes, not frequencies) · questions grouped by RQ | Two panels, 3–4 short bullets each |
| 16 | Results | **RQ1:** artifacts are seen as inherently valuable and sharing is an established, growing norm (most papers link one; the share rose over the period). Not every paper needs one; sharing should be encouraged and rewarded. Without artifacts, replication is hard and unreliable | Key statement plus a 4-tile grid of motivations: supporting evidence · community norm · reuse · understanding |
| 16b | Results | **RQ2 · overview:** the 12 challenges as named groups, the angle symbols under each name | Compact grid of 12 chips, legend for the angles |
| 16c | Results | **RQ2 · C1–C3:** not worth it · portability · maintenance | Table: Challenge (name + symbols) \| Points raised (angle-marked) |
| 16d | Results | **RQ2 · C4–C6:** tacit knowledge · doesn't fit purpose · standards and guidelines | Same table |
| 16e | Results | **RQ2 · C7–C9:** hosting · double-blind review · external constraints | Same table |
| 16f | Results | **RQ2 · C10–C12:** reviewer incentives · technical obstacles · limited communication; plus the reviewer context (few submit to AE, most pass) | Same table |
| 17 | Validity / Discussion | Replicability (data shared, confidentiality kept) · construct (any link counts; unlinked artifacts missed; authors not contacted) · internal (survey bias; triangulation) · "available" = link alive, quality not checked · external (only the SE research community) | Four or five labelled rows |

That's about 15 slides in place of the current 6 placeholders (11 section slide unchanged).

## RQ2 tables: marking the angles

- The **Challenge** column holds the name, with the symbols underneath in small grey text:
  ■ creator · ▲ user · ★ reviewer.
- In the **Points raised** column, each bullet starts with the symbol of the angle(s) that
  raised it, in that angle's colour. The text stays black. A point raised by several angles
  gets several symbols.
- Colours stay within the house palette and differ in brightness, so they work in greyscale
  and for colour-blind viewers:
  - creator ■ = LMU green `00883A`
  - user ▲ = dark grey `5F6368`
  - reviewer ★ = black `1A1A1A`
- The shape carries the meaning, not only the colour.
- A small legend sits at the top right of each RQ2 table slide.
- Alternative if you prefer: one font style per angle (creator **bold**, user *italic*,
  reviewer plain). That needs no extra symbols, but is harder to read at a glance.
- Up to 3–4 short points per angle per challenge. Fuller bullets from the summary go into
  the notes.

## Notes per slide

- page references
- the full bullets from `timperley-summary.md` for that section
- the matching discussion questions from `timperley-discussion-questions.md` as prompts
  (not on the slides)

## Build

- Edit the uploaded `.pptx` with python-pptx: fill the placeholder text, add slides by
  duplicating the existing BASE layout, keep the theme.
- Render to images and check every slide for overflow.
- Save as `Vorl_2/slides/lecture2-team-paper2.pptx` and send it.
