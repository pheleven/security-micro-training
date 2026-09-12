# role-operator

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute CWE-89 lesson. I administer a vendor-managed reporting application; I cannot change its source code. No vendor or product version has been supplied.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated time: four minutes, including the exercise. By the end, you can choose an appropriate vendor remediation path and identify evidence needed to close it.

**0:00–1:20 — Understand the failure.** SQL is the language an application uses to query its database. SQL injection occurs when externally controlled input becomes part of the database’s instructions instead of remaining data. Depending on permissions and the vulnerable query, this can expose, change, or delete information. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

*Original fictional scenario:* Your reporting application accepts a customer-name filter. Its intended job is “retrieve records matching this name.” If the application builds the database command by joining text with that filter, specially structured input could change the command’s meaning and retrieve additional records. The failed boundary is between the supplied filter and executable database instructions.

The vendor’s usual code remedy is **parameterized queries**: define the command separately, then supply filter values as data. Your responsibility is to coordinate and verify the supported remedy. [OWASP’s parameterized-query explanation](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

**1:20–2:25 — Choose an actionable response.** No product or version was supplied, so this lesson cannot establish whether your deployment is affected or name an available patch. CWE-89 describes a weakness category.

Use this proposed maintenance workflow:

1. Record the deployed product, running build, reporting components, and enabled features using supported administrative information or vendor confirmation.
2. Ask the vendor whether that exact deployment is affected, which advisory applies, and what supported fix or temporary mitigation addresses it.
3. Request evidence that the remedy covers the affected reporting path, including vendor regression-test results. Arrange implementation through the responsible maintenance owner.
4. Verify the running build against the applicable advisory, or obtain deployment-specific confirmation for a vendor-hosted service. Check representative reports, filters, exports, and expected user access.

Successful reports establish service continuity; they do not alone demonstrate that injection is fixed. Keep the advisory, deployment evidence, and relevant security-validation results together.

**2:25–3:10 — Limit damage and recurrence.** Ask the vendor or database owner to confirm that the application account has only the permissions and data access it needs. Read-only access can limit damage but still permits disclosure of accessible records. [OWASP’s least-privilege guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#least-privilege)

An application firewall may provide temporary protection when source changes are unavailable. It can miss attack paths or reject legitimate requests, so treat it as mitigation with a review date. Maintain deployment inventory and review applicable vendor advisories. [MITRE’s mitigation guidance](https://cwe.mitre.org/data/definitions/89.html)

**3:10–4:00 — Try and check.** *Fictional exercise:* The vendor enables a firewall rule. Normal exports work, and the reporting database account is read-only. The ticket says “SQL injection fixed.” Should you close it as permanently remediated?

**Pause before checking.**

**Expected answer:** No. Record the mitigation, request deployment-specific fix and validation evidence, and retain follow-up ownership. Firewall coverage and read-only permissions do not establish that unsafe query construction was corrected.

**Remember: verify the vendor’s remedy in your deployment before calling the weakness fixed.**
