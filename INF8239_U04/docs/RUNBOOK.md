# Incident Runbook — complete after LAB13

1. Detection and classification: Automated pipeline check (`scripts/lab13_governance.py`) identifies gate failures or anomaly triggers; classified as REVIEW or STOP based on severity.
2. Containment authority: ML Engineer initiates containment, supported by Institutional Owner (A) and Legal/Data Scientist (C).
3. Evidence preservation: Automatically store decision logs, metrics, and report outputs in `reports/lab13/deployment_decision.json` and system logs.
4. Internal and affected-party communication: Notify affected representatives and internal stakeholders via designated incident response channels.
5. Rollback or safe baseline: Revert to the previous validated model checkpoint or suspend automated recommendations immediately.
6. Postmortem, owner and due date: Conduct root-cause analysis managed by Institutional Owner and ML Engineer within 5 business days of the incident.