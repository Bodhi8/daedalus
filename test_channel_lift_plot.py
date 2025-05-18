import matplotlib.pyplot as plt
from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.simulation.counterfactual import simulate_channel_counterfactual

# Setup
channels = ["Email_Spend", "Search_Spend", "Social_Spend"]
multipliers = [0.5, 1.0, 1.5, 2.0, 2.5]

# Generate baseline data once
baseline_df = generate_marketing_data(n=1000)
baseline_mean = baseline_df["Conversions"].mean()

# Start plotting
plt.figure(figsize=(10, 6))

for channel in channels:
    lifts = []
    for m in multipliers:
        df_cf = simulate_channel_counterfactual(baseline_df, channel=channel, multiplier=m)
        lift = df_cf["Conversions"].mean() - baseline_mean
        lifts.append(lift)

    plt.plot(multipliers, lifts, marker='o', label=channel)

# Customize chart
plt.axhline(0, color='gray', linestyle='--')
plt.xlabel("Spend Multiplier")
plt.ylabel("Estimated Conversion Lift")
plt.title("Conversion Lift vs Spend Multiplier by Channel")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
