# 06 — Programme research, prompt parsing & differentiation

## Authoritative order
1. Actual online application form and the specific **intake-year** programme requirements.
2. Official university/department page (curriculum, optional modules, faculty, research centres, projects).
3. Official handbook/FAQ.
4. Older sample essays, forums or archived pages only as context. Never substitute them for current requirements.

Capture `school | programme exact title | intake | official link | retrieved_date | prompt exact text | question_count | max_words/characters | whether spaces counted | attachment/format | special title requirements | evidence link`.

## Parse the exact task before writing
- SOP/general PS vs structured Q&A writing sample: one narrative essay **cannot** replace multiple separately titled answers.
- `up to 4,000 characters` ≠ `4,000 words`.
- `around 750 words` plus independent `max 1800 characters` subanswers demands checking **both** global and question-specific constraints.
- Essay 1 (career + why programme), Essay 2 (challenge), Scholarship Essay (achievements/values): three different evaluation functions, not cosmetic variations.
- Interview: 1-minute individual answer and subsequent group discussion are different deliverables.

## Why School research matrix
For each proposed resource, document:
1. exact verified name and current availability;
2. applicant’s already evidenced question/experience;
3. gap;
4. specific action student realistically intends to take;
5. post-degree application.
Remove course name drops with no causal connection. Do not claim exclusive access to modules/faculty when programme description does not support it.

## Multiple school strategy
Keep a fixed **fact ledger** and flexible **argument ledger**. A finance essay may focus underwriting and valuation; an economics essay emphasizes transmission/identification and interpretation; an operations essay emphasizes process and coordination; an AI essay prioritizes implementation governance and measurement. Use overlapping factual scenes judiciously while changing question, stakes, evidence and goal, never retroactively changing events.

## Length measurement
For word-limited English: count whitespace-separated words for a transparent estimate but recognize portal can count hyphens differently. For character-limited: count Unicode characters, including spaces and newlines unless portal specifies otherwise; do not target exactly the limit if portal behavior is unknown. Use `python scripts/check_limits.py path.txt --max-words 500` etc.

## Specific recurring historical examples — CHECK AGAIN before reuse
Past prompts in this project included KCL Corporate Finance 4,000-character statement; KCL PEEM a structured writing sample with clearly separated titled answers and subquestion character limits; NTU MiM two 400-word essays and a 400-word scholarship prompt; HKU Economics around 1200-word requested PS; HKUST Global Operations and Family Office SOP requested around 850 words; CUHK ISTM 500 words; NTU Enterprise AI around 600 words. These are **historical task specifications**, not current verified school policies. Exact programme names/requirements may change.
