# Collberg & Proebsting (2016), *Repeatability in Computer Systems Research* (CACM 59(3))

_Page numbers are the printed journal pages (62–69)._

**In one sentence:** Of 402 code-backed systems papers (2011/12, ACM venues), only
32–54 % had code that could be obtained *and built*. The authors propose funding
"repeatability engineering" and requiring a "sharing contract" with every paper.

### Unclear aspects / methodological questions

- **"Weak repeatability" is very weak.** It only means "code is available and
  builds". Nobody ran the code or checked results (p. 64). So 54 % is an upper
  bound on real repeatability. Is the title "Repeatability" then overstated?
- **Three rates (A = 32.3 %, B = 48.3 %, C = 54.0 %)**. Which one should be
  quoted as "the" result? C also counts papers where the authors only *claim*
  their code builds (OK Auth), and is capped by a 59.5 % survey response rate.
- **Strict counting rules (p. 65).** Code was "not available" if it needed an NDA
  or license, came with a request for credit, or arrived more than 2 months after
  the email. Is it fair to treat "available under NDA" the same as "lost"?
- **Build attempts by students with a 30-minute limit.** Failing to build may
  say as much about the builder's skill and the tool chain as about the paper.
  (An independent group later re-checked the builds, footnote f.)
- **Exclusions.** 106 papers excluded so that no author got more than one
  email (EX), plus 30 papers left undetermined (EM ø). Could this bias the
  rates?
- **Correlational subgroup claims.** NSF vs. non-NSF shows "no significant
  difference", but no test or numbers are given in the text. The industry
  explanations (IP, internships) are speculation.

### Central claims to take a position on

- **"The root of the problem is sociological, not technological" (p. 69).**
  Do you agree? Yet both recommendations are institutional and administrative,
  not about changing reward structures. Do they address the root cause?
- **Sharing contracts.** Would a contract actually change behaviour, or would
  authors just declare "no sharing"? The authors argue reviewers would "take a
  dim view" of non-repeatable papers. Is that realistic, and fair to industry
  authors or security researchers with legitimate reasons? Who enforces the
  contract after publication?
- **Funding shift.** Moving money from research to engineering. Who loses?
  Is random auditing (like financial audits) realistic?
- **VM images rejected (p. 65).** They doubt VMs because of performance
  measurement, future VM support and security. Heumüller et al. recommend the
  opposite (containers). Who is right, and for which kind of research?

### Ethics / tone

- **Opening anecdote:** Open Records Act and FOIA requests to obtain another
  group's code and emails. Is this a legitimate tool for science or an
  aggressive overreach? Does it help or hurt the case?
- Authors' quotes (disk crash, student left, "reimplement :(") are anonymised but
  vivid. Persuasive storytelling vs. evidence.

### Terminology (link to the lecture)

- Their definitions: **repeatability** = same method, same environment, same
  results, using the original artifacts; **reproducibility** = independent
  confirmation without the original artifacts. ACM badges (described in
  Heumüller et al., p. 4–5) use **replicated** vs **reproduced** for a similar
  split. Terms are not used consistently across the field. Which set does the
  lecture use?



### Points of interest

- **Repeatability vs. benefaction (p. 63–64).** Two reasons to share: so others
  can *check* your results, and so they can *build on* them. The authors note
  that a cleaned-up release *later* helps benefaction but is useless for
  repeatability. Which of the two matters more to you as a researcher?
- **The reasons authors gave for not sharing (p. 66–68)** are a useful
  catalogue: code not clean, student left, disk crash, industry IP, licensing,
  obsolete platforms, fear of misuse in unfair comparisons, support burden,
  privacy and security risks. Which of these are *legitimate*, which are
  *excuses*, and which are *fixable* with better practice (version control,
  backups)?
- **"Your best bet is to reimplement :(".** Reimplementing from the paper
  alone is the stricter test (reproducibility). Is it actually more valuable
  scientifically than rerunning the original code?
- **Support burden.** One group stopped sharing because helping outsiders took
  more time than their own research (p. 68). Sharing code ≠ promising support.
  Should those be separated? The sharing contract tries to do exactly that.
- **Published code ≠ code used for the paper.** 83 % said their code is
  identical (p. 66). How would you even prove which version produced a result?
- **Artifact evaluation already existed (p. 65)**, voluntary and without
  effect on acceptance. PLDI: 12/52 artifacts passed in 2014, 27/58 in 2015.
  Should artifact evaluation influence acceptance?

### Subjective discourse / opinion prompts

- **Should code be mandatory for publication?** The authors call it
  "unrealistic" (p. 68). Is that pragmatism or giving up too early? Other
  fields (e.g., some journals in biology or economics) require data deposits.
- **Is a paper without code still science?** If nobody can check a result,
  how much should we trust it? Where would you draw the line?
- **Responsibility.** Is non-sharing an individual failing, a supervisor's
  failing, or a system failing (publish-or-perish, short PhD contracts)?
- **Publicly funded research.** Does taxpayer funding create an *obligation* to
  share? The NSF quote "when appropriate" (p. 63) shows how vague promises are.
- **Would *you* share your seminar or thesis code today, as is?** If not, why
  not, and does that make you more sympathetic to the authors who refused?
- **Pessimism.** The authors "remain pessimistic" about changing reward
  structures (p. 69). Ten years later, with artifact badges at most major
  venues, were they too pessimistic?
- **Naming and shaming.** The paper anonymises refusals but publishes the
  per-venue rates (Table 2). Is public pressure on venues a fair lever?
