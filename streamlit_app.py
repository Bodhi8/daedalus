import streamlit as st
import matplotlib.pyplot as plt

from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.simulation.counterfactual import simulate_channel_counterfactual

# Title
st.title("📊 Marketing Channel Causal Simulator")
st.markdown("Simulate the impact of increasing spend on a marketing channel using counterfactuals.")

# Sidebar controls
channel = st.selectbox("Choose a Channel", ["Email_Spend", "Search_Spend", "Social_Spend"])
multiplier = st.slider("Spend Multiplier", min_value=0.5, max_value=2.5, value=1.0, step=0.1)

# Generate base data
df = generate_marketing_data(n=1000)
original_mean = df["Conversions"].mean()

# Run counterfactual
df_cf = simulate_channel_counterfactual(df, channel=channel, multiplier=multiplier)
cf_mean = df_cf["Conversions"].mean()
gain = cf_mean - original_mean

# Display results
st.metric(label="Original Avg. Conversions", value=f"{original_mean:.2f}")
st.metric(label=f"Counterfactual ({multiplier:.1f}x {channel})", value=f"{cf_mean:.2f}")
st.metric(label="Estimated Lift", value=f"{gain:.2f}", delta=f"{gain:.2f}")

# Plot multiplier curve
st.subheader("📈 Lift Curve for Selected Channel")
multipliers = [0.5, 1.0, 1.5, 2.0, 2.5]
gains = []
for m in multipliers:
    df_cf_temp = simulate_channel_counterfactual(df, channel=channel, multiplier=m)
    lift = df_cf_temp["Conversions"].mean() - original_mean
    gains.append(lift)

fig, ax = plt.subplots()
ax.plot(multipliers, gains, marker='o', label=channel)
ax.axhline(0, color='gray', linestyle='--')
ax.set_xlabel("Spend Multiplier")
ax.set_ylabel("Conversion Lift")
ax.set_title(f"Lift Curve for {channel}")
ax.grid(True)
ax.legend()

st.pyplot(fig)
