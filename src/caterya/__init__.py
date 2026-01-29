"""
CATERYA - Ethical AI Evaluation Framework

A physics-inspired framework for quantifying AI trustworthiness.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

__version__ = "0.1.0"
__author__ = "Ary HH"
__email__ = "aryhharyanto@proton.me"

from .core import CATERYAEvaluator, EvaluationResults
from .metrics import (
    get_metric,
    METRIC_REGISTRY,
    # Bias & Fairness
    FairnessEnergyMap,
    SymmetryIndex,
    EthicalEnergyScore,
    # Interpretability  
    InformationAuthenticity,
    EthicalCoherenceScore,
    FeynmanTest,
    # Robustness
    EthicalHorizonMap,
    EthicalGradientAnalysis,
    HumanConstantStability,
    # Transparency
    ProvenanceMetrics,
    MoralCurvature,
    ContextualEthicsSimulator,
)

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "CATERYAEvaluator",
    "EvaluationResults",
    "get_metric",
    "METRIC_REGISTRY",
    # Metrics
    "FairnessEnergyMap",
    "SymmetryIndex",
    "EthicalEnergyScore",
    "InformationAuthenticity",
    "EthicalCoherenceScore",
    "FeynmanTest",
    "EthicalHorizonMap",
    "EthicalGradientAnalysis",
    "HumanConstantStability",
    "ProvenanceMetrics",
    "MoralCurvature",
    "ContextualEthicsSimulator",
]
