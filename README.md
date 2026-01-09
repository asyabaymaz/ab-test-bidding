# ab-test-bidding
A/B test analysis comparing Facebook Maximum Bidding and Average Bidding strategies based on Purchase conversion metric.

# Overview
This project analyzes the results of an A/B test comparing two Facebook bidding strategies:
Maximum Bidding (Control Group) and Average Bidding (Test Group).
The primary success metric used in the analysis is Purchase.

# Business Problem
Facebook introduced a new bidding strategy called Average Bidding as an alternative to
the existing Maximum Bidding method.
The objective of this project is to determine whether Average Bidding leads to higher
conversion performance compared to Maximum Bidding.

# Dataset
The dataset contains website advertising performance metrics and consists of two groups:
- Control Group: Maximum Bidding
- Test Group: Average Bidding

Each group is stored on a separate sheet in the ab_testing.xlsx file.

Key variables:
- impression: Number of ad impressions  
- click: Number of ad clicks  
- purchase: Number of purchases after clicks  
- earning: Revenue generated from purchases  

# Methodology
- Data loading and preprocessing
- Assumption checks (normality and variance homogeneity)
- Independent two-sample t-test on the Purchase metric

# Results
The hypothesis test results indicate no statistically significant difference
between the Purchase means of the control and test groups (p-value > 0.05).

## Conclusion
Based on the A/B test results, Average Bidding does not provide a statistically
significant improvement in conversions compared to Maximum Bidding.
It is recommended to continue using the current bidding strategy or conduct
further testing with a larger sample size or longer test duration.
