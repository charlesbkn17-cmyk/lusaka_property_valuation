from __future__ import annotations

from pathlib import Path
import pandas as pd
import geopandas as gpd


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [str(col).strip().lower() for col in df.columns]
    return df


def load_valuation_roll(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = normalize_columns(df)

    rename_map = {
        "propertyid": "property_id",
        "property_id": "property_id",
        "valuationvalue": "valuation_value",
        "valuation_value": "valuation_value",
        "marketvalue": "valuation_value",
        "market_value": "valuation_value",
        "assessedvalue": "valuation_value",
        "assessed_value": "valuation_value",
        "propertytype": "property_type",
        "property_type": "property_type",
        "landarea": "land_area",
        "land_area": "land_area",
        "buildingarea": "building_area",
        "building_area": "building_area",
        "latitude": "latitude",
        "longitude": "longitude",
    }

    df = df.rename(columns=rename_map)

    if "property_id" not in df.columns:
        raise ValueError("Valuation file must include property_id.")
    if "valuation_value" not in df.columns:
        raise ValueError("Valuation file must include valuation_value.")

    df["valuation_value"] = pd.to_numeric(df["valuation_value"], errors="coerce")
    df = df.dropna(subset=["valuation_value"]).copy()

    if "latitude" in df.columns and "longitude" in df.columns:
        df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
        df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    df = df.drop_duplicates(subset=["property_id"]).reset_index(drop=True)
    return df


def load_geodata(path: str | Path) -> gpd.GeoDataFrame:
    return gpd.read_file(path)


def make_point_gdf(df: pd.DataFrame, x_col: str = "longitude", y_col: str = "latitude") -> gpd.GeoDataFrame:
    df = df.copy().dropna(subset=[x_col, y_col])
    geometry = gpd.points_from_xy(df[x_col], df[y_col])
    return gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
