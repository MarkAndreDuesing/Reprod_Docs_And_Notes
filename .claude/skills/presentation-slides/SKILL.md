---
name: presentation-slides
description: Build summary slides and discussion-question slides in the LMU house style (Arial, green accent) as .pptx, either as a new deck or inserted into an existing deck without touching other slides. Use whenever the user asks for slides summarising a paper, document or topic, or for discussion slides.
---

# Presentation Slides

General method for summary and discussion slides. Everything specific to a deck (source,
scope, audience, existing deck, categories) is an input you ask for; the rules and style
below are fixed.

## Inputs to collect first

Ask only for what is missing:
1. **Source material** and the **scope** to cover (whole source or certain sections).
2. **Parts covered by others**, to leave out or only point to.
3. **Target:** a new deck, or an existing `.pptx` to extend (which slide to insert after,
   which existing slide to copy the header style from).
4. **Audience** and how much detail they need.
5. **Categories** used in the source, if findings are grouped (e.g. challenges, themes), and
   the groups that raised them (e.g. stakeholder perspectives), for the category patterns.
6. **Discussion questions**, if any (see the `discussion-questions` skill to produce them).

Then propose a slide plan (one line per slide: header, pattern, content) and get approval
before building.

## Rules

- **Plain headers:** section names only ("Methodology", "Results"). Never invent titles,
  taglines or subtitles. A section over several slides repeats the same header, with a small
  grey location label in the body (e.g. "RQ2 · C1-C3"), never "(1/2)".
- **Short wording:** one idea per bullet, at most about 5 bullets per slide, fragments are
  fine. Detail, numbers and quotes go in the speaker notes.
- **Content over numbers:** show approaches, results and ideas. Use numbers only to support a
  result.
- **Visuals over prose:** tiles, panels, tables, grids and labelled rows wherever they save
  words without losing content.
- **Citations:** no page references for the main source on the slides (put them in the notes).
  Other sources get a marker [n] and a References slide before the closing slide.
- **Extending a deck:** never change other people's slides, theme or layouts. Insert after
  the agreed slide, reuse the deck's header shape and layout. Hide superseded draft slides
  instead of deleting them, and say so.
- **No additions the user did not ask for:** no agendas, slogans, footers or extra sections.
  Suggest them in chat instead.

## Slide patterns (types in `build_slides.py`)

| Type | Use for |
|---|---|
| `title`, `section` | green full-bleed title and section slides; also the closing slide |
| `callout` | overview: green callout with the source's core questions + bold-label bullets |
| `rows` | definitions, limitations / validity: label + short text per row |
| `table` | comparisons, definitions with several attributes |
| `bullets` | research questions, short lists |
| `panels` | method: one panel per component, optional design line and foot |
| `tiles` | a main result statement + 3-4 tiles (e.g. motivations, elements of a framework) |
| `grid` | overview of all categories, with group markers |
| `category_table` | categorised findings, about 3 categories per slide: category name with group markers underneath; each point starts with the marker of the group(s) that raised it; legend top right |
| `question` | one discussion question per slide (layout below) |
| `references` | numbered outside sources |

**Question slide layout:** header (e.g. "Paper 1 · Discussion"); green subheader
"Category: Topic" with a plain descriptive topic; a grey context line; the question in bold;
a grey box with "↳ Example:" and "↳ You:" (perspective question); example answers and
background in the speaker notes. Sort question slides by category.

**Group markers:** shape plus colour, so they work in greyscale (defaults ■ green, ▲ grey,
★ black). Rename groups per deck in `groups`.

## Style (LMU house style, fixed)

| Element | Setting |
|---|---|
| Font | Arial throughout |
| Accent | green `00883A`; text `1A1A1A`; muted grey `5F6368` |
| Panels | rounded, `F1F3F2`; accent panels `E3F1E8` |
| Title, section, closing slides | green background, white text, left-aligned |
| Headers | 40pt bold green, top left |
| Body | 18-22pt; questions 28pt bold; context 20pt grey |
| Tables | green header row, alternating light grey rows |
| Format | 16:9 (13.33" × 7.5"), 0.7" side margins |

In extend mode the existing deck's header shape is reused, so its fonts and colours win.

## How to build

1. Copy `content-template.json` and fill it (one entry per slide; `notes` for speaker notes).
   For an existing deck set `"mode": "extend"`, `base`, `insert_after`, `style_ref`.
2. Build: `python3 .claude/skills/presentation-slides/build_slides.py content.json out.pptx`
   (needs `python-pptx`).
3. Check: render to PDF (`soffice --headless --convert-to pdf out.pptx`, then `pdftoppm`)
   and look at every new slide for overflow or overlap. LibreOffice skips hidden slides, so
   unhide a copy to check those.
4. Deliver the `.pptx`, list what was added where, and mention how to open it in Google
   Slides (upload to Drive, Open with → Google Slides). Keep the content file next to the
   deck so changes can be rebuilt.

`examples/` holds the deck structure and scripts this style was developed with; they are
for reference only.
