# Discussion Points – Week 1 Papers

Page numbers: Collberg & Proebsting use the printed journal pages (62–69); Heumüller et al. use PDF pages (1–32).

---

## Collberg & Proebsting (2016), *Repeatability in Computer Systems Research* (CACM 59(3))

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

---

## Heumüller, Nielebock, Krüger & Ortmeier (2020), *Publish or perish, but do not forget your software artifacts* (EMSE)

**In one sentence:** Of 604 ICSE papers (2007–2017) that built software
(76.6 % of all papers), 47.8 % link to it but only 27 % of artifacts were
still downloadable in 2019. Linking shows a small positive correlation with
citations.

### Unclear aspects / methodological questions

- **Availability measured in 2019, not at publication time.** A 2007 paper had
  12 years for its link to break, a 2017 paper only 2. So the "positive trend"
  (5.7 % → 58.5 % available) mixes *more sharing* with *less time for links to
  decay*. The authors notice the linked and available lines are oddly parallel
  (p. 16) but leave it open.
- **Negative slopes?** The regression slopes are reported as "−4.02 %" and
  "−4.04 %" (p. 16) although the trend clearly increases. Typo or axis direction?
- **Correlation presented as causation.** RQ3 finds a *small* effect
  (Cliff's δ ≈ 0.10, CI [0.008, 0.192], lower bound almost zero) for *linked*
  artifacts only. Available and named artifacts show no significant difference.
  Yet the text concludes that linking "positively affects the impact of
  research" (p. 20). Confounders: paper type, well-known groups, topic, tool
  papers being cited for the tool.
- **Why does "linked" matter but "available" not?** Their explanation (links
  worked at publication time) is plausible but untested. Three tests were run
  without multiple-comparison correction.
- **Light-touch classification.** Papers were not read fully: abstract →
  skim → keyword search (p. 11). Validation found "less than 10 %" errors on a
  16.6 % sample, but the exact error rates are only in Table 2. Is <10 % good
  enough when the effect size is this small?
- **No author contact, and web searches dropped.** A web search found 16 %
  of "non-available" named artifacts anyway (p. 24), but this was left out of the
  results. Collberg & Proebsting emailed authors. Which approach gives the
  more meaningful availability number?
- **Availability ≠ repeatability.** Nothing was run (p. 9, p. 24). Combine with
  Collberg's result that many available artifacts do not even build: the real
  repeatability rate of ICSE papers is probably much lower than 27 %.
- **What is the clustering for?** 209 author communities are computed, but they
  mainly support "the problem exists in most communities". Does this add much,
  given the authors themselves call it rough (p. 17)?
- **Definition of "artifact".** Runnable software only, including scripts, but
  not datasets. This affects the "named artifact" and "unique identifier" numbers
  (the authors admit this, p. 18).

### Central claims to take a position on

- **"Your weblinks will break"** → use persistent, non-commercial archives
  (Zenodo, Software Heritage). Only *one* artifact in the whole dataset used
  one. GitHub is commercial too. Is it a safe home for research code?
- **Container + source + binary as the ideal distribution.** Realistic effort for
  a PhD student? And Collberg & Proebsting's VM concerns (obsolescence,
  security, performance measurement) apply to containers as well.
- **"Living badges"** that are updated as others replicate the work. Good idea?
  Who would maintain them, and what is the incentive?
- **"We do not blame any author" (p. 22)** vs. Collberg & Proebsting's
  confrontational approach. Which framing is more likely to change behaviour?
- **The citation argument as motivation.** If the effect is this small, is
  "you'll get more citations" a strong enough incentive? Should sharing instead be
  required (like ESE's open-science policy)?

### Practising what they preach

- The authors publish their dataset and scripts on Zenodo and received the
  EMSE open-science badge. Their study could therefore be repeated.
  Could we check one or two of their classifications ourselves?

---

## Cross-paper discussion questions

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
