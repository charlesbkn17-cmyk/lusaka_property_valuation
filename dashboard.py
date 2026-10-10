from __future__ import annotations

from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = Path(__file__).resolve().parent / "models" / "gradient_boosting_model.joblib"


def load_model(model_path: Path = MODEL_PATH):
    return joblib.load(model_path)


def main():
    st.set_page_config(page_title="Kalingalinga AVM Dashboard", layout="wide")
    st.title("Lusaka Property Valuation Dashboard")
    st.caption("Kalingalinga demonstration: 12 recorded properties and additional detected missing properties")

    if not MODEL_PATH.exists():
        st.warning("No trained model found. Please run: python scripts/train_model.py")
        return

    model = load_model(MODEL_PATH)
    st.success("Model loaded successfully.")

    st.subheader("Property prediction")
    with st.form("prediction_form"):
        land_area = st.number_input("Land area (m²)", min_value=0.0, value=350.0)
        building_area = st.number_input("Building area (m²)", min_value=0.0, value=200.0)
        total_building_area = st.number_input("Total building area (m²)", min_value=0.0, value=210.0)
        building_count = st.number_input("Building count", min_value=0.0, value=1.0)
        building_ratio = st.number_input("Building ratio", min_value=0.0, max_value=5.0, value=0.6)
        distance_to_school = st.number_input("Distance to school (m)", min_value=0.0, value=150.0)
        distance_to_market = st.number_input("Distance to market (m)", min_value=0.0, value=350.0)
        distance_to_hospital = st.number_input("Distance to hospital (m)", min_value=0.0, value=700.0)
        submitted = st.form_submit_button("Predict value")

    if submitted:
        sample = pd.DataFrame([
            {
                "land_area": land_area,
                "building_area": building_area,
                "total_building_area": total_building_area,
                "building_count": building_count,
                "building_ratio": building_ratio,
                "distance_to_school": distance_to_school,
                "distance_to_market": distance_to_market,
                "distance_to_hospital": distance_to_hospital,
            }
        ])
        prediction = model.predict(sample)[0]
        st.metric("Estimated property value", f"ZMW {prediction:,.2f}")

    st.subheader("Kalingalinga valuation gap summary")
    # Demo summary based on the sample dataset
    recorded_count = 12
    mapped_count = 19
    missing_count = mapped_count - recorded_count
    st.metric("Recorded valuation records", recorded_count)
    st.metric("Mapped buildings in area", mapped_count)
    st.metric("Missing/unmatched properties", missing_count)
    st.info("The system reports more than 12 total properties in Kalingalinga after comparing mapped buildings with the existing valuation roll.")


if __name__ == "__main__":
    main()
