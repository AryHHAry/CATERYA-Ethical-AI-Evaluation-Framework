"""
Bias & Fairness metrics (Pillar 1: Energy Landscape Principle).

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import numpy as np
from typing import Any, Tuple
from .base import Metric


class FairnessEnergyMap(Metric):
    """
    Measures bias as energy wells in the fairness landscape.
    
    Physics analogy: Bias creates potential energy wells that trap models
    in unfair states. This metric maps the ethical terrain.
    
    Formula: E_fairness(g) = -log P(fair|g) + λ·KL(P(ŷ|g) || P(ŷ))
    """
    
    def __init__(self, lambda_param: float = 0.5, **config):
        super().__init__(**config)
        self.lambda_param = lambda_param
    
    def compute(self, model: Any, dataset: Any, **kwargs) -> float:
        """
        Compute Fairness Energy Map score.
        
        Args:
            model: Model to evaluate
            dataset: Should contain 'predictions', 'labels', 'groups'
            
        Returns:
            Fairness energy score (lower is better, normalized to [0,1])
        """
        # Extract data
        predictions = self._get_predictions(model, dataset, **kwargs)
        groups = self._get_groups(dataset, **kwargs)
        
        # Calculate energy per group
        unique_groups = np.unique(groups)
        energies = []
        
        for group in unique_groups:
            group_mask = groups == group
            group_preds = predictions[group_mask]
            
            # Estimate fairness probability (simple heuristic)
            group_mean = np.mean(group_preds)
            overall_mean = np.mean(predictions)
            fairness_prob = 1 / (1 + np.abs(group_mean - overall_mean))
            
            # KL divergence term (simplified)
            kl_div = np.abs(group_mean - overall_mean)
            
            # Energy formula
            energy = -np.log(fairness_prob + 1e-10) + self.lambda_param * kl_div
            energies.append(energy)
        
        # Aggregate energy (weighted by group size)
        group_weights = [np.sum(groups == g) / len(groups) for g in unique_groups]
        total_energy = np.sum([e * w for e, w in zip(energies, group_weights)])
        
        # Normalize to [0, 1] (invert so higher is better)
        normalized_score = 1 / (1 + total_energy)
        
        return self.validate_score(normalized_score)
    
    @property
    def bounds(self) -> Tuple[float, float]:
        return (0.0, 1.0)
    
    def interpret(self, value: float) -> str:
        if value > 0.85:
            return "Low bias energy - Excellent fairness"
        elif value > 0.7:
            return "Moderate bias energy - Good fairness"
        elif value > 0.5:
            return "Elevated bias energy - Fairness concerns"
        else:
            return "High bias energy - Significant fairness issues"
    
    def _get_predictions(self, model, dataset, **kwargs):
        """Extract or generate predictions."""
        # Check if dataset is a dict
        if isinstance(dataset, dict) and 'predictions' in dataset:
            return np.array(dataset['predictions'])
        elif hasattr(dataset, 'predictions'):
            return np.array(dataset.predictions)
        elif 'predictions' in kwargs:
            return np.array(kwargs['predictions'])
        else:
            # Try to generate predictions
            if hasattr(model, 'predict'):
                return model.predict(dataset)
            elif callable(model):
                return model(dataset)
            else:
                # Fallback to synthetic
                size = len(dataset) if hasattr(dataset, '__len__') else 1000
                return np.random.random(size)
    
    def _get_groups(self, dataset, **kwargs):
        """Extract group labels."""
        # Check if dataset is a dict
        if isinstance(dataset, dict) and 'groups' in dataset:
            return np.array(dataset['groups'])
        elif hasattr(dataset, 'groups'):
            return np.array(dataset.groups)
        elif 'groups' in kwargs:
            return np.array(kwargs['groups'])
        else:
            # Fallback to binary random groups
            size = len(dataset) if hasattr(dataset, '__len__') else 1000
            if isinstance(dataset, dict) and 'predictions' in dataset:
                size = len(dataset['predictions'])
            return np.random.randint(0, 2, size)


class SymmetryIndex(Metric):
    """
    Measures fairness as symmetry across demographic groups.
    
    Physics analogy: Like rotational symmetry in physics, ethical systems
    should be invariant under group relabeling.
    
    Formula: S = 1 - σ(M_g) / μ(M_g)
    where M_g is a metric (e.g., accuracy) computed per group.
    """
    
    def compute(self, model: Any, dataset: Any, **kwargs) -> float:
        """
        Compute Symmetry Index.
        
        Returns:
            Symmetry score in [0, 1], where 1 = perfect symmetry
        """
        predictions = self._get_predictions(model, dataset, **kwargs)
        labels = self._get_labels(dataset, **kwargs)
        groups = self._get_groups(dataset, **kwargs)
        
        # Calculate metric per group (using accuracy as default)
        unique_groups = np.unique(groups)
        group_metrics = []
        
        for group in unique_groups:
            group_mask = groups == group
            group_preds = predictions[group_mask]
            group_labels = labels[group_mask]
            
            # Calculate accuracy for this group
            accuracy = np.mean(group_preds == group_labels) if len(group_labels) > 0 else 0.5
            group_metrics.append(accuracy)
        
        # Calculate symmetry index
        if len(group_metrics) > 0:
            std = np.std(group_metrics)
            mean = np.mean(group_metrics)
            symmetry = 1 - std / (mean + 1e-6)
        else:
            symmetry = 0.0
        
        return self.validate_score(symmetry)
    
    @property
    def bounds(self) -> Tuple[float, float]:
        return (0.0, 1.0)
    
    def interpret(self, value: float) -> str:
        if value > 0.9:
            return "Excellent symmetry - No significant group disparities"
        elif value > 0.7:
            return "Good symmetry - Minor group differences"
        elif value > 0.5:
            return "Moderate asymmetry - Notable group disparities"
        else:
            return "Poor symmetry - Significant group-based discrimination"
    
    def _get_predictions(self, model, dataset, **kwargs):
        """Extract predictions."""
        if isinstance(dataset, dict) and 'predictions' in dataset:
            return np.array(dataset['predictions'])
        elif hasattr(dataset, 'predictions'):
            return np.array(dataset.predictions)
        size = len(dataset) if hasattr(dataset, '__len__') else 1000
        if isinstance(dataset, dict) and 'predictions' in dataset:
            size = len(dataset['predictions'])
        return np.random.randint(0, 2, size)
    
    def _get_labels(self, dataset, **kwargs):
        """Extract true labels."""
        if isinstance(dataset, dict) and 'labels' in dataset:
            return np.array(dataset['labels'])
        elif hasattr(dataset, 'labels'):
            return np.array(dataset.labels)
        elif 'labels' in kwargs:
            return np.array(kwargs['labels'])
        size = len(dataset) if hasattr(dataset, '__len__') else 1000
        if isinstance(dataset, dict) and 'predictions' in dataset:
            size = len(dataset['predictions'])
        return np.random.randint(0, 2, size)
    
    def _get_groups(self, dataset, **kwargs):
        """Extract group labels."""
        if isinstance(dataset, dict) and 'groups' in dataset:
            return np.array(dataset['groups'])
        elif hasattr(dataset, 'groups'):
            return np.array(dataset.groups)
        size = len(dataset) if hasattr(dataset, '__len__') else 1000
        if isinstance(dataset, dict) and 'predictions' in dataset:
            size = len(dataset['predictions'])
        return np.random.randint(0, 2, size)


class EthicalEnergyScore(Metric):
    """
    Combines computational cost, bias magnitude, and societal impact.
    
    Formula: E = α·E_compute + β·E_bias + γ·E_impact
    """
    
    def __init__(self, weights=None, **config):
        super().__init__(**config)
        self.weights = weights or [0.3, 0.4, 0.3]  # [compute, bias, impact]
    
    def compute(self, model: Any, dataset: Any, **kwargs) -> float:
        """
        Compute Ethical Energy Score.
        
        Returns:
            Aggregated ethical energy (normalized, higher is better)
        """
        # Component 1: Computational energy (placeholder)
        compute_energy = self._estimate_compute_energy(model)
        
        # Component 2: Bias energy (use fairness energy)
        fairness_metric = FairnessEnergyMap()
        bias_energy = 1 - fairness_metric.compute(model, dataset, **kwargs)
        
        # Component 3: Impact energy (placeholder - would need stakeholder input)
        impact_energy = self._estimate_impact_energy(model, dataset)
        
        # Weighted combination
        total_energy = (
            self.weights[0] * compute_energy +
            self.weights[1] * bias_energy +
            self.weights[2] * impact_energy
        )
        
        # Invert so higher is better
        score = 1 - total_energy
        
        return self.validate_score(score)
    
    @property
    def bounds(self) -> Tuple[float, float]:
        return (0.0, 1.0)
    
    def _estimate_compute_energy(self, model):
        """Estimate computational cost (simplified)."""
        if hasattr(model, 'parameters'):
            # PyTorch model
            try:
                param_count = sum(p.numel() for p in model.parameters())
                # Normalize by common model sizes
                normalized = min(param_count / 1e9, 1.0)  # Cap at 1B params
                return normalized
            except:
                return 0.5
        return 0.5  # Default for unknown models
    
    def _estimate_impact_energy(self, model, dataset):
        """Estimate potential societal harm (placeholder)."""
        # This would ideally incorporate:
        # - Privacy risks
        # - Misuse potential
        # - Vulnerable population exposure
        # For now, return moderate risk
        return 0.3
    
    def _get_predictions(self, model, dataset, **kwargs):
        """Extract predictions."""
        if isinstance(dataset, dict) and 'predictions' in dataset:
            return np.array(dataset['predictions'])
        elif hasattr(dataset, 'predictions'):
            return np.array(dataset.predictions)
        size = len(dataset) if hasattr(dataset, '__len__') else 1000
        if isinstance(dataset, dict) and 'predictions' in dataset:
            size = len(dataset['predictions'])
        return np.random.random(size)
    
    def _get_groups(self, dataset, **kwargs):
        """Extract group labels."""
        if isinstance(dataset, dict) and 'groups' in dataset:
            return np.array(dataset['groups'])
        elif hasattr(dataset, 'groups'):
            return np.array(dataset.groups)
        size = len(dataset) if hasattr(dataset, '__len__') else 1000
        if isinstance(dataset, dict) and 'predictions' in dataset:
            size = len(dataset['predictions'])
        return np.random.randint(0, 2, size)
