#!/usr/bin/env python
# scripts/show_best.py
#
# Prints the current best experiment result.

import json
from pathlib import Path

BEST_CONFIG_FILE = Path(__file__).parent.parent / "experiments" / "best_config.json"


def main():
    if not BEST_CONFIG_FILE.exists():
        print("No best result yet. Run: python src/run_experiment.py")
        return

    data = json.loads(BEST_CONFIG_FILE.read_text())
    print("=== Current Best Result ===")
    print(f"experiment_id : {data['experiment_id']}")
    print(f"timestamp_utc : {data['timestamp_utc']}")
    print(f"hypothesis    : {data['hypothesis']}")
    print(f"macro_f1      : {data['macro_f1']}")
    print(f"accuracy      : {data['accuracy']}")
    print(f"config        : {json.dumps(data['config'], indent=2)}")


if __name__ == "__main__":
    main()
