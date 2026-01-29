#!/usr/bin/env python3
"""
CATERYA Demo Script

Demonstrates basic usage with synthetic data.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import sys
from pathlib import Path

# Add src to path for local development
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from caterya import CATERYAEvaluator
from caterya.utils import generate_synthetic_dataset


def main():
    print("=" * 60)
    print("CATERYA - Ethical AI Evaluation Framework")
    print("Physics-Inspired Trustworthiness Measurement")
    print("=" * 60)
    print()
    
    # Generate synthetic dataset
    print("📊 Generating synthetic dataset...")
    dataset = generate_synthetic_dataset(n_samples=1000, n_groups=2)
    print(f"   - Samples: {len(dataset['predictions'])}")
    print(f"   - Groups: {len(set(dataset['groups']))}")
    print()
    
    # Create simple mock model
    class MockModel:
        def predict(self, data):
            return data['predictions']
    
    model = MockModel()
    
    # Initialize evaluator
    print("🔬 Initializing CATERYA Evaluator...")
    evaluator = CATERYAEvaluator()
    print()
    
    # Run evaluation
    print("⚡ Running evaluation across all pillars...")
    print("   This may take a moment...")
    print()
    
    results = evaluator.evaluate(
        model=model,
        dataset=dataset,
        pillars=['bias', 'interpretability', 'robustness', 'transparency']
    )
    
    # Display results
    print("=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)
    print()
    
    # Main score
    print(f"🎯 CATERYA Open Score: {results.open_score:.2f}/100")
    print()
    
    # Interpret overall score
    if results.open_score >= 80:
        print("   ✅ Excellent trustworthiness")
    elif results.open_score >= 60:
        print("   ⚠️  Good, with room for improvement")
    elif results.open_score >= 40:
        print("   ⚠️  Moderate concerns - improvements needed")
    else:
        print("   ❌ Significant ethical issues detected")
    print()
    
    # Pillar scores
    print("📋 Pillar Scores:")
    print("-" * 60)
    
    pillar_names = {
        'bias': 'Bias & Fairness (Energy Landscape)',
        'interpretability': 'Interpretability (Information Principle)',
        'robustness': 'Robustness (Stability Principle)',
        'transparency': 'Transparency (Entanglement Principle)'
    }
    
    for pillar, score in results.pillar_scores.items():
        name = pillar_names.get(pillar, pillar.title())
        bar = '█' * int(score * 20) + '░' * (20 - int(score * 20))
        print(f"   {name:45} [{bar}] {score:.3f}")
    print()
    
    # Detailed metrics
    print("🔍 Detailed Metrics:")
    print("-" * 60)
    for metric, score in results.metric_scores.items():
        print(f"   {metric:30} {score:.4f}")
    print()
    
    # Generate visualizations
    print("📈 Generating visualizations...")
    results.generate_visualizations(output_dir='./reports')
    print()
    
    # Save results
    print("💾 Saving results...")
    results.save('./reports/evaluation_results.json')
    print("   ✓ Results saved to: ./reports/evaluation_results.json")
    print()
    
    print("=" * 60)
    print("Demo completed successfully!")
    print("Check './reports/' directory for visualizations and data.")
    print("=" * 60)


if __name__ == '__main__':
    main()
