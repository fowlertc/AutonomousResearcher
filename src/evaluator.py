# src/evaluator.py  (fixed – do not edit)
#
# Trains a RandomForestClassifier and returns predictions.

from sklearn.ensemble import RandomForestClassifier


def train_and_predict(X_train, X_test, y_train, config: dict):
    """Train a RandomForestClassifier using *config* and return predictions on X_test."""
    clf = RandomForestClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"],
        min_samples_split=config["min_samples_split"],
        criterion=config["criterion"],
        random_state=config["random_state"],
    )
    clf.fit(X_train, y_train)
    return clf.predict(X_test)
