"""
Metrics module for CATERYA framework.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

from .base import Metric
from .bias import FairnessEnergyMap, SymmetryIndex, EthicalEnergyScore
from .interpretability import InformationAuthenticity, EthicalCoherenceScore, FeynmanTest
from .robustness import EthicalHorizonMap, EthicalGradientAnalysis, HumanConstantStability
from .transparency import ProvenanceMetrics, MoralCurvature, ContextualEthicsSimulator


# Global metric registry
METRIC_REGISTRY = {
    # Bias & Fairness
    'fairness_energy': FairnessEnergyMap,
    'symmetry_index': SymmetryIndex,
    'ethical_energy': EthicalEnergyScore,
    
    # Interpretability
    'information_authenticity': InformationAuthenticity,
    'ethical_coherence': EthicalCoherenceScore,
    'feynman_test': FeynmanTest,
    
    # Robustness
    'ethical_horizon': EthicalHorizonMap,
    'ethical_gradient': EthicalGradientAnalysis,
    'human_constant': HumanConstantStability,
    
    # Transparency
    'provenance': ProvenanceMetrics,
    'moral_curvature': MoralCurvature,
    'contextual_ethics': ContextualEthicsSimulator,
}


def get_metric(name: str) -> type:
    """
    Get metric class by name.
    
    Args:
        name: Metric name (e.g., 'symmetry_index')
        
    Returns:
        Metric class
        
    Raises:
        ValueError: If metric name not found
    """
    if name not in METRIC_REGISTRY:
        raise ValueError(
            f"Unknown metric: {name}. "
            f"Available metrics: {list(METRIC_REGISTRY.keys())}"
        )
    return METRIC_REGISTRY[name]


__all__ = [
    'Metric',
    'get_metric',
    'METRIC_REGISTRY',
    # Bias & Fairness
    'FairnessEnergyMap',
    'SymmetryIndex',
    'EthicalEnergyScore',
    # Interpretability
    'InformationAuthenticity',
    'EthicalCoherenceScore',
    'FeynmanTest',
    # Robustness
    'EthicalHorizonMap',
    'EthicalGradientAnalysis',
    'HumanConstantStability',
    # Transparency
    'ProvenanceMetrics',
    'MoralCurvature',
    'ContextualEthicsSimulator',
]
