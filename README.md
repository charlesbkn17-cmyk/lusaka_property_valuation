# GIS and Machine Learning-Based Automated Valuation Model for Property Tax Assessment in Lusaka

This repository implements a practical GIS and machine learning-based Automated Valuation Model (AVM) for property tax assessment in Lusaka, with a specific valuation-gap workflow for Kalingalinga.

The system is designed to:
- load and clean property valuation records
- load building footprints for a target area
- perform spatial matching between valuation records and mapped buildings
- identify properties that are missing from the valuation roll
- estimate values for missing properties using a Gradient Boosting regressor
- provide a dashboard for viewing recorded and missing properties

## Key feature: Kalingalinga valuation gap detection

The demo dataset is prepared to simulate a real scenario in Kalingalinga:
- 12 existing valuation records are loaded
- more than 12 buildings are mapped in the study area
- the system detects which buildings are not represented in the valuation roll
- the missing properties are reported as additional properties in the area

This matches the requirement that the system should show more than 12 properties in Kalingalinga rather than only the original 12 records.

## Repository structure

```text
lusaka_property_valuation/
├── README.md
├── requirements.txt
├── config.py
├── dashboard.py
├── scripts/
│   └── train_model.py
├── backend/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── geospatial.py
│   ├── features.py
│   ├── model.py
│   ├── pipeline.py
│   └── api.py
├── data/
│   └── sample/
│       ├── kalingalinga_valuation_roll.csv
│       ├── kalingalinga_buildings.geojson
│       └── kalingalinga_amenities.geojson
├── models/
│   └── .gitkeep
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Train the model

```bash
python scripts/train_model.py
```

## Run the API

```bash
uvicorn backend.api:app --reload
```

Open:
- http://127.0.0.1:8000/docs

## Run the dashboard

```bash
streamlit run dashboard.py
```

## Demo scenario

The sample Kalingalinga dataset contains:
- 12 recorded properties in the valuation roll
- 19 mapped building footprints in the study area
- 7 unmatched or missing properties identified by spatial comparison

This means the system can show a total of more than 12 properties in Kalingalinga when the gap analysis is applied.

## Expected outputs

The model produces:
- property value prediction for matched and missing properties
- property gap summary
- counts of identified properties versus recorded properties
- valuation gap metrics
- RMSE, MAE, MAPE, and R²

## Notes

This repository is designed as a working prototype for a thesis or municipal pilot project. For a real deployment, swap the sample data with actual Lusaka City Council valuation records and building-footprint layers.
