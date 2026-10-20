# Collberg & Proebsting (2016): Condensed Notes

_Made from the user's own copied snippets and comments (worked example for
`templates/paper-notes-template.md`). Page numbers are printed journal pages (62–69)._

## Core claims
- A lot of published systems research comes without its code, so others can't repeat it (p. 63).
- Sharing software costs real effort, so funders should pay for the engineering.
- Publishers should require authors to declare up front what they will share.

## Key definitions
- **Repeatability:** you re-run the same method in the same environment and get the same results (p. 63–64).
- **Benefaction:** you share so others can build on your work and don't have to redo it.
- **Reproducibility:** independent confirmation; unlike repeatability, it does not necessarily need the original artifacts.
- **Weak repeatability (the study's bar):** the code is available and it builds. Results were not checked (p. 64).
- These are the 2011-era definitions; the seminar uses the 2020 definitions.

## The diagnosis
- The problem is sociological, not technological: producing shareable artifacts or replicating others' work brings little professional credit (p. 69).
- Nosek: new findings earn publications, jobs and tenure; replications "produce a shrug."

## Study method
- 601 ACM papers (p. 64).
- Search order: the paper, the authors' websites, web search, GitHub / Google Code / SourceForge, then email (at most one email per author) (p. 65).
- **"Code not available"** when: only partial code or binaries; "send soon" and nothing came; an NDA or licence had to be signed; authors demanded credit for follow-up work; code arrived more than 2 months after the request.
- **Builds:** one assistant with 30 minutes, then another with unlimited time; often fixing makefiles and finding old OS, compiler and library versions.

## Findings
- Industry-only papers shared least; academic-only papers more than average (p. 66).
- Releasing reworked code later helps benefaction but not repeatability: the published results can never be checked.

## Why code isn't shared (grouped, p. 66–68)
- **Effort:** clean-up and documentation take time; users ask for support.
- **People:** student left, developer died, emails bounced, authors too busy.
- **Infrastructure:** no backups (a server lost three disks at once).
- **Fragility:** prototypes with "many moving pieces" only one person could run.
- **IP and commercial:** patents, commercialisation, employer rules, licensed parts.
- **Attribution and competition:** use without citation, competitors' advantage. Proposed fix: Stodden's Open Research License.

## On VM images (p. 64–65)
- Appeal: bundle code, data, OS and libraries.
- Problems: unreliable performance measurements; future hypervisors may not run the image; old unpatched images are a security risk.
- User's question: "isn't the point of VMs to be able to do this?" Answer: a VM makes it possible to *run* the code but distorts *timing*. That matters for performance papers, much less for functional ones, which also resolves much of the disagreement with Heumüller et al. (containers).

## Recommendations (p. 68–69)
- Mandatory code is "unrealistic".
- **Fund repeatability engineering:** staff to document, maintain, release and support; random audits that artifacts were shared as promised.
- **Require a sharing contract:** declared at submission and printed in the paper; states resources, support, duration and cost; commits reviewers and readers to take it into account.
- **Sharing is not licensing:** sharing = what is available; licence = what you may do with it. Both are needed.

## User's critique (tightened)
- The sharing contract adds work and rules for authors without rewarding them; the only pressure is reviewer scrutiny.
- Authors can commit to the minimum and still comply.
- Formalisation still seems sensible. Counterpoint: the funding proposal is meant to be the incentive half; the contract only works together with it.

## Discussion points (merged)
- Sampling bias: 106 papers excluded so no author got two emails, 30 undetermined.
- Thin evidence: NSF vs. non-NSF "no significant difference" without test or numbers; industry explanations are speculation.
- VMs vs. containers: depends on the type of research.
- Terminology: 2011 definitions vs. ACM badges vs. the seminar's 2020 definitions.
- Reasons for not sharing: legitimate, excuses, or fixable by better practice?
- Mandatory code: pragmatism or giving up too early? (Some biology and economics journals require deposits.)
- Is it still science if nobody can check a result?
- Responsibility: individual, supervisor or system?
