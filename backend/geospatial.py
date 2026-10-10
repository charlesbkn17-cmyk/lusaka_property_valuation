from __future__ import annotations

import geopandas as gpd
import pandas as pd


def to_utm(gdf: gpd.GeoDataFrame, target_epsg: str = "EPSG:32735") -> gpd.GeoDataFrame:
    if gdf.crs is None:
        raise ValueError("GeoDataFrame does not have a CRS.")
    if gdf.crs != target_epsg:
        return gdf.to_crs(target_epsg)
    return gdf


def spatial_join_properties(properties_gdf: gpd.GeoDataFrame, buildings_gdf: gpd.GeoDataFrame):
    properties = to_utm(properties_gdf)
    buildings = to_utm(buildings_gdf)

    joined = gpd.sjoin(properties, buildings, how="left", predicate="intersects")

    counts = joined.groupby("property_id").size().reset_index(name="building_count")
    properties = properties.merge(counts, on="property_id", how="left")
    properties["building_count"] = properties["building_count"].fillna(0)

    if "building_area" in buildings.columns:
        building_area = joined.groupby("property_id")["building_area"].sum().reset_index(name="total_building_area")
        properties = properties.merge(building_area, on="property_id", how="left")
        properties["total_building_area"] = properties["total_building_area"].fillna(0)

    return properties


def add_amenity_features(properties_gdf: gpd.GeoDataFrame, amenities_gdf: gpd.GeoDataFrame):
    properties = to_utm(properties_gdf)
    amenities = to_utm(amenities_gdf)

    if "amenity_type" in amenities.columns:
        for amenity_type in amenities["amenity_type"].dropna().unique():
            subset = amenities[amenities["amenity_type"] == amenity_type]
            if subset.empty:
                continue

            dist = properties.geometry.apply(
                lambda geom: subset.distance(geom).min() if not subset.empty else float("nan")
            )
            properties[f"distance_to_{amenity_type}"] = dist

    return properties


def find_unmatched_properties(valuation_df: pd.DataFrame, matched_df: pd.DataFrame):
    all_ids = set(valuation_df["property_id"].tolist())
    matched_ids = set(matched_df["property_id"].tolist())
    return sorted(all_ids - matched_ids)
