# Tiny hands-on exercises

Use this reference only when hands-on practice is requested. The task should let the learner change or decide something concrete and check the result within the lesson's existing 3–5 minutes. Reserve roughly 60–90 seconds for doing and checking it; shorten the explanation accordingly. A separate requested exercise gets its own stated budget.

## Build one task

- Choose one skill aligned with the objective: repair a short query, construct a safe argument list under a stated parser contract, review a few configuration lines, or triage a few synthetic log entries. Match the learner's actual role and constraints. Code execution is optional; an in-chat edit or decision is a valid hands-on task.
- Supply a tiny original artifact and all context needed to reason about it. Label toy code, fictional tools, and synthetic data. State consequential assumptions, such as whether a utility supports an option terminator, who controls a path mapping, or which events a log records. Verify real API and command semantics against inspected primary documentation.
- Give one clear action and observable success criteria before the attempt. For code, include ordinary behavior that must keep working and one adverse or boundary input that must be handled correctly. For evidence review, define the decision and the evidence needed to justify it while preserving uncertainty. Criteria describe the outcome without revealing the repair or triage answer.
- Keep execution, when requested, disposable and local with supplied fixture data, for example an in-memory database. No network calls, credentials, real logs, package downloads, service setup, or production mutations belong in the required exercise. If the learner lacks a tool, use the in-chat alternative. Never silently execute a deliberately vulnerable example or learner-supplied code; a request to learn or inspect is not a request to run it.

## Coach and verify

In interactive mode, present the task and criteria, ask for one edit or decision, and wait. Do not place the repaired code, correct verdict, or answer key above or below the question. Assess the submitted reasoning or artifact; after a partial answer, explain the precise gap and use a different small case for the retry. Count the task and retry within the existing three-round maximum. Honor a skip or written-mode request immediately.

In written mode, put a clear “Pause before checking” cue between the task and a compact worked answer with rationale. Include a way to compare the learner's result to the criteria. No external site or runner is required to see the answer.

Distinguish an inspected solution, a proposed test, a learner-reported result, and a test the agent actually ran. Report execution only when tool evidence exists. A toy test supports a specific behavior under its stated assumptions; it does not establish production security, complete detection coverage, or mastery. Close with the mechanism-specific action and prevention habit. Cite factual feedback and give the learner direct free sources for further study, following `SKILL.md`.
