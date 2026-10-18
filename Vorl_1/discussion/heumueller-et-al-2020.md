# Heumüller, Nielebock, Krüger & Ortmeier (2020), *Publish or perish, but do not forget your software artifacts* (EMSE)

_Page numbers are PDF pages (1–32)._

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



### Points of interest

- **Guideline comparison (Table 1, pp. 4–7).** Eight guidelines and 14
  properties, but only *runnable software* and *documentation* are demanded by
  all. What should a *minimum* standard for artifacts be? Which properties
  would you drop or add?
- **Artifacts are the norm.** 76.6 % of ICSE papers build software, 96 % of
  technical papers (p. 13–14). So reproducibility in SE is largely a
  *software* problem, not a data problem. Does that make SE more or less
  reproducible than other fields?
- **Where code lives.** A shift from university pages to GitHub (6.7 % → 65.8 %,
  p. 18). University pages die when people move; GitHub depends on a company.
  Who should be responsible for long-term hosting: authors, universities,
  publishers, or public infrastructure like Software Heritage?
- **Static vs. living badges (p. 23).** A badge only says "this worked at review
  time". Software rots (dependencies, compilers, OS). How long should an
  artifact be expected to work: 5 years, 10, forever?
- **Purpose decides format (p. 22–23).** Containers for *replicating*, source
  for *building on*. Matches Collberg's repeatability vs. benefaction split.
- **Double-blind review makes sharing harder (p. 21)**: you must anonymise the
  artifact. Is that a real obstacle or an excuse?
- **"Ashamed of their source code" (p. 22).** Prototype code is rarely
  pretty. Should the community explicitly accept "research-quality" code?

### Subjective discourse / opinion prompts

- **The title.** "Publish or perish, but do not forget your software artifacts"
  frames sharing as self-interest (citations). Is appealing to self-interest
  the right strategy, or does it undermine the idea that sharing is a
  scientific duty?
- **Carrot or stick?** The paper prefers motivation (badges, citations) and
  "does not blame" authors. Collberg prefers commitments and audits. Which
  would work on *you*?
- **Who pays?** Packaging, containers, persistent archives and documentation
  take time that does not count for a PhD or tenure. Should artifact work be
  credited (e.g., as a citable publication, like JOSS)?
- **Is availability enough?** If a downloaded artifact cannot be run without
  weeks of effort, is it meaningfully "available"? What would you count as
  a *usable* artifact?
- **Self-critique of a field.** The paper belongs to a genre of SE studies on
  SE research itself (§7). Is this kind of meta-research valuable, or does it
  mostly produce numbers everyone already suspected ("sobering" results)?
- **ICSE as representative (p. 25).** The authors assume the top venue
  represents the community. Would you expect smaller venues, workshops or
  journals to be better or worse?
