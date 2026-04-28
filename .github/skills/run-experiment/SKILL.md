# Skill: run-experiment

## Purpose

Run a single ML experiment using the current `src/search_space.py` configuration and record the result.

## Usage

```bash
python src/run_experiment.py
```

## What It Does

1. Loads the Iris dataset via `src/data.py`.
2. Reads hyperparameters from `src/search_space.py`.
3. Trains a `RandomForestClassifier` on a fixed train split (80 / 20, seed 42).
4. Evaluates macro F1 and accuracy on the test split via `src/metrics.py`.
5. Appends a JSON line to `experiments/results.jsonl` with:
   - `experiment_id` (UUID)
   - `timestamp_utc`
   - `hypothesis`
   - `macro_f1`
   - `accuracy`
   - `config`
   - `improved_frontier`
   - `parent_experiment_id`
6. If `macro_f1` exceeds the previous best, overwrites `experiments/best_config.json`.

## Output Example

```json
{
  "experiment_id": "3f7a1b2c-...",
  "timestamp_utc": "2024-01-15T10:23:45.123456",
  "hypothesis": "Baseline config",
  "macro_f1": 0.9467,
  "accuracy": 0.9500,
  "config": {"n_estimators": 100, "max_depth": null, "min_samples_split": 2, "criterion": "gini", "random_state": 42},
  "improved_frontier": true,
  "parent_experiment_id": null
}
```

## Prerequisites

```bash
pip install -r requirements.txt
```
