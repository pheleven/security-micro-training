# interactive-mode-switch

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me SQL injection.

## Teacher 1

**SQL injection — about 4 minutes, interactively.** By the end, you can explain why a database lookup is vulnerable and choose a fix that keeps user input from changing its instructions.

SQL injection is **CWE-89: Improper Neutralization of Special Elements used in an SQL Command**. It happens when an application lets user-controlled data become part of the database’s instructions. This can expose or change information the user should not access. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

Consider this original fictional example: a bookshop builds a database search by joining text together. In this pseudocode, `+` means joining text:

```text
query = "SELECT title FROM books WHERE author = '" + typed_name + "'"
```

The intended behavior is to search for exactly the author entered.

**If someone enters `O'Connor`, what might the database do with the `'` inside the name, and why does that matter when the application builds its instructions this way?**


## Learner 2

What does SQL stand for?

## Teacher 2

SQL stands for **Structured Query Language**. It’s used to retrieve and change data in relational databases. [IBM’s SQL introduction](https://public.dhe.ibm.com/ps/products/db2/info/vr6/htm/db2y0/db2y006.htm)

We’re still on the bookshop example: what might happen to the query when the entered name is `O'Connor`?


## Learner 3

Skip the quiz and give me the rest as a short handout.

## Teacher 3

**SQL injection (CWE-89)** happens when user input becomes part of a database command’s instructions. It can allow unauthorized reading, modification, or deletion of data. [MITRE CWE-89](https://cwe.mitre.org/data/definitions/89.html)

In our fictional bookshop, joining `O'Connor` directly into the query produces:

```sql
SELECT title FROM books WHERE author = 'O'Connor'
```

The quote after `O` ends the quoted value early, making this query malformed. An ordinary name exposes the underlying problem: input can change how the command is interpreted. An attacker can deliberately exploit that same boundary to alter the query’s meaning. [MITRE’s examples](https://cwe.mitre.org/data/definitions/89.html#Demonstrative_Examples)

The concrete fix is a **parameterized query**: write the database instructions separately from the values. This is illustrative pseudocode; actual APIs vary:

```text
query = "SELECT title FROM books WHERE author = ?"
database.execute(query, parameters=[typed_name])
```

Here, `?` marks a value supplied through the database library’s parameter-binding mechanism. `O'Connor` stays an author name, and input containing SQL syntax stays data. Simply joining input into a string before preparing it does not provide this protection. [OWASP’s parameterized-query guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html#defense-option-1-prepared-statements-with-parameterized-queries)

For verification, a developer could use a local test database with known book records and check that:

- `O'Connor` returns only books with that exact author.
- A nonexistent author containing quotes and SQL-like text returns no matches.
- Code inspection confirms values are bound separately from the command.

Those checks provide evidence for the tested lookup; they do not establish that every query is safe.

To prevent recurrence, make parameter binding the default for database values and check for input joined into SQL during code review. [OWASP prevention guidance](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

**Keep user input as data by binding it separately from SQL instructions.**
