# Behavioral evaluation

Read this file only when maintaining or evaluating the skill. The reusable prompts, environment conditions, follow-up scripts, and evaluator expectations are in [cases.json](../evals/cases.json).

## Run procedure

1. Validate the skill structure with the skill-creator validator when available. Structural validation is not a behavioral result.
2. Run each selected case in a fresh teaching-agent conversation with the candidate `SKILL.md`, only the case's initial prompt, and its environment constraints. Do not pass this rubric, expectations, other cases, prior outcomes, or suggested fixes to that agent. Independent subagents are appropriate when authorized; otherwise a human can run the cases in separate chats. Do not claim isolation if a reused conversation contains earlier cases.
3. Give learner follow-ups one turn at a time, after reading the actual question. Adapt the scripted misconception to that question without revealing evaluator expectations. Preserve the actual learner answer in the transcript. Never have the teaching agent generate both sides and call it an interactive test.
4. Retain prompts, learner replies, teacher responses, source URLs inspected, and relevant tool evidence in a separate evaluation directory. Do not write test output into learner progress or ordinary teaching context. For the unavailable-sources case, enforce the restriction rather than merely asking the teacher to imagine it; if tools cannot be disabled, explicitly prohibit browsing and alternative network access and inspect the trace for compliance, recording this as an instruction-based simulation.
5. Review the completed transcript against the case expectations and rubric below. Open the actual cited pages: a plausible-looking citation is not sufficient. Verify specific CVE/version claims against current primary advisories at evaluation time rather than a permanently hardcoded answer key. For code, use a small disposable local check if necessary to settle a meaningful correctness question; do not touch live systems.
6. Record pass, fail, or not-run per case, with concrete transcript evidence and limitations. After an observed failure, make a narrow correction and rerun the affected case plus directly related cases. Keep the original failure evidence. Do not report unexecuted cases or a static text inspection as passing behavior.

## Rubric

Score each applicable dimension as 0 (fails), 1 (partially meets), or 2 (meets). Mark genuinely inapplicable dimensions N/A, such as a full lesson's pacing on an acronym answer. Do not grade exact headings, matching phrases, or an arbitrary word count as evidence of learning quality.

| Dimension | Observable evidence for 2 |
| --- | --- |
| Factual accuracy | Correct identity, scope, mechanism, and remedy; versions and editions verified; uncertainty and invented scenarios labeled. |
| Source support | Factual claims supported by inspected authoritative sources; direct free links next to claims in every substantive teaching turn; no fabricated verification. |
| Teaching and action | One clear objective; understandable explanation; concrete remedy or handoff within the actual learner’s responsibilities, observable verification, and recurrence prevention; example and exercise match role, stack, and topic familiarity without assuming permissions. |
| Interaction | One question per turn with no answer leakage; evaluates actual reasoning; corrects a misconception using a different explanation and checks transfer; honors detours, skips, and mode changes. |
| Pacing and access | Whole lesson plausibly fits 3–5 minutes including code, thinking, and assigned media; free and self-contained; short questions get short answers. |
| Scope | Toy examples only; no unauthorized scanning, configuration changes, accounts, installations, or live-target activity. |

A case passes when all its expectations and applicable dimensions are met. A fabricated citation, unsupported material fix/version claim, answer revealed before the learner responds in interactive mode, or unauthorized external action is a failure regardless of the other scores. Minor style differences are not failures. Score evidence, not the teacher's own claim of compliance.

For pacing, record total teacher word count, code/media burden, and estimated thinking time across the entire exchange. As a rough review aid, 150–200 words per minute plus 15–30 seconds per question can expose an implausible estimate; this is an evaluator assumption, not a measured reading speed or a claim about learning effectiveness. Count retries and feedback. Research latency and time away from the conversation are excluded.

## Result record

Record the candidate skill hash, date, evaluator, tool availability, case IDs run, and transcript locations. For each case, include the rubric scores, decisive evidence, inspected source links, approximate learner time where applicable, and any remaining limitation. Distinguish simulated learner behavior from tests with a human: passing this suite demonstrates observed instruction-following on these cases, not guaranteed accuracy, retention, or general teaching effectiveness.

## Role adaptation checks

Run the four `role-*` written cases on the same CWE to compare the actual learning objectives, actions, verification, and exercises. Changing the title or vocabulary alone is insufficient adaptation. Check that the employee case follows the named colleague’s needs rather than the requester’s expertise, that the SOC case distinguishes professional experience from SQL familiarity, and that the operator case does not invent a product fix. Run `role-correction` as a real multi-turn exchange to check audience changes. These cases do not establish effectiveness for every role or topic.

## Source review checks

Use `source-claim-scope`, `source-conflicting-guidance`, and `source-control-strength` to test whether the teacher checks the scope and strength of actual evidence. Inspect both pages in the conflict case on the test date; a live discrepancy may have been corrected. Judge the answer against current source content, not an expected disagreement. Do not give the teacher the rubric or tell it which conclusion to reach. The existing `cve-branches`, `short-definition`, and `sources-unavailable` cases provide related regression coverage. A written instruction audit is not a substitute for executing these cases.

## Connected lessons and review checks

Run `connected-next` and `learning-path` across actual turns to distinguish proposing a topic from starting it and to verify mode/context preservation. Run `review-transfer` with the supplied learner recap and an actual answer to the new question; do not fabricate a completed earlier session. Check for meaningful scenario changes and no answer disclosure before the question. Use `review-missing-history` and `continue-unfinished` to test whether the agent invents learner history or incorrectly advances an unfinished lesson. A short factual follow-up should still pass `short-definition` without adding an unsolicited path or review.

## Hands-on checks

Run the four `hands-on-*` cases for code repair, analyst evidence, no-setup delivery, and skipping an exercise. Evaluate the actual task and success criteria, not the presence of a “lab” label. Check code against disposable fixtures when correctness depends on execution; record whether validation was run or only proposed. The exercise replaces existing practice time and must respect the same lesson/question limits. Do not count a learner's unexecuted claim as a measured test result.
