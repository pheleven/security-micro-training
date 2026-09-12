# Review source support

Use this procedure when guidance conflicts, versions or dates matter, a tutorial supplies the explanation, or a citation's support is uncertain. Ordinary short answers still require the claim check in `SKILL.md`; this reference supplies the additional checks for difficult cases.

## Match claims to evidence

Identify the few claims the learner must rely on: the mechanism, affected scope, remedy or mitigation, and verification outcome. For each, inspect the actual source passage and check:

- **Identity and scope:** Does it address this identifier, framework edition, product, runtime branch, API, and configuration? Do not carry a condition or fix across branches without evidence.
- **Meaning:** Does the source support the whole claim, including qualifiers? A value-binding example does not by itself establish that an identifier can be bound. A log entry can support an observation without proving attacker intent or successful exploitation.
- **Strength:** Preserve terms such as possible, conditional, partial, and temporary when they affect the decision. Avoid converting mitigation guidance into a promise of prevention.
- **Time:** Distinguish publication, update, release, and your verification dates. A recent retrieval or search crawl does not make old guidance current. Recheck maintenance status and current advisories before recommending a historical fix as today's upgrade target.
- **Link:** Cite the supporting page or section with a descriptive Markdown link. Read the content, not just the title, search snippet, or domain. A secondary resource may help learning, but technical claims should be checked against primary documentation or research.

If a sentence combines claims with different support, split it or add the appropriate citations. Do not add citations that merely mention the topic. Clearly mark proposed checklists, illustrative examples, and inferences; cite the facts underlying them without claiming the source prescribed your exact workflow. Keep this working audit out of the learner response unless requested.

## Resolve disagreements without guessing

First check whether the sources discuss different products, branches, configurations, CVEs, or historical points. A release-note correction or an explicit superseding advisory can explain a difference; cite that evidence when available. Do not assume the newest-looking page is correct merely because it was updated recently.

If the discrepancy remains, state what differs and link both sources. Teach the supported common ground. Omit an exact operational recommendation that depends on resolving the dispute, or explain the additional vendor confirmation needed. A conservative-sounding guess is still a guess; do not invent a fixed version, support status, or claim that a workaround fully repairs the issue.

## Check learning resources

Inspect recommended pages for relevant content and free access. For videos, verify the actual segment through available captions/transcript or accessible content before assigning it; a title alone does not establish accuracy, timestamps, or duration. Use the original text lesson when media cannot be verified. Attribute material and link rather than reproducing a course or transcript.

Keep required learning within the lesson budget. Source links should let the learner verify and explore further without making external reading a hidden prerequisite. Do not say all sources are verified if any recommended material was inaccessible or uninspected.
