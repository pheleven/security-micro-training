# learning-path

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to plan a short learning path for a Python developer new to SQL injection. Don’t start teaching yet.

## Teacher 1

Here’s a proposed **three-lesson path: 3–5 minutes each, 9–15 minutes total**. I’ll use Python `sqlite3` for the examples; no setup is required.

| Lesson | One objective | Source |
|---|---|---|
| **1. Recognize SQL injection — CWE-89** | Identify where user input can change the meaning of a query in a tiny Python example. | [MITRE’s SQL injection definition](https://cwe.mitre.org/data/definitions/89.html) |
| **2. Repair a Python query** | Rewrite a string-built query using `sqlite3` parameter binding, with a small regression check included. | [Python’s placeholder guide](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries) |
| **3. Handle dynamic sorting safely** | Choose a safe approach for user-selected sort columns, applying the limits of parameter binding. | [OWASP’s allow-list guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-3-allow-list-input-validation) |

The order moves from recognizing the weakness to fixing it, then handling a related case where the remedy needs adjustment. Each lesson will include one short check using original toy examples. The sources are free; opening them is optional and outside the time estimate.

This is the plan only. Lessons will begin when you request one.


## Learner 2

Start the first lesson interactively.

## Teacher 2

**Lesson 1: Recognize SQL injection (CWE-89)**
Estimated total time: **4 minutes**, including our exchange. By the end, you’ll be able to identify where user input could change a query’s meaning.

SQL injection happens when externally supplied input becomes SQL instructions instead of remaining ordinary data. It can change which records a query returns. [MITRE’s CWE-89 definition](https://cwe.mitre.org/data/definitions/89.html)

In this **original toy example**, a Python application searches a fictional product catalog. The intended behavior is to return only products whose name matches the supplied text. `supplied_name` comes from a search box:

```python
query = (
    f"SELECT name, price FROM products "
    f"WHERE name = '{supplied_name}'"
)
rows = connection.execute(query).fetchall()
```

Focus on how the application constructs `query`; you don’t need to invent an attack.

**What assumption does this code make about `supplied_name`, and how could that assumption fail?**
