from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
SAMPLE_DATA_DIR = DATA_DIR / "sample"
MODELS_DIR = BASE_DIR / "models"

KALINGALINGA_VALUATION_FILE = SAMPLE_DATA_DIR / "kalingalinga_valuation_roll.csv"
KALINGALINGA_BUILDINGS_FILE = SAMPLE_DATA_DIR / "kalingalinga_buildings.geojson"
KALINGALINGA_AMENITIES_FILE = SAMPLE_DATA_DIR / "kalingalinga_amenities.geojson"
MODEL_PATH = MODELS_DIR / "gradient_boosting_model.joblib"
MODEL_DATA_PATH = MODELS_DIR / "model_dataset.csv"
