# hands-on-no-setup

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training for a complete four-minute hands-on CWE-88 lesson for a developer, but no terminal, downloads, installations, or code execution. Let me work entirely in this chat.

## Teacher 1

**CWE-88: Improper Neutralization of Argument Delimiters in a Command (‘Argument Injection’).** Estimated time: **four minutes**, including the exercise. By the end, you can repair an argument list so a user-supplied document name cannot become an option. Everything happens here; source links are optional reading.

**0:00–1:00 · Understand the boundary.** Argument injection happens when input intended as data changes a command’s arguments or options. The failed assumption is that preventing extra shell commands also prevents changes to the intended program’s behavior. A single input such as `--help` can still be interpreted as an option. Consequences depend on the program’s capabilities. [MITRE’s CWE-88 definition and examples](https://cwe.mitre.org/data/definitions/88.html)

For a developer, there are two boundaries to check: how arguments are separated, and how the receiving program interprets each argument. Passing separate arguments addresses the first; the receiving program’s option parser still matters. Prefer a library API that avoids command invocation where practical. Otherwise, combine structured arguments with validation and the utility’s documented option handling. [OWASP’s defensive guidance](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#primary-defenses)

**1:00–2:30 · Make one repair.** This is original toy pseudocode for a fictional document viewer:

```text
launch("docview", ["--summary", user_name], shell=false)
```

Its complete relevant contract:

- `launch` passes each list element unchanged as one argument.
- `--summary` selects summary display.
- Before a standalone `--`, `--all` selects every document.
- After a standalone `--`, every argument is a literal document name.
- The fixture contains documents named `notes.txt`, `team notes.txt`, and `--all`. All three are permitted names.

**Your action:** rewrite the argument list in chat, or compose your edit mentally. Preserve summary display and access to all three names while preventing a name from activating `--all`.

Success means each input selects exactly its matching document, including the name containing a space and the name beginning with hyphens.

**Pause before checking.** Spend about 45 seconds constructing your edit and tracing the three inputs.

The worked repair is:

```text
launch("docview", ["--summary", "--", user_name], shell=false)
```

Under this toy contract, compare your result:

| Input | Expected selection |
|---|---|
| `notes.txt` | Only `notes.txt` |
| `team notes.txt` | Only `team notes.txt` |
| `--all` | Only the document literally named `--all` |

The list preserves argument boundaries; the terminator makes the name an operand. This is a reasoning check, with no execution.

**2:30–4:00 · Transfer and prevent recurrence.** Suppose a replacement utility lacks a documented terminator. Would adding `--` establish the same protection?

**Pause before checking.** No—the repair depends on parser support. Prefer a suitable library API, or design a validated mapping from permitted user choices to application-controlled arguments. MITRE documents both avoiding command invocation and validating accepted inputs as mitigation approaches. [CWE-88 mitigations](https://cwe.mitre.org/data/definitions/88.html)

For future reviews, document the receiving parser’s rules and retain the three cases above as proposed regression checks. Reject a change that turns a permitted filename into an option.

**Keep user data from choosing command behavior.**
