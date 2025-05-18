from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.inference.ipw_estimator import IPWEstimator

# Generate synthetic data
df = generate_marketing_data(n=1000)

# Initialize IPW estimator
estimator = IPWEstimator(df)

# Define treatment as high spend vs low spend
estimator.binarize_treatment("Spend")

# Estimate ATE using IPW
ate = estimator.estimate_ate(outcome_col="Conversions", covariates=["Impressions", "Clicks"])
print(f"Estimated ATE using IPW (high vs. low spend): {ate:.4f}")
