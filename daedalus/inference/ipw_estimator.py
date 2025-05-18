import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression

class IPWEstimator:
    def __init__(self, df):
        self.df = df.copy()

    def binarize_treatment(self, treatment_col, threshold="median"):
        if threshold == "median":
            threshold = self.df[treatment_col].median()
        self.df["T"] = (self.df[treatment_col] > threshold).astype(int)

    def estimate_ate(self, outcome_col, covariates):
        X = self.df[covariates]
        T = self.df["T"]

        # Step 1: Estimate propensity scores
        ps_model = LogisticRegression()
        ps_model.fit(X, T)
        self.df["propensity"] = ps_model.predict_proba(X)[:, 1]

        # Step 2: Calculate inverse weights
        self.df["weight"] = self.df["T"] / self.df["propensity"] + \
                            (1 - self.df["T"]) / (1 - self.df["propensity"])

        # Step 3: Fit weighted linear regression
        outcome = self.df[outcome_col]
        model = LinearRegression()
        model.fit(T.values.reshape(-1, 1), outcome, sample_weight=self.df["weight"])

        return model.coef_[0]
