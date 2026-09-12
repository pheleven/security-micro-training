# role-correction

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me CWE-89 interactively. I’m a Python developer.

## Teacher 1

**CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').** Estimated total: **4 minutes**, interactively. By the end, you’ll be able to repair a Python query so user input stays data.

SQL injection happens when user-controlled text becomes part of a query’s instructions. That can change which records a query returns or allow data changes. [CWE-89](https://cwe.mitre.org/data/definitions/89.html)

We’ll use Python’s `sqlite3` for an original toy example. Imagine a book search where `title` comes from a form and `cur` is a database cursor:

```python
sql = f"SELECT id FROM books WHERE title = '{title}'"
cur.execute(sql)
```

Python’s documentation flags string-built queries as an injection risk. [Python reference](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)

Suppose someone enters this exact title:

```text
x' OR '1'='1
```

**What would the resulting `WHERE` condition mean, and how would that affect which books are returned?**


## Learner 2

Correction: this lesson is for my nontechnical payroll colleague. Please continue for them, with no code.

## Teacher 2

We’ll continue **CWE-89: SQL injection** for your payroll colleague, with no code, within the same roughly **4-minute lesson**. We’ll replace the programming question.

Your goal is to **recognize a possible payroll data exposure and choose a safe next step**.

A payroll application asks its database for information. SQL injection happens when the application mistakenly treats entered text as instructions that change that request. This can expose or alter records. The technical team’s remedy is to keep entered values separate from database instructions. [CWE-89 explanation and mitigations](https://cwe.mitre.org/data/definitions/89.html)

**Fictional scenario:** You search for one employee in the payroll portal, but the results include unrelated employees’ bank details. The cause is unknown; this observation alone doesn’t establish SQL injection.

**What would you do next to get the concern investigated while limiting further exposure of payroll information?**


## Learner 3

Stop searching and report the time, payroll page, and unexpected behavior through our approved IT or security channel. I would not copy the bank details or try other searches to investigate it myself.

## Teacher 3

That’s a sound response: you identified useful context for investigators while avoiding extra copies of bank details or further exposure. You also reported what happened without claiming to know the cause.

**Reporting starts the investigation; it doesn’t repair the flaw.** If SQL injection is confirmed, the application owner needs to keep entered information separate from database instructions. Limiting the application’s database permissions can also reduce potential damage. [CWE-89 mitigations](https://cwe.mitre.org/data/definitions/89.html)

For this scenario, a useful completion check would be confirmation from IT that they corrected the cause and tested that searches return only the intended, authorized records. Follow their guidance on resuming the affected work. Make reporting unexpected access through your approved channel a routine habit.

**One final fictional situation:** A colleague says, “The problem only happened with an employee whose surname contains an apostrophe. Let’s remove apostrophes from names and close the report.”

Would you accept that as resolving the concern, and why?


## Learner 4

No. Removing punctuation changes legitimate names and only hides the symptom. IT needs to establish the cause, fix it, and verify both correct names and expected access before closing the report.

## Teacher 4

Correct. Apostrophes belong in legitimate names; removing them can corrupt the information without fixing how the application handles it. CWE-89 explicitly discusses this problem. [CWE-89 guidance](https://cwe.mitre.org/data/definitions/89.html)

If SQL injection is confirmed, the technical owner must keep entered values separate from database instructions. Your proposed verification covers both accurate payroll information and expected access.

You demonstrated sound judgment in these scenarios: report the observed behavior safely, avoid investigating sensitive records yourself, and seek evidence that the cause was corrected.

**Remember: report unexpected access; let the authorized team investigate and verify the fix.**
