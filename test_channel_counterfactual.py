from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.simulation.counterfactual import simulate_channel_counterfactual

# Generate base data
df = generate_marketing_data(n=1000)
original_mean = df["Conversions"].mean()

# Simulate 2x Social spend only
df_cf = simulate_channel_counterfactual(df, channel="Social_Spend", multiplier=2.0)
cf_mean = df_cf["Conversions"].mean()

# Compare
print(f"Original mean conversions:     {original_mean:.2f}")
print(f"Counterfactual (2x Social):    {cf_mean:.2f}")
print(f"Estimated gain:                {cf_mean - original_mean:.2f}")
