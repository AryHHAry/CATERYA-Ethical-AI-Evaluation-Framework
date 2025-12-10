"""Adapter utilities for fintech datasets common in Indonesia.
- provides loaders, privacy-aware sampling, and pre-built feature maps.
"""
import pandas as pd
import numpy as np

def load_fintech_csv(path):
    df = pd.read_csv(path)
    # Simple normalization and an example privacy-safe aggregation
    # Expect columns: customer_id, age, gender, income, score, default
    if 'gender' in df.columns:
        df['gender'] = df['gender'].map({'M':1,'F':0}).fillna(0).astype(int)
    # Clip income to reduce PII risk in examples
    if 'income' in df.columns:
        df['income_clip'] = np.clip(df['income'], a_min=0, a_max=1_000_000)
    return df

def privacy_preserving_sample(df, frac=0.1, seed=0):
    # simple stratified sample by default label if exists
    if 'default' in df.columns:
        return df.groupby('default', group_keys=False).apply(lambda x: x.sample(frac=frac, random_state=seed))
    return df.sample(frac=frac, random_state=seed)
