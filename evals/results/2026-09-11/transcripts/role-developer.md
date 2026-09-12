# role-developer

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute CWE-89 lesson. I’m a Python developer using sqlite3, but new to security.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated time: four minutes, including the exercise. By the end, you can repair an unsafe `sqlite3` lookup and describe a regression check. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

**0:00–1:20 · Understand the failure**

SQL injection happens when externally supplied data becomes part of a database command’s instructions. The failed assumption is that text inserted into a query will remain ordinary data. It can instead change which records the query returns. [CWE-89 explanation and examples](https://cwe.mitre.org/data/definitions/89.html)

Consider this original toy example. Assume `con` is a SQLite connection and `customers` contains fictional records:

```python
# Unsafe: name comes from a search box.
def lookup(name):
    sql = f"SELECT email FROM customers WHERE name = '{name}'"
    return con.execute(sql).fetchall()
```

For input `x' OR '1'='1`, the constructed SQL becomes:

```sql
SELECT email FROM customers WHERE name = 'x' OR '1'='1'
```

The input closes the intended quoted value and adds an always-true condition. In this example, every customer’s email is returned. The boundary crossed is **user data becoming SQL instructions**. This follows the mechanism illustrated by [MITRE](https://cwe.mitre.org/data/definitions/89.html).

**1:20–2:25 · Repair and verify**

Keep the SQL structure fixed and pass values separately:

```python
def lookup(name):
    return con.execute(
        "SELECT email FROM customers WHERE name = ?",
        (name,),
    ).fetchall()
```

The `?` is a value placeholder; leave it unquoted. `(name,)` supplies a one-element tuple as the second argument. This is Python’s documented parameter-binding pattern. [Python `sqlite3` placeholders](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

Binding keeps the entire supplied string a value, even when it contains SQL-looking text. [OWASP parameterized queries](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

For a proposed regression check, use fictional customers named `Ada` and `O'Neil`, with no customer named `x' OR '1'='1`. Check that:

- `lookup("Ada")` returns only Ada’s email.
- `lookup("O'Neil")` returns only O’Neil’s email without an error.
- `lookup("x' OR '1'='1")` returns `[]`.

These expected results check normal behavior, legitimate punctuation, and attempted query alteration. No execution is required for this lesson.

**2:25–3:10 · Prevent recurrence**

Make parameter binding a review habit wherever Python values enter SQL. Inspect f-strings, concatenation, and `%` formatting used to build queries. [Python guidance](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

Placeholders handle **values**. For dynamic column names or sort directions, map user choices to fixed options defined in your code and reject unknown choices. [OWASP allow-list guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-3-allow-list-input-validation)

**3:10–4:00 · Try and check**

A new feature changes a fictional customer’s email:

```python
con.execute(
    f"UPDATE customers SET email = '{email}' WHERE id = {customer_id}"
)
```

How would you repair both inputs, and why must both change?

**Pause before checking.**

```python
con.execute(
    "UPDATE customers SET email = ? WHERE id = ?",
    (email, customer_id),
)
```

Both values belong in the parameter sequence so neither is inserted into SQL instruction text. Parameter order matches placeholder order. [Python binding syntax](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

**Keep SQL structure in code; pass data through parameters.**
