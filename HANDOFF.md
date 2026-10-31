# Handoff: Paper Analysis for a New Lecture Week

Use this to start a new chat session that prepares the next lecture week
(`Vorl_2/`, `Vorl_3/`, …) the same way `Vorl_1/` was done. The user will give
you the lecture slides and two papers.

## Context

- **Course:** Seminar *Reproducibility of Scientific Results in Software
  Engineering Research*, SoSy-Lab, LMU Munich (Dr. Stefan Winter, Sophia Hans).
- **Repo:** `MarkAndreDuesing/Reprod_Docs_And_Notes`, the user's personal notes for the seminar.
- **Goal each week:** read two papers efficiently within limited time
  (max. about 4 h for a long paper) and come to the seminar with good
  discussion points.
- **Worked example:** `Vorl_1/`, a long empirical study (Heumüller et al.
  2020, 32 pages) and a short argument piece (Collberg & Proebsting 2016,
  8 pages). Read its files before starting; match their depth and style.

## Where everything is

| File | What it is |
|------|-----------|
| `templates/README.md` | **Start here.** Folder layout, file naming, the 9-step workflow, balance rule |
| `templates/reading-guide-template.md` | Three-pass method, five Cs, claim → evidence → doubt table, time plans by paper type, standard questions, discussion roles |
| `templates/paper-discussion-template.md` | Sections for one paper's discussion file |
| `templates/cross-paper-template.md` | Comparison table and cross-paper questions |
| `.claude/skills/discussion-slides/` | Skill for the discussion slide deck: structure, style rules, renderer, content template |
| `templates/paper-notes-template.md` | Condensed bullet notes of what a paper says (incl. condensing the user's own copied snippets) |
| `templates/moderation-template.md` | **The user moderates lecture 2.** Question sequence and the quality test for discussion questions |
| `Vorl_1/reading-guide.md` | Filled example: per-block time plan mapped to real page ranges |
| `Vorl_1/discussion/*.md` | Filled examples: one file per paper and `cross-paper.md` |
| `Vorl_1/notes/collberg-proebsting-2016.md` | Filled example of condensed notes, made from the user's own snippets and comments |
| `Vorl_1/seminar-notes.md` | The user's notes from the week-1 seminar: what they focus on and what they want when moderating |
| `templates/tts-plan-template.md`, `templates/tools/`, `Vorl_1/audio/` | Text-to-speech work. **Handled in a separate chat; leave it alone** (see below) |

## Steps for the new week

1. **Set up the folder.** Create `Vorl_N/` and put the slides and both paper PDFs in it.
   Keep the original PDF file names.
2. **Identify each paper.** Get the title, authors, venue, year and page count
   (`pdfinfo`, `pdftotext -l 1`). Decide whether it is an **empirical study**
   or an **argument/position piece**, because that sets the time plan.
3. **Map the structure.** List each section with its page range and where
   tables, figures and formulas sit, and where the references start. Find
   pages with `pdftotext -f N -l N` per page. State whether page numbers are
   **printed journal pages** or **PDF pages**.
4. **Write `Vorl_N/reading-guide.md`** from the template:
   - Long empirical paper: a 4 h block plan (survey, background, **method read
     slowly**, break, results, discussion and threats, related work, synthesis),
     with real page ranges per block.
   - Short argument paper: a 1.5 h plan.
   - Rule: if behind schedule, cut background and related work, never method or synthesis.
   - Add paper-specific "questions to ask while reading".
5. **Read both papers in full**, not just the abstract. Extract the text with
   `pdftotext` and read it all. Read each paper's discussion and
   threats-to-validity sections early, so your critique goes beyond what the
   authors already admit.
5b. **Write condensed notes per paper** in `Vorl_N/notes/` from
   `paper-notes-template.md`. If the user pastes their own snippets and
   comments, condense those, keep their emphasis, and tighten their comments
   (with a counterpoint where useful).
6. **Write one discussion file per paper** in `Vorl_N/discussion/`
   (`<surname>[-et-al]-<year>.md`), with these sections:
   - one-sentence summary with key numbers, plus the page-number note
   - unclear aspects / methodological questions
   - central claims to take a position on
   - **points of interest**
   - **subjective discourse / opinion prompts**
   - ethics / tone and terminology (link to the lecture slides) where relevant
7. **Write `Vorl_N/discussion/cross-paper.md`:** a comparison table, discussion
   questions and broader opinion questions. Also link back to earlier weeks'
   papers where useful.
8. **Check terminology.** The seminar uses the **2020 definitions** of
   repeatability, reproducibility and replicability; the week-1 papers used
   the 2011 ones. Map every paper's terms to the 2020 ones and check against
   the slides.
8b. **Write `Vorl_N/moderation.md`** from `moderation-template.md`: the user
   moderates the lecture-2 discussion. Questions must lead to real
   discussion: not obvious, not "I don't know"-open, with a hook in the
   paper and two defensible opposing answers. Include 1–2 outside-the-box
   questions and favour solutions over blame. Add short background facts
   (current practice, technology basics).
9. **Update the root `README.md`** with a line for `Vorl_N/`.
10. **Commit and push**, then summarise the strongest points in chat.

## What the user wants (learned in week 1)

- **Balance, not only criticism.** Give roughly equal weight to methodological
  critique, points of interest, and opinion questions without a right answer
  (linked to the user's own experience as a student or researcher). The user
  explicitly asked for more of the last two after a first draft was mostly
  criticism of the data.
- **Page references on every point.**
- **Concrete, paper-specific points.** Good examples from week 1:
  - availability measured years later mixes "more sharing" with "less link decay";
  - a correlation was described as causation (tiny Cliff's δ);
  - "weak repeatability" only means the code builds;
  - one paper is sceptical of VMs while the other recommends containers.
- **Discussion angles** (details and week-1 examples in `templates/README.md`):
  root causes and solutions over blame; practical consequences such as rules
  or policies and how they'd be circumvented; long-term view and cost;
  whether the measures behind results are valid; then vs. now; short side
  research for background.
- **Discussion roles need only the paper:** presenter, advocate, critic/reviewer,
  practitioner. Don't use roles that need prior materials (archaeologist, hacker).
- **One file per paper plus a cross-paper file.** Don't put everything in one file.
- **Templates are living documents.** If the user asks for a new kind of output,
  formalise it into `templates/` so later weeks can reuse it.
- **Writing style:** plain, direct English. The user writes in English and German
  ("Vorl" = Vorlesung, i.e. lecture).

## Repo and git conventions

- Work on the branch the session gives you. Commit with clear messages and push.
- Open a pull request only when the user asks. The user merges PRs themselves and
  deletes the branch afterwards. If your branch's PR was already merged,
  restart the branch from the latest `main` before adding new work.
- PDFs and notes go in the repo. Large generated files (audio) only when asked.

## Environment notes

- `pdftotext`, `pdfinfo`, Python 3 and ffmpeg are available.
- Outbound web access is restricted: web search works, but many sites
  (university pages, blogs) cannot be fetched directly. Say so when a source
  could not be opened, and mark facts recalled from memory as such.

## Not part of this chat: text-to-speech

Current state, for reference: two voice-test rounds are done (Paper 1 with 110
voices, Paper 2 with 61). Ratings are in `Vorl_1/audio/voice-test*/ratings-round*.csv`,
the round-3 shortlist of 28 voices is `Vorl_1/audio/voices-round3.csv`, and
`Vorl_1/audio/tts-plan.md` records the plan, track lists and rating-sheet links.


The TTS work (turning papers into British-English MP3s with Piper, voice
tests and rating sheets) continues in the **original chat**. In the new chat:

- Don't generate audio or touch `Vorl_1/audio/`, `templates/tools/` or
  `templates/tts-plan-template.md`.
- One thing helps that chat: for each table, figure and formula, note its
  **page number** in the reading guide or discussion file. The TTS scripts
  describe these items with page references.
- The next voice-test round (round 3, 28 voices in `Vorl_1/audio/voices-round3.csv`)
  will use one of the new papers once its analysis exists.

## Prompt to start the new chat

> Please read `HANDOFF.md` and `templates/README.md` in the repo, look at
> `Vorl_1/` as the worked example, then prepare lecture 2 (`Vorl_2/`) for the
> slides and two papers I'm attaching: reading guide, condensed notes and a
> discussion file per paper, a cross-paper file, and a moderation plan (I'm
> moderating this discussion), following the templates. Commit and push when
> done.
