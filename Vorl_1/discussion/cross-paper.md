# Cross-Paper Discussion: Collberg & Proebsting (2016) × Heumüller et al. (2020)

## Quick comparison

| | Collberg & Proebsting | Heumüller et al. |
|---|---|---|
| Field / venues | Systems, PL, security, DB (8 conferences, 5 journals, 2011/12) | Software engineering (ICSE research track, 2007–2017) |
| Sample | 601 papers, 402 code-backed | 789 papers, 604 with software |
| Measures | Code obtainable **and builds** | Code **linked** and **downloadable** |
| Contacts authors? | Yes (email + survey) | No |
| Headline | 32–54 % weakly repeatable | 27 % available (58.5 % in 2017) |
| Diagnosis | Incentives (sociological) | Communication and persistence |
| Proposals | Funding for repeatability engineering, sharing contracts | Unique IDs, persistent archives, containers, living badges |
| Tone | Confrontational, anecdotal opening | Explicitly non-blaming |
| Shares its own data? | Yes (website, sharing contract example) | Yes (Zenodo, open-science badge) |

## Discussion questions

1. Both papers find roughly the same picture (around half of artifacts obtainable,
   far fewer verified) four years and two communities apart. Has anything
   improved since artifact evaluation and badges became common?
2. Collberg: problem is **incentives** → contracts and funding.
   Heumüller: problem is **communication and persistence** → identifiers,
   archives, containers. Which diagnosis convinces you more?
3. Neither paper checks whether *results* are reproducible. What would a study
   need to look like to measure that, and is it feasible at scale?
4. Is 100 % artifact sharing even a desirable goal, given IP, privacy and
   security reasons (Collberg p. 68; Heumüller §5.1)?
5. **Repeatability vs. benefaction** (Collberg) and **replicate vs. build on**
   (Heumüller) are the same split. Which purpose should artifact policies
   optimise for?
6. **Containers / VMs:** Collberg sceptical, Heumüller in favour. Has the move
   from VMs to Docker since 2016 solved Collberg's concerns?

## Broader / subjective discussion

- **What does "reproducible" mean to you?** Same code → same numbers? Same idea,
  new code → same conclusion? Which one actually builds trust in a result?
- **Novelty vs. confirmation.** Both papers point at incentives that reward
  new results over checking old ones. Would you, as a student, choose a
  replication study as a thesis topic? Why or why not?
- **Is there a reproducibility *crisis* in computer science**, as in
  psychology, or is CS better off because results are "just code"?
- **Personal practice:** after reading these, what is *one* thing you would
  do differently in your own projects (version tags, DOIs, READMEs, containers)?
- **Who should act first:** individual researchers, supervisors, conferences,
  funders, or universities?
