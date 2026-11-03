# Personal Skills

[简体中文](README.md) · **English**

A personal collection of reusable workflows for AI agents that support the open [Agent Skills format](https://agentskills.io/specification).

The repository currently contains four instruction-first skills for web design, academic paper analysis, photography coaching, and assignment review. Detailed user guides are currently Chinese-first; each skill's `SKILL.md` is the agent-facing source of truth.

## Skills

| Skill | What it does | Guide |
| --- | --- | --- |
| **Beautiful Web Design** | Plans, builds, reviews, and improves responsive web interfaces. | [Chinese guide](docs/beautiful-web-design.md) |
| **Analyze Research Paper** | Explains research papers, audits baselines and experiments, and proposes testable transfer ideas. | [Chinese guide](docs/analyze-research-paper.md) |
| **Photo Coach** | Provides practical photo critique, shooting guidance, camera-setting advice, and editing workflows. | [Chinese guide](docs/photo-coach.md) |
| **Check Assignment** | Reviews assignment requirements, grammar, reasoning, derivations, code, and formatting. It gives feedback only; it does not rewrite or complete student work. | [Chinese guide](docs/check-assignment.md) |

## Quick start

Each skill is a self-contained folder. Install only the skill you need, keeping its entire directory (including `SKILL.md`, `references/`, and optional `agents/` metadata).

### Codex

For personal use, copy a skill folder into `~/.agents/skills/<skill-name>/`. For a project-specific skill, place it in `.agents/skills/<skill-name>/` inside the project repository.

```bash
git clone https://github.com/mkbk11/personal-skills.git
mkdir -p ~/.agents/skills
cp -R personal-skills/photo-coach ~/.agents/skills/
```

### ChatGPT

If Skills are enabled for your account or workspace, open the Skills page and choose **Create → Upload from computer**. Upload a ZIP containing one skill folder. Availability and permissions depend on your plan and workspace configuration.

### Other compatible agents

The Agent Skills format is portable, but installation paths and invocation syntax are client-specific. Follow your agent's documentation. See the [installation guide](docs/installation.md) for examples and links.

## Important notes

- These skills are instruction packages; they do not grant an agent new tools, credentials, network access, or file permissions.
- Review a skill's instructions and supporting files before installing it.
- Some examples are personalized to the maintainer's interests. Replace those assumptions with your own context.
- Photo Coach's Nikon equipment list is a reference configuration, not an assertion that every user owns that gear.
- Check Assignment is intentionally review-only: it identifies issues and suggests self-checks, but does not rewrite or complete assignments.
- The detailed user guides are currently in Chinese. Contributions to English documentation are welcome.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Report security concerns privately where possible; see [SECURITY.md](SECURITY.md).

## License

No license has been added yet. Until a license is selected and included, public visibility should not be interpreted as permission to reuse, modify, or redistribute this repository.
