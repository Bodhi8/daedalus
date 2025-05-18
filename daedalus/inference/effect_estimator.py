import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class EffectEstimator:
    def __init__(self, df):
        self.df = df

    def estimate_ate(self, treatment_col, outcome_col, control_cols=[]):
        """
        Estimate the Average Treatment Effect (ATE) using linear regression.
        """
        X = self.df[[treatment_col] + control_cols]
        y = self.df[outcome_col]

        model = LinearRegression()
        model.fit(X, y)

        coef = model.coef_[0]  # Coefficient of the treatment variable
        return coef
