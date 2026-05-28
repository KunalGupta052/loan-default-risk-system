import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def clean(df):
    df = df.drop_duplicates()
    num_cols = df.select_dtypes(include=np.number).columns
    for col in num_cols:
        Q1, Q3 = df[col].quantile([0.25, 0.75])
        IQR = Q3 - Q1
        df[col] = df[col].clip(Q1 - 1.5*IQR, Q3 + 1.5*IQR)
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    return df

def save(df, path):
    df.to_csv(path, index=False)
    print(f"Saved: {path} | Shape: {df.shape}")

if __name__ == "__main__":
    df = load_data("data/raw/cs-training.csv")
    df = clean(df)
    save(df, "data/processed/clean_loans.csv")
