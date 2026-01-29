# CATERYA Deployment Guide

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

This guide covers deploying the CATERYA framework to various platforms, with a focus on Streamlit deployment.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Deployment](#local-deployment)
3. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
4. [Hugging Face Spaces Deployment](#hugging-face-spaces-deployment)
5. [Docker Deployment](#docker-deployment)
6. [Development Setup](#development-setup)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB+ recommended)
- **CPU**: Any modern processor (Intel i5/Ryzen 5 or better recommended)
- **GPU**: Optional (framework runs on CPU by default)

### Software Requirements

```bash
# Git
git --version

# Python
python --version  # or python3 --version

# pip
pip --version  # or pip3 --version
```

---

## Local Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework.git
cd CATERYA-Ethical-AI-Evaluation-Framework
```

### 2. Create Virtual Environment (Recommended)

```bash
# Using venv
python -m venv venv

# Activate on Linux/Mac
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install CATERYA package
pip install -e .

# Or install requirements directly
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
# From project root
streamlit run examples/streamlit_app.py

# Or with custom port
streamlit run examples/streamlit_app.py --server.port 8502
```

The app will open automatically in your browser at `http://localhost:8501`.

### 5. Run the CLI Demo (Alternative)

```bash
# Simple command-line demo
python examples/run_demo.py
```

---

## Streamlit Cloud Deployment

Streamlit Cloud provides free hosting for public repositories.

### Step 1: Prepare Repository

1. **Ensure your repository is public** on GitHub
2. **Check required files exist**:
   - `requirements.txt` ✓
   - `examples/streamlit_app.py` ✓
   - `.streamlit/config.toml` ✓

### Step 2: Deploy to Streamlit Cloud

1. **Go to**: [share.streamlit.io](https://share.streamlit.io)
2. **Sign in** with your GitHub account
3. **Click**: "New app"
4. **Configure**:
   - **Repository**: `AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework`
   - **Branch**: `main`
   - **Main file path**: `examples/streamlit_app.py`
   - **App URL** (optional): Choose a custom subdomain
5. **Click**: "Deploy!"

### Step 3: Advanced Settings (Optional)

In Streamlit Cloud dashboard:

```toml
# Advanced settings
[server]
maxUploadSize = 200
enableXsrfProtection = true

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

### Expected Deploy Time

- First deployment: 2-5 minutes
- Subsequent updates: 1-2 minutes

---

## Hugging Face Spaces Deployment

HuggingFace Spaces provides free GPU-enabled hosting.

### Step 1: Create a Space

1. **Go to**: [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Click**: "Create new Space"
3. **Configure**:
   - **Space name**: `caterya-evaluation`
   - **License**: Apache 2.0
   - **SDK**: Streamlit
   - **Hardware**: CPU Basic (free) or upgrade as needed

### Step 2: Add Files

Create these files in your Space:

**app.py** (same as streamlit_app.py):
```python
# Copy contents from examples/streamlit_app.py
```

**requirements.txt**:
```
torch>=2.0.0
transformers>=4.30.0
numpy>=1.24.0
scipy>=1.10.0
pandas>=2.0.0
plotly>=5.14.0
streamlit>=1.28.0
scikit-learn>=1.3.0
```

**README.md** (for the Space):
```markdown
---
title: CATERYA Ethical AI Evaluation
emoji: ⚛️
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
pinned: false
license: apache-2.0
---

# CATERYA - Ethical AI Evaluation Framework

Physics-inspired framework for quantifying AI trustworthiness.

[GitHub Repository](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework)
```

### Step 3: Upload Source Code

Either:
- **Upload files directly** through the web interface
- **Git push** to the Space repository:

```bash
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/caterya-evaluation
git push hf main
```

---

## Docker Deployment

### Build and Run Locally

```bash
# Build image
docker build -t caterya:latest .

# Run container
docker run -p 8501:8501 caterya:latest

# Access at http://localhost:8501
```

### Docker Compose (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  caterya:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./reports:/app/reports
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

Run with:
```bash
docker-compose up
```

### Deploy to Cloud Platforms

**AWS ECS, Google Cloud Run, Azure Container Instances**:

1. Build and push image to registry:
```bash
docker tag caterya:latest YOUR_REGISTRY/caterya:latest
docker push YOUR_REGISTRY/caterya:latest
```

2. Deploy using platform-specific tools (AWS CLI, gcloud, az CLI)

---

## Development Setup

### For Contributors

```bash
# Clone with all branches
git clone https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework.git
cd CATERYA-Ethical-AI-Evaluation-Framework

# Create development environment
python -m venv venv-dev
source venv-dev/bin/activate  # or venv-dev\Scripts\activate on Windows

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run with code coverage
pytest tests/ --cov=src/caterya --cov-report=html

# Lint code
flake8 src/ tests/
black src/ tests/ --check

# Type checking
mypy src/
```

### Setting Up Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

---

## Troubleshooting

### Common Issues

#### 1. Import Error: "No module named 'caterya'"

**Solution**:
```bash
# Make sure you're in the project root
pip install -e .

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:${PWD}/src"
```

#### 2. Streamlit Port Already in Use

**Solution**:
```bash
# Use a different port
streamlit run examples/streamlit_app.py --server.port 8502
```

#### 3. Memory Issues on Low-RAM Systems

**Solution**:
- Reduce `n_samples` in the Streamlit sidebar
- Close other applications
- Use Docker with memory limits:
```bash
docker run -m 2g -p 8501:8501 caterya:latest
```

#### 4. Slow Performance

**Optimizations**:
- Enable GPU if available (PyTorch will auto-detect)
- Use CPU-optimized PyTorch:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
- Cache results in Streamlit:
```python
@st.cache_data
def run_evaluation(...):
    ...
```

#### 5. Streamlit Cloud Deployment Fails

**Checklist**:
- ✓ Repository is public
- ✓ `requirements.txt` includes all dependencies
- ✓ Python version specified (add `runtime.txt` with `python-3.9`)
- ✓ No large files (>100MB) in repository
- ✓ Path to app file is correct

#### 6. Docker Build Fails

**Solution**:
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker build --no-cache -t caterya:latest .
```

---

## Performance Optimization Tips

### For Production Deployments

1. **Enable caching**:
```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_model():
    ...
```

2. **Use lightweight models**:
- Quantized models for faster inference
- Distilled models for lower memory usage

3. **Optimize visualization rendering**:
```python
# Use static plots for large datasets
st.pyplot(fig, use_container_width=True)

# Or downsample data before plotting
data_subset = data[::10]  # Every 10th point
```

4. **Monitor resource usage**:
```bash
# In Docker
docker stats caterya

# System-wide
htop  # or top
```

---

## Security Considerations

### For Public Deployments

1. **Rate limiting**: Implement request throttling
2. **Input validation**: Sanitize all user inputs
3. **HTTPS**: Use SSL certificates (automatic on Streamlit Cloud)
4. **Secrets management**: Use environment variables, not hard-coded values
5. **Updates**: Keep dependencies updated regularly

```bash
# Check for security vulnerabilities
pip install safety
safety check
```

---

## Monitoring and Logging

### Streamlit Cloud

- View logs in the app dashboard
- Monitor resource usage
- Set up email alerts for downtime

### Self-Hosted

```python
# Add logging to your app
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Evaluation started")
```

---

## Scaling Considerations

For high-traffic deployments:

1. **Use a load balancer** (nginx, HAProxy)
2. **Deploy multiple instances** behind the load balancer
3. **Implement caching layer** (Redis, Memcached)
4. **Use CDN** for static assets
5. **Database for results** (PostgreSQL, MongoDB)

---

## Support and Resources

- **GitHub Issues**: [Report bugs](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/issues)
- **Discussions**: [Ask questions](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/discussions)
- **Email**: aryhharyanto@proton.me
- **Documentation**: [Full docs](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/tree/main/docs)

---

## Quick Reference Commands

```bash
# Local development
streamlit run examples/streamlit_app.py

# Run tests
pytest tests/ -v

# Run demo
python examples/run_demo.py

# Docker
docker build -t caterya . && docker run -p 8501:8501 caterya

# Update dependencies
pip install -r requirements.txt --upgrade

# Check code quality
flake8 src/ && black src/ --check && mypy src/
```

---

**Happy Deploying! 🚀**

*For detailed scientific documentation, see [docs/math.md](../docs/math.md) and [docs/architecture.md](../docs/architecture.md)*
