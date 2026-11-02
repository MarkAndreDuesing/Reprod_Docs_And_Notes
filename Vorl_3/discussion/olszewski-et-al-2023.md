# Olszewski et al. (2023), *"Get in Researchers; We're Measuring Reproducibility": A Reproducibility Study of Machine Learning Papers in Tier 1 Security Conferences* (ACM CCS 2023)

_Page numbers are printed proceedings pages (3433–3459 = PDF pages 1–27; body 3433–3444)._

**In one sentence:** Of 744 ML papers at CCS, S&P, NDSS and USENIX Security (2013–2022), 60 %
share no code; of the 298 artifacts, 56 % do not run within one hour of debugging and only 20 %
reproduce the claimed results within 5 %. A permutation test finds no significant change in
code availability since AECs (p = 0.068), although USENIX AE artifacts seem to work more often.

**Type:** empirical, quantitative (indirect study by coding papers; direct study by running code).

### Unclear aspects / methodological questions

- **The H0 test does not isolate AECs (pp. 3435, 3441).** H0 compares code availability before
  and after 2020 across *all four* conferences. Only USENIX had an AEC in 2020–2022; CCS started
  in 2023 and NDSS and S&P had none (p. 3435). The test therefore measures a **time trend**,
  three-quarters of it at venues without AE. A fair test would compare USENIX with the other
  three (a difference-in-differences design).
- **Ten data points.** The permuted values are per-year *proportions* (p. 3441): seven years
  before, three after. A permutation test on 10 points has very little power. With 744 papers,
  a paper-level test (e.g. logistic regression on year, venue and AEC) was possible.
- **"We accept the null hypothesis" (p. 3441).** A non-significant test fails to reject H0; it
  does not show that H0 is true. Yet the contributions say AECs "have yet to achieve their
  intended goals" (p. 3434) and the abstract says there is "no statistically significant
  difference". Also, p = 0.068 is described as not "nearly" meeting a threshold of 0.05.
- **Strict threshold, applied one way.** The paper adopts p < 0.005 as the bar (p. 3435) but
  only uses it to dismiss p = 0.068. The positive AE claim then rests on Fig. 8 with no test at all.
- **H0's wording (p. 3435).** "A null hypothesis claims that there is no causal relationship…"
  An observational before/after comparison can't test causation in either direction.
- **AEC goal ≠ code availability.** AE is voluntary and checks *submitted* artifacts. It is not
  designed to make non-submitters share code. Availability is a weak outcome measure for AE.
- **Time caps define the result (pp. 3436, 3443).** One hour of debugging, 10 hours of
  training (some models need months), CPU unless stated. "Does not run" is "does not run
  for this team under these limits". How were truncated-training runs classified: "different
  results" or "missing parameters"? The paper does not say.
- **"Within 5 % of the claimed metric" (p. 3436).** Relative or absolute is not stated. For a
  99 % accuracy claim, 5 percentage points (94 %) is a very wide window.
- **Selection (p. 3435).** The **union** of two reviewers' lists maximises recall but admits
  borderline papers. No agreement measure is given for selection (κ = 0.83 is for coding).
- **Fig. 8 selection bias (p. 3441).** Authors who submit to AE are those who expect their
  code to work. "AE artifacts work more often" may show who submits, not what AE does.
- **"Most positive result" (p. 3443).** A good guard against negative bias, but combined with
  the union selection and unclear 5 % rule, the reader can't tell how lenient the coding was.

### Central claims to take a position on

- **"Common platitudes … ('Just make code available') fail to meaningfully move our community
  forward" (p. 3444).** 44 % of available code runs at all. Agree, or is availability still the
  necessary first step (Winter's view)?
- **"There is no real incentive for any code to be maintained once it is accepted" (p. 3441).**
  4 of 19 USENIX 2022 badges could not be re-created a short time later. Should a badge
  carry a date, or expire?
- **"Reproducible by design" with Docker/VMs and pinned requirements (pp. 3442, 3444).**
  Compare the week-1 seminar note: "we probably won't use Docker in 40 years". Containers
  solve 5-year drift; do they solve 20-year drift?
- **"Effort and funding are likely better spent" on future papers than on resurrecting old
  ones (p. 3444).** Pragmatic, but those papers' claims stay in the literature unverified.
- **More AE would "guarantee" one complete instance (p. 3442).** Only if AE is mandatory.
  Should Tier 1 venues require artifacts? (The paper contrasts them with NeurIPS and its reproducibility challenge, p. 3435.)

### Points of interest

- **Scale and cost:** 8 person-years and 10 000+ compute hours (p. 3434). The paper itself
  argues that reproducibility work is under-valued compared with novelty.
- **90 % of papers that withhold data give no reason (p. 3438).** Only 7 % cite sensitive data
  and 3 % proprietary data. A "data availability statement" requirement would cost little.
- **95 % of artifacts are on GitHub (p. 3439).** Winter et al. show GitHub links break less
  than institutional pages but are not archival. One artifact was only findable via Twitter.
- **"DONE!" (p. 3440):** code for a performance claim whose only output is "DONE!". Example
  of recommendation 5: the artifact should print the paper's tables.
- **Re-running AE badges (p. 3441).** Mismatches came from permissions given only to the AEC
  and from package drift. AE checks the artifact *for the committee at that moment*.
- **Own reproducibility (§8.1, p. 3443).** They can't share the 298 repositories (licences,
  size), only a CSV and figure scripts. Honest, and a reminder that reproducibility studies
  are hard to reproduce. Compare Collberg & Proebsting (week 1), whose build results some authors contested (from memory, not re-checked).
- **Funding and staff turnover (p. 3444)** named as the most significant but least discussed
  challenge, with NSF "Transition to Practice" as a lever.
- **Industry:** only 6 % of papers (p. 3442), so the systems-research finding of low industry
  reproducibility could not be tested.

### Subjective discourse / opinion prompts

- **Would your own code pass their test?** One hour, README only, a fresh machine. What would
  break first: dependencies, paths, data, or missing output scripts?
- **Is one hour fair?** Too short for complex systems, but a realistic budget for a reviewer or
  a student wanting to build on the work. Who should the time limit model?
- **Title and tone.** The pun ("Get in loser, we're going shopping") and phrases like
  "platitudes" signal an outsider shake-up. Does a provocative tone help a community paper?
- **Security-specific reasons not to share:** attack code, malware samples, personal data.
  Should such papers be held to a different reproducibility standard, as §6.4 hints?
- **ML randomness:** if results vary run to run, is "within 5 %" reproducibility, or should
  authors report variance and seeds so a reproducer knows what to expect?

### Ethics / tone

- Failing artifacts are reported in aggregate; named examples are almost all **positive**
  case studies (Oesch, Chen, Siby, Zheng, Das, Mehnaz, Bollinger, Pasquini). Negative cases stay
  anonymous ("one paper claims a performance boost…"). A fair way to criticise a community.
- The full CSV with per-paper coding is public, so individual failures can still be looked up.
  Is that appropriate transparency or naming and shaming?

### Terminology (link to the lecture)

- Uses the **NAS (2019)** terms explicitly instead of ACM's 2020 harmonisation (p. 3434).
- NAS *computational reproducibility* (independent team, same code and data) = ACM 2020
  **reproducibility**, the lecture's term. NAS *replicability* (new data, possibly new method)
  ≈ ACM 2020 **replicability**. *Generalizability* is extra.
- **Indirect vs. direct study** is a useful pair: Winter et al. is entirely an indirect study in
  this sense (availability, documentation); Olszewski et al. adds the direct one.
- The direct study measures *reproducibility* only in the weak form "the authors' code prints a
  number close to the paper's". Footnote 1 (p. 3434): wrong code reproduces wrong results.
