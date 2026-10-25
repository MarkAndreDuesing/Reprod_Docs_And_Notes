---
name: discussion-questions
description: Turn source material (a paper, report or topic) and the user's own question ideas into a refined set of discussion questions with context, follow-ups, example answers and background. Use when the user wants to prepare, select, refine or moderate discussion questions.
---

# Discussion Questions

General method for preparing discussion questions. The source, audience and the user's own
ideas are inputs; the method and quality rules are fixed. For slides, hand the result to the
`presentation-slides` skill (question slide type).

## Inputs to collect first

Ask only for what is missing:
1. **Source material** and the **scope** within it.
2. **Audience:** what they already know, and how closely they will have read the source
   (assume they remember section headings and a few summary bullets, not details).
3. **Format:** number of questions, minutes per question, whether spares are wanted.
4. **Excluded topics**, e.g. parts other people cover.
5. **The user's existing ideas**, and how they are marked (ratings, colours, comments). Ask
   what each marking means; never assume a convention. Extract markings exactly (e.g. read
   highlight colours from the file) and confirm your reading.
6. **Examples the user likes or dislikes**, if any.

## Method

1. **Read** the source in the given scope and the user's ideas. List each idea with its
   marking and the source section it belongs to.
2. **Research first.** Do full web searches on every open point, fact the user asked about,
   or claim that needs checking, before drafting. Save results with sources to a research
   file. Mark anything you could not verify. Research is background for follow-ups,
   example answers and notes, never the basis of a question.
3. **Group.** Cluster ideas by the source's own structure (sections, categories), merging
   duplicates. Propose the grouping and wait for approval.
4. **Draft** each question in this form:
   - **Title:** "Category Name: Topic", topic plain and descriptive, never catchy.
   - **Context:** one short sentence on what the source says.
   - **Question:** one sentence, general, close to the user's original idea (reword lightly,
     don't reinvent).
   - **Example:** one concrete situation that makes the question tangible.
   - **You:** one short perspective question (as reader, reviewer, author, user…).
   - **Example answers:** at least two defensible positions.
   - **Background:** research facts for the presenter only.
5. **Test** every question against the checklist below and fix failures.
6. **Present** the drafts compactly; revise with the user; keep what they say they like
   unchanged and learn the pattern from it.
7. Keep one source file for the final questions (e.g. the content file used for the slides)
   so the notes file and slides stay in sync.

## Quality checklist

A question passes only if all hold:
- **Not obvious:** at least two reasonable, opposing answers exist; no "1 + 1 = 2", no plain
  yes/no where everyone says yes.
- **Answerable:** the audience can engage from the source and general knowledge; it needs no
  background research or specialist experience they lack.
- **Not arbitrary:** not a matter of taste ("ice cream or vanilla?").
- **Not a blame game:** avoid "individuals should try harder" vs. "the system needs funding".
  Look for an angle about mechanisms, consequences or trade-offs (what would make someone act
  differently, what should happen when X occurs).
- **Grounded:** clearly tied to something the source says; a first-time reader sees the link
  from the title and context alone.
- **General core:** specific cases belong in Example/You, not in the question. Don't build a
  question around a single anecdote or respondent.
- **Not over-personalised:** only the You line is "put yourself in the shoes"; the question
  itself addresses the topic.
- **In scope:** no heavy overlap with excluded topics; if unavoidable, flag it in the notes.
- **Short:** title, context, question, example and You each fit on one or two lines.

## Good vs. weak (generic illustrations)

| Weak | Why | Better |
|---|---|---|
| "Should reviewers be allowed to refuse unsafe software?" | obvious yes | keep the question, add You: "If refusing were allowed, which work could no longer be evaluated?" |
| "Isn't finding mistakes the point of review?" | rhetorical, one answer | Context: "Authors fear sharing exposes mistakes." Question: "What would make you more or less willing to share your own work?" |
| "Your paper claims 3× speed-up; the reviewer uses a VM. What counts?" | case as core, needs expert knowledge | general question on the topic; the case moves to Example, or drop if the audience lacks the background |
| "Is the problem lazy researchers or missing funding?" | blame game | ask about a mechanism: "Who should carry the cost of X, and how?" |

## Output

- A questions file: title, context, question, example, You, example answers, background
  per question, sorted by the source's structure.
- Optionally the slides via `presentation-slides` (type `question`): title, context,
  question and follow-ups on the slide; answers and background in the speaker notes.
