<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg" />
  <img src="assets/banner.svg" width="100%" alt="Maverick — Make the score mean something. Building Driftproof. Fixing how AI gets evaluated." />
</picture>

<p>
<a href="https://github.com/driftproofhq/driftproof"><b>↗ Driftproof</b></a> &nbsp;&nbsp;·&nbsp;&nbsp;
<a href="https://driftproofhq.com/writing/three-releases/">Writing</a> &nbsp;&nbsp;·&nbsp;&nbsp;
<a href="https://github.com/pulls?q=is%3Apr+author%3Amavericksea-ai+is%3Apublic+-org%3Adriftproofhq+-user%3Amavericksea-ai">Contributions</a> &nbsp;&nbsp;·&nbsp;&nbsp;
<a href="mailto:hello@driftproofhq.com">Get in touch</a>
</p>

I’m **Maverick**, building [Driftproof](https://driftproofhq.com) and contributing to the tools that evaluate AI models and agents.

I work on a deceptively simple question: **did the system actually measure what its score says it measured?** That has led me from missing execution evidence to inflated metrics, stale grading, and results attributed to the wrong model.

## 01 / Building Driftproof

**Agent skills change. Models change. Their evaluations should keep up.**

Driftproof runs tasks with and without a skill, samples answers and judge scores, and writes dated, hash-verified receipts. It gives you results to inspect and compare when the model underneath a skill changes.

<table>
<tr>
<td width="50%" valign="top">
<h3>Use the instrument</h3>
<p>Evaluate a skill against a baseline and inspect the evidence behind the result.</p>
<a href="https://github.com/driftproofhq/driftproof"><b>Explore the source →</b></a>
</td>
<td width="50%" valign="top">
<h3>Read the findings</h3>
<p>Published runs, measurement limits, and what changed when the instrument was corrected.</p>
<a href="https://driftproofhq.com/writing/three-releases/"><b>Three model releases later →</b></a>
</td>
</tr>
</table>

## 02 / Fixes that shipped

Selected merged contributions to projects I use and study.

| Where | Why the fix matters |
| :--- | :--- |
| **NVIDIA · SkillEvaluator** | Reading a script must not count as running it. [Require invocation evidence ↗](https://github.com/NVIDIA/SkillEvaluator/pull/154) |
| **ModelScope · EvalScope** | Unrecognized answers must not disappear from recall and F1 denominators. [Correct PubMedQA scoring ↗](https://github.com/modelscope/evalscope/pull/1828) |
| **MLflow** | Relative score checks must handle negative baselines correctly. [Use the baseline’s magnitude ↗](https://github.com/mlflow/mlflow/pull/26252) |
| **Alibaba · skill-up** | Tool argument rules need the argument structure preserved. [Fix judge matching ↗](https://github.com/alibaba/skill-up/pull/304) |
| **Addy Osmani · agent-skills** | Grades must match declared expectations and the current run. [Bind expectation IDs ↗](https://github.com/addyosmani/agent-skills/pull/576) · [Clear stale grading ↗](https://github.com/addyosmani/agent-skills/pull/587) |

<details>
<summary>More merged work in agent-skills</summary>

- [#578](https://github.com/addyosmani/agent-skills/pull/578) — Preserve on-disk edits when expanding simplify-ignore sections.
- [#598](https://github.com/addyosmani/agent-skills/pull/598), [#615](https://github.com/addyosmani/agent-skills/pull/615) — Align ADR grading and templates with the expected status and date.
- [#600](https://github.com/addyosmani/agent-skills/pull/600), [#614](https://github.com/addyosmani/agent-skills/pull/614) — Strengthen floor-guard checks for untracked files, deletions, thresholds, and diff parsing.

</details>

## 03 / Open-source activity

<!-- activity:start -->
<table>
<tr><td width="50%" valign="top"><h3>↗ Recently active · merged</h3>
<p><a href="https://github.com/NVIDIA/SkillEvaluator/pull/242"><b>NVIDIA/SkillEvaluator #242</b></a><br/><sub>Add opt-in Unicode character facts for Tier 3 judges</sub></p>
<p><a href="https://github.com/NVIDIA/SkillEvaluator/pull/217"><b>NVIDIA/SkillEvaluator #217</b></a><br/><sub>fix(tier3): score unrecovered failures and align recovery verdicts</sub></p>
<p><a href="https://github.com/NVIDIA/SkillEvaluator/pull/190"><b>NVIDIA/SkillEvaluator #190</b></a><br/><sub>fix(tier3): derive accuracy scores from criterion verdicts</sub></p>
</td><td width="50%" valign="top"><h3>◌ Under review</h3>
<p><a href="https://github.com/addyosmani/agent-skills/pull/694"><b>addyosmani/agent-skills #694</b></a><br/><sub>fix(constraints): enforce security and accessibility quality gates</sub></p>
<p><a href="https://github.com/langchain-ai/openevals/pull/293"><b>langchain-ai/openevals #293</b></a><br/><sub>Add optional character facts for Unicode-sensitive judging</sub></p>
<p><a href="https://github.com/promptfoo/promptfoo/pull/12005"><b>promptfoo/promptfoo #12005</b></a><br/><sub>feat(eval): add character facts template filter</sub></p>
</td></tr>
<tr><td colspan="2" valign="top"><h3>Reported issues</h3>
<p><a href="https://github.com/NVIDIA/SkillEvaluator/issues/221"><b>NVIDIA/SkillEvaluator #221</b></a><br/><sub>[BUG]: macOS cancellation cleanup test races with process exit</sub></p>
<p><a href="https://github.com/anthropics/claude-code/issues/105497"><b>anthropics/claude-code #105497</b></a><br/><sub>[BUG] Native plugin eval LLM grader misgrades literal NBSP; equivalent escaped Python literals grade correctly</sub></p>
<p><a href="https://github.com/langchain-ai/openevals/issues/292"><b>langchain-ai/openevals #292</b></a><br/><sub>Code-correctness judge can reverse grades on NBSP-sensitive answers</sub></p>
</td></tr>
</table>
<sub>Public external PRs and issues · ordered by latest activity · refreshed 2026-10-30 UTC.</sub>
<!-- activity:end -->

---

**Working on agent skills or evaluation infrastructure?** I’m interested in reproducible failures, useful tools, and getting the measurement right.

[hello@driftproofhq.com](mailto:hello@driftproofhq.com) · [driftproofhq.com](https://driftproofhq.com)

<sub>Contribution statuses checked October 10, 2026.</sub>
