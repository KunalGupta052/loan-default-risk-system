"""
Risk Score: 0-100 (higher = riskier)
Bands: Low (0-30), Medium (31-60), High (61-80), Critical (81-100)
"""

def compute_risk_score(default_prob: float) -> dict:
    score = round(default_prob * 100, 1)
    if score <= 30:
        band = "Low Risk"
        color = "green"
        action = "Approve"
    elif score <= 60:
        band = "Medium Risk"
        color = "orange"
        action = "Review"
    elif score <= 80:
        band = "High Risk"
        color = "red"
        action = "Reject or Collateral Required"
    else:
        band = "Critical Risk"
        color = "darkred"
        action = "Reject"
    
    return {
        "risk_score": score,
        "band": band,
        "color": color,
        "recommended_action": action
    }

if __name__ == "__main__":
    for p in [0.05, 0.35, 0.65, 0.88]:
        print(compute_risk_score(p))
