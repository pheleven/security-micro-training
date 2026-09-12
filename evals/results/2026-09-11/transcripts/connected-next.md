# connected-next

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute CWE-88 lesson for a developer. Use pseudocode; suggest one useful next topic after the lesson.

## Teacher 1

**CWE-88: Improper Neutralization of Argument Delimiters in a Command ('Argument Injection').** Estimated time: four minutes, including the exercise. By the end, you can repair a process invocation so user input cannot become an unintended option.

Argument injection lets untrusted input change a command’s arguments or options. Consequences depend on the invoked program: unexpected behavior, data disclosure or modification, and sometimes code execution. This lesson focuses on input intended as a filename becoming an option. [MITRE CWE-88](https://cwe.mitre.org/data/definitions/88.html)

During the first minute, inspect this **original fictional example, using pseudocode**. Assume `report-viewer` accepts filenames, recognizes `--show-all` as an option that displays every report, and supports `--` to end option parsing.

```text
# Before: launches directly, without a shell
runProcess(
    executable = "/app/bin/report-viewer",
    arguments = [request.filename],
    shell = false
)
```

For `summary.txt`, the program displays one report. For `--show-all`, it displays everything.

The failed assumption is that one argument must be data. Argument boundaries can remain intact while the receiving program interprets that argument as an option. Preventing shell interpretation or quoting input does not, by itself, prevent argument injection. [OWASP argument injection guidance](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#argument-injection)

Spend the next minute on the repair. Prefer a library API that performs the needed operation without constructing a command. When a process is necessary, combine separate arguments with validation and the program’s documented option rules. [OWASP primary defenses](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#primary-defenses)

```text
# After: original pseudocode
allowedFiles = {"summary.txt", "quarterly.txt"}
name = request.filename
require name in allowedFiles

runProcess(
    executable = "/app/bin/report-viewer",
    arguments = ["--", name],
    shell = false
)
```

Here, the allowlist restricts inputs to the application’s supported choices. The fictional tool’s `--` makes subsequent arguments filenames. For a real tool, verify that it supports this delimiter in that position; do not assume it is universal. MITRE demonstrates this defense for `ls`. [CWE-88 mitigation example](https://cwe.mitre.org/data/definitions/88.html#Demonstrative_Examples)

Use the third minute to plan verification and prevention:

- Propose regression cases for `summary.txt`, `--show-all`, and `summary.txt --show-all`. The first should display only the selected report; the others should be rejected before launch.
- In review, trace each user-controlled argument to the receiving tool’s parser. Document permitted values and option handling alongside the process wrapper.

These are proposed checks for this example, not tests already performed.

For the final minute, consider another fictional tool. `picture-tool` recognizes `--overwrite` and supports `--`:

```text
runProcess("/app/bin/picture-tool", [uploadedName], shell=false)
```

A teammate proposes rejecting spaces. Would that prevent option injection, and what would you change?

**Pause before checking.**

No: `--overwrite` contains no spaces. Use an application-controlled filename mapping or explicit allowlist, retain separate arguments, and put the supported `--` before filename operands. The reasoning is the same: controlling argument boundaries alone does not control their meaning. [OWASP defenses](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#primary-defenses)

Remember: **keep user data from becoming program options.**

Optional next topic, outside the four minutes: [CWE-78, OS Command Injection](https://cwe.mitre.org/data/definitions/78.html), to examine how command separators introduce another parsing boundary when constructing shell commands.


## Learner 2

Next.

## Teacher 2

**CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection').** Estimated time: four minutes, including the exercise. By the end, you can replace a shell command built from user input with an operation that keeps input out of command syntax.

CWE-78 occurs when externally influenced input changes an intended OS command because special elements are not properly neutralized. One failure mode lets an attacker append another command using a command separator. [MITRE CWE-78](https://cwe.mitre.org/data/definitions/78.html)

Recall the distinction from the previous lesson: input can change a program’s **options** through argument injection. Here, we’ll examine input changing what a **shell executes**.

Consider this **original fictional scenario, using pseudocode**. A reporting service counts lines in a selected file:

```text
# Before: shell parses the assembled string
command = "report-count " + request.filename
runShell(command)
```

Assume a Unix-style shell. An input such as:

```text
report.txt; extra-command
```

makes the assembled text describe two commands. `extra-command` is a placeholder, not something to run. The trust boundary is crossed when the service inserts a filename into text the shell interprets as instructions. The attacker’s command runs with the application’s privileges, which can increase the impact. [MITRE mechanism and consequences](https://cwe.mitre.org/data/definitions/78.html)

Spend the second minute on the repair. Prefer a library operation that avoids invoking an OS command. [OWASP primary defense](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#defense-option-1-avoid-calling-os-commands-directly)

```text
# After: illustrative library API, no shell
reports = {
    "monthly": "/app/reports/monthly.txt",
    "annual":  "/app/reports/annual.txt"
}

require request.reportId in reports
path = reports[request.reportId]
return TextLibrary.countLines(path)
```

In this example, users select an application-defined report. Their input never becomes shell syntax.

If an external program is essential, use a fixed executable and a process API that passes arguments separately without a shell. Then apply the CWE-88 controls: validate permitted values and check how the target interprets options. Merely changing to an argument array does not make every argument safe. [OWASP parameterization and validation](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#defense-option-3-parameterization-in-conjunction-with-input-validation)

During the third minute, plan these regression checks for the replacement:

- A known report with three lines returns `3`.
- Unknown IDs, including `monthly; extra-command`, are rejected before file access.
- A process-launch spy records no subprocess calls.

These are proposed tests, not executed results. As a prevention habit, require reviewers to identify any flow from request data into shell execution.

For the final minute, inspect this different proposal:

```text
runProcess(
    "/bin/sh",
    ["-c", "report-count " + request.filename],
    shell = false
)
```

Does `shell = false` solve the problem?

**Pause before checking.**

No. The code explicitly launches a shell and asks it to interpret the constructed command. Replace that invocation with the library operation, or invoke the intended executable directly with validated, separate arguments. The relevant question is whether a shell ultimately interprets user-influenced command text. [OWASP shell-parsing distinction](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html#java)

**Keep user input out of shell command text.**
