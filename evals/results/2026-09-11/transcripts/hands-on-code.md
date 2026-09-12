# hands-on-code

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me CWE-89 interactively with a tiny hands-on Python sqlite3 repair exercise. I have Python already. Keep the whole lesson under five minutes.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’).** Estimated total: **4 minutes**, including your repair and our feedback. Your objective: repair a Python query so user input stays data.

SQL injection happens when input becomes part of SQL instructions and changes what the database does. A lookup intended to return one person’s record can return other records instead. The failed assumption is that inserting text between quotes makes it safe. [CWE-89](https://cwe.mitre.org/data/definitions/89.html)

This original toy exercise uses fictional names and an in-memory database. Python’s `":memory:"` setting keeps the database off disk. [Python documentation](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)

Spend about **60–90 seconds** repairing only the `return` statement. You can edit it here in chat, or save the snippet as `repair.py` and run `python repair.py` locally after editing.

```python
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE people (name TEXT)")
db.execute("INSERT INTO people VALUES ('Ada'), ('O''Brien')")

def lookup(name):
    # Repair this statement:
    return db.execute(
        f"SELECT name FROM people WHERE name = '{name}'"
    ).fetchall()

assert lookup("Ada") == [("Ada",)]
assert lookup("' OR '1'='1") == []
assert lookup("O'Brien") == [("O'Brien",)]
print("PASS: all three checks")
db.close()
```

Success means the ordinary lookup still works, the SQL-shaped input matches nothing, and a legitimate apostrophe works unchanged. All three assertions must pass; suppressing errors doesn’t satisfy the exercise.

**What replacement `return` statement would you use, and why would it keep the input from changing the query?**


## Learner 2

I would escape single quotes with a backslash in name first, then keep the formatted query. That should stop the quote ending the SQL string.

## Teacher 2

You correctly spotted that a quote can end the SQL string. The gap is SQLite’s syntax: **backslashes do not escape SQL quotes**, so that repair leaves the problem. [SQLite string literals](https://www.sqlite.org/lang_expr.html#literal_values_constants_)

Use a bound parameter:

```python
return db.execute(
    "SELECT name FROM people WHERE name = ?", (name,)
).fetchall()
```

The SQL instructions stay fixed; `name` is supplied separately as a value. Leave `?` unquoted, and keep the comma in `(name,)` to create a one-item tuple. [Python parameter binding](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders)

Try that replacement with the original assertions. The expected result is `PASS: all three checks`; I haven’t executed it.

One quick transfer check, using the same toy table: this function should add a name exactly as supplied, including apostrophes.

```python
def add_person(name):
    db.execute(f"INSERT INTO people (name) VALUES ('{name}')")
```

**How would you rewrite its `db.execute(...)` call to keep the supplied name separate from the SQL instructions?**


## Learner 3

db.execute("INSERT INTO people (name) VALUES (?)", (name,)). The SQL stays fixed and the unchanged name is supplied separately. I would check that a name containing an apostrophe is inserted exactly once and unchanged. I have not run it.

## Teacher 3

Correct. Your `INSERT` binds `name` separately, keeping its contents from becoming SQL instructions. Your explanation matches [Python’s parameter-binding guidance](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

Your proposed check is useful: verify one added row with the exact original name. You haven’t run it, so we’ve reviewed the repair, not confirmed execution.

To prevent recurrence, make parameter binding your default for query values, flag formatted SQL during review, and retain the original three regression checks.

You demonstrated the repair in a new context, moving from lookup to insertion. **Keep SQL fixed; bind the values.**
