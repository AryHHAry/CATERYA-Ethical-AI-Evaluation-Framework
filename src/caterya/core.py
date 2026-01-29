"""
Core evaluation engine for CATERYA framework.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field
import numpy as np
from pathlib import Path
import json

from .metrics import get_metric, METRIC_REGISTRY


@dataclass
class EvaluationResults:
    """Container for evaluation results."""
    
    pillar_scores: Dict[str, float] = field(default_factory=dict)
    metric_scores: Dict[str, float] = field(default_factory=dict)
    open_score: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        """Convert results to dictionary."""
        return {
            'pillar_scores': self.pillar_scores,
            'metric_scores': self.metric_scores,
            'open_score': self.open_score,
            'metadata': self.metadata
        }
    
    def save(self, filepath: Union[str, Path]) -> None:
        """Save results to JSON file."""
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load(cls, filepath: Union[str, Path]) -> 'EvaluationResults':
        """Load results from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return cls(**data)
    
    def generate_visualizations(self, output_dir: Union[str, Path] = './reports') -> None:
        """Generate HTML visualizations of results."""
        from .visualizers import generate_all_visualizations
        generate_all_visualizations(self, output_dir)


class CATERYAEvaluator:
    """
    Main evaluator class for CATERYA framework.
    
    Coordinates evaluation pipeline across all four pillars:
    1. Bias & Fairness (Energy Landscape)
    2. Interpretability (Information Principle)
    3. Robustness (Stability Principle)
    4. Transparency & Accountability (Entanglement Principle)
    
    Example:
        >>> evaluator = CATERYAEvaluator()
        >>> results = evaluator.evaluate(model, dataset)
        >>> print(f"Trust Score: {results.open_score:.2f}/100")
    """
    
    PILLAR_METRICS = {
        'bias': ['fairness_energy', 'symmetry_index', 'ethical_energy'],
        'interpretability': ['information_authenticity', 'ethical_coherence', 'feynman_test'],
        'robustness': ['ethical_horizon', 'ethical_gradient', 'human_constant'],
        'transparency': ['provenance', 'moral_curvature', 'contextual_ethics']
    }
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize CATERYA evaluator.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.aggregation_method = self.config.get('aggregation_method', 'geometric_mean')
        self.pillar_weights = self.config.get('pillar_weights', {
            'bias': 0.25,
            'interpretability': 0.25,
            'robustness': 0.25,
            'transparency': 0.25
        })
    
    def evaluate(
        self,
        model: Any,
        dataset: Any,
        pillars: Optional[List[str]] = None,
        metrics: Optional[List[str]] = None,
        **kwargs
    ) -> EvaluationResults:
        """
        Run comprehensive CATERYA evaluation.
        
        Args:
            model: AI model to evaluate
            dataset: Evaluation dataset
            pillars: List of pillars to evaluate (default: all)
            metrics: List of specific metrics to evaluate (overrides pillars)
            **kwargs: Additional arguments passed to metrics
            
        Returns:
            EvaluationResults containing all scores and metadata
        """
        pillars = pillars or ['bias', 'interpretability', 'robustness', 'transparency']
        
        results = EvaluationResults(
            metadata={
                'pillars': pillars,
                'aggregation_method': self.aggregation_method,
                **kwargs
            }
        )
        
        # Determine which metrics to run
        if metrics:
            metrics_to_run = metrics
        else:
            metrics_to_run = []
            for pillar in pillars:
                metrics_to_run.extend(self.PILLAR_METRICS[pillar])
        
        # Run each metric
        for metric_name in metrics_to_run:
            try:
                metric = get_metric(metric_name)()
                score = metric.compute(model, dataset, **kwargs)
                results.metric_scores[metric_name] = score
            except Exception as e:
                print(f"Warning: Failed to compute {metric_name}: {e}")
                results.metric_scores[metric_name] = 0.0
        
        # Aggregate by pillar
        for pillar in pillars:
            pillar_metrics = [
                results.metric_scores[m] 
                for m in self.PILLAR_METRICS[pillar]
                if m in results.metric_scores
            ]
            if pillar_metrics:
                results.pillar_scores[pillar] = np.mean(pillar_metrics)
            else:
                results.pillar_scores[pillar] = 0.0
        
        # Calculate CATERYA Open Score
        results.open_score = self._calculate_open_score(results.pillar_scores)
        
        return results
    
    def evaluate_metric(
        self,
        metric_name: str,
        model: Any,
        dataset: Any,
        **kwargs
    ) -> float:
        """
        Evaluate a single metric.
        
        Args:
            metric_name: Name of metric to evaluate
            model: AI model
            dataset: Evaluation dataset
            **kwargs: Additional arguments for metric
            
        Returns:
            Metric score
        """
        metric = get_metric(metric_name)()
        return metric.compute(model, dataset, **kwargs)
    
    def _calculate_open_score(self, pillar_scores: Dict[str, float]) -> float:
        """
        Calculate unified CATERYA Open Score from pillar scores.
        
        Args:
            pillar_scores: Dictionary of pillar names to scores
            
        Returns:
            Aggregated score in range [0, 100]
        """
        scores = list(pillar_scores.values())
        
        if not scores:
            return 0.0
        
        if self.aggregation_method == 'arithmetic_mean':
            # Simple average
            aggregated = np.mean(scores)
        elif self.aggregation_method == 'geometric_mean':
            # Geometric mean (penalizes weak pillars)
            aggregated = np.prod(scores) ** (1 / len(scores))
        elif self.aggregation_method == 'harmonic_mean':
            # Harmonic mean (most conservative)
            aggregated = len(scores) / np.sum([1 / (s + 1e-10) for s in scores])
        else:
            # Default to geometric mean
            aggregated = np.prod(scores) ** (1 / len(scores))
        
        # Scale to [0, 100]
        return float(aggregated * 100)
    
    def list_available_metrics(self) -> Dict[str, List[str]]:
        """
        List all available metrics organized by pillar.
        
        Returns:
            Dictionary mapping pillar names to metric lists
        """
        return self.PILLAR_METRICS.copy()
    
    def get_metric_info(self, metric_name: str) -> Dict[str, Any]:
        """
        Get information about a specific metric.
        
        Args:
            metric_name: Name of metric
            
        Returns:
            Dictionary with metric bounds, description, etc.
        """
        metric = get_metric(metric_name)()
        return {
            'name': metric_name,
            'bounds': metric.bounds,
            'description': metric.__doc__ or "No description available"
        }
