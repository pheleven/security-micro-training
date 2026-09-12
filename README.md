# Security Micro Training

A Codex skill for free, approachable, cited security lessons with an estimated 3–5 minute learner budget. Give it a CWE, CVE, OWASP category, MITRE ATT&CK item, or related topic to learn the mechanism, a concrete remedy, how to check it, and a prevention habit.

## Use

```text
$security-micro-training teach me CWE-89 interactively
$security-micro-training explain ATT&CK in a four-minute handout for a SOC analyst
$security-micro-training teach me CWE-88 with a tiny in-chat repair exercise
$security-micro-training review CWE-89 with a new scenario
$security-micro-training plan three short SQL injection lessons for a Python developer
```

Interactive teaching asks one question at a time and responds to your reasoning. Ask for a handout, “skip the quiz,” or “no code” to change delivery. Narrow factual questions get short cited answers. Role, experience, stack, and framework edition can be supplied in plain language.

Completed lessons may suggest one connected topic; “next” starts it. “Continue” during an unfinished exercise stays on the current lesson. Review uses the current conversation or your recap. Optional hands-on practice uses original toy artifacts and observable checks within the same time budget.

## Install

Clone this repository into a local checkout, then copy `SKILL.md`, `agents/`, `references/`, and `evals/` into a directory named `security-micro-training` under your agent's skill directory. Inspect an existing installation before replacing it. Keep only one active copy to avoid competing versions.

For Codex skill locations and discovery, see the [official skill documentation](https://learn.chatgpt.com/docs/build-skills). The root [SKILL.md](SKILL.md) is the entry point; the agent must be able to read its relative references. This project does not require its own service, account, package installation, or API key.

## Sources, cost, and scope

The skill requires inspected primary sources and clickable links in substantive teaching responses, including feedback. Time-sensitive CVE guidance is verified and dated. If sources cannot be verified, the agent must explain the limitation instead of improvising an uncited lesson. Links provide further learning; required instruction remains self-contained.

Learning resources must be freely accessible. The skill itself is [MIT licensed](LICENSE); the host agent may have its own usage charges. Third-party sources retain their own licenses. Lessons use original explanations and examples, rather than copied courses or transcripts.

Training does not authorize scans, exploitation, service installation, or changes to live systems. Progress stays in the conversation; there are no saved learner profiles, accounts, or background reminders. A lesson or toy check does not establish production security or mastery.

## Maintain and test

Run the dependency-free repository checks with Python 3.9 or later:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

These checks validate packaging, local references, and evaluation case structure. They do not establish factual accuracy or teaching behavior. Follow [the behavioral evaluation procedure](references/evaluation.md) to run the [25 cases](evals/cases.json) in fresh teaching conversations and inspect their actual source support. Record failures and reruns, candidate hashes, and limitations. Simulated learner results do not measure human retention.

The [release evaluation](evals/results/2026-09-11/evaluation-report.md) includes 25 passing behavioral cases, retained pre-fix failures, source-operation evidence, and explicit limitations. GitHub CI runs repository validation and validator tests; it does not run model-based teaching evaluations.
