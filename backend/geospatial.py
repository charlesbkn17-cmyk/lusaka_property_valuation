from __future__ import annotations

import geopandas as gpd
import pandas as pd


def to_utm(gdf: gpd.GeoDataFrame, target_epsg: str = "EPSG:32735") -> gpd.GeoDataFrame:
    if gdf.crs is None:
        raise ValueError("GeoDataFrame has no CRS.")
    if gdf.crs != target_epsg:
        return gdf.to_crs(target_epsg)
    return gdf


def spatial_join_properties(properties_gdf: gpd.GeoDataFrame, buildings_gdf: gpd.GeoDataFrame):
    props = to_utm(properties_gdf)
    buildings = to_utm(buildings_gdf)

    joined = gpd.sjoin(props, buildings, how="left", predicate="intersects")

    counts = joined.groupby("property_id").size().reset_index(name="building_count")
    props = props.merge(counts, on="property_id", how="left")
    props["building_count"] = props["building_count"].fillna(0)

    if "building_area" in buildings.columns:
        area_sum = joined.groupby("property_id")["building_area"].sum().reset_index(name="total_building_area")
        props = props.merge(area_sum, on="property_id", how="left")
        props["total_building_area"] = props["total_building_area"].fillna(0)

    return props


def add_amenity_features(properties_gdf: gpd.GeoDataFrame, amenities_gdf: gpd.GeoDataFrame):
    props = to_utm(properties_gdf)
    amenities = to_utm(amenities_gdf)

    if "amenity_type" in amenities.columns:
        for amenity_type in amenities["amenity_type"].dropna().unique():
            subset = amenities[amenities["amenity_type"] == amenity_type]
            if subset.empty:
                continue
            dist = props.geometry.apply(lambda geom: subset.distance(geom).min() if not subset.empty else float("nan"))
            props[f"distance_to_{amenity_type}"] = dist

    return props


def find_unmatched_properties(valuation_df: pd.DataFrame, matched_df: pd.DataFrame):
    all_ids = set(valuation_df["property_id"].tolist())
    matched_ids = set(matched_df["property_id"].tolist())
    return sorted(all_ids - matched_ids)
