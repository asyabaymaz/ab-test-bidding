#####################################################
# A/B Test Analysis of Conversion Rates Across Bidding Methods
#####################################################


#####################################################
#  Data Loading: Load the dataset containing the control and test group data from the ab_testing.xlsx file and assign them to separate variables.
#####################################################

import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

# Pandas Display Settings
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

dataframe_control = pd.read_excel("datasets/ab_testing.xlsx" , sheet_name="Control Group")
dataframe_test = pd.read_excel("datasets/ab_testing.xlsx" , sheet_name="Test Group")

df_control = dataframe_control.copy()
df_test = dataframe_test.copy()

#####################################################
# Basic Data Check
#####################################################

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head())
    print("##################### Tail #####################")
    print(dataframe.tail())
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df_control)
check_df(df_test)

#####################################################
# Combine Control and Test Group Data
#####################################################

#Adding group label to each dataset and combining the control and test group data

df_control["group"] = "control"
df_test["group"] = "test"
df = pd.concat([df_control, df_test], axis=0, ignore_index=False)



#####################################################
#  Defining the A/B Test Hypotheses
#####################################################

# Adım 1: Hipotezi tanımlayınız.

# H0: M1 = M2 (There is no difference in the average Purchase between the control and test groups.)
# H1: M1 != M2 (There is a difference in the average Purchase between the control and test groups.)



df.groupby("group").agg({"Purchase": "mean"})


#####################################################
# Performing the Hypothesis Test
#####################################################

# Step 1: Check the assumptions before conducting the hypothesis test: These assumptions are Normality and Variance Homogeneity.

# --------------------------------------------------
# Normality Assumption (Shapiro-Wilk Test)
# --------------------------------------------------
# H0: The data follows a normal distribution.
# H1: The data does not follow a normal distribution.
# Decision rule:
#   p < 0.05  → Reject H0
#   p ≥ 0.05  → Fail to reject H0

test_stat, pvalue = shapiro(df.loc[df["group"] == "control", "Purchase"])
print(f"Shapiro-Wilk Test (Control): Test Stat = {test_stat:.4f}, p-value = {pvalue:.4f}")
# p-value = 0.5891 → Fail to reject H0 (normality assumption is satisfied for the control group)

# --------------------------------------------------
# Variance Homogeneity (Levene Test)
# --------------------------------------------------
# H0: Variances are equal (homogeneous).
# H1: Variances are not equal.
# Decision rule:
#   p < 0.05  → Reject H0
#   p ≥ 0.05  → Fail to reject H0

test_stat, pvalue = levene(df.loc[df["group"] == "control", "Purchase"],
    df.loc[df["group"] == "test", "Purchase"])
print(f"Levene Test: Test Stat = {test_stat:.4f}, p-value = {pvalue:.4f}")
# p-value = 0.1083 → Fail to reject H0 (variance homogeneity assumption is satisfied)


#####################################################
# Select and Apply the Appropriate Hypothesis Test
#####################################################
# Based on the results of the normality and variance homogeneity tests, a parametric test is appropriate.
# Independent Two-Sample t-Test is applied.

# Hypotheses:
# H0: M1 = M2 There is no statistically significant difference in the mean Purchase between the control and test groups.
# H1: M1 ≠ M2 There is a statistically significant difference in the mean Purchase between the control and test groups.

# Decision rule:
#   p < 0.05  → Reject H0
#   p ≥ 0.05  → Fail to reject H0


test_stat, pvalue = ttest_ind(df.loc[df["group"] == "control", "Purchase"],
                              df.loc[df["group"] == "test", "Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value=0.3493

#####################################################
# Interpret the Hypothesis Test Results
#####################################################

# Based on the p-value obtained from the Independent Two-Sample t-Test:P value = 0.3493
# Since p-value ≥ 0.05, we fail to reject the null hypothesis (H0).
# This indicates that there is no statistically significant difference between the average Purchase values of the control and test groups.


#####################################################
# Step 4: Business Recommendation
#####################################################

# Based on the A/B test results, Average Bidding does not provide a statistically
# significant improvement in Purchase compared to Maximum Bidding.
# Therefore, it is recommended that the company continues using the current bidding strategy.
