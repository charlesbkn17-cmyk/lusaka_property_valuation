from __future__ import annotations

from pathlib import Path

from config import KALINGALINGA_AMENITIES_FILE, KALINGALINGA_BUILDINGS_FILE, KALINGALINGA_VALUATION_FILE, MODEL_PATH
from backend.pipeline import run_pipeline


def main():
    model, metrics, dataset = run_pipeline(
        valuation_file=KALINGALINGA_VALUATION_FILE,
        buildings_file=KALINGALINGA_BUILDINGS_FILE,
        amenities_file=KALINGALINGA_AMENITIES_FILE,
        save_model_path=MODEL_PATH,
    )

    print("Training completed successfully.")
    print(f"Rows in model dataset: {len(dataset)}")
    print(f"Model metrics: {metrics}")
    print(f"Saved model to: {MODEL_PATH}")


if __name__ == "__main__":
    main()
