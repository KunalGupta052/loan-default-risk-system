import streamlit as st
import pandas as pd
import plotly.express as px
import sys
sys.path.append(".")

st.set_page_config(page_title="Loan Risk Analytics", page_icon="🏦", layout="wide")
st.title("🏦 Loan Default Prediction & Risk Analytics")

# --- Sidebar: Single Applicant Scoring ---
st.sidebar.header("🔍 Applicant Risk Scorer")

revolving = st.sidebar.slider("Revolving Utilization", 0.0, 1.0, 0.3)
age = st.sidebar.number_input("Age", 18, 100, 35)
late_30 = st.sidebar.number_input("30-59 Days Late", 0, 20, 0)
debt_ratio = st.sidebar.slider("Debt Ratio", 0.0, 5.0, 0.3)
monthly_income = st.sidebar.number_input("Monthly Income", 0, 100000, 5000)
open_credit = st.sidebar.number_input("Open Credit Lines", 0, 50, 5)
late_90 = st.sidebar.number_input("90+ Days Late", 0, 20, 0)
real_estate = st.sidebar.number_input("RE Loans", 0, 20, 1)
late_60 = st.sidebar.number_input("60-89 Days Late", 0, 20, 0)
dependents = st.sidebar.number_input("Dependents", 0, 20, 0)

if st.sidebar.button("⚡ Predict Risk"):
    total_late = late_30 + late_60 + late_90
    # Simple heuristic scoring (replace with model.predict after training)
    score = min(100, round(
        (revolving * 30) + (total_late * 5) + (debt_ratio * 10) +
        (max(0, 50 - age) * 0.3), 1
    ))
    band = "Low Risk 🟢" if score<=30 else "Medium Risk 🟡" if score<=60 else "High Risk 🔴"
    action = "✅ Approve" if score<=30 else "⚠️ Review" if score<=60 else "❌ Reject"
    
    st.sidebar.metric("Risk Score", f"{score}/100")
    st.sidebar.info(f"**Band:** {band}\n\n**Action:** {action}")

# --- Main Dashboard ---
@st.cache_data
def load():
    try:
        return pd.read_csv("data/processed/clean_loans.csv")
    except:
        # Demo data if file not present
        import numpy as np
        np.random.seed(42)
        n = 1000
        return pd.DataFrame({
            'SeriousDlqin2yrs': np.random.binomial(1, 0.07, n),
            'age': np.random.randint(22, 75, n),
            'DebtRatio': np.random.uniform(0, 2, n),
            'RevolvingUtilizationOfUnsecuredLines': np.random.uniform(0, 1, n),
            'MonthlyIncome': np.random.randint(1000, 20000, n),
            'NumberOfTimes90DaysLate': np.random.randint(0, 5, n),
        })

df = load()

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Applicants", f"{len(df):,}")
col2.metric("Defaults", f"{df['SeriousDlqin2yrs'].sum():,}")
col3.metric("Default Rate", f"{df['SeriousDlqin2yrs'].mean()*100:.1f}%")
col4.metric("Avg Age", f"{df['age'].mean():.0f} yrs")

st.markdown("---")

col5, col6 = st.columns(2)

with col5:
    st.subheader("Default Rate by Age Group")
    df['age_band'] = pd.cut(df['age'], bins=[0,25,35,50,120], labels=['<25','25-35','35-50','50+'])
    age_def = df.groupby('age_band', observed=True)['SeriousDlqin2yrs'].mean().reset_index()
    age_def.columns = ['Age Band','Default Rate']
    fig = px.bar(age_def, x='Age Band', y='Default Rate', color='Default Rate',
                 color_continuous_scale='Reds', text_auto='.1%')
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("Debt Ratio Distribution")
    fig2 = px.histogram(df, x='DebtRatio', color='SeriousDlqin2yrs',
                        nbins=50, barmode='overlay',
                        color_discrete_map={0:'steelblue', 1:'red'},
                        labels={'SeriousDlqin2yrs':'Defaulted'})
    st.plotly_chart(fig2, use_container_width=True)

col7, col8 = st.columns(2)

with col7:
    st.subheader("Late Payments vs Default")
    df['total_late'] = df['NumberOfTimes90DaysLate'].clip(0,10)
    lp = df.groupby('total_late')['SeriousDlqin2yrs'].mean().reset_index()
    fig3 = px.line(lp, x='total_late', y='SeriousDlqin2yrs', markers=True,
                   labels={'total_late':'90+ Days Late Count','SeriousDlqin2yrs':'Default Rate'})
    st.plotly_chart(fig3, use_container_width=True)

with col8:
    st.subheader("Portfolio Risk Distribution")
    df['risk_score'] = (df['RevolvingUtilizationOfUnsecuredLines']*30 +
                        df['NumberOfTimes90DaysLate']*5 +
                        df['DebtRatio']*10).clip(0,100)
    df['risk_band'] = pd.cut(df['risk_score'], bins=[0,30,60,80,100],
                              labels=['Low','Medium','High','Critical'])
    rb = df['risk_band'].value_counts().reset_index()
    fig4 = px.pie(rb, names='risk_band', values='count',
                  color_discrete_sequence=['green','orange','red','darkred'])
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.caption("Built by: [Your Name] | Loan Default Risk System | NBFC Analytics")
