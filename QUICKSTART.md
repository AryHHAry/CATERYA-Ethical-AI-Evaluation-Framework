# CATERYA Quick Start Guide

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

Get started with CATERYA in 5 minutes!

---

## 🚀 Installation (30 seconds)

```bash
# Clone the repository
git clone https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework.git
cd CATERYA-Ethical-AI-Evaluation-Framework

# Install
pip install -e .
```

---

## 🎯 Try It Now!

### Option 1: Interactive Web Dashboard (Recommended)

```bash
streamlit run examples/streamlit_app.py
```

This opens a web interface at `http://localhost:8501` where you can:
- ⚙️ Configure evaluation parameters
- 🔬 Run evaluations on synthetic data
- 📊 View interactive visualizations
- 💾 Download results

### Option 2: Command Line Demo

```bash
python examples/run_demo.py
```

This runs a complete evaluation and prints results to console.

---

## 💻 Basic Python Usage

### Minimal Example (3 lines)

```python
from caterya import CATERYAEvaluator
from caterya.utils import generate_synthetic_dataset

# Create evaluator
evaluator = CATERYAEvaluator()

# Generate test data
dataset = generate_synthetic_dataset(n_samples=1000)

# Mock model for demo
class MockModel:
    def predict(self, data):
        return data['predictions']

# Run evaluation
results = evaluator.evaluate(
    model=MockModel(),
    dataset=dataset
)

# Get score
print(f"Trust Score: {results.open_score:.2f}/100")
```

### Complete Example with Your Model

```python
from caterya import CATERYAEvaluator
import numpy as np

# Initialize evaluator
evaluator = CATERYAEvaluator(config={
    'aggregation_method': 'geometric_mean',
    'pillar_weights': {
        'bias': 0.25,
        'interpretability': 0.25,
        'robustness': 0.25,
        'transparency': 0.25
    }
})

# Prepare your data
# Dataset should be a dict with:
# - 'predictions': model outputs
# - 'labels': ground truth
# - 'groups': demographic groups (optional)
dataset = {
    'predictions': your_model.predict(X_test),
    'labels': y_test,
    'groups': demographic_labels  # optional
}

# Run comprehensive evaluation
results = evaluator.evaluate(
    model=your_model,
    dataset=dataset,
    pillars=['bias', 'interpretability', 'robustness', 'transparency']
)

# Access results
print(f"CATERYA Open Score: {results.open_score:.2f}/100")
print(f"\nPillar Scores:")
for pillar, score in results.pillar_scores.items():
    print(f"  {pillar}: {score:.3f}")

print(f"\nDetailed Metrics:")
for metric, score in results.metric_scores.items():
    print(f"  {metric}: {score:.4f}")

# Generate visualizations
results.generate_visualizations(output_dir='./my_results')

# Save results
results.save('./my_results/evaluation.json')
```

---

## 📊 Understanding Results

### CATERYA Open Score

Range: **0-100**

- **80-100**: ✅ Excellent trustworthiness
- **60-80**: ⚠️ Good, minor improvements needed
- **40-60**: ⚠️ Moderate concerns
- **0-40**: ❌ Significant ethical issues

### The Four Pillars

#### 1. Bias & Fairness (Energy Landscape)
Measures fairness across demographic groups using physics-inspired energy landscapes.

**Key Metrics**:
- `fairness_energy`: Bias magnitude
- `symmetry_index`: Group parity
- `ethical_energy`: Combined ethical cost

#### 2. Interpretability (Information Principle)
Evaluates authentic understanding vs. pattern matching.

**Key Metrics**:
- `information_authenticity`: True comprehension
- `ethical_coherence`: Reasoning stability
- `feynman_test`: Explainability

#### 3. Robustness (Stability Principle)
Tests ethical stability under adversarial conditions.

**Key Metrics**:
- `ethical_horizon`: Decision boundaries
- `ethical_gradient`: Decay rate
- `human_constant`: Value preservation

#### 4. Transparency & Accountability (Entanglement)
Traces provenance and accountability.

**Key Metrics**:
- `provenance`: Data/model lineage
- `moral_curvature`: Contextual adaptability
- `contextual_ethics`: Cross-cultural consistency

---

## 🔧 Common Use Cases

### Evaluate a Hugging Face Model

```python
from transformers import pipeline
from caterya import CATERYAEvaluator

# Load model
classifier = pipeline("sentiment-analysis")

# Prepare dataset
texts = ["This is great!", "This is terrible!"]
predictions = [p['label'] for p in classifier(texts)]

dataset = {
    'predictions': predictions,
    'labels': ['positive', 'negative'],
    'text': texts  # optional, for context
}

# Evaluate
evaluator = CATERYAEvaluator()
results = evaluator.evaluate(classifier, dataset)
```

### Evaluate a Custom PyTorch Model

```python
import torch
from caterya import CATERYAEvaluator

# Your model
model = YourNeuralNetwork()
model.eval()

# Get predictions
with torch.no_grad():
    predictions = model(test_data).numpy()

# Prepare dataset
dataset = {
    'predictions': predictions,
    'labels': test_labels,
    'groups': demographic_groups
}

# Evaluate
evaluator = CATERYAEvaluator()
results = evaluator.evaluate(model, dataset)
```

### Evaluate Specific Pillars

```python
# Only evaluate bias and interpretability
results = evaluator.evaluate(
    model=model,
    dataset=dataset,
    pillars=['bias', 'interpretability']
)
```

### Evaluate Specific Metrics

```python
# Run only specific metrics
results = evaluator.evaluate(
    model=model,
    dataset=dataset,
    metrics=['symmetry_index', 'feynman_test', 'provenance']
)
```

### Single Metric Evaluation

```python
# Evaluate just one metric
score = evaluator.evaluate_metric(
    metric_name='symmetry_index',
    model=model,
    dataset=dataset
)
print(f"Symmetry Index: {score:.3f}")
```

---

## 📈 Visualization Examples

### Generate HTML Reports

```python
# Automatic report generation
results.generate_visualizations(output_dir='./reports')
# Creates:
# - reports/results.json
# - reports/report.html
```

### Custom Plotly Visualizations

```python
import plotly.graph_objects as go

# Create gauge chart for Open Score
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=results.open_score,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "CATERYA Open Score"},
    gauge={'axis': {'range': [0, 100]}}
))
fig.show()

# Pillar comparison
fig = go.Figure(data=[
    go.Bar(
        x=list(results.pillar_scores.keys()),
        y=list(results.pillar_scores.values())
    )
])
fig.update_layout(title="Pillar Scores")
fig.show()
```

---

## 🐳 Docker Quick Start

```bash
# Build and run
docker build -t caterya .
docker run -p 8501:8501 caterya

# Access at http://localhost:8501
```

---

## 🌐 Deploy Online (Free!)

### Streamlit Cloud

1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy!

### Hugging Face Spaces

1. Create Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose Streamlit SDK
3. Upload `examples/streamlit_app.py` as `app.py`
4. Add `requirements.txt`
5. Done!

---

## 🔍 Next Steps

### Learn More

- **[README.md](README.md)**: Full project overview
- **[docs/math.md](docs/math.md)**: Mathematical foundations
- **[docs/architecture.md](docs/architecture.md)**: System design
- **[VISION.md](VISION.md)**: Roadmap and future plans

### Get Involved

- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Contribution guidelines
- **[GOVERNANCE.md](GOVERNANCE.md)**: Project governance
- **[GitHub Discussions](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/discussions)**: Ask questions

### Examples

Check `examples/` directory for:
- `run_demo.py`: CLI demonstration
- `streamlit_app.py`: Interactive dashboard
- More examples coming soon!

---

## 💡 Tips and Tricks

### Performance

```python
# For large datasets, use batching
batch_size = 1000
results_list = []
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    results_list.append(evaluator.evaluate(model, batch))
```

### Custom Configuration

```python
# Advanced configuration
config = {
    'aggregation_method': 'harmonic_mean',  # Most conservative
    'pillar_weights': {
        'bias': 0.4,  # Emphasize fairness
        'interpretability': 0.3,
        'robustness': 0.2,
        'transparency': 0.1
    }
}
evaluator = CATERYAEvaluator(config=config)
```

### Debugging

```python
# List available metrics
print(evaluator.list_available_metrics())

# Get metric info
info = evaluator.get_metric_info('symmetry_index')
print(info)
```

---

## ❓ FAQ

**Q: Can I use CATERYA with any ML framework?**  
A: Yes! PyTorch, TensorFlow, scikit-learn, or any custom model.

**Q: Do I need a GPU?**  
A: No, CATERYA runs efficiently on CPU.

**Q: How long does evaluation take?**  
A: Typically 1-10 seconds for 1000 samples, depending on model complexity.

**Q: Can I add custom metrics?**  
A: Yes! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Q: Is it free for commercial use?**  
A: Yes! Apache 2.0 license permits commercial use.

---

## 🆘 Getting Help

- **Bug reports**: [GitHub Issues](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/issues)
- **Questions**: [GitHub Discussions](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/discussions)
- **Email**: aryhharyanto@proton.me

---

## 📝 Minimal Working Example (Copy-Paste Ready)

```python
#!/usr/bin/env python3
"""Minimal CATERYA evaluation example"""

from caterya import CATERYAEvaluator
from caterya.utils import generate_synthetic_dataset

# Setup
evaluator = CATERYAEvaluator()
dataset = generate_synthetic_dataset(n_samples=500)

# Mock model
class SimpleModel:
    def predict(self, data):
        return data['predictions']

# Evaluate
results = evaluator.evaluate(SimpleModel(), dataset)

# Results
print(f"Trust Score: {results.open_score:.1f}/100")
print(f"\nPillars: {results.pillar_scores}")
print(f"\nReport saved to: ./reports/report.html")
results.generate_visualizations()
```

Save as `test_caterya.py` and run:
```bash
python test_caterya.py
```

---

**That's it! You're now ready to evaluate AI trustworthiness with CATERYA! 🎉**

*For advanced usage, see the full documentation and examples.*
