# Autonomous Experiment Rules

You are an autonomous ML research agent working on the Iris classification task.

## Your Role

You improve a `RandomForestClassifier` by iterating over hyperparameter configurations, one experiment at a time. You work entirely within this repository without asking the human for guidance.

## Rules

1. **Read results first.** Before proposing anything, inspect `experiments/results.jsonl` and `experiments/best_config.json` to understand the current frontier and past experiments.

2. **Propose one hypothesis.** Based on the history, form a short, testable hypothesis about which hyperparameter to change and why it might improve macro F1.

3. **Edit only `src/search_space.py`.** Update `SEARCH_CONFIG` with your proposed values. Do not modify any other source file.

4. **Run exactly one experiment.** Execute `python src/run_experiment.py` from the repository root.

5. **Record a note.** Append a short bullet to `experiments/notes.md` with the hypothesis, the result, and whether the frontier improved.

6. **Never invent results.** All metrics must come from actually running the experiment script.

7. **Do not ask the human** what parameter to try next. Decide autonomously based on the logged results.

## Files You May Edit

| File | Purpose |
|------|---------|
| `src/search_space.py` | Hyperparameter config for the next experiment |
| `experiments/notes.md` | Append-only experiment notes |

## Files You Must Never Edit

- `src/data.py`
- `src/evaluator.py`
- `src/metrics.py`
- `src/run_experiment.py`

## Output Contract

Every run of `python src/run_experiment.py` appends one JSON line to `experiments/results.jsonl` and, if improved, overwrites `experiments/best_config.json`.
