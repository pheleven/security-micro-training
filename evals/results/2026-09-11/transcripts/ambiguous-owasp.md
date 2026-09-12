# ambiguous-owasp

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me OWASP A01.

## Teacher 1

Do you mean [OWASP Top 10:2025 — A01: Broken Access Control](https://top10.owasp.org/2025/A01_2025-Broken_Access_Control/), or a different OWASP project or edition?


## Learner 2

OWASP Top 10 for web applications, 2021.

## Teacher 2

**OWASP Top 10:2021 — A01: Broken Access Control.** This interactive lesson takes about **4 minutes**. By the end, you’ll be able to identify a missing permission check that exposes another person’s records—one slice of this broad category.

Access control determines what someone is allowed to view or change. When it fails, an application can expose information or allow actions outside that person’s permissions. [OWASP’s 2021 explanation](https://top10.owasp.org/2021/A01_2021-Broken_Access_Control/#description)

**Fictional scenario:** A customer portal lets Maya view her own invoice at `/invoices/1042`. She changes the number to `1043`, and the portal returns another customer’s invoice. The server checks that Maya is logged in, then retrieves whichever invoice number she requests.

What additional decision should the server make before returning the invoice, and why isn’t checking that Maya is logged in enough?
