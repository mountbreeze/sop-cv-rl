# 07 — Quality assurance, cross-document integrity and anti-template audit

## Seven gates
| Gate | Test | Action on failure |
| --- | --- | --- |
| 1. Prompt | Every question answered? Separate titles required? Correct form? | Split/rewrite |
| 2. Evidence | Can every concrete act, number and outcome be traced? | Delete or mark internally as unverified |
| 3. Role | Did intern/research assistant actually have this authority? | Downgrade action verb to observed role |
| 4. Reasoning | Is there real obstacle → method change → evidence → limitation? | Replace broad claim with specific act |
| 5. Fit | Current official programme details verified? Real action linked? | Remove resource or investigate |
| 6. Voice | AI-ish rhetorical Qs / repeated reflections / three-item lists? | Edit sentence rhythm and logic |
| 7. Portfolio | CV/PS/RL dates, scale, employers, positions, achievements consistent? | Reconcile against evidence ledger |

## Anti-AI line edit scan
Find repeated `I learned`, `I realised`, `This experience taught me`, `One question`, `not only ... but also`, `passion`, `dynamic landscape`, `holistic`, `impact`, `transformative`, `unique opportunity`, `prestigious`, `world-class`. None is universally forbidden, but recurring reliance indicates weak specificity.

Check for:
- **Rhetorical self-interview**: “Why was growth so low?” → “The projection still depended on unverified market-share assumptions.”
- **Triadic chains**: “analyze, communicate and collaborate” → name causal action.
- **Mechanical transitions**: “Furthermore, another internship…” → connect through upgraded analytical object.
- **Empty conclusions**: If final sentence adds nothing, delete it.
- **Fake insight**: “I realized data mattered” → actual data-definition change.
- **School praise**: “unparalleled teaching at a world-class school” → exact resource, constraint, action.

## Cross-file consistency ledger
`experience_id | CV verb/metric | essay verb/metric | recommendation observed claim | dates | evidence link | consistency status`.
Cross-check awards, GPA, class rank, company names, issuer count vs completed deals, model output vs business adoption, research proposal vs published finding.

## Length & layout
Use script for counts; respect **hard maxima** and requested target density, not blind filling. Run layout QA on final Word/PDF: orphaned headings, unexplained whitespace, table row heights, CV section position, readable font, repeated bullets, truncated footer, application title mismatches.

## Adversarial review
Ask:
1. Can applicant defend every phrase in interview?
2. Could actual recommender truthfully claim to have witnessed it?
3. Is this identical logic being sent to three unlike programmes?
4. Is a business claim being passed off as a causal result?
5. Does the paragraph improve if one abstract conclusion is removed?
6. Did we cite a course that no longer exists?
7. Did we publicly expose student, client or unpublished research detail?

## Deliverable checklist
- Editable artifact if requested; PDF only when asked/required.
- Correct exact programme and intake.
- Prompt-answer compliance and actual word/character counts.
- Fact-check and official-source status (what remains unverified).
- One last independent AI-style audit with concrete substitutions.
- No leaked source files or third-party identity/contacts in public Git.
