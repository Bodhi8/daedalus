import matplotlib.pyplot as plt
from daedalus.mechanics.data_generator import generate_marketing_data

# Generate data
df = generate_marketing_data(n=1000)

# Sort by Spend for smooth plotting
df_sorted = df.sort_values("Spend")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(df_sorted["Spend"], df_sorted["Conversions"], label="Conversions", color="blue")
plt.xlabel("Spend ($)")
plt.ylabel("Conversions")
plt.title("Diminishing Returns: Spend vs. Conversions")
plt.grid(True)
plt.tight_layout()
plt.show()
