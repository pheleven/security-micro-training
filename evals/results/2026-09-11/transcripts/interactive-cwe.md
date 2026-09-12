# interactive-cwe

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me CWE-89 interactively. I can read basic Python.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated total: **4 minutes**, across a few short exchanges. By the end, you can repair a Python database lookup so user input stays data.

SQL injection happens when user input becomes part of a database command’s instructions. This can let someone read or change data beyond what the application intended. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Here’s an original toy example using Python’s `sqlite3`. Imagine a book search intended to return books with exactly the entered title:

```python
title = input("Book title: ")
query = f"SELECT * FROM books WHERE title = '{title}'"
cursor.execute(query)
```

The `WHERE` condition selects matching rows. Python’s documentation warns that assembling SQL with string operations allows input to alter the query. [Python documentation](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

Suppose the entered title is:

```text
anything' OR '1'='1
```

**After substituting that text into the f-string, would the query return only an exact title match or every book—and why?**


## Learner 2

Every book, because the OR part is true. I would fix it by deleting single quotes from the title before adding it to the SQL string.

## Teacher 2

Correct: the `OR` condition is true, so every book matches.

Deleting single quotes would also damage legitimate titles like `Alice's Adventures in Wonderland`. Blocking selected characters is not a dependable general defense against SQL injection; the underlying problem is assembling SQL instructions from user input. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Use a **parameterized query** instead:

```python
cursor.execute(
    "SELECT * FROM books WHERE title = ?",
    (title,),
)
```

The `?` marks a data value. The value travels separately from the SQL instructions, so its contents cannot become extra query logic. `(title,)` is a one-item tuple supplying that value. [Python’s parameter binding documentation](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

Let’s check that distinction in a new toy scenario. A fictional author table contains only `O'Brien` and `Rivera`:

```python
author = "nobody' OR '1'='1"
cursor.execute(
    "SELECT * FROM authors WHERE name = ?",
    (author,),
)
```

**For a regression test of this query, would you expect zero rows or both authors—and why?**


## Learner 3

Zero rows. The entire string is the bound name value, and neither stored author has that exact name. The OR text cannot alter the condition.

## Teacher 3

Correct. The bound value is treated as data, so the `OR` text cannot change the query’s condition. Neither author matches that complete string. [Python documentation](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

To verify this fix in the toy example, keep regression checks for:

- `O'Brien` → exactly that author, preserving the apostrophe.
- `nobody` → zero rows.
- `nobody' OR '1'='1` → zero rows.

For prevention, make parameter binding your default for SQL values. During code review, flag f-strings and concatenation that insert input into SQL commands. Separating data from instructions addresses the underlying weakness. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

You correctly explained both the vulnerable query and why binding prevents that behavior. Applying the pattern yourself is the next thing to practice.

**Keep SQL structure fixed; pass values separately.**
