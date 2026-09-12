# Release evaluation: 11 September 2026

All **25 behavioral cases passed** on the final candidate. Six validator tests passed, and repository packaging, local links, evaluation schema, and the skill-creator structural validator passed. These are simulated learner results, not measured human learning or retention.

The final `SKILL.md` SHA-256 is `7d34d90838300f0555f571d987570b3c694723cd203fe8aa760be26869e7eece`. Runtime reference hashes, per-case scores, evidence, word counts, and transcript links are in [results.json](results.json). Every final teaching session used matching runtime files.

## What was exercised

- Written and interactive lessons, misconceptions, mode switches, and short cited answers.
- Developer, SOC analyst, operator, and nontechnical employee adaptation, including a mid-lesson audience correction.
- CVE branch/history guidance, framework-edition clarification, source conflicts, citation scope, mitigation limits, and unavailable browsing.
- Connected lessons, a three-lesson plan, fresh review scenarios, missing history, and continuing an unanswered exercise.
- Optional code repair, synthetic-log triage, no-setup argument-list repair, and skipping an exercise.

Fresh Codex CLI teaching sessions used `gpt-6-astra` and a read-only shell sandbox. They received the runtime skill, one learner request, and environmental constraints. They did not receive evaluator expectations. The root evaluator supplied each subsequent learner reply after reading the actual question and reviewed the resulting responses against the maintained rubric.

The source-unavailable case disabled browsing and prohibited alternate network access. Its trace shows only reading the skill, followed by a request for authoritative source text. Other factual responses contain direct citations; source operations were inspected and the reviewer checked cited primary material. [Tool evidence](tool-evidence.json) records source operations and command outcomes. Original JSONL/session evidence remains in the local evaluation archive; source-page bodies and unrelated session metadata are not distributed here.

## Corrections and execution evidence

An earlier candidate treated “complete four-minute lesson” as an interactive opening in the developer and SOC cases. The delivery rule now explicitly recognizes a complete lesson as written unless the learner requests interactive delivery. The final full-suite run includes both corrected cases. The [earlier failure responses](prior-failures.md) remain available instead of being overwritten.

Usage limits interrupted some initial or follow-up attempts. Work resumed after the reported resets, retaining the interruption records locally. All 25 final case results include completed responses; no failed tool call or unexecuted case counts as a behavioral pass.

The written SQL lesson's trace records four successful assertions against an in-memory fixture, including its vulnerable baseline. The reviewer additionally ran [nine assertions](code_checks.py) for the hands-on lookup/insertion repairs, exact invoice-note preservation, and the skipped-exercise repair. See [code results](code-results.json). These establish the checked toy behavior only.

## Timing and limits

Complete individual lessons in this run contain approximately 338–521 teacher words, including code tokens and excluding citation URLs. The two connected lessons contain 471 and 456 words and receive separate four-minute estimates. Code inspection, exercise thinking, and retries were considered alongside reading; the examples plausibly fit their stated 3–5 minute budgets. Skips shorten delivery. Research, tool latency, and time away are excluded. These are estimates, not measured completion times.

Clarification, learning-path startup, and “continue” tests intentionally stop at their specified checkpoint. They do not establish the quality of an entire later lesson. One pass per case does not establish a failure rate, universal factual accuracy, detection coverage, production security, or long-term retention. The skill still requires source verification on future invocations, especially for changing CVE guidance.
