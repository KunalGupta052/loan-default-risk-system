import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, classification_report
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE

TARGET = 'SeriousDlqin2yrs'

def train():
    df = pd.read_csv("data/processed/featured_loans.csv")
    
    # Drop non-numeric & ID cols
    df = df.select_dtypes(include=np.number).dropna()
    
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Handle imbalance
    sm = SMOTE(random_state=42)
    X_train, y_train = sm.fit_resample(X_train, y_train)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = XGBClassifier(n_estimators=200, max_depth=5, learning_rate=0.05,
                          use_label_encoder=False, eval_metric='logloss', random_state=42)
    model.fit(X_train, y_train)
    
    y_prob = model.predict_proba(X_test)[:,1]
    y_pred = model.predict(X_test)
    
    print(f"AUC: {roc_auc_score(y_test, y_prob):.4f}")
    print(classification_report(y_test, y_pred))
    
    joblib.dump(model, "src/model/xgb_model.pkl")
    joblib.dump(scaler, "src/model/scaler.pkl")
    joblib.dump(list(df.drop(columns=[TARGET]).columns), "src/model/feature_cols.pkl")
    print("Model saved.")

if __name__ == "__main__":
    train()
