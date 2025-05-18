from daedalus.mechanics.data_generator import generate_marketing_data
from daedalus.inference.effect_estimator import EffectEstimator

df = generate_marketing_data(n=1000)
channels = ["Email_Spend", "Search_Spend", "Social_Spend"]

for channel in channels:
    estimator = EffectEstimator(df)
    ate = estimator.estimate_ate(treatment_col=channel, outcome_col="Conversions", control_cols=["Total_Impressions", "Clicks"])
    print(f"ATE for {channel}: {ate:.4f}")
