# role-soc

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute CWE-89 lesson. I’m an experienced SOC analyst, but SQL is new to me. I can inspect application and proxy logs; I don’t own the code.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’).** Estimated time: four minutes, including the exercise. By the end, you can turn suspicious request evidence into a justified triage decision and a verifiable remediation handoff. [CWE-89](https://cwe.mitre.org/data/definitions/89.html)

SQL is a language applications use to query databases. In this original toy query, `SELECT` retrieves a column, `FROM` names the table, and `WHERE` filters rows:

```sql
SELECT title FROM tickets WHERE owner = 'alex';
```

Single quotes delimit text. Suppose the application builds that command by pasting user input between quotes. Input containing `alex' OR '1'='1` would produce:

```sql
SELECT title FROM tickets WHERE owner = 'alex' OR '1'='1';
```

The added condition is always true, so this toy query selects every ticket’s title. **The failed boundary is between input data and database instructions.** Depending on the vulnerable operation and permissions, SQL injection can expose, modify, or delete data. [CWE explanation and examples](https://cwe.mitre.org/data/definitions/89.html)

For your SOC workflow, use this proposed sequence:

- **Correlate:** Connect the suspicious proxy request to application events using a request identifier, timestamp, endpoint, and user identity where available.
- **Corroborate:** Look for database syntax errors and unexpected application outcomes. Suspicious input shows what arrived; it does not establish what the database executed. An apostrophe also occurs in legitimate names.
- **Handoff:** Give the application owner the affected route and parameter, correlated events, observed outcome, and explicit uncertainty. Request database audit evidence through its owner if application logs cannot resolve the outcome.

OWASP recommends recording application errors, identities, outcomes, and interaction identifiers because application context adds information beyond infrastructure logs. [Logging guidance](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

The owner’s concrete remedy is **parameterized queries**: define the SQL structure first, then bind input separately as a value. Conceptually:

```text
SQL template: SELECT title FROM tickets WHERE owner = ?
Bound value: the supplied owner text
```

Here, `?` is a placeholder, not text substitution. Proper binding keeps even SQL-looking input as data. Request evidence that the affected query uses binding, plus owner-run regression checks in a test environment showing that quoted and SQL-looking values retain literal meaning and normal searches still work. A closed ticket alone supplies neither check. [OWASP parameterization guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

For recurrence prevention, request parameterization checks in code review. Maintain correlated application logging and periodically verify collection works; missing events limit conclusions. [OWASP logging verification](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#verification)

Now consider these **synthetic logs from a different feature**:

```text
proxy rid=R8 route=/directory input="O'Brien" status=500
app   rid=R8 event=database_syntax_error

proxy rid=R9 route=/directory input="x' OR '1'='1" status=200
app   rid=R9 event=request_complete
```

What would you report, and what evidence would you seek next?

**Pause before checking.**

Expected answer: report suspected unsafe query handling and a possible injection attempt, with impact unconfirmed. R8 suggests quote-handling trouble; R9 does not record returned data or query behavior. Seek correlated application outcome details and owner-provided query or audit evidence. This distinction follows OWASP’s separate treatment of HTTP status, action outcome, and analytical confidence. [Event attributes](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html#event-attributes)

**Follow suspicious input to an observed outcome; verify the fix at the data-to-command boundary.**
