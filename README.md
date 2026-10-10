# Kalingalinga GIS + ML Automated Valuation Model

This repository contains a working prototype for a GIS and Machine Learning-based Automated Valuation Model (AVM) for property tax assessment in Lusaka, with a Kalingalinga valuation-gap analysis workflow.

## What the project demonstrates

The project is designed to show that the number of properties in a given area can be greater than the number listed in the valuation record. In the sample Kalingalinga scenario:

- 12 properties are recorded in the valuation roll
- 19 building footprints are mapped in the study area
- 7 properties are identified as missing or unmatched in the valuation roll

This supports the valuation-gap objective of the study: the system can show more than 12 properties in Kalingalinga when spatial data are compared against the valuation roll.

## This repository includes

- valuation data loader
- spatial comparison workflow
- building footprint processing
- amenity-based feature engineering
- Gradient Boosting regression model
- dashboard for property value prediction
- API for model inference

## Data expectations

The project expects three main dataset types:

### 1. Valuation roll CSV
A CSV file containing at least the following columns:

```csv
property_id,latitude,longitude,valuation_value,property_type,land_area,building_area
KAL_01,-15.3950,28.3230,760000,Residential,320,190
KAL_02,-15.3960,28.3245,820000,Residential,350,210
```

### 2. Building footprints GeoJSON
A polygon dataset representing structures in the pilot area.

### 3. Amenity data GeoJSON
A point dataset with amenities such as schools, markets, hospitals, roads, and other relevant facilities.

## Sample Kalingalinga data included

The repository includes a sample Kalingalinga dataset that demonstrates the gap-analysis workflow.

### Sample valuation roll
File: `data/sample/kalingalinga_valuation_roll.csv`

### Sample building footprints
File: `data/sample/kalingalinga_buildings.geojson`

### Sample amenity data
File: `data/sample/kalingalinga_amenities.geojson`

## Kalingalinga valuation gap summary

The sample scenario in this repository is based on the following interpretation:

```text
Recorded properties: 12
Mapped properties in the area: 19
Missing or unmatched properties: 7
```

Therefore, the system can report more than 12 properties in Kalingalinga after performing the spatial comparison.

## Project structure

```text
lusaka_property_valuation/
├── README.md
├── requirements.txt
├── config.py
├── dashboard.py
├── backend/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── geospatial.py
│   ├── features.py
│   ├── model.py
│   ├── pipeline.py
│   └── api.py
├── scripts/
│   └── train_model.py
├── data/
│   └── sample/
│       ├── kalingalinga_valuation_roll.csv
│       ├── kalingalinga_buildings.geojson
│       └── kalingalinga_amenities.geojson
├── models/
│   └── .gitkeep
├── .gitignore
└── .venv/
```

## Running the project

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Train the model

```bash
python scripts/train_model.py
```

### Run the dashboard

```bash
streamlit run dashboard.py
```

### Run the API

```bash
uvicorn backend.api:app --reload
```

Then open the API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Academic interpretation of the model output

The valuation-gap workflow supports the following interpretation:

> The existing valuation roll contains 12 recorded properties. However, spatial comparison with mapped building footprints in the Kalingalinga pilot area identified 19 properties. The difference of 7 properties indicates that some properties were absent from the valuation roll and therefore not represented in the tax assessment database. This suggests that the current valuation records undercount the actual property stock in the area and may contribute to a reduction in municipal revenue collection.

## Notes

This repository is intended as a working prototype and demonstration of the valuation-gap logic for a thesis project. Replace the sample data with actual operating data from Lusaka City Council and geospatial sources when conducting the full study.
