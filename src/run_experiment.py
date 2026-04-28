# src/run_experiment.py  (fixed – do not edit)
#
# Runs one experiment: loads data, trains, evaluates, logs result.

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

# Ensure project root is on the path when run as a script
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data import get_train_test
from src.evaluator import train_and_predict
from src.metrics import compute_metrics
from src.search_space import HYPOTHESIS, SEARCH_CONFIG

EXPERIMENTS_DIR = Path(__file__).parent.parent / "experiments"
RESULTS_FILE = EXPERIMENTS_DIR / "results.jsonl"
BEST_CONFIG_FILE = EXPERIMENTS_DIR / "best_config.json"


def _load_best_macro_f1() -> float:
    """Return the best macro F1 seen so far, or -1 if no results yet."""
    if not BEST_CONFIG_FILE.exists():
        return -1.0
    data = json.loads(BEST_CONFIG_FILE.read_text())
    return float(data.get("macro_f1", -1.0))


def _load_last_experiment_id() -> str | None:
    """Return the experiment_id of the most recent run, or None."""
    if not RESULTS_FILE.exists():
        return None
    lines = [l for l in RESULTS_FILE.read_text().splitlines() if l.strip()]
    if not lines:
        return None
    return json.loads(lines[-1]).get("experiment_id")


def run():
    EXPERIMENTS_DIR.mkdir(exist_ok=True)

    X_train, X_test, y_train, y_test = get_train_test()
    y_pred = train_and_predict(X_train, X_test, y_train, SEARCH_CONFIG)
    metrics = compute_metrics(y_test, y_pred)

    best_macro_f1 = _load_best_macro_f1()
    improved = metrics["macro_f1"] > best_macro_f1
    parent_id = _load_last_experiment_id()

    record = {
        "experiment_id": str(uuid.uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "hypothesis": HYPOTHESIS,
        "macro_f1": metrics["macro_f1"],
        "accuracy": metrics["accuracy"],
        "config": SEARCH_CONFIG,
        "improved_frontier": improved,
        "parent_experiment_id": parent_id,
    }

    with RESULTS_FILE.open("a") as fh:
        fh.write(json.dumps(record) + "\n")

    if improved:
        BEST_CONFIG_FILE.write_text(json.dumps(record, indent=2) + "\n")

    print(f"experiment_id : {record['experiment_id']}")
    print(f"hypothesis    : {record['hypothesis']}")
    print(f"macro_f1      : {record['macro_f1']}")
    print(f"accuracy      : {record['accuracy']}")
    print(f"improved      : {record['improved_frontier']}")

    return record


if __name__ == "__main__":
    run()
