# Model Card — complete after LAB13

## Intended use
Prioritization of synthetic risk cases for human review (Decision Support System with Human-in-the-Loop oversight).

## Out-of-scope use
1. Automatic intervention, automated punitive actions, or sanctions without human review.
2. Direct automated eligibility decisions for individuals or communities.
3. Official emergency or disaster declarations.

## Data and split
- Dataset: `territorial_risk_synthetic.csv`
- Sensitive features audited: `protected_group`, `age_band`
- Excluded direct identifiers: `name`, `document_number`, `email`, `phone`

## Global and subgroup evaluation
- Global Accuracy: 0.7188 (71.88%)
- Global Recall: 0.7174 (71.74%) (Exceeds minimum gate requirement of `min_recall: 0.68`)
- Fairness Auditing (Fairlearn):
  - Recall Gap (`recall_gap`): 0.1376 (13.76%) <= 0.16 (Passes quality gate)
  - FPR Gap (`fpr_gap`): 0.1250 (12.50%) <= 0.16 (Passes quality gate)
  - Causal Justification: Disparities in smaller subgroups (e.g., N=59 in group G2) reflect sample size variation rather than causal model discrimination.

## Green AI evidence
- Selected Model: LightGBM (`lgbm`)
- Model File Size: 3.56 KB (Limit: <= 1024 KB)
- Training Time: 0.028 seconds
- Inference Latency: 0.0155 ms (Limit: <= 500 ms)
- Conclusion: LightGBM is ~82% lighter and significantly more efficient than baseline tree models, minimizing energy consumption and carbon footprint in production deployment.

## Limitations, human oversight and appeal
- Limitations: Synthetic dataset bounds generalization; performance depends on data quality and stability.
- Human Oversight (HITL): The DSS prioritizes cases and presents evidence, but final review, appeal, and decisions remain strictly under human accountability (RACI: Institutional Owner / Product Owner).

## Owner and review date
- Owner: Marlin García / INF8239 - Gobernanza e Inteligencia Artificial
- Review Date: October 2026
- Version: 1.0.0 (Lab 13 / Unidad 04)