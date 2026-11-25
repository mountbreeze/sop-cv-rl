# 01 — Intake, evidence ledger, consent & privacy

## Inputs / intake hierarchy
Read in this order: (1) exact current application prompts and official programme page; (2) dated CV/resume + transcript; (3) written internship/project/research details; (4) brainstorm interview and career goals; (5) recommendation evidence provided by recommenders; (6) older essays as style context, never automatically as fact. When official source and user-supplied old prompt conflict, surface that conflict.

## Source-of-truth matrix

| Field | Example | Status | Source | Allowed copy |
| --- | --- | --- | --- | --- |
| Internship role and dates | Analyst intern, months | Verified / self-reported / unverified | CV + contract if given | CV, SOP, RL |
| Analysis performed | Built comparison table | Confirmed / proposed | Student interview | CV/SOP |
| Quantitative metric | 18 firms researched | Confirmed / estimated / unknown | work log | Only if confirmed |
| Business outcome | Memo discussed by team | Observed / uncertain | supervisor feedback | Conservative phrasing |
| Faculty comment | Professor questioned assumption | Referee observed / student recalled | referee form | RL only after confirmation |
| Programme course | Module name | Current official / historical / unchecked | URL + access date | Only current official |

Keep claim-level audit: `claim_id, exact_claim, source_document, page_or_quote, timestamp, verification_status, consent_status, used_in, owner`. Flag all contradictory numeric/date details explicitly. Do not upgrade an applicant’s assertion to an independent supervisor observation.

## Evidence levels for claimed impact

- L0: plausible scenario for brainstorm, NOT applicant fact.
- L1: applicant did a described task.
- L2: a tangible work product existed (model, slides, memo, cleaning script).
- L3: others reviewed or discussed the work.
- L4: an authorized person/team adopted a recommendation.
- L5: measured attributable business / research impact supported by reliable records.

Phrase at the highest **substantiated** level only. `Assisted on 20+ bond projects` is not `executed 20+ bond issuances`. Model sophistication and statistical significance also do not prove commercial impact.

## Honest story-enhancement protocol

If user says “创作/扩写/给实习编个故事”, interpret as **realistic story mining** not fabricating. Present: (i) supported rewrite usable now; (ii) optional probing hypothesis clearly marked `【故事假设，需确认】`; (iii) 3–6 targeted questions. Unknown values remain `【需要本人确认】` in internal materials, never silently become facts in final deliverables. Quantitative placeholders belong only in drafts for verification, not polished applicant-facing assertions.

Interview details to probe: precise assignment, source of data, initial decision framing, why method failed, constraints, student’s actual independent actions, who gave feedback, concrete output and how used, uncertainty or alternative interpretation.

## Privacy
Repository is public. Do not commit students’ names, emails, phone numbers, grades, signatures, raw letters, CVs, unpublished research, customer information, or anonymization-reversible narratives without specific consent. All examples here are generalized method patterns; student-specific files stay in separate authorized private storage. Do not reuse confidential details across applicants. Preserve applicant/recommender control over final submissions.
