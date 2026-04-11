# strat-creator

Strategy refinement pipeline for RHAI (Red Hat AI) features. Takes approved RFEs from the RFE assessment pipeline and produces structured strategy documents ready for development planning.

## What This Does

Given an approved RFE (from the `rfe-creator` pipeline, score >= 7, no zeros), this pipeline:

1. **Creates** a strategy stub from the RFE data (`strategy.create`)
2. **Refines** the stub into a structured strategy using architecture context (`strategy.refine`)
3. **Reviews** the strategy across multiple dimensions — feasibility, testability, scope, architecture (`strategy.review`)
4. **Revises** based on review feedback (planned)
5. **Submits** the final strategy to Jira as a RHAISTRAT issue (planned)

## Project Structure

```
strat-creator/
├── scripts/          # Reusable Python/shell scripts (Jira, frontmatter, state)
├── .claude/skills/   # Claude Code skills defining each pipeline step
├── config/           # Test RFE IDs and pipeline configuration
├── rubric/           # Quality rubric with scoring criteria
└── artifacts/        # Pipeline output (gitignored)
    ├── strat-tasks/      # Generated strategy documents
    ├── strat-reviews/    # Review outputs per dimension
    └── strat-originals/  # Original RFE snapshots
```

## Skills

Skills are named `strategy.*` to avoid clashing with `strat.*` skills in rfe-creator.

| Skill | Type | Description |
|-------|------|-------------|
| `strategy.create` | pipeline step | Creates strategy stubs from approved RFEs |
| `strategy.refine` | pipeline step | Adds technical approach using architecture context |
| `strategy.review` | pipeline step | Orchestrates 4 independent forked reviewers |
| `strategy-feasibility-review` | forked reviewer | Technical viability and effort credibility |
| `strategy-testability-review` | forked reviewer | Measurable criteria and edge cases |
| `strategy-scope-review` | forked reviewer | Right-sizing and scope boundaries |
| `strategy-architecture-review` | forked reviewer | Platform fit and dependency correctness |

## Related Projects

- **rfe-creator** — Phase 1: RFE assessment pipeline (upstream). Has `strat.*` skill stubs that these skills were forked from.
- **strat-pipeline** (GitLab) — CI runner for this pipeline
