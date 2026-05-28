import pandas as pd

def engineer(df):
    # Debt-to-income proxy
    df['debt_ratio_band'] = pd.cut(df['DebtRatio'], bins=[0,0.3,0.6,1,999], labels=['Low','Medium','High','Critical'])
    
    # Age risk band
    df['age_band'] = pd.cut(df['age'], bins=[0,25,35,50,120], labels=['Young','Early','Mid','Senior'])
    
    # Credit utilization flag
    df['high_utilization'] = (df['RevolvingUtilizationOfUnsecuredLines'] > 0.75).astype(int)
    
    # Late payment score
    df['total_late'] = df['NumberOfTime30-59DaysPastDueNotWorse'] + \
                       df['NumberOfTime60-89DaysPastDueNotWorse'] + \
                       df['NumberOfTimes90DaysLate']
    
    # Encode categoricals
    df = pd.get_dummies(df, columns=['debt_ratio_band','age_band'], drop_first=True)
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/processed/clean_loans.csv")
    df = engineer(df)
    df.to_csv("data/processed/featured_loans.csv", index=False)
    print(f"Features done | Shape: {df.shape}")
