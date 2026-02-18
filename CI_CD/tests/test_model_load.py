from pathlib import Path
import joblib
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = PROJECT_ROOT / "models" / "model.joblib"


def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Модель по пути {MODEL_PATH} не найдена"


def test_model_can_be_loaded_and_predict():
    model = joblib.load(MODEL_PATH)

    assert hasattr(model, "predict"), "У загруженной модели нет метода 'predict' или это не модель"


def test_model_predict():
    model = joblib.load(MODEL_PATH)

    X = pd.DataFrame([{
        "Pclass": 3,
        "Sex": "male",
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": "S",
    }])

    y_pred = model.predict(X)

    assert isinstance(y_pred, np.ndarray), "Predict модели работает некорректно"

