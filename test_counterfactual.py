from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.simulation.counterfactual import simulate_counterfactual

# Generate original data
df = generate_marketing_data(n=1000)
original_mean = df["Conversions"].mean()

# Simulate counterfactual: double the spend
df_cf = simulate_counterfactual(df, treatment_col="Spend", multiplier=2.0)
cf_mean = df_cf["Conversions"].mean()

# Compare
print(f"Original average conversions:     {original_mean:.2f}")
print(f"Counterfactual average conversions (2x Spend): {cf_mean:.2f}")
