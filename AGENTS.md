# Repository Guidance for AI Agents

本文件约束在此仓库中工作的 AI coding agents。

## Repository intent

- This repository contains portable Agent Skills, not a single application.
- Each top-level skill directory with a `SKILL.md` is an independently installable skill.
- `docs/` contains user-facing documentation; it is not part of a skill package unless explicitly copied into one.

## Editing rules

1. When changing a Skill's behavior, update its `SKILL.md`, relevant `references/`, and matching `docs/<skill-name>.md` together.
2. Keep Skill names in directory names and YAML frontmatter identical.
3. Preserve the review-only boundary of `check-assignment`: diagnose and advise; never rewrite, expand, or complete student work.
4. Preserve uncertainty in `photo-coach`: do not assume the user owns the Nikon reference kit.
5. In `analyze-research-paper`, separate paper facts, derived calculations, interpretations, and untested ideas.
6. In `beautiful-web-design`, never claim a build, browser check, or interaction test was completed unless it actually ran.
7. Do not add personal secrets, private documents, API keys, or sensitive data.
8. Do not add or change a repository license without explicit maintainer approval.
9. Keep the root README concise; put detailed instructions in `docs/`.
10. Avoid adding dependencies, scripts, or extra directories unless they serve a clear maintenance or user need.

## Validation

Run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

The validator checks structure and links only. It does not assess response quality, factual accuracy, or security.
