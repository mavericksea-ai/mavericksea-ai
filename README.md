# Maverick

I build [Driftproof](https://driftproofhq.com), an open-source instrument that measures whether an AI skill's with-versus-without gap is real or noise, and whether it held after the last model release, and records the result as a dated, hash-verified receipt.

## Merged contributions

- addyosmani/agent-skills #576: the eval grader binds each result to its declared expectation and rejects malformed output.
- addyosmani/agent-skills #578: the simplify-ignore hook no longer discards edits made outside the Edit tool.
- addyosmani/agent-skills #587: stale grading files are cleared before a rejected run is written; the executor model is recorded per run.

## Open

- NVIDIA/SkillEvaluator #149: unrecovered command failures scored as first-attempt clean (fix in #151, verified).
- confident-ai/deepeval #3329 and #3330: PromptAlignmentMetric scores missing judge verdicts as a perfect pass.
- harbor-framework/harbor #3355 and #3356: pass@k groups trials by display name, inflating scores for same-name tasks.

Open to research, tooling and evaluation-infrastructure conversations: hello@driftproofhq.com
