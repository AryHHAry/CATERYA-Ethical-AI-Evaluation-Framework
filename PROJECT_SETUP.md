# CATERYA Project Setup Guide

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

This guide explains how to set up, run, and deploy the CATERYA framework.

---

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)
- (Optional) Docker for containerized deployment

### Hardware Requirements

**Minimum:**
- RAM: 4GB
- Storage: 2GB free space
- CPU: Any modern processor

**Recommended:**
- RAM: 8GB+ (for larger evaluations)
- Storage: 5GB+ (with datasets)
- CPU: Multi-core processor
- GPU: Optional but beneficial for larger models

---

## 🚀 Quick Start (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework.git
cd CATERYA-Ethical-AI-Evaluation-Framework
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install in development mode
pip install -e .

# Or install from requirements.txt
pip install -r requirements.txt
```

### 4. Run Demo

```bash
# Command-line demo
python examples/run_demo.py

# Interactive web dashboard
streamlit run examples/streamlit_app.py
```

The Streamlit app will open in your browser at `http://localhost:8501`

---

## 🐳 Docker Deployment

### Build and Run

```bash
# Build Docker image
docker build -t caterya:latest .

# Run container
docker run -p 8501:8501 caterya:latest
```

### Access the Application

Open your browser and navigate to `http://localhost:8501`

---

## ☁️ Cloud Deployment Options

### Streamlit Cloud

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository
5. Set main file path: `examples/streamlit_app.py`
6. Deploy!

### Hugging Face Spaces

1. Create a new Space on [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose Streamlit as the SDK
3. Upload these files:
   - `examples/streamlit_app.py` → rename to `app.py`
   - `requirements.txt`
   - `src/` directory
4. The Space will automatically deploy

### Docker Hub

```bash
# Build and tag
docker build -t yourusername/caterya:latest .

# Push to Docker Hub
docker push yourusername/caterya:latest

# Others can then run:
docker pull yourusername/caterya:latest
docker run -p 8501:8501 yourusername/caterya:latest
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage
pytest --cov=caterya tests/

# Run specific test file
pytest tests/test_metrics.py -v
```

---

## 📦 Project Structure

```
CATERYA-Ethical-AI-Evaluation-Framework/
├── README.md                    # Main documentation
├── LICENSE                      # Apache 2.0 license
├── requirements.txt             # Python dependencies
├── setup.py                     # Package configuration
├── Dockerfile                   # Container configuration
├── .gitignore                   # Git ignore rules
│
├── docs/                        # Documentation
│   ├── math.md                  # Mathematical foundations
│   └── architecture.md          # System design
│
├── src/caterya/                # Core framework
│   ├── __init__.py
│   ├── core.py                  # Main evaluator
│   ├── metrics/                 # All metrics
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── bias.py
│   │   ├── interpretability.py
│   │   ├── robustness.py
│   │   └── transparency.py
│   ├── visualizers/             # Visualization tools
│   ├── simulators/              # Context simulators
│   └── utils/                   # Helper functions
│
├── examples/                    # Usage examples
│   ├── run_demo.py             # CLI demo
│   └── streamlit_app.py        # Web dashboard
│
├── tests/                       # Test suite
│   ├── __init__.py
│   ├── test_core.py
│   └── test_metrics.py
│
├── data/                        # Data files
│   └── synthetic/               # Example datasets
│
└── .github/                     # GitHub configuration
    └── workflows/               # CI/CD pipelines
```

---

## 💻 Development Workflow

### Making Changes

1. **Create a branch:**
   ```bash
   git checkout -b feature/my-new-feature
   ```

2. **Make your changes** to the code

3. **Run tests:**
   ```bash
   pytest tests/
   ```

4. **Format code:**
   ```bash
   black src/ tests/
   flake8 src/ tests/
   ```

5. **Commit:**
   ```bash
   git add .
   git commit -m "Add my new feature"
   ```

6. **Push and create PR:**
   ```bash
   git push origin feature/my-new-feature
   ```

### Adding New Metrics

1. Create metric class in appropriate pillar file (e.g., `src/caterya/metrics/bias.py`)
2. Register metric in `src/caterya/metrics/__init__.py`
3. Add tests in `tests/test_metrics.py`
4. Update documentation

Example:
```python
# In src/caterya/metrics/bias.py
class MyNewMetric(Metric):
    def compute(self, model, dataset, **kwargs):
        # Your implementation
        return score
    
    @property
    def bounds(self):
        return (0.0, 1.0)

# In src/caterya/metrics/__init__.py
METRIC_REGISTRY['my_new_metric'] = MyNewMetric
```

---

## 🔧 Configuration

### Evaluation Configuration

Create a `config.yaml` file:

```yaml
evaluation:
  pillars:
    - bias
    - interpretability
    - robustness
    - transparency
  
  aggregation:
    method: "geometric_mean"  # or "arithmetic_mean", "harmonic_mean"
    weights:
      bias: 0.3
      interpretability: 0.25
      robustness: 0.25
      transparency: 0.2
```

Use in code:
```python
import yaml
from caterya import CATERYAEvaluator

with open('config.yaml') as f:
    config = yaml.safe_load(f)

evaluator = CATERYAEvaluator(config=config)
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue: Import errors**
```bash
# Solution: Install in development mode
pip install -e .
```

**Issue: Streamlit not found**
```bash
# Solution: Install streamlit
pip install streamlit
```

**Issue: CUDA errors (for GPU users)**
```bash
# Solution: Install CPU-only PyTorch
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

**Issue: Memory errors with large datasets**
```python
# Solution: Use batch processing
dataset_batches = [dataset[i:i+100] for i in range(0, len(dataset), 100)]
for batch in dataset_batches:
    results = evaluator.evaluate(model, batch)
```

---

## 📚 Additional Resources

- **Main README**: [README.md](README.md)
- **Vision Document**: [VISION.md](VISION.md)
- **Contribution Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Governance**: [GOVERNANCE.md](GOVERNANCE.md)
- **Mathematical Foundations**: [docs/math.md](docs/math.md)
- **System Architecture**: [docs/architecture.md](docs/architecture.md)

---

## 🆘 Getting Help

- **GitHub Issues**: [Report bugs or request features](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/issues)
- **GitHub Discussions**: [Ask questions or share ideas](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/discussions)
- **Email**: aryhharyanto@proton.me

---

## ✅ Checklist for First-Time Setup

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -e .`)
- [ ] Demo runs successfully (`python examples/run_demo.py`)
- [ ] Streamlit app works (`streamlit run examples/streamlit_app.py`)
- [ ] Tests pass (`pytest tests/`)
- [ ] Documentation reviewed

---

**Welcome to CATERYA! Let's build trustworthy AI together.** 🚀

*"Between particles and consciousness, we measure trust."*

**— Ary HH, Founder**
