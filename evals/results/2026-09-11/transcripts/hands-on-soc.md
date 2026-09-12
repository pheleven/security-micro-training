# hands-on-soc

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training for a complete four-minute CWE-89 hands-on lesson for a SOC analyst. Give me a tiny synthetic log exercise and an answer I can check myself. I cannot access application code.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’)**
Estimated time: **four minutes**, including the exercise. By the end, you can write an evidence-based SQL injection triage note without application-code access.

**0:00–0:50 — Understand the boundary**

SQL injection happens when an application lets externally controlled input change a database command’s meaning. For example, a search value intended as text becomes part of the query’s instructions. Successful exploitation can expose or change data. The failed boundary is **user data becoming database instructions**. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

In a vulnerable query, `' OR '1'='1` can introduce an always-true condition. Seeing that text in a request establishes a suspicious signal; it does not show how the application processed it.

**0:50–1:50 — Act within your role**

Use this proposed triage workflow:

- Preserve the timestamp, request ID, endpoint, suspicious parameter, and observed outcome.
- Correlate the request with application errors and available database audit events. Request missing evidence from the application or database owner.
- Record separately what you observed, what you suspect, and what remains unknown.

Application context and database audit trails can supplement web logs; interaction identifiers help connect related events. [OWASP Logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#event-attributes)

Route the suspected weakness to the application owner with a concrete remedy: **parameterized queries with bound values**, keeping input separate from SQL instructions. Ask for review evidence covering the affected query path and regression results showing ordinary searches still work while SQL-like input cannot broaden results. These are proposed acceptance checks; a closed ticket alone is insufficient evidence. [OWASP SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

**1:50–2:30 — Reduce recurrence**

Propose monitoring suspicious input alongside correlated application errors or unusual outcomes. Treat this as a detection hypothesis to validate, not complete coverage: the evidence below cannot establish execution from an HTTP status alone.

Ask owners to retain regression checks and limit the application’s database privileges to necessary operations. Restricted privileges reduce potential impact; they do not repair unsafe query construction. [MITRE mitigations](https://cwe.mitre.org/data/definitions/89.html)

**2:30–4:00 — Hands-on: write a triage note**

Original synthetic logs; no tools needed. All requests share one fictional client. `q` is decoded input; `bytes` is response-body size. Matching `rid` values identify the same request.

```text
10:00:00 web rid=a /search q="pencil"        status=200 bytes=820
10:00:04 web rid=b /search q="' OR '1'='1"   status=500 bytes=120
10:00:04 app rid=b database_error="SQL syntax error"
10:00:08 web rid=c /search q="' OR '1'='1"   status=200 bytes=910
```

Write two sentences identifying the suspicious requests, whether success is established, and your next evidence check. Success means citing specific evidence while preserving uncertainty.

Transfer: If the gateway explicitly recorded “blocked before forwarding” for `c`, what would change?

**Pause before checking.**

**Check your answer:** “Requests `b` and `c` suggest SQL injection probing; `b` also has a correlated database syntax error. Successful exploitation remains unconfirmed: request application/database evidence for `c` to determine what executed and whether unauthorized data was returned.”

The error strengthens concern, but neither it nor `c`’s status and size proves exploitation. In the transfer case, the gateway records prevention of that request reaching the application; it does not demonstrate that the underlying weakness is fixed.

**Rule of thumb: correlate the signal, qualify the conclusion, and hand off a verifiable repair.**
