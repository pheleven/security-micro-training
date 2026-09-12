# role-employee

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to write a complete four-minute CWE-89 lesson for my nontechnical payroll colleague. I’m a security engineer, but they don’t write code or administer systems.

## Teacher 1

**SQL injection in payroll — approximately four minutes**

The formal name is **CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')**. By the end, you can make a useful report about suspicious payroll-tool behavior and recognize what the technical team needs to verify. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

**0:00–1:20 · Understand the problem**

SQL is a language software uses to ask a database for information or change stored records. SQL injection happens when software mistakenly treats someone’s input as part of those instructions. An attacker may then change what the database does, potentially exposing, changing, or deleting information. [MITRE’s explanation and consequences](https://cwe.mitre.org/data/definitions/89.html)

*Fictional payroll example:* You search for an employee named `O'Neil`, and the payroll tool displays a database error.

The apostrophe belongs in the name. In poorly built software, that same character can interfere with database instructions. An attacker could deliberately exploit this confusion. The failed boundary is between **information someone enters** and **instructions the software executes**. Removing apostrophes from legitimate names can record incorrect information. [MITRE’s input-handling examples](https://cwe.mitre.org/data/definitions/89.html)

Treat this fictional error as a reason to report a concern; it does not establish that an attack occurred.

**1:20–2:25 · Take action and hand off the fix**

For that scenario, use this reporting approach:

- Stop the affected action instead of experimenting with unusual entries.
- Use your organization’s existing approved IT or security reporting channel.
- Record the tool, page, time, ordinary task, and what differed from the expected result. Describe the error without copying payroll records into an unapproved message.

A useful report could say: “At 10:15, the employee search showed a database error while I searched a surname containing an apostrophe. I stopped that search. Please advise how to continue.”

The technical owner’s remedy is to keep database instructions separate from entered values, commonly using **parameterized queries**. Think of a fixed instruction with a separate slot for the name: the supplied name stays information and cannot rewrite that instruction. Developers implement this protection. Reporting starts the handoff; it does not repair the software. [OWASP’s explanation of parameterized queries](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

**2:25–3:10 · Verify and prevent recurrence**

Ask the technical owner for a plain-language confirmation of what changed and the results of authorized checks: legitimate names work, and attempted instruction-like input stays data. A closed ticket or vanished error alone is insufficient evidence.

Your habit: report repeat failures accurately, and avoid inventing naming workarounds. Leave security testing to the authorized team.

**3:10–4:00 · Try and check**

*New fictional scenario:* An expense-search tool unexpectedly shows records outside your usual work. A coworker suggests trying special characters to investigate.

What should you do, and what should happen before the concern is considered resolved?

**Pause before checking.**

**Expected answer:** Stop exploring, report the unexpected results through the approved channel without spreading the records, and request the technical owner’s findings and verification. Unexpected results warrant investigation; they do not identify SQL injection by themselves.

**Remember: report the behavior accurately; let the technical owner diagnose, repair, and verify.**
