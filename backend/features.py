from __future__ import annotations

import pandas as pd


def build_model_dataset(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()

    for col in ["land_area", "building_area", "total_building_area", "building_count"]:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")

    if "valuation_value" not in data.columns:
        raise ValueError("Dataset does not contain valuation_value.")

    numeric_cols = ["land_area", "building_area", "total_building_area", "building_count"]
    for col in numeric_cols:
        if col in data.columns:
            data[col] = data[col].fillna(data[col].median())

    distance_cols = [c for c in data.columns if c.startswith("distance_to_")]
    for col in distance_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors="coerce")
            data[col] = data[col].fillna(data[col].median())

    if "land_area" in data.columns and "total_building_area" in data.columns:
        data["building_ratio"] = data["total_building_area"] / data["land_area"].replace(0, pd.NA)
        data["building_ratio"] = data["building_ratio"].fillna(0)

    feature_cols = [
        "property_id",
        "valuation_value",
        "land_area",
        "building_area",
        "total_building_area",
        "building_count",
        "building_ratio",
    ]

    for col in distance_cols:
        if col not in feature_cols:
            feature_cols.append(col)

    final = data[feature_cols].copy()
    return final


def prepare_X_y(df: pd.DataFrame, target_col: str = "valuation_value"):
    model_df = df.copy().dropna(subset=[target_col])
    feature_cols = [c for c in model_df.columns if c not in ["property_id", target_col]]

    X = model_df[feature_cols].apply(pd.to_numeric, errors="coerce")
    X = X.fillna(X.median(numeric_only=True))

    y = pd.to_numeric(model_df[target_col], errors="coerce")
    y = y.fillna(y.median())

    return X, y, feature_cols
