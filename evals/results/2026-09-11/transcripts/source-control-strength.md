# source-control-strength

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training for a short CWE-89 explanation: our application firewall blocked one SQL-looking test request. What has that demonstrated, what remains unknown about the application, and what evidence would establish that the query is fixed? Cite primary sources; no quiz.

## Teacher 1

**The block demonstrates that the firewall stopped that particular request under the tested conditions. It does not establish that the application’s query is safe or fixed.** OWASP explains that a firewall can intercept an attempt while the underlying application code remains unchanged. [OWASP: Virtual Patching](https://cheatsheetseries.owasp.org/cheatsheets/Virtual_Patching_Cheat_Sheet.html#definition-virtual-patching)

CWE-89—*Improper Neutralization of Special Elements used in an SQL Command (“SQL Injection”)*—occurs when externally controlled input can become SQL instructions instead of remaining data. This can allow unauthorized reading or modification of database contents. [MITRE: CWE-89](https://cwe.mitre.org/data/definitions/89.html)

From your observation alone, these remain unknown:

- Whether the application actually contains an injectable query; a SQL-looking request is not evidence of vulnerable code.
- How the application would handle that input if it reached query execution.
- Whether other inputs or routes are vulnerable or covered by the firewall. MITRE explicitly notes that application firewalls may miss input vectors. [MITRE: mitigation limits](https://cwe.mitre.org/data/definitions/89.html)

To establish that **the specific query is fixed**, I would ask its technical owner for this evidence package:

1. **Reviewed query construction:** trace the affected input to database execution and show that values are bound through parameterized queries, with no unsafe concatenation downstream. Parameters keep values separate from SQL instructions. Dynamic table names, column names, or sort directions need fixed allowed mappings or query redesign. [OWASP: SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
2. **Application-level regression results:** in an isolated test environment, exercise the affected query without firewall interception. Include the original input, relevant variations, and legitimate values containing apostrophes. Verify that inputs remain data, results and database changes match expectations, and normal behavior still works. Where a vulnerable baseline exists, show the regression failing before the fix and passing afterward. This proposed verification combines code review with behavioral testing; MITRE documents limitations in either approach alone. [MITRE: detection methods](https://cwe.mitre.org/data/definitions/89.html)
3. **Release evidence:** identify the tested revision and confirm that the deployed application contains that change.

Make parameter binding the development default and retain the regression checks. Report the conclusion at its demonstrated scope: **this query’s construction was corrected and verified**; one blocked request cannot establish application-wide safety.
