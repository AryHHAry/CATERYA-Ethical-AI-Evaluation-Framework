"""
Utility functions for CATERYA.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import numpy as np


def normalize_score(score, min_val=0, max_val=1):
    """Normalize score to [0, 1] range."""
    return np.clip((score - min_val) / (max_val - min_val), 0, 1)


def generate_synthetic_dataset(n_samples=1000, n_groups=2):
    """
    Generate synthetic dataset for testing.
    
    Args:
        n_samples: Number of samples
        n_groups: Number of demographic groups
        
    Returns:
        Dictionary with predictions, labels, groups
    """
    np.random.seed(42)
    return {
        'predictions': np.random.rand(n_samples),
        'labels': np.random.randint(0, 2, n_samples),
        'groups': np.random.randint(0, n_groups, n_samples)
    }


__all__ = ['normalize_score', 'generate_synthetic_dataset']
