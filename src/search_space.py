# src/search_space.py
#
# This is the ONLY file the autonomous agent is allowed to edit.
# Change the values in SEARCH_CONFIG to propose a new experiment.

SEARCH_CONFIG = {
    "n_estimators": 100,
    "max_depth": None,
    "min_samples_split": 2,
    "criterion": "gini",
    "random_state": 42,
}

# Short description of why you chose these values.
# The runner copies this into the results log as the "hypothesis" field.
HYPOTHESIS = "Baseline config: default scikit-learn RandomForestClassifier settings."
