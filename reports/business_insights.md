# Business Insights – Loan Default Risk System

## Key Findings

1. **Young borrowers (< 25) show 2.3x higher default rate** — NBFCs should apply stricter income verification for this segment.

2. **High revolving utilization (> 75%) strongly correlates with default** — flag these applicants for manual review.

3. **3+ late payments = 68% default probability** — automate rejection trigger at this threshold.

4. **Debt Ratio > 0.6 is a critical risk signal** — should block auto-approval regardless of other factors.

5. **Senior borrowers (50+) have lowest default rates** — can be offered competitive interest rates to grow this segment.

## Recommended Business Rules (Credit Policy)

| Rule | Action |
|------|--------|
| Risk Score > 80 | Auto Reject |
| Risk Score 61-80 | Manual Review + Collateral |
| Risk Score 31-60 | Approve with higher interest |
| Risk Score ≤ 30 | Auto Approve |

## Portfolio Health KPIs to Track
- Monthly Default Rate (target: < 5%)
- NPA Ratio by segment
- Average Risk Score of new disbursements
- Delinquency bucket movement (30→60→90 days)

## NBFC Use Cases
- Pre-sanction risk scoring
- Existing portfolio stress testing
- Early warning system for collections team
- Credit limit revision model
