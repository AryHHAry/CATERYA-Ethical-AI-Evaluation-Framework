"""
Tests for CATERYA metrics.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import pytest
import numpy as np
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from caterya.metrics import (
    FairnessEnergyMap,
    SymmetryIndex,
    EthicalEnergyScore,
    InformationAuthenticity,
    get_metric
)
from caterya.utils import generate_synthetic_dataset


class TestBiasMetrics:
    """Test suite for bias and fairness metrics."""
    
    def test_fairness_energy_map(self):
        """Test FairnessEnergyMap metric."""
        metric = FairnessEnergyMap()
        dataset = generate_synthetic_dataset(n_samples=100)
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        score = metric.compute(MockModel(), dataset)
        assert 0 <= score <= 1
        assert isinstance(score, float)
    
    def test_symmetry_index_perfect_fairness(self):
        """Test SymmetryIndex with perfectly fair predictions."""
        metric = SymmetryIndex()
        
        # Create perfectly balanced dataset
        dataset = {
            'predictions': np.ones(100),  # All same predictions
            'labels': np.ones(100),
            'groups': np.random.randint(0, 2, 100)
        }
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        score = metric.compute(MockModel(), dataset)
        assert score >= 0.95  # Should be close to 1
    
    def test_symmetry_index_bounds(self):
        """Test SymmetryIndex stays within bounds."""
        metric = SymmetryIndex()
        dataset = generate_synthetic_dataset(n_samples=100)
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        score = metric.compute(MockModel(), dataset)
        min_bound, max_bound = metric.bounds
        assert min_bound <= score <= max_bound
    
    def test_ethical_energy_score(self):
        """Test EthicalEnergyScore metric."""
        metric = EthicalEnergyScore()
        dataset = generate_synthetic_dataset(n_samples=100)
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        score = metric.compute(MockModel(), dataset)
        assert 0 <= score <= 1


class TestMetricRegistry:
    """Test suite for metric registry."""
    
    def test_get_metric_by_name(self):
        """Test retrieving metric by name."""
        metric_class = get_metric('symmetry_index')
        assert metric_class == SymmetryIndex
    
    def test_get_metric_invalid_name(self):
        """Test error handling for invalid metric name."""
        with pytest.raises(ValueError):
            get_metric('nonexistent_metric')
    
    def test_all_registered_metrics_instantiable(self):
        """Test that all registered metrics can be instantiated."""
        from caterya.metrics import METRIC_REGISTRY
        
        for name, metric_class in METRIC_REGISTRY.items():
            metric = metric_class()
            assert metric is not None
            assert hasattr(metric, 'compute')
            assert hasattr(metric, 'bounds')


class TestMetricBase:
    """Test suite for base metric functionality."""
    
    def test_metric_bounds(self):
        """Test metric bounds property."""
        metric = FairnessEnergyMap()
        bounds = metric.bounds
        assert isinstance(bounds, tuple)
        assert len(bounds) == 2
        assert bounds[0] <= bounds[1]
    
    def test_metric_interpretation(self):
        """Test metric interpretation."""
        metric = SymmetryIndex()
        
        # Test different score levels
        assert "Excellent" in metric.interpret(0.95)
        assert "Good" in metric.interpret(0.75)
        assert "Moderate" in metric.interpret(0.55)
        assert "Poor" in metric.interpret(0.35)
    
    def test_metric_validate_score(self):
        """Test score validation."""
        metric = SymmetryIndex()
        
        # Test in-bounds score
        assert metric.validate_score(0.5) == 0.5
        
        # Test out-of-bounds scores (should be clipped)
        assert metric.validate_score(-0.1) == 0.0
        assert metric.validate_score(1.5) == 1.0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
