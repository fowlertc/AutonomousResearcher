# src/data.py  (fixed – do not edit)
#
# Loads the Iris dataset and returns a fixed train/test split.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

SPLIT_SEED = 42
TEST_SIZE = 0.2


def get_train_test():
    """Return (X_train, X_test, y_train, y_test) for the Iris dataset."""
    iris = load_iris()
    X, y = iris.data, iris.target
    return train_test_split(X, y, test_size=TEST_SIZE, random_state=SPLIT_SEED, stratify=y)
