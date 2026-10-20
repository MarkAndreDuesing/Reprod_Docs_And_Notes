# Reading Guide – Lecture 2 (Oct 27)

Two papers on **artifact evaluation (AE) and artifact sharing**, published a year apart.
They cite each other (Hermann et al. cite Timperley et al. as a preprint, and Timperley et al.
use Hermann et al. for three of their recommendations). There are no new slides this week;
the reference point is still `Vorl_1/IntroductoryLecture.pdf` (definitions on slide 3/24,
reading list on slide 14/24).

| | Paper A | Paper B |
|---|---|---|
| File | `3368089.3409767.pdf` | `s10664-021-09973-5.pdf` |
| Title | *Community Expectations for Research Artifacts and Evaluation Processes* | *Understanding and improving artifact sharing in software engineering research* |
| Authors | Ben Hermann, **Stefan Winter** (our lecturer), Janet Siegmund | Christopher S. Timperley, Lauren Herckis, Claire Le Goues, Michael Hilton |
| Venue | ESEC/FSE 2020 (conference) | Empirical Software Engineering 26:67 (2021, journal) |
| Length | 12 pages (two-column, dense) | 41 pages (single-column) |
| Type | Empirical, **qualitative**: document analysis of 79 calls for artifacts + survey of AEC members | Empirical, **mixed methods**: publication survey of 1434 papers + survey of 153 authors, then a DoI-framework secondary analysis and recommendations |
| Page numbers | Printed proceedings pages **469–480** (= PDF pages 1–12). This guide uses printed pages. | Printed "Page x of 41" = PDF pages, **1–41**. |

## Structure maps

### Hermann et al. 2020 (printed pp. 469–480)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction (RQ1–3 on p. 470) | 469–470 | — |
| §2 Background and related work | 470–471 | — |
| §3 Expectations in ACM guidelines and calls for artifacts (pre-study) | 471–472 | footnote 5 on p. 471: ACM swapped the terms after acceptance |
| §4 Survey of AEC members: method §4.1 | 472–473 | **Fig. 1** committee sizes/responses per conference and year (p. 473); **Fig. 2** histogram of AECs served on (p. 473) |
| §4.2 Perceived purpose (RQ1) | 473–474 | — |
| §4.3 Expectations as reviewer and as user (RQ2, RQ3) | 474–477 | boxed key findings on pp. 474–477 |
| §5 Further insights (satisfaction, interactivity, coupling to acceptance, reviewer experience) | 477–478 | — |
| §6 Threats to validity | 478–479 | — |
| §7 Implications, §8 Conclusion | 479 | — |
| References | 480 | skip |

No formulas and no tables; the numbers are inline counts such as "45 (39/7)" = total (PL/SE).

### Timperley et al. 2021 (pp. 1–41)

| Section | Pages | Tables / figures |
|---|---|---|
| Abstract, §1 Introduction | 1–3 | — |
| §2 Background: artifacts, ACM badges, Diffusion of Innovations (DoI), Implementation Science (IS) | 3–6 | — |
| §3 Methodology (RQ1, RQ2.1–2.3 on p. 6), publication survey §3.1, author survey §3.2 | 6–9 | **Fig. 1** study overview (p. 7); **Table 1** survey questions (p. 8); **Table 2** respondent roles (p. 8) |
| §3.3–3.4 Secondary analysis, recommendation subgroups | 9–10 | — |
| §3.5 Threats to validity | 10–11 | — |
| §4.1 RQ1 value of artifacts | 11–12 | **Fig. 2** papers with artifacts per year (p. 12); **Table 3** motivations for sharing (p. 12) |
| §4.2 RQ2 challenges for creators / users / reviewers | 13–24 | **Table 4** challenges C1–C12 (pp. 14–15); **Table 5** user challenges with counts (p. 19); **Fig. 3** artifact availability by year (p. 20); **Fig. 4** FSE AEC funnel (p. 21) |
| §5 Secondary analysis with DoI | 24–28 | **Fig. 5** communication channels (p. 26) |
| §6 Recommendations R1–R8 | 28–35 | **Table 6** recommendations × challenges × target group (pp. 29–30, printed sideways) |
| §7 Related work | 35–37 | — |
| §8 Conclusion | 37–38 | — |
| References | 38–41 | skip |

No formulas.

## 4-hour plan: Timperley et al. (41 pages, body ≈ pp. 1–38)

| Block | Time | Pages | What to do | Output |
|-------|------|-------|------------|--------|
| 1. Survey (Pass 1) | 15 min | Abstract, §1 (pp. 1–3), §8 (pp. 37–38), all captions | Find RQ1 and RQ2.1–2.3 and the headline numbers (1434 papers, 62.69 % with artifact, 153 respondents, ~14 % dead links, FSE AEC: 74 submitted, 64 accepted) | Claims column; five Cs |
| 2. Background | 20 min | §2 (pp. 3–6) | Skim. ACM badge criteria (pp. 4–5) are worth noting; DoI's four elements (p. 5) are needed later | 4 DoI terms in your own words |
| 3. Method (slow) | 55 min | §3 (pp. 6–11), Tables 1–2 | How is "artifact" defined (any link!)? Who was surveyed (2018 authors only)? How were codes built? Read the threats (pp. 10–11) **now** | List of judgement calls; what was *not* checked |
| — Break | 10 min | | | |
| 4. Results | 55 min | §4 (pp. 11–24), Tables 3–5, Figs. 2–4 | For each table/figure, predict the message, then check. Map C1–C12 to creators/users/reviewers. Check the Fig. 4 percentages yourself | Evidence column; `✗` on numbers that don't add up |
| 5. Secondary analysis | 20 min | §5 (pp. 24–28), Fig. 5 | Does DoI add insight, or relabel §4? | One sentence verdict |
| 6. Recommendations | 30 min | §6 (pp. 28–35), Table 6 | For each R: who must act, what does it cost, is it new or borrowed? | R1–R8 table with "who / cost / new?" |
| 7. Related work | 5 min | §7 (pp. 35–37) | Only the bits on Hermann, Heumüller and Collberg | `→` links |
| 8. Synthesis | 30 min | — | Discussion template; top 3 points | One-page sheet |

Total: 240 min. If behind schedule, cut blocks 2, 5 and 7, never 3 or 8.

### Questions to ask while reading Timperley et al.

- **Definition of "artifact":** any link to external material counts, including
  companion websites (p. 3). Does "62.69 % have an artifact" mean much then?
- **RQ1 evidence:** the "value" claim rests on link prevalence plus positive quotes. Is
  sharing the same as valuing?
- **Survey population:** authors of 2018 papers at top venues. Who is missing (people who
  left research, authors who never share)?
- **Thematic analysis:** the authors say it does not measure prevalence (p. 9). Do they
  stick to that when they write "a large number" or rank challenges?
- **Fig. 4 maths:** 74 submitted out of 196 artifact papers, but reported as 26.33 %.
  Of what?
- **Recommendations:** which ones actually come from the data, and which are borrowed
  from the literature (Table 6 has both columns)?

## 2-hour plan: Hermann et al. (12 dense pages, qualitative survey)

Short, but empirical and dense, so it needs more time than an 8-page argument piece. Two
columns of FSE text hold about as many words as 25 journal pages.

| Block | Time | Pages | What to do |
|-------|------|-------|------------|
| Survey | 10 min | Abstract, §1 (469–470), §8 (479), boxed findings | RQ1–3 and the five boxed key findings |
| Pre-study | 20 min | §3 (471–472), **footnote 5** | Which purposes and criteria do the 79 calls state? Note the terminology problem |
| Method | 20 min | §4.1 (472–473), Figs. 1–2, §6 threats (478–479) | Response rate, PL/SE split, card sorting. Read the threats now |
| Results | 40 min | §4.2–4.3 (473–477) | Reviewer vs user view; criteria per artifact type (code, proofs, data) |
| Further insights | 10 min | §5 (477–478) | Coupling to acceptance; reviewer experience |
| Synthesis | 20 min | — | Template; compare with Timperley |

### Questions to ask while reading Hermann et al.

- **Terminology:** the paper uses the *pre-August-2020* ACM terms (footnote 5, p. 471). Translate
  every "replicability" into the lecture's 2020 terms as you read.
- **Who answered?** 257 of 1034 responded, only 124 completed; respondents are mostly PL.
  Is this "the community"?
- **Counts in a qualitative study:** open card sorting with counts like "45 (39/7)". How
  much can you read into a difference of 7 vs 9?
- **Reviewer vs user:** only 76 respondents ever reused an artifact (p. 477). Does the
  "users want reusability" finding rest on enough people?
- **Conflict of interest?** Not in a bad sense, but the authors are themselves AE organisers
  (Winter, Hermann). Does insider knowledge help or bias the reading?

## Discussion roles (paper only)

Same four as week 1: **presenter**, **advocate**, **critic/reviewer**, **practitioner**.
Since you moderate this week, you don't take a role yourself; see `moderation.md`.
