# review-transfer

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training for an interactive review. Earlier I read a lesson about CWE-89 and parameter binding; its example was a product search. I’m a Python developer. Give me a different scenario to reason through.

## Teacher 1

Let’s review **[CWE-89: Improper Neutralization of Special Elements used in an SQL Command (“SQL Injection”)](https://cwe.mitre.org/data/definitions/89.html)**. Estimated total: **4 minutes**. Your objective is to assess and repair SQL construction in a Python background job.

**Original scenario:** A support application lets users save an email address using parameter binding. Later, a nightly job reads that address and archives matching tickets. Assume `db` is a Python `sqlite3` connection and the user exists.

```python
email = db.execute(
    "SELECT email FROM users WHERE id = ?", (user_id,)
).fetchone()[0]

db.execute(
    f"UPDATE tickets SET archived = 1 WHERE sender_email = '{email}'"
)
```

A teammate says: “The address was saved with parameter binding and now comes from our database, so this job is safe.” The API reference for this exercise is [Python’s SQLite documentation](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders); no setup is needed.

**Would you approve this code as safe from SQL injection? Explain your reasoning and show any change you would require.**


## Learner 2

I would approve it. The earlier parameter binding cleaned the email, and retrieving it from our own database should make it trustworthy.

## Teacher 2

The earlier save did use the right mechanism, but **parameter binding doesn’t clean the email or make it permanently trustworthy**. It keeps the value separate from SQL instructions for that particular execution. Characters such as `'` remain in stored text. [Python’s SQLite examples](https://docs.python.org/3/library/sqlite3.html#tutorial) demonstrate this preservation.

When the nightly job inserts that stored value into an f-string, it creates a new opportunity for data to become SQL syntax. Coming from your database doesn’t remove that risk. [CWE-89](https://cwe.mitre.org/data/definitions/89.html) explicitly discusses unsafe reuse of previously stored data.

The job needs binding again:

```python
db.execute(
    "UPDATE tickets SET archived = 1 WHERE sender_email = ?",
    (email,),
)
```

Here, the SQL structure stays fixed and `email` is supplied separately. [Python binding reference](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

Let’s check that distinction with a **new fictional regression-test scenario**. A billing job copies a saved customer note onto invoice 42. The note contains the literal text `Approved'; --`, originally stored using binding.

```python
db.execute(
    "UPDATE invoices SET note = ? WHERE id = ?",
    (saved_note, 42),
)
```

Assume invoices 42 and 43 both exist. **What should the test assert about the exact note saved on invoice 42 and whether invoice 43 changes—and why?**


## Learner 3

Invoice 42 should contain exactly the original string Approved'; --, including the quote and comment-looking characters. Invoice 43 should remain unchanged. Both the note and ID are bound values, so the note cannot end the statement or remove the WHERE condition.

## Teacher 3

Correct. Invoice 42 receives exactly `Approved'; --`, and invoice 43 stays unchanged. The placeholders keep both values separate from SQL syntax, so the note’s characters cannot alter the `WHERE` clause. [Python’s binding documentation](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

Those two assertions make a useful regression check: preserve the intended text and leave unrelated rows unchanged.

Your answer demonstrates the distinction that needed correction: binding protects an execution; it doesn’t permanently clean stored data. During code review, inspect each SQL execution—including background jobs—for values interpolated through f-strings or concatenation.

**Bind data values every time you execute SQL, even when they came from your own database.**
