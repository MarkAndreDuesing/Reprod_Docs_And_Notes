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

## Focus areas the user cares about

Learned from week 1 (seminar notes):
- **Incentives:** guidelines and badges help, but incentives are still
  misaligned. Ask how they could be aligned, rather than blaming individual
  researchers, supervisors, venues, funders or universities.
- **Guidelines and regulation:** what concrete rules could follow from the
  paper (venue rules, funder rules, even government regulation), how people
  might circumvent them, and where existing guidelines conflict (e.g. NASA
  requires GitHub, others require persistent archives).
- **Long-term cost:** even the best archiving needs maintenance (we won't be
  using Docker in 40 years); more options and persistence cost money, so who
  funds it? Which format is most durable (source code?).
- **Metrics:** are citations a good measure of impact at all?
- **Then vs. now:** what has changed since the paper (e.g. Zenodo and ACM
  artifact requirements today).
- **Side research worth a few minutes:** e.g. how artifact practice differs
  between research and industry, how Docker containers work.
- **The user's own opinions:** keep and tighten them, and add a counterpoint.

## Balance to aim for

Don't only criticise the data. Each paper file should have roughly equal
parts of:
- **methodological critique** (what is unclear or weakly supported)
- **points of interest** (ideas worth exploring further)
- **subjective discourse** (opinion questions without a right answer, linked
  to your own experience as a researcher or student)
