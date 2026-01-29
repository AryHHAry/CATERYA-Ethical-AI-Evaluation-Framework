"""
Tests for CATERYA core functionality.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from caterya import CATERYAEvaluator, EvaluationResults
from caterya.utils import generate_synthetic_dataset


class TestCATERYAEvaluator:
    """Test suite for CATERYAEvaluator class."""
    
    def test_evaluator_initialization(self):
        """Test evaluator can be initialized."""
        evaluator = CATERYAEvaluator()
        assert evaluator is not None
        assert evaluator.aggregation_method == 'geometric_mean'
    
    def test_evaluator_with_config(self):
        """Test evaluator with custom configuration."""
        config = {
            'aggregation_method': 'arithmetic_mean',
            'pillar_weights': {'bias': 0.5, 'interpretability': 0.5}
        }
        evaluator = CATERYAEvaluator(config=config)
        assert evaluator.aggregation_method == 'arithmetic_mean'
    
    def test_evaluate_synthetic_data(self):
        """Test evaluation with synthetic dataset."""
        evaluator = CATERYAEvaluator()
        dataset = generate_synthetic_dataset(n_samples=100)
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        model = MockModel()
        results = evaluator.evaluate(model, dataset)
        
        assert isinstance(results, EvaluationResults)
        assert 0 <= results.open_score <= 100
        assert len(results.pillar_scores) > 0
    
    def test_evaluate_single_pillar(self):
        """Test evaluation of single pillar."""
        evaluator = CATERYAEvaluator()
        dataset = generate_synthetic_dataset(n_samples=100)
        
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        model = MockModel()
        results = evaluator.evaluate(model, dataset, pillars=['bias'])
        
        assert 'bias' in results.pillar_scores
        assert len(results.pillar_scores) == 1
    
    def test_list_available_metrics(self):
        """Test listing of available metrics."""
        evaluator = CATERYAEvaluator()
        metrics = evaluator.list_available_metrics()
        
        assert 'bias' in metrics
        assert 'interpretability' in metrics
        assert 'robustness' in metrics
        assert 'transparency' in metrics
        assert len(metrics['bias']) > 0


class TestEvaluationResults:
    """Test suite for EvaluationResults class."""
    
    def test_results_initialization(self):
        """Test results can be initialized."""
        results = EvaluationResults()
        assert results.open_score == 0.0
        assert isinstance(results.pillar_scores, dict)
        assert isinstance(results.metric_scores, dict)
    
    def test_results_to_dict(self):
        """Test conversion to dictionary."""
        results = EvaluationResults(
            open_score=75.5,
            pillar_scores={'bias': 0.8},
            metric_scores={'symmetry_index': 0.85}
        )
        
        result_dict = results.to_dict()
        assert result_dict['open_score'] == 75.5
        assert result_dict['pillar_scores']['bias'] == 0.8
    
    def test_results_save_load(self, tmp_path):
        """Test saving and loading results."""
        results = EvaluationResults(
            open_score=75.5,
            pillar_scores={'bias': 0.8}
        )
        
        # Save
        filepath = tmp_path / "test_results.json"
        results.save(filepath)
        assert filepath.exists()
        
        # Load
        loaded_results = EvaluationResults.load(filepath)
        assert loaded_results.open_score == 75.5
        assert loaded_results.pillar_scores['bias'] == 0.8


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
