# Assignment Review — Domain Checklists

Use only sections relevant to the user's assignment and its stated rubric. These are **inspection questions**, not templates for completing missing work. Report findings as location-based suggestions; never write solutions, corrected paragraphs, or replacement code.

## 1. Mathematics and statistics

- Does the student define variables, parameter domains, assumptions, and sample size?
- Is each inference justified by a known identity, distribution property, theorem, or algebraic operation?
- Do transformations preserve inequalities, signs, limits, absolute values, and domains?
- For MOM/MLE: were the objective, likelihood support, maximization constraints, parameterization, and endpoint conditions considered? Is the estimator's expression consistent with the preceding steps?
- For simulation: are distributions, sample sizes, seeds, number of trials, and comparison metrics consistent with the question? Do numerical conclusions match the shown output?
- For hypothesis tests: do null/alternative hypotheses, test selection, assumptions, statistic, one/two-sided tail, p-value, significance level and decision agree?
- For Mann–Whitney / Wilcoxon rank-sum: look at independent groups, rank ties, sample sizes, U/W definition, exact vs approximate p-value, and interpretation as distributional comparison rather than an automatic median test.
- Are reported estimators, confidence intervals, errors, and conclusions physically/statistically plausible?

**Feedback pattern:** “第 2 题公式 (3) 到 (4) 的变形条件需要核对；这里使用的性质是否要求某个量为正？请回查定义域并逐项检验。” Do not complete the chain.

## 2. Programming, scraping, and data tasks

- Is the implementation aligned with the task's specified language, modules, data source, output, and restrictions?
- Are input types, boundaries, missing values, empty results, duplicate data and errors handled?
- Do regex patterns match the intended structure, avoid accidental overcapture, and address dynamic HTML limitations where relevant?
- For Selenium: is page readiness checked, are selectors credible, is crawl frequency responsible, and are exceptions/empty states accounted for?
- For SQLite/data storage: verify schema types, insert/replace semantics, consistent keys, transactions, and how results are verified.
- Can functions be explained? Look for unused parameters, unexpected side effects, hidden global state, missing return values and wrong variable scope.
- Are claimed outputs consistent with actual code and logs?
- Are comments and naming understandable without changing them automatically?

**Execution rule:** Unless the user asks for safe execution, label findings “静态检查” and avoid running downloaded or unknown scripts. If execution is explicitly authorized and safe, report exactly what ran and what remains untested.

## 3. Deep learning / experimental coursework

- Are dataset names/versions, splits, labels, preprocessing, train/val/test boundaries and seeds clear?
- Are training settings (backbone, optimizer, schedule, epochs, batch, resolution, augmentation) consistent between methods?
- Do metrics have correct direction and interpretation (e.g. mAP50 vs mAP50–95, mIoU, accuracy, precision/recall)?
- Are baseline and improved model under comparable protocols? Are differences and units calculated correctly?
- Are plots/tables numbered, labeled and supported by actual experiments? Are results and speculation separated?
- Is reproducibility information sufficient **if the rubric requires it**?
- Avoid suggesting new experiments as if they were mandatory unless the rubric actually asks for them.

## 4. Written assignments (Chinese / English)

- **English:** subject–verb agreement, tense, articles, prepositions, number, parallel structure, pronoun antecedents, punctuation, capitalization, academic terminology.
- **Chinese:** ambiguous referents, logical connectives, missing subjects, punctuation consistency, technical term consistency, repeated or contradictory claims.
- **Structure:** does each paragraph serve the prompt, connect premise to evidence, and avoid unsupported conclusion?
- **Referencing:** are in-text citations matched to the bibliography, and are borrowed claims and figures attributed where the assignment requires citations?
- Distinguish an actual grammar error from optional stylistic preference. **Do not offer replacement sentences** or “polished version”; ask the student to reconsider the grammatical relation or concept.

## 5. Presentation, notebook, and report submission

- Required page/slide count, section order, filename, duration, team/individual constraints and submission format.
- Figures: readable axes/units, legends, captions, image quality, source attribution.
- Slides: content density, consistency, whether essential steps can be explained within the allotted time.
- Notebooks: cell order, code-output consistency, hidden dependencies, fixed paths, external data availability.
- Tables: units, denominator, rounding, totals, footnotes and interpretation consistency.
- Screenshots/PDF: visible text, complete pages, legible equations and absence of accidental cropping.

## 6. Evidence and integrity

- Do not claim plagiarism or AI-generated authorship from style alone; automated detection is unreliable.
- Identify verifiable sourcing problems (missing citation, quotation mismatch, figure without attribution) and suggest verification.
- Do not provide new references or substantive claims to insert automatically.
- If teacher-specific policy forbids AI assistance, remind the user to follow that rule; deliver feedback only if compatible.
