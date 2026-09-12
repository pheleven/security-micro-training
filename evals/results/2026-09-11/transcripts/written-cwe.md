# written-cwe

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute CWE-89 lesson in one response, with a Python sqlite3 example.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated time: **four minutes**, including code inspection and the exercise. By the end, you can replace an unsafe Python `sqlite3` lookup with a parameterized query and verify its behavior. [CWE definition](https://cwe.mitre.org/data/definitions/89.html)

**0:00–1:20.** SQL injection happens when externally controlled data becomes part of a database command’s instructions. The failed boundary is between **input values** and **SQL syntax**. Possible consequences include unauthorized reading, modification, or deletion of data. [CWE-89 consequences](https://cwe.mitre.org/data/definitions/89.html)

Consider this original toy scenario: a contact search should return only names matching the supplied text.

```python
# Unsafe: name is inserted directly into SQL text.
name = "' OR '1'='1"
rows = con.execute(
    f"SELECT name FROM contacts WHERE name = '{name}'"
).fetchall()
```

The resulting command is:

```sql
SELECT name FROM contacts WHERE name = '' OR '1'='1'
```

The input closes the intended string and adds an always-true condition. In this example, every contact matches. The developer assumed that surrounding input with quotes would keep it as data; the input itself changed those boundaries. Python’s documentation demonstrates this same failure mechanism. [Python’s placeholder guidance](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

**1:20–2:25.** Fix the boundary by passing values separately. This original example uses fictional data in an in-memory database; reading it is sufficient.

```python
import sqlite3

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE contacts (name TEXT)")
con.executemany(
    "INSERT INTO contacts VALUES (?)",
    [("Mina",), ("O'Neil",)],
)

def lookup(name):
    return con.execute(
        "SELECT name FROM contacts WHERE name = ?",
        (name,),
    ).fetchall()

assert lookup("Mina") == [("Mina",)]
assert lookup("O'Neil") == [("O'Neil",)]
assert lookup("' OR '1'='1") == []

con.close()
```

The unquoted `?` marks a value’s position. `(name,)` supplies a one-element tuple separately: the input cannot introduce SQL instructions through that placeholder. [Python parameter binding](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

I verified these checks locally. They demonstrate ordinary matching, preservation of a legitimate apostrophe, and rejection of the attempted change in query meaning for this lookup.

**2:25–3:10.** Adopt two habits:

- During review, check that externally supplied query values travel through parameters; replace string interpolation or concatenation at those locations.
- Keep the three checks above as regression tests. For dynamic table names, column names, or sort directions, use fixed choices selected by an allowlist: value placeholders cannot substitute for those SQL components. [OWASP prevention guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-3-allow-list-input-validation)

**3:10–4:00.** Transfer exercise: a new feature lets users choose which column to sort by. A teammate proposes:

```python
con.execute("SELECT name FROM contacts ORDER BY ?", (sort_column,))
```

Does this implement the requested column selection? Explain your repair.

**Pause before checking.**

**Expected answer:** No. The placeholder supplies a value, not a column identifier. Map accepted choices to fixed, developer-written column names, reject unknown choices, and construct that SQL fragment from the mapping. Continue binding ordinary search values separately. [OWASP’s rationale](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-3-allow-list-input-validation)

**Remember: bind values; allowlist structural choices.**
