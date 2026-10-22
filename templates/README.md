# Paper Analysis Workflow (Template)

Steps used for each lecture week (first applied in `Vorl_1/`). Copy this
structure for every new week.

## Folder structure per week

```
Vorl_N/
├── <lecture slides>.pdf
├── <paper 1>.pdf
├── <paper 2>.pdf
├── reading-guide.md          ← time plan for this week's papers (from reading-guide-template.md)
├── slides/                   ← discussion deck (skill: .claude/skills/discussion-slides)
├── moderation.md             ← only in weeks the user moderates (from moderation-template.md)
├── audio/                    ← optional MP3s + tts-plan.md (from tts-plan-template.md)
├── notes/
│   └── <author>-<year>.md    ← condensed notes per paper (from paper-notes-template.md)
└── discussion/
    ├── <author>-<year>.md    ← one per paper (from paper-discussion-template.md)
    └── cross-paper.md        ← comparison (from cross-paper-template.md)
```

File names: first author's surname (add `-et-al` for 3+ authors) and year,
lowercase, e.g. `heumueller-et-al-2020.md`.

## Steps

1. **Collect.** Put slides and papers into a new `Vorl_N/` folder.
2. **Identify.** For each PDF, note title, authors, venue, year, page count,
   and whether it is an **empirical study** or an **argument/position piece**.
   This decides how deep you read (see `reading-guide-template.md`).
3. **Map the structure.** For long papers, list sections with their page
   ranges and where the tables/figures are. Mark the references section
   (skip it). This becomes the time plan.
4. **Plan the time.** Fill in the time plan in `reading-guide-template.md`.
   Rule of thumb: about 25 % of the time on the method, 20 % on results,
   15 % on synthesis.
5. **Read: claim → evidence → doubt.** Keep the three-column notes table
   while reading. Use the margin codes. Read the paper's **discussion and
   threats-to-validity sections early**: they often already answer critique
   you were about to write, so your own points go beyond them.
5b. **Write condensed notes per paper** from `paper-notes-template.md`: what
   the paper says, in short bullets (claims, definitions, method, findings,
   catalogue lists, recommendations). If the user supplies their own copied
   snippets and comments, condense those and tighten their comments.
6. **Write the per-paper discussion file** from `paper-discussion-template.md`:
   - summary in one sentence (with the key numbers)
   - unclear aspects / methodological questions
   - central claims to take a position on
   - points of interest
   - subjective discourse / opinion prompts
   - ethics / tone, terminology (where relevant)
   Always give page numbers, and say whether they are journal or PDF pages.
7. **Write the cross-paper file** from `cross-paper-template.md`:
   comparison table, discussion questions, broader opinion questions.
8. **Link to the lecture.** Check terms and concepts against the slides.
   The seminar uses the **2020 definitions** of repeatability, reproducibility
   and replicability; older papers often use the 2011 ones (e.g. Collberg &
   Proebsting). Always map each paper's terms to the 2020 ones.
9. **Pick your top 3** points to bring to the session.
10. **If the user moderates:** write `moderation.md` from
   `moderation-template.md` (question sequence, quality test for questions,
   outside-the-box questions, background facts).
11. **Slides (if asked):** use the `discussion-slides` skill
   (`.claude/skills/discussion-slides/SKILL.md`): fixed structure, plain section
   headers, house style.

## Focus areas the user cares about

General angles that make a paper worth discussing (week-1 examples in brackets):
- **Root causes and solutions over blame:** when a paper identifies a problem,
  ask what would actually fix it and who would have to act, rather than who is
  at fault. (Week 1: misaligned incentives for sharing artifacts.)
- **Practical consequences:** what rules, guidelines or policies could follow
  from the paper, how people might work around them, and where existing
  rules conflict. (Week 1: one guideline requires GitHub, others persistent archives.)
- **Long-term view and cost:** does the proposal still hold in 10–40 years,
  and who pays to keep it working? (Week 1: archiving formats age.)
- **Are the measures valid?** Question the metric behind a result, not only the
  result. (Week 1: are citations a good measure of impact?)
- **Then vs. now:** what has changed in practice since the paper was written.
- **Short side research:** a few minutes on background that makes the
  discussion better informed (e.g. a technology the paper relies on, or how
  practice differs between research and industry).
- **The user's own opinions:** keep and tighten them, and add a counterpoint.

## Balance to aim for

Don't only criticise the data. Each paper file should have roughly equal
parts of:
- **methodological critique** (what is unclear or weakly supported)
- **points of interest** (ideas worth exploring further)
- **subjective discourse** (opinion questions without a right answer, linked
  to your own experience as a researcher or student)
