# Broneske, Kittan & Krüger (2024): Condensed Notes

_Page numbers: printed "91:x" = PDF page x (1–24)._

## Core claims
- Most artifact research looks at artifacts researchers make themselves; datasets built
  from **other people's** version-control data (SEDs) raise extra problems: privacy,
  consent, licences (pp. 1–2).
- A meta study of 200 papers shows diverse but mostly convenient sharing practices (§3).
- Sharing SEDs faces **ethical and legal** problems; reusing them faces **technical**
  problems (I6, I7, p. 16).
- Three recommendations: avoid collecting personal data, account for licences, ensure
  quality and reusability (p. 17).

## Key definitions
- **Software-evolution dataset (SED):** data extracted from a software repository's
  version-control and associated systems, often with person-related information (pp. 1–2).
- **Data minimisation:** not collecting data you don't need; **anonymisation:** e.g.
  hashing names (p. 16).
- Terms "replicability", "reproducibility" appear only as keywords; the paper does not
  define them. In the lecture's 2020 terms, reusing someone's SED for the same analysis is
  closest to **reproducibility** (same data, different team).

## Study method (pp. 3–9)
- **ROs:** RO1 elicit sharing practices; RO2 classify problems of sharing and using SEDs;
  RO3 specify recommendations (pp. 4–5).
- **Sample:** MSR data-showcase and mining-challenge tracks 2017–2021: 124 papers → 41
  dataset papers + 23 use papers; 2 GHTorrent papers added (pp. 5–6, Table 1 p. 7).
- **Snowballing** (Google Scholar, Nov–Dec 2022): 10 most-cited citing papers per dataset
  paper → 324 candidates → 112 use + 24 problem papers; 200 papers in total after merging
  (pp. 6–7).
- **Coding:** the second author extracted data **alone** (for consistency); the first
  author cross-checked all 43 dataset papers and a random sample (pp. 7–8).
- **Expert discussion:** **one** authority on research-data management and ethics reviews
  (over 2 years, 80+ SE reviews), semi-structured, 10 questions, unbiased questions first
  (Table 2, p. 8). Ethics approval obtained.
- **Analysis:** collaborative card sorting, so no inter-rater agreement (p. 9).

## Findings
- **RO1 (I1–I5, p. 12):** 41 SEDs, mostly repository metadata (23); data mostly from
  GitHub (> 90 %, directly or via GHTorrent); shared on Zenodo (18) or GitHub (13); 6 on
  personal/institutional websites, **3 already offline** (Oct 2022, p. 11); formats mostly
  spreadsheets (19), text (14), relational DBs (11).
- **Privacy (Table 6, p. 13):** 23 SEDs without sensitive data, 8 anonymised (some only
  after publication), **10 with sensitive data and no discussion** of privacy.
- **Reuse problems (Table 7, p. 14):** quantity/reliability (15), missing data (13),
  redundant data (12), topicality (10), faulty data (8), accessibility (6), others (3);
  10 reused without problems, 2 never reused.

## Catalogue: problems of sharing (I6, pp. 13–14)
- **Privacy:** names, emails, but also work data that could evaluate a person.
- **Consent:** contributors did not contribute for research use; "a Gray area" (expert).
- **Platform terms:** GitHub allows research use of public data only if publications are
  open access (p. 14).
- **Copyright:** sharing source code requires **compatible** licences across all projects.

## Recommendations (p. 17)
- **Avoid collecting personal data:** minimise and anonymise during collection; "if it's
  truly anonymous, GDPR does not apply".
- **Account for different licences:** filter for compatible licences, or share only
  links plus a replicable collection method.
- **Ensure quality and reusability:** standard analysis pipelines; standard formats.

## Critique (tightened)
- n = 1 expert; justified by "regulations are similar everywhere" (p. 8). Plausible for
  GDPR basics, weak for "recommendations".
- One coder, no agreement measure; the authors' own interpretations dominate (p. 18).
- Inconsistent counts (112/136 vs. 133/158) and a table mix-up ("Table 8" for Table 7, p. 14).
- Counterpoint: the paper is explicitly a first step, publishes its dataset on Zenodo,
  and the qualitative breadth (200 papers) is unusual.

## Discussion points (merged)
- Is mining public repositories ethical without consent?
- "Share links, not data": good for privacy and licences, bad for replicability (links rot,
  repositories change).
- Topicality: should datasets be maintained, versioned, or frozen?
- Who should check SED ethics: authors, ethics boards, artifact committees, venues?
