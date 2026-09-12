# source-claim-scope

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training for a short explanation: does the parameter-substitution example at https://docs.python.org/3/library/sqlite3.html prove that I can bind a table name using a question-mark placeholder? Explain the boundary with sources; no quiz.

## Teacher 1

**No.** The Python example demonstrates binding a **value**: in `SELECT * FROM lang WHERE first_appeared = ?`, the parameter supplies `1972`; the table name `lang` remains part of the SQL text. That example does not establish that identifiers can be bound. [Python’s placeholder examples](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

The boundary is SQL structure versus data. SQLite defines parameters as placeholders for runtime values within expressions, and its binding documentation describes replacing literals. A table name is an identifier, so `?` cannot supply it. [SQLite parameters](https://www.sqlite.org/lang_expr.html#parameters), [SQLite binding documentation](https://www.sqlite.org/c3ref/bind_blob.html)

Original illustration, assuming a table `items` with a `name` column:

```python
# Valid: binds a comparison value.
cur.execute("SELECT * FROM items WHERE name = ?", ("pen",))

# Invalid: a placeholder cannot occupy the table-name position.
cur.execute("SELECT * FROM ?", ("items",))
```

When table selection must vary, keep names fixed in code or map permitted choices to specific, developer-defined table names, rejecting unknown choices. Continue binding the query’s data values. OWASP explicitly identifies table and column names as places where bind variables cannot be used and recommends this allow-list approach or query redesign. [OWASP guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#sample-of-safe-table-name-validation)
