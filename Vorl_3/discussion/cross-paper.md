# Cross-Paper Discussion: Winter et al. (2022) × Olszewski et al. (2023)

_Page numbers: Winter et al. printed pp. 145–156; Olszewski et al. printed pp. 3433–3459._

## Quick comparison

| | Winter, Timperley, Hermann, Cito, Bell, Hilton & Beyer | Olszewski et al. (University of Florida) |
|---|---|---|
| Field / venues | SE and PL, 12 ACM conferences, 64 venues, 2011–2020 | Security, CCS / S&P / NDSS / USENIX Security, 2013–2022 |
| Sample | 3 650 articles (all papers ≥ 4 pages) | 744 ML papers; 298 artifacts run |
| AE context | AE since 2011, widespread | AEC only at USENIX (2020) in the study period; CCS from 2023 |
| Who measures | AE organisers (insiders) | Security researchers outside AE organisation |
| Indirect / direct | **Indirect only:** badges, links, HTTP status, GitHub API, file names | **Both:** coding of papers + running the code |
| Comparison | Badged (AE) vs. not badged, per venue | Before vs. after 2020; AE vs. non-AE at USENIX (descriptive) |
| Statistics | KS tests per venue, stratified, BH-corrected | One permutation test on 10 yearly proportions, p = 0.068 |
| Headline | No citation gain; Available badge → far fewer dead links; small activity gain; unclear reuse; licences missing | 60 % no code; 56 % don't run; 20 % reproduce; no significant AEC effect on availability |
| Diagnosis | Missing rewards; badges tied to the wrong process; no standards | Packaging, missing files, poor instructions, hardware, not designed for reproducibility; no incentive to maintain |
| Proposals | Alternative rewards; Available badge in paper review; community standards; licence files | Pinned dependencies, Docker/VMs, complete repos, non-expert-tested READMEs, share hardware data, outputs = paper tables; more AE |
| Terminology | ACM 2020 | NAS 2019 (computational reproducibility = ACM 2020 reproducibility) |
| Own artifact | Data, scripts and tool on Zenodo | CSV and figure scripts on GitHub; repos not shareable |
| Tone | Measured, self-critical about AE | Provocative title, "platitudes" |

## Where they agree

- **AE helps, but less than hoped.** Winter: modest, mostly via archival hosting. Olszewski:
  no significant availability effect, but AE artifacts seem to work more often.
- **Incentives are the root problem.** Winter: artifacts don't raise citations and escape
  citation tracking (p. 155). Olszewski: "no real incentive for any code to be maintained once
  it is accepted" (p. 3441); funding and staff turnover (p. 3444).
- **Standards for packaging and documentation** (Winter p. 155; Olszewski recommendations 1–3).
- **Neither checks correctness** of the code or whether results are scientifically right.

## Where they differ or conflict

- **Is availability progress?** Winter treats availability as the "vital" first criterion
  (p. 149). Olszewski calls "just make code available" a platitude (p. 3444), since 56 % of
  available code doesn't run.
- **GitHub.** 95 % of Olszewski's artifacts are on GitHub (p. 3439). Winter's Table 4 shows
  public VCS links break in 4 % of cases vs. 1 % for DOIs, and only DOI/publisher hosting
  meets the Available badge's retention rule (p. 151). GitHub is "available", not archival.
- **What counts as an effect.** Winter runs many careful tests and reports no effect for
  citations. Olszewski runs one weak test, rejects an effect, then infers a positive one
  without a test. Same question (does AE work?), very different statistical standards.

## Discussion questions

1. **Indirect vs. direct.** Winter's study never runs an artifact; Olszewski's shows that 56 %
   of available code doesn't run. How much is an availability or documentation measure worth
   without running anything? What would a direct study of Winter's 1 285 AE articles' artifacts find?
2. **What does a badge certify, and for how long?** Olszewski re-created 15 of 19 USENIX 2022
   badges (p. 3441); Winter finds badged artifacts slightly more maintained (p. 152). Should
   badges carry an "as of" date, a re-check, or an expiry?
3. **Same incentives problem, different cures.** Winter wants new rewards (R+ index,
   test-of-time awards); Olszewski wants authors to build "reproducible by design" and
   funders to step in. Which lever would change behaviour fastest in your field?
4. **Measures and their validity.** Citations (Winter RQ1), HTTP status (RQ2), commits (RQ3),
   URL mentions (RQ4), file names (RQ5), "within 5 % in one hour" (Olszewski). For each: what
   does it really measure? Which would you trust most?
5. **Can AE make non-submitters share?** Both papers measure AE effects on *all* papers,
   although AE is voluntary. Is mandatory artifact submission the logical next step, and how
   would security papers with malware or personal data be handled?

## Broader opinion questions

- **Then vs. now.** Week 1 (Collberg & Proebsting, Heumüller) measured builds and links;
  week 2 (Hermann, Timperley) asked people; week 3 measures AE's effects. Has the field moved
  from "is it available?" to "does it work?" Is "is it correct?" the next step?
- **Docker in 40 years.** Olszewski recommends containers; the week-1 seminar note doubted
  Docker's longevity. Which artifact format would you bet on for 20 years: source + pinned
  requirements, container image, VM image?
- **Insiders vs. outsiders.** AE organisers find modest but positive effects; outside
  measurers find "significant progress still needs to be made". Who should evaluate a
  community's process?
- **Who pays?** 8 person-years for one direct study (Olszewski p. 3434). Should funders or
  venues pay for systematic direct reproduction, and who would do the work?

## Links to earlier weeks

- **Heumüller et al. 2020 (week 1):** small positive citation correlation for ICSE; Winter
  disagrees and explains the difference (p. 147).
- **Collberg & Proebsting 2016 (week 1):** 30-minute build rule; Olszewski uses a 1-hour
  debugging cap with a similar logic (p. 3436) and cites 32 % building (p. 3444).
- **Hermann et al. 2020 (week 2):** Winter's venue list and the reviewer-vs-user split that
  Winter sees again in documentation styles (p. 154).
- **Timperley et al. 2021 (week 2):** Winter reuses the CMU dataset (p. 150); Olszewski's
  five problems echo Timperley's creator challenges (packaging, documentation, bitrot).

## Terminology check

| Concept | Lecture (ACM 2020) | Winter et al. | Olszewski et al. |
|---|---|---|---|
| Same team, same setup | repeatability | — | — |
| Different team, authors' artifacts | reproducibility | "results reproduced" badge (p. 146) | (computational) reproducibility (NAS) |
| Different team, own artifacts/data | replicability | "replicated" badge | replicability (NAS) |
| Other environments | — | — | generalizability |
| Checks only availability | — | (whole study) | indirect study |
| Re-runs code | — | — | direct study |
