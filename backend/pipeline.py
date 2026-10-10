from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import pandas as pd

from backend.data_loader import load_valuation_roll, make_point_gdf
from backend.features import build_model_dataset
from backend.geospatial import add_amenity_features, spatial_join_properties
from backend.model import train_model


def run_pipeline(valuation_file: str | Path, buildings_file: str | Path, amenities_file: str | Path, save_model_path: str | Path):
    valuation_df = load_valuation_roll(valuation_file)
    properties_gdf = make_point_gdf(valuation_df)

    buildings_gdf = gpd.read_file(buildings_file)
    amenities_gdf = gpd.read_file(amenities_file)

    properties_gdf = spatial_join_properties(properties_gdf, buildings_gdf)
    properties_gdf = add_amenity_features(properties_gdf, amenities_gdf)

    model_dataset = build_model_dataset(properties_gdf)
    model_dataset.to_csv(Path(save_model_path).parent / "model_dataset.csv", index=False)

    model, metrics, feature_cols = train_model(model_dataset, save_path=save_model_path)
    return model, metrics, model_dataset
