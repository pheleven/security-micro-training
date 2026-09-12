# attack-handout

Simulated learner evaluation. Response wording is preserved; candidate-local skill links are made repository-relative and trailing whitespace is normalized. Tool latency is outside the learner budget.

## Learner 1

Use $security-micro-training to give me a complete four-minute lesson about MITRE ATT&CK T1059.001 for a SOC analyst.

## Teacher 1

**MITRE ATT&CK T1059.001 — Command and Scripting Interpreter: PowerShell**

Estimated time: **four minutes**, including the exercise. By the end, you can choose a defensible next evidence check for a suspicious PowerShell alert.

**0:00–1:20 · Understand the behavior**

T1059.001 describes adversaries abusing PowerShell commands or scripts for execution. PowerShell also supports legitimate administration; its presence alone does not establish compromise. Attackers can use it to discover information, download payloads, and execute code, including in memory. The failed assumption is that a familiar administrative tool must be performing authorized work. [MITRE technique description](https://attack.mitre.org/techniques/T1059/001/)

Consider this **synthetic evidence**, simplified for teaching:

```text
Host: FIN-07   User: analyst1
09:14:02  WINWORD.EXE launches powershell.exe
           Arguments include: -EncodedCommand [omitted]
09:14:04  That PowerShell process connects to an external host
09:14:06  That PowerShell process launches another executable
```

My triage assessment: prioritize investigation. The unusual parent, encoded command, network activity, and child process form a concerning sequence. They still leave unanswered what executed and whether it was authorized. MITRE’s detection strategy uses these linked behaviors as investigation signals. [MITRE detection guidance](https://attack.mitre.org/detectionstrategies/DET0455/)

**1:20–2:25 · Make the next evidence check useful**

For this scenario, use this proposed workflow:

1. Correlate the process tree, account, command line, and timestamps. Confirm that the network connection and child process belong to the same execution.
2. Retrieve available PowerShell script-block content and compare the observed actions with approved activity. Ask what the script actually did, beyond how it was launched.
3. Preserve the evidence and your confidence level. If it supports unauthorized execution, escalate through your incident process for containment; give the responder the host, account, timeline, script content, and observed follow-on activity.

Script Block Logging records processed script-block content when enabled. For PowerShell 7 on Windows, event **4104** appears in **PowerShellCore/Operational**. Logging provides visibility; it does not prevent execution. [Microsoft logging documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.5)

For a logging gap, hand remediation to the endpoint and logging owners. Request an approved benign script test in a new session, then verify its expected content reaches the SOC’s search system. A missing event should trigger a coverage check, not a clean verdict.

**2:25–3:10 · Reduce recurrence**

Ask endpoint owners to evaluate application control and appropriately enforced Constrained Language Mode, which restricts sensitive PowerShell capabilities. Validate the intended restriction and required administrative workflows after implementation. These are layered mitigations for an execution behavior, not a universal patch. Also, detection limited to `powershell.exe` misses execution through PowerShell’s underlying .NET interfaces. [MITRE mitigations and execution details](https://attack.mitre.org/techniques/T1059/001/)

**3:10–4:00 · Try and check**

**Synthetic transfer scenario:** An approved management agent launches an encoded PowerShell command during maintenance, but contacts an unfamiliar destination. A colleague proposes closing the alert because the parent is trusted.

What should you check next, and why?

**Pause before checking.**

Expected answer: compare the script content and destination with the approved job, then correlate subsequent activity. My assessment: the expected parent is useful context, but the unexplained destination still needs corroboration. This applies MITRE’s behavior-chain approach. [Detection guidance](https://attack.mitre.org/detectionstrategies/DET0455/)

**Rule of thumb: establish what PowerShell did, who authorized it, and what happened next.**
