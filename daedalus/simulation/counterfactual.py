import numpy as np
import pandas as pd

def simulate_channel_counterfactual(df, channel, multiplier=2.0):
    """
    Simulates a counterfactual where a single channel's spend is multiplied,
    and downstream metrics (impressions, clicks, conversions) are updated.
    Assumes all impressions are driven by sqrt(spend).
    """
    df_cf = df.copy()

    # Apply intervention to selected channel
    df_cf[channel] *= multiplier

    # Recalculate impressions per channel
    for ch in ["Email_Spend", "Search_Spend", "Social_Spend"]:
        df_cf[f"{ch}_Impr"] = np.sqrt(df_cf[ch]) * 40  # fixed multiplier for now

    # Recompute total impressions
    df_cf["Total_Impressions"] = df_cf[["Email_Spend_Impr", "Search_Spend_Impr", "Social_Spend_Impr"]].sum(axis=1)

    # Retain CTR and CVR from original for consistency
    ctr = df_cf["Clicks"] / df["Total_Impressions"]
    cvr = df_cf["Conversions"] / df["Clicks"]

    df_cf["Clicks"] = df_cf["Total_Impressions"] * ctr
    df_cf["Conversions"] = df_cf["Clicks"] * cvr

    return df_cf
