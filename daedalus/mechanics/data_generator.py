import numpy as np
import pandas as pd

def generate_marketing_data(n=1000, seed=42):
    np.random.seed(seed)

    # Independent channel spends
    email_spend = np.random.uniform(50, 500, size=n)
    search_spend = np.random.uniform(100, 1000, size=n)
    social_spend = np.random.uniform(80, 800, size=n)

    # Diminishing returns: Impressions per channel
    email_impr = np.sqrt(email_spend) * np.random.uniform(30, 50, size=n)
    search_impr = np.sqrt(search_spend) * np.random.uniform(40, 60, size=n)
    social_impr = np.sqrt(social_spend) * np.random.uniform(35, 55, size=n)

    total_impr = email_impr + search_impr + social_impr

    # Clicks depend on total impressions
    ctr = np.random.uniform(0.01, 0.05, size=n)
    clicks = total_impr * ctr

    # Conversions depend on clicks
    cvr = np.random.uniform(0.02, 0.10, size=n)
    conversions = clicks * cvr

    df = pd.DataFrame({
        "Email_Spend": email_spend,
        "Search_Spend": search_spend,
        "Social_Spend": social_spend,
        "Total_Impressions": total_impr,
        "Clicks": clicks,
        "Conversions": conversions
    })

    return df
