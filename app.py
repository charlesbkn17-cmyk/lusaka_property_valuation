import os
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


st.set_page_config(page_title="Lusaka AVM Demo", page_icon="🏘️", layout="wide")


@st.cache_data
def build_synthetic_data():
    rng = np.random.default_rng(42)
    n = 240
    land_area = rng.uniform(180, 1000, n)
    building_area = rng.uniform(80, 450, n)
    total_building_area = building_area + rng.uniform(5, 120, n)
    building_count = rng.integers(1, 6, n)
    building_ratio = rng.uniform(0.3, 1.8, n)
    distance_to_school = rng.uniform(50, 800, n)
    distance_to_market = rng.uniform(100, 1200, n)
    distance_to_hospital = rng.uniform(200, 1500, n)

    # Realistic value formula in ZMW
    value = (
        1200 * land_area
        + 850 * building_area
        + 22000 * total_building_area / 100
        + 35000 * building_count
        - 200 * distance_to_school
        - 150 * distance_to_market
        - 100 * distance_to_hospital
        + 45000 * building_ratio
        + rng.normal(0, 15000, n)
    )

    df = pd.DataFrame(
        {
            "land_area": land_area,
            "building_area": building_area,
            "total_building_area": total_building_area,
            "building_count": building_count,
            "building_ratio": building_ratio,
            "distance_to_school": distance_to_school,
            "distance_to_market": distance_to_market,
            "distance_to_hospital": distance_to_hospital,
            "market_value": value,
        }
    )
    return df


@st.cache_resource
def train_demo_model():
    df = build_synthetic_data()
    features = [
        "land_area",
        "building_area",
        "total_building_area",
        "building_count",
        "building_ratio",
        "distance_to_school",
        "distance_to_market",
        "distance_to_hospital",
    ]
    X = df[features]
    y = df["market_value"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    metrics = {
        "RMSE": float(np.sqrt(mean_squared_error(y_test, y_pred))),
        "MAE": float(mean_absolute_error(y_test, y_pred)),
        "MAPE": float(np.mean(np.abs((y_test - y_pred) / y_test)) * 100),
        "R2": float(r2_score(y_test, y_pred)),
    }

    return model, metrics


def page_home():
    st.title("🏘️ GIS and Machine Learning-Based Automated Valuation Model")
    st.subheader("Property Tax Assessment System for Lusaka")
    st.markdown(
        """
        This public demonstration shows a GIS-informed Automated Valuation Model (AVM)
        for property tax assessment in Lusaka. The system highlights the valuation gap in
        the Kalingalinga pilot area and presents a machine learning model for estimating values.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Recorded properties", "12")
    with col2:
        st.metric("Mapped properties", "19")
    with col3:
        st.metric("Valuation gap", "7 properties")

    st.info(
        "The project compares the current valuation roll against spatially mapped properties in the pilot area. "
        "The identified gap indicates that some properties are not captured by the municipal property tax database."
    )


def page_gap():
    st.header("Valuation Gap Analysis")
    recorded = 12
    mapped = 19
    gap = mapped - recorded
    percent = round((gap / mapped) * 100, 1)

    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Recorded valuation records", recorded)
    kpi2.metric("Mapped properties", mapped)
    kpi3.metric("Missing properties", f"{gap} ({percent}%)")

    chart_df = pd.DataFrame(
        {
            "Category": ["Recorded", "Missing"],
            "Count": [recorded, gap],
        }
    )
    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(chart_df.set_index("Category"))
    with col2:
        # Create pie chart using matplotlib
        fig, ax = plt.subplots(figsize=(6, 4))
        sizes = [recorded, gap]
        labels = ["Officially recorded", "Missing from roll"]
        colors = ["#2ecc71", "#e74c3c"]
        ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
        ax.set_title("Property Status Distribution")
        st.pyplot(fig)

    st.markdown(
        """
        ### Interpretation
        The valuation roll contains 12 known properties, while analysis of the mapped property footprint data indicates 19 properties in the same pilot area.
        This creates a valuation gap of 7 properties, meaning some properties are currently absent from the official assessment roll and may not be contributing to municipal rates revenue.
        """
    )


def page_model():
    st.header("Property Valuation Model")
    model, metrics = train_demo_model()

    st.subheader("Model performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("RMSE", f"ZMW {metrics['RMSE']:.0f}")
    col2.metric("MAE", f"ZMW {metrics['MAE']:.0f}")
    col3.metric("MAPE", f"{metrics['MAPE']:.2f}%")
    col4.metric("R²", f"{metrics['R2']:.2f}")

    st.markdown(
        """
        The primary model is a Gradient Boosting Regressor, selected because it captures non-linear relationships among land, building, and accessibility variables.
        """
    )

    st.subheader("Predict a property value")
    with st.form("property_input"):
        land_area = st.number_input("Land area (m²)", min_value=50.0, value=420.0)
        building_area = st.number_input("Building area (m²)", min_value=20.0, value=180.0)
        total_building_area = st.number_input("Total building area (m²)", min_value=20.0, value=210.0)
        building_count = st.number_input("Building count", min_value=1, value=2, step=1)
        building_ratio = st.number_input("Building ratio", min_value=0.1, max_value=3.0, value=0.8, step=0.1)
        distance_to_school = st.number_input("Distance to school (m)", min_value=10.0, value=180.0)
        distance_to_market = st.number_input("Distance to market (m)", min_value=20.0, value=400.0)
        distance_to_hospital = st.number_input("Distance to hospital (m)", min_value=50.0, value=800.0)
        submitted = st.form_submit_button("Predict value")

    if submitted:
        input_df = pd.DataFrame(
            [{
                "land_area": land_area,
                "building_area": building_area,
                "total_building_area": total_building_area,
                "building_count": building_count,
                "building_ratio": building_ratio,
                "distance_to_school": distance_to_school,
                "distance_to_market": distance_to_market,
                "distance_to_hospital": distance_to_hospital,
            }]
        )
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated property value: ZMW {prediction:,.2f}")


def page_architecture():
    st.header("System Architecture and Workflow")
    st.markdown(
        """
        ### Workflow
        1. Acquire valuation records and spatial datasets.
        2. Clean and validate property and geospatial inputs.
        3. Match recorded properties with building footprints.
        4. Derive valuation features such as size, building density, and amenity proximity.
        5. Train a Gradient Boosting model for property value estimation.
        6. Display the gap report and predicted values in a dashboard.
        """
    )

    steps = [
        "Data acquisition",
        "Data cleaning",
        "Spatial matching",
        "Feature engineering",
        "Machine learning",
        "Dashboard output",
    ]
    step_cols = st.columns(len(steps))
    for i, step in enumerate(steps):
        with step_cols[i]:
            st.markdown(f"### {i + 1}\n{step}")


def main():
    with st.sidebar:
        st.image("https://images.unsplash.com/photo-1523217582562-09d0def993a6?auto=format&fit=crop&w=400&q=80", use_column_width="stretch")
        st.title("Navigation")
        page = st.radio(
            "Choose section",
            [
                "Home",
                "Valuation Gap",
                "Model",
                "System Architecture",
            ],
        )

    if page == "Home":
        page_home()
    elif page == "Valuation Gap":
        page_gap()
    elif page == "Model":
        page_model()
    else:
        page_architecture()

    st.markdown("---")
    st.caption("Lusaka Property Valuation Demo | Designed for oral examination and public demonstration")


if __name__ == "__main__":
    main()
