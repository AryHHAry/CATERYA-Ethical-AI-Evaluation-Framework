"""
Base classes for CATERYA metrics.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

from abc import ABC, abstractmethod
from typing import Any, Tuple


class Metric(ABC):
    """
    Abstract base class for all CATERYA metrics.
    
    All metrics must implement:
    - compute(): Calculate the metric value
    - bounds: Define the valid range
    - interpret(): Provide human-readable interpretation
    """
    
    def __init__(self, **config):
        """
        Initialize metric with configuration.
        
        Args:
            **config: Metric-specific configuration parameters
        """
        self.config = config
    
    @abstractmethod
    def compute(self, model: Any, dataset: Any, **kwargs) -> float:
        """
        Compute the metric value.
        
        Args:
            model: AI model to evaluate
            dataset: Evaluation dataset
            **kwargs: Additional arguments
            
        Returns:
            Metric score (typically in [0, 1])
        """
        pass
    
    @property
    @abstractmethod
    def bounds(self) -> Tuple[float, float]:
        """
        Return the theoretical bounds of the metric.
        
        Returns:
            Tuple of (min_value, max_value)
        """
        pass
    
    def interpret(self, value: float) -> str:
        """
        Provide human-readable interpretation of metric value.
        
        Args:
            value: Metric score
            
        Returns:
            Interpretation string
        """
        # Default implementation with threshold-based interpretation
        min_val, max_val = self.bounds
        normalized = (value - min_val) / (max_val - min_val)
        
        if normalized >= 0.9:
            return "Excellent"
        elif normalized >= 0.7:
            return "Good"
        elif normalized >= 0.5:
            return "Moderate"
        elif normalized >= 0.3:
            return "Poor"
        else:
            return "Critical"
    
    def validate_score(self, score: float) -> float:
        """
        Validate that score is within bounds.
        
        Args:
            score: Computed score
            
        Returns:
            Score clipped to valid range
        """
        min_val, max_val = self.bounds
        return max(min_val, min(max_val, score))
    
    def __str__(self) -> str:
        """String representation of metric."""
        return f"{self.__class__.__name__}(bounds={self.bounds})"
    
    def __repr__(self) -> str:
        """Detailed representation of metric."""
        return f"{self.__class__.__name__}(config={self.config})"
