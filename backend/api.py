from __future__ import annotations

from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from backend.model import load_model, predict

app = FastAPI(title="Lusaka Property Valuation API")
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "gradient_boosting_model.joblib"


@app.get("/")
def root():
    return {"message": "Lusaka Property Valuation API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


class PropertyPredictionRequest(BaseModel):
    land_area: float
    building_area: float | None = None
    total_building_area: float | None = None
    building_count: float | None = 0
    building_ratio: float | None = 0.0
    distance_to_school: float | None = None
    distance_to_market: float | None = None
    distance_to_hospital: float | None = None


@app.post("/predict")
def predict_property(request: PropertyPredictionRequest):
    if not MODEL_PATH.exists():
        raise HTTPException(status_code=404, detail="Model not found. Train the model first.")

    model = load_model(MODEL_PATH)

    payload = {
        "land_area": request.land_area,
        "building_area": request.building_area if request.building_area is not None else request.land_area * 0.5,
        "total_building_area": request.total_building_area if request.total_building_area is not None else request.land_area * 0.5,
        "building_count": request.building_count if request.building_count is not None else 1,
        "building_ratio": request.building_ratio if request.building_ratio is not None else 0.5,
        "distance_to_school": request.distance_to_school if request.distance_to_school is not None else 100.0,
        "distance_to_market": request.distance_to_market if request.distance_to_market is not None else 300.0,
        "distance_to_hospital": request.distance_to_hospital if request.distance_to_hospital is not None else 600.0,
    }

    df = pd.DataFrame([payload])
    prediction = predict(model, df)[0]

    return {
        "predicted_property_value": float(prediction),
        "currency": "ZMW",
    }
