from __future__ import annotations

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from backend.features import prepare_X_y


def train_model(df: pd.DataFrame, target_col: str = "valuation_value", save_path: str | Path | None = None):
    X, y, feature_cols = prepare_X_y(df, target_col)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = HistGradientBoostingRegressor(
        learning_rate=0.05,
        max_depth=8,
        max_leaf_nodes=31,
        random_state=42,
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)
    mae = mean_absolute_error(y_test, predictions)
    mape = mean_absolute_percentage_error(y_test, predictions) * 100
    r2 = r2_score(y_test, predictions)

    metrics = {
        "rmse": float(rmse),
        "mae": float(mae),
        "mape": float(mape),
        "r2": float(r2),
    }

    if save_path is not None:
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, save_path)

    return model, metrics, feature_cols


def load_model(path: str | Path):
    return joblib.load(path)


def predict(model, X: pd.DataFrame):
    return model.predict(X)
