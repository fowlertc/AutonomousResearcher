# src/metrics.py  (fixed – do not edit)
#
# Metric helpers used by the evaluator.

from sklearn.metrics import f1_score, accuracy_score


def compute_metrics(y_true, y_pred):
    """Return a dict with macro_f1 and accuracy."""
    return {
        "macro_f1": round(float(f1_score(y_true, y_pred, average="macro")), 6),
        "accuracy": round(float(accuracy_score(y_true, y_pred)), 6),
    }
