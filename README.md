# AutonomousResearcher

A minimal local experiment harness that demonstrates an autoresearch-style loop for machine learning experiments.

## Overview

An agent improves a `RandomForestClassifier` on the Iris dataset by editing only `src/search_space.py`, running one experiment at a time, and logging results to `experiments/results.jsonl`.

**Objective metric:** macro F1  
**Secondary metric:** accuracy

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

## Running an Experiment

```bash
python src/run_experiment.py
```

This will:
- Load the Iris dataset with a fixed train/test split
- Train a `RandomForestClassifier` using parameters from `src/search_space.py`
- Evaluate macro F1 and accuracy
- Append a JSON line to `experiments/results.jsonl`
- Update `experiments/best_config.json` if the result improves the frontier

## Show the Current Best Result

```bash
python scripts/show_best.py
```

## Using the Custom Agent in VS Code

1. Open this repository in VS Code with the GitHub Copilot extension installed.
2. Open the Copilot Chat panel.
3. Type `@experiment-runner` to activate the custom agent.
4. Use the following prompt to kick off the first autonomous experiment loop:

```
@experiment-runner Review experiments/results.jsonl and experiments/best_config.json, propose one hypothesis about which hyperparameter to change and why, update src/search_space.py with your proposed config, run the experiment with `python src/run_experiment.py`, then append a short note about the result to experiments/notes.md.
```

## Project Layout

```
.
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   ├── copilot-instructions.md
│   ├── agents/
│   │   └── experiment-runner.agent.md
│   └── skills/
│       └── run-experiment/
│           └── SKILL.md
├── src/
│   ├── __init__.py
│   ├── search_space.py      ← agent edits only this file
│   ├── data.py              ← fixed
│   ├── evaluator.py         ← fixed
│   ├── metrics.py           ← fixed
│   └── run_experiment.py    ← fixed
├── scripts/
│   └── show_best.py
└── experiments/
    ├── results.jsonl
    ├── best_config.json
    └── notes.md
```