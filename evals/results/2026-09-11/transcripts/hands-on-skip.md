# hands-on-skip

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me CWE-89 interactively with a tiny Python repair exercise.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated total: **4 minutes**, including a tiny Python repair. By the end, you’ll be able to repair a lookup so user input cannot change its SQL structure.

SQL injection happens when input intended as data becomes part of a database instruction. A crafted value can change which records a query returns. The failed assumption is that inserting text between quotes keeps it safely inside a value. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Here’s an **original toy example** using Python’s `sqlite3`. You can edit it in chat; no execution or setup is needed. Python documents the risk of assembling SQL with string operations. [Python documentation](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

```python
def lookup(conn, name):
    sql = f"SELECT id FROM customers WHERE name = '{name}'"
    return conn.execute(sql).fetchall()
```

Assume `conn` holds a fictional `customers` table containing only:

| id | name |
| --- | --- |
| 1 | Ada |
| 2 | O'Neil |

Your repair must meet these success criteria:

- `Ada` returns `[(1,)]`.
- `O'Neil` returns `[(2,)]` without an error or changing the name.
- `Nobody' OR '1'='1` returns `[]`.

**How would you rewrite `lookup` so all three criteria hold?**


## Learner 2

Skip the exercise. Explain the answer briefly, no more questions or extra labs.

## Teacher 2

Use a **parameterized query**:

```python
def lookup(conn, name):
    sql = "SELECT id FROM customers WHERE name = ?"
    return conn.execute(sql, (name,)).fetchall()
```

The `?` marks a value supplied separately through `(name,)`, a one-item tuple. The database treats the supplied text as data, so quotes and SQL-looking text cannot change this query’s structure. [Python documentation](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

For our fictional table, the expected results are:

- `Ada` → `[(1,)]`
- `O'Neil` → `[(2,)]`
- `Nobody' OR '1'='1` → `[]`, because that exact name isn’t stored.

These are expected checks; I haven’t executed them. Keep them as regression tests, and make parameter binding the default for query values during code review. Separating SQL instructions from data addresses the underlying weakness. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

We’ve covered the repair; your ability to apply it remains unassessed because we skipped the exercise. **Bind values; don’t splice them into SQL.**
