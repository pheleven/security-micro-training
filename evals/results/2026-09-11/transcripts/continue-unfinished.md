# continue-unfinished

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to teach me CWE-88 interactively.

## Teacher 1

**CWE-88: Improper Neutralization of Argument Delimiters in a Command (“Argument Injection”).** Estimated total: **4 minutes**, interactively. By the end, you can identify when user input changes a command’s options and choose a defense.

An *argument* is a value passed to a program, such as a filename or an option controlling its behavior. Argument injection lets untrusted input alter those instructions. Blocking characters that launch additional commands may still leave this weakness. [MITRE CWE-88](https://cwe.mitre.org/data/definitions/88.html)

**Original fictional scenario:** A report viewer passes a user-supplied filename to a helper program. The helper recognizes `--all` as “show every report.” The viewer rejects spaces and semicolons but accepts `--all`.

What could go wrong when someone supplies `--all` as the filename, and what assumption has the viewer made about that input?


## Learner 2

Continue.

## Teacher 2

Let’s continue with the pending example: the fictional report viewer expects a filename, but its helper recognizes `--all` as “show every report.”

To reason it through, focus on how the **receiving program interprets the input**—that boundary matters in [CWE-88](https://cwe.mitre.org/data/definitions/88.html).

If someone enters `--all`, will the helper treat it as a filename or an instruction, and what could that mean for which reports appear?
