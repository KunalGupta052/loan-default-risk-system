import joblib
import numpy as np
import pandas as pd

model = joblib.load("src/model/xgb_model.pkl")
scaler = joblib.load("src/model/scaler.pkl")
feature_cols = joblib.load("src/model/feature_cols.pkl")

def predict(input_dict: dict) -> dict:
    df = pd.DataFrame([input_dict])[feature_cols]
    X = scaler.transform(df)
    prob = model.predict_proba(X)[0][1]
    label = "DEFAULT" if prob >= 0.5 else "NO DEFAULT"
    return {"probability": round(float(prob), 4), "prediction": label}

if __name__ == "__main__":
    sample = {col: 0 for col in feature_cols}
    print(predict(sample))
