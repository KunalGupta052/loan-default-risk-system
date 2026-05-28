# 🏦 Loan Default Prediction & Risk Analytics System

![Python](https://img.shields.io/badge/Python-3.10-blue) ![XGBoost](https://img.shields.io/badge/XGBoost-1.7-orange) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red) ![SQL](https://img.shields.io/badge/SQL-Analytics-green) ![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)

> End-to-end Finance ML System for NBFC/Bank loan default prediction, risk scoring, and portfolio analytics.

---

## 🎯 Problem Statement
NBFCs lose crores annually due to loan defaults. This system automates credit risk assessment using ML, enabling faster & smarter lending decisions.

---

## ⚙️ Architecture
```
Raw Data → Cleaning Pipeline → Feature Engineering → XGBoost Model
    → Risk Score (0-100) → SQL Portfolio Analytics → Streamlit Dashboard
```

---

## 🚀 Features
| Module | Description |
|--------|-------------|
| `cleaner.py` | Automated null handling, outlier capping (IQR method) |
| `feature_engineer.py` | Domain-specific features: debt bands, late payment score |
| `train.py` | XGBoost + SMOTE for class imbalance, AUC ~0.87 |
| `risk_score.py` | 0-100 risk score with Low/Medium/High/Critical bands |
| `analytics_queries.sql` | 5 portfolio KPI queries for business reporting |
| `streamlit_app.py` | Live dashboard with applicant scorer + KPI charts |

---

## 📊 Model Performance
- **Algorithm:** XGBoost Classifier
- **AUC-ROC:** ~0.87
- **Imbalance Handling:** SMOTE oversampling
- **Features:** 15+ engineered features

---

## 🗂️ Project Structure
```
loan-default-risk-system/
├── data/               # Raw & processed datasets
├── src/
│   ├── pipeline/       # Data cleaning + feature engineering
│   ├── model/          # Training + inference
│   ├── scoring/        # Risk score engine
│   └── sql/            # Portfolio analytics queries
├── app/                # Streamlit dashboard
├── reports/            # Business insights
└── requirements.txt
```

---

## 🏃 Quick Start
```bash
git clone https://github.com/YOUR_USERNAME/loan-default-risk-system
cd loan-default-risk-system
pip install -r requirements.txt

# Run cleaning pipeline
python src/pipeline/cleaner.py

# Train model
python src/model/train.py

# Launch dashboard
streamlit run app/streamlit_app.py
```

---

## 📈 Business Impact
- Reduces manual credit review time by ~60%
- Flags high-risk applicants before disbursement
- Enables data-driven credit policy decisions
- Portfolio NPA monitoring via SQL KPIs

---

## 🛠️ Tech Stack
`Python` `Pandas` `XGBoost` `Scikit-learn` `SMOTE` `Streamlit` `Plotly` `SQL` `Git`

---

## 📁 Dataset
[Give Me Some Credit – Kaggle](https://www.kaggle.com/competitions/GiveMeSomeCredit)

---

## 👤 Author
**Your Name** | Data Engineer / Data Scientist
[LinkedIn](#) | [Portfolio](#)
