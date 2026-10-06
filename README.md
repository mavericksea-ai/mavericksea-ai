# Maverick

I build [Driftproof](https://driftproofhq.com), an open-source instrument that measures whether an AI skill's with-versus-without gap is real or noise, and whether it held after the last model release, and records the result as a dated, hash-verified receipt. The method is written up in [a preprint on Zenodo](https://doi.org/10.5281/zenodo.23050796).

Most of the fixes below share one theme: an evaluation that reports a result it did not actually measure.

## Merged contributions

- [mlflow/mlflow #26252](https://github.com/mlflow/mlflow/pull/26252): `MetricThreshold(min_relative_change=...)` divided by the signed baseline, so with a negative baseline metric it accepted worse models and rejected better ones. The change is now measured against the baseline's magnitude. Issue [#26144](https://github.com/mlflow/mlflow/issues/26144).
- [NVIDIA/SkillEvaluator #154](https://github.com/NVIDIA/SkillEvaluator/pull/154): Tier 3 credited reading a script as executing it; credit now requires evidence of an actual invocation. Four review rounds with NVIDIA's code owners.
- [addyosmani/agent-skills #576](https://github.com/addyosmani/agent-skills/pull/576): the eval grader binds each result to its declared expectation and rejects malformed output.
- [addyosmani/agent-skills #578](https://github.com/addyosmani/agent-skills/pull/578): the simplify-ignore hook no longer discards edits made outside the Edit tool.
- [addyosmani/agent-skills #587](https://github.com/addyosmani/agent-skills/pull/587): stale grading files are cleared before a rejected run is written; the executor model is recorded per run.
- [addyosmani/agent-skills #598](https://github.com/addyosmani/agent-skills/pull/598): the ADR eval grades the status and date the skill asks for, rather than timeless wording.
- [addyosmani/agent-skills #600](https://github.com/addyosmani/agent-skills/pull/600): the constraint skill's floor-guard reference now sees untracked files, deleted tests and loosened maximum budgets.
- [addyosmani/agent-skills #614](https://github.com/addyosmani/agent-skills/pull/614) and [#615](https://github.com/addyosmani/agent-skills/pull/615): follow-ups the maintainer invited on #600 and #598. The floor guard now checks changed lines that start with `++` or `--` and runs correctly from a subfolder, and the ADR template's Status line starts at Proposed.

## Open, in review

- [stanfordnlp/dspy #10474](https://github.com/stanfordnlp/dspy/pull/10474): BootstrapFewShot saved demonstrations that DSPy's own judge metrics had rejected.
- [langchain-ai/langsmith-sdk #3583](https://github.com/langchain-ai/langsmith-sdk/pull/3583): evaluate_comparative with randomize_order recorded scores against the wrong runs.
- [confident-ai/deepeval #3330](https://github.com/confident-ai/deepeval/pull/3330): PromptAlignmentMetric scored missing judge verdicts as a perfect pass. Another contributor has since proposed the same check for eleven metrics ([#3347](https://github.com/confident-ai/deepeval/pull/3347)).
- [confident-ai/deepeval #3355](https://github.com/confident-ai/deepeval/pull/3355) and [#3357](https://github.com/confident-ai/deepeval/pull/3357): the prompt optimizer kept one score per metric class, and concurrent evaluations shared span metric objects.
- [harbor-framework/harbor #3356](https://github.com/harbor-framework/harbor/pull/3356): pass@k grouped trials by display name, inflating scores for same-name tasks.
- [EleutherAI/lm-evaluation-harness #4221](https://github.com/EleutherAI/lm-evaluation-harness/pull/4221): bootstrap standard errors for binary F1 and MCC computed from confusion counts, replacing 100,000 sklearn calls.
- [obra/superpowers #2304](https://github.com/obra/superpowers/pull/2304): task briefs no longer end early at a fenced example that contains a task heading.
- [anthropics/skills #1945](https://github.com/anthropics/skills/pull/1945): the claude-api eval guides sized the noise floor as if repeated runs were extra test cases; the interval narrows with cases, not reps, and the guides now give the paired-interval arithmetic. Issue [#1944](https://github.com/anthropics/skills/issues/1944).

## Reported

- [NVIDIA/SkillEvaluator #149](https://github.com/NVIDIA/SkillEvaluator/issues/149): unrecovered command failures scored as first-attempt clean. A fix by another contributor is open as [#151](https://github.com/NVIDIA/SkillEvaluator/pull/151).

Open to research, tooling and evaluation-infrastructure conversations: hello@driftproofhq.com
