# Earlier delivery-mode failures

Candidate `SKILL.md` SHA-256: `ff546b9b24691d08c44754fc6b3b8b778754f5777539be802077b4af8dd61815`. Both prompts requested a complete lesson, but the responses below ended at an interactive opening. These are retained failures, not final release results.

## role-developer

### Learner

Use $security-micro-training to give me a complete four-minute CWE-89 lesson. I’m a Python developer using sqlite3, but new to security.

### Teacher

**CWE-89: SQL Injection**—formally, “Improper Neutralization of Special Elements used in an SQL Command.” Estimated total: **four minutes**, including our short exchanges. By the end, you’ll be able to repair an unsafe `sqlite3` lookup and describe a test that checks the fix.

SQL injection happens when user input becomes part of a database command’s instructions. The failed assumption is that text inserted into a query will remain ordinary data. It can instead change what the query does. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Here’s an original toy example: a book search using a Python `sqlite3` cursor named `cur`. Python’s documentation warns against assembling SQL with string formatting. [Python guidance](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

```python
title = input("Book title: ")
sql = f"SELECT title FROM books WHERE title = '{title}'"
rows = cur.execute(sql).fetchall()
```

Suppose someone enters this exact text:

```text
' OR '1'='1
```

**Looking at where that text lands in `sql`, would the query find only a matching title or every row—and why?**

## role-soc

### Learner

Use $security-micro-training to give me a complete four-minute CWE-89 lesson. I’m an experienced SOC analyst, but SQL is new to me. I can inspect application and proxy logs; I don’t own the code.

### Teacher

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command (‘SQL Injection’).** Estimated total: four minutes, including our exchanges. By the end, you can make an evidence-backed triage decision and specify a verifiable remediation handoff.

SQL tells a database what data to retrieve or change. In this simplified, original example:

```sql
SELECT amount FROM invoices WHERE customer = 'Acme';
```

`SELECT` retrieves a column; `WHERE` filters rows; straight quotes delimit text. If an application builds the command by pasting user input between those quotes, input can change the command’s meaning. That is the failed boundary: supplied data becomes database instructions, potentially exposing or modifying records. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Consider this **synthetic evidence**, with the request value already decoded:

```text
Proxy: request_id=r17  /invoices?customer=O'Brien  status=500
App:   request_id=r17  database syntax error near "Brien"
```

**What conclusion would you record from these two entries, and what additional evidence would you seek before calling this successful exploitation?**
