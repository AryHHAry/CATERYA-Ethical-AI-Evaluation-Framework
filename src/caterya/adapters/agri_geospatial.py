"""Adapter for agritech geospatial data (simple utilities)
- handle raster/vector placeholders and small integrations
"""
import numpy as np
import pandas as pd

def encode_latlon(df, lat_col='lat', lon_col='lon'):
    # simple positional features
    df['lat_sin'] = np.sin(np.deg2rad(df[lat_col]))
    df['lon_cos'] = np.cos(np.deg2rad(df[lon_col]))
    return df

def sample_field_patches(df, patch_size=16):
    # placeholder: create synthetic patch features
    n = len(df)
    patches = np.random.randn(n, patch_size)
    cols = [f'patch_{i}' for i in range(patch_size)]
    return pd.DataFrame(patches, columns=cols)
