-- 1. Default rate by age band
SELECT age_band,
       COUNT(*) AS total,
       SUM(SeriousDlqin2yrs) AS defaults,
       ROUND(100.0 * SUM(SeriousDlqin2yrs) / COUNT(*), 2) AS default_rate_pct
FROM loans
GROUP BY age_band
ORDER BY default_rate_pct DESC;

-- 2. Average debt ratio by risk band
SELECT risk_band,
       ROUND(AVG(DebtRatio), 3) AS avg_debt_ratio,
       COUNT(*) AS applicants
FROM loans
GROUP BY risk_band;

-- 3. Late payment distribution
SELECT total_late_payments,
       COUNT(*) AS count,
       ROUND(100.0 * SUM(SeriousDlqin2yrs)/COUNT(*), 2) AS default_rate
FROM loans
GROUP BY total_late_payments
ORDER BY total_late_payments;

-- 4. High utilization vs default
SELECT high_utilization,
       COUNT(*) AS total,
       ROUND(100.0 * SUM(SeriousDlqin2yrs)/COUNT(*), 2) AS default_rate
FROM loans
GROUP BY high_utilization;

-- 5. Portfolio risk summary (KPI card)
SELECT
    COUNT(*) AS total_applicants,
    SUM(SeriousDlqin2yrs) AS total_defaults,
    ROUND(100.0 * SUM(SeriousDlqin2yrs)/COUNT(*), 2) AS overall_default_rate,
    ROUND(AVG(DebtRatio), 3) AS avg_debt_ratio,
    ROUND(AVG(age), 1) AS avg_age
FROM loans;
