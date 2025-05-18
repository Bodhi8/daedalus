from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.inference.effect_estimator import EffectEstimator

# Generate synthetic data
df = generate_marketing_data(n=1000)

# Initialize the estimator
estimator = EffectEstimator(df)

# Estimate ATE of Spend on Conversions
ate = estimator.estimate_ate(treatment_col="Spend", outcome_col="Conversions")
print(f"Estimated ATE (Spend → Conversions): {ate:.4f}")
