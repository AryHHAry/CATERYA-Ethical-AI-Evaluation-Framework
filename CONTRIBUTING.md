# Contributing to CATERYA

**Created and maintained by Ary HH (aryhharyanto@proton.me)**

Thank you for considering contributing to CATERYA! This project exists because people like you care about making AI trustworthy, measurable, and accountable.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How Can I Contribute?](#how-can-i-contribute)
3. [Development Setup](#development-setup)
4. [Pull Request Process](#pull-request-process)
5. [Coding Standards](#coding-standards)
6. [Testing Guidelines](#testing-guidelines)
7. [Documentation](#documentation)
8. [Community](#community)

---

## Code of Conduct

### Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Examples of behavior that contributes to a positive environment:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy toward other community members

**Examples of unacceptable behavior:**
- The use of sexualized language or imagery, and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by emailing aryhharyanto@proton.me. All complaints will be reviewed and investigated promptly and fairly.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned with this Code of Conduct.

**This Code of Conduct is adapted from the [Contributor Covenant, version 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).**

---

## How Can I Contribute?

### 1. Reporting Bugs

**Before submitting a bug report:**
- Check the [existing issues](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/issues) to avoid duplicates
- Update to the latest version to see if the bug persists
- Collect information: Python version, OS, hardware specs, minimal reproduction steps

**Submitting a bug report:**
- Use the bug report template
- Include a clear, descriptive title
- Provide step-by-step reproduction instructions
- Describe expected vs. actual behavior
- Include error messages, logs, and screenshots if relevant

### 2. Suggesting Enhancements

**Before submitting a feature request:**
- Check if the feature already exists or is planned (see [VISION.md](VISION.md))
- Consider if it aligns with CATERYA's physics-inspired philosophy
- Think about whether it benefits the broader community (not just your specific use case)

**Submitting a feature request:**
- Use the feature request template
- Explain the problem you're trying to solve (not just the solution you envision)
- Provide examples or use cases
- Consider edge cases and potential drawbacks

### 3. Contributing Code

**Great first contributions:**
- Fix typos or improve documentation
- Add tests for existing metrics
- Implement visualization improvements
- Create example notebooks or tutorials
- Optimize performance of existing functions

**Larger contributions:**
- New ethical metrics (e.g., Privacy Leakage Score)
- Integrations with ML frameworks (e.g., PyTorch Lightning callbacks)
- Visualization dashboards
- Dataset contributions

### 4. Contributing Metrics

CATERYA is built on quantifiable metrics. When proposing new metrics:

**Requirements:**
- **Mathematical Foundation**: Clear formula with theoretical justification
- **Physics Analogy** (preferred): How does it relate to energy, entropy, symmetry, etc.?
- **Validation**: Demonstrate it measures what it claims to measure
- **Implementation**: Working Python code with tests
- **Documentation**: Explain when to use it and how to interpret results

**Example Metric Proposal Template:**
```markdown
## Metric Name: [e.g., Privacy Leakage Score]

### Problem
What ethical concern does this address? [e.g., AI models memorizing sensitive training data]

### Physics Analogy
[e.g., Information theory: entropy of model outputs vs. training data]

### Mathematical Formulation
[LaTeX equations or clear pseudocode]

### Implementation
[Link to code or PR]

### Validation
[Experiments showing it works as intended]

### Limitations
[Known edge cases or failure modes]
```

### 5. Improving Documentation

Documentation is as important as code. We need:
- **Tutorials**: Step-by-step guides for common tasks
- **API Reference**: Docstrings for all public functions
- **Case Studies**: Real-world applications of CATERYA
- **Translations**: Making content accessible in multiple languages

---

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- (Optional) Docker for containerized development

### Installation

1. **Fork and clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/CATERYA-Ethical-AI-Evaluation-Framework.git
cd CATERYA-Ethical-AI-Evaluation-Framework
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install in development mode:**
```bash
pip install -e ".[dev]"
```

This installs CATERYA plus development dependencies (pytest, black, flake8, etc.)

4. **Verify installation:**
```bash
python -c "import caterya; print(caterya.__version__)"
pytest tests/
```

### Directory Structure

```
CATERYA-Ethical-AI-Evaluation-Framework/
├── src/caterya/              # Core framework code
│   ├── __init__.py
│   ├── core.py               # Main evaluator class
│   ├── metrics/              # All evaluation metrics
│   │   ├── __init__.py
│   │   ├── bias.py           # Fairness Energy Map, Symmetry Index
│   │   ├── interpretability.py
│   │   ├── robustness.py
│   │   └── transparency.py
│   ├── visualizers/          # Plotting and interactive visualizations
│   ├── simulators/           # Contextual Ethics Simulator
│   └── utils/                # Helper functions
├── examples/                 # Usage examples
│   ├── run_demo.py
│   └── streamlit_app.py
├── tests/                    # Test suite
│   ├── test_metrics.py
│   ├── test_core.py
│   └── test_visualizers.py
├── data/synthetic/          # Example datasets
├── docs/                    # Extended documentation
└── requirements.txt
```

---

## Pull Request Process

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Naming conventions:**
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `refactor/` for code cleanup
- `test/` for test additions

### 2. Make Your Changes

- Write clear, self-documenting code
- Add docstrings to all public functions
- Include type hints where applicable
- Update documentation if needed

### 3. Test Your Changes

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_metrics.py

# Check code coverage
pytest --cov=caterya tests/
```

### 4. Format Your Code

```bash
# Auto-format with black
black src/ tests/

# Check style with flake8
flake8 src/ tests/

# Sort imports
isort src/ tests/
```

### 5. Commit Your Changes

Write clear, descriptive commit messages:

```bash
git commit -m "Add Privacy Leakage Score metric

- Implements information-theoretic privacy measure
- Includes tests and documentation
- Adds visualization to dashboard"
```

**Commit message guidelines:**
- First line: Concise summary (<50 chars)
- Blank line
- Detailed explanation (wrap at 72 chars)
- Reference issues: "Closes #123"

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub with:
- Clear title and description
- Link to related issues
- Screenshots/examples if visual changes
- Checklist of changes

### 7. Code Review

- Address reviewer feedback promptly
- Keep discussions respectful and focused
- Be open to alternative approaches
- Don't take criticism personally—we're all learning

### 8. Merge

Once approved and tests pass, a maintainer will merge your PR. Congratulations! 🎉

---

## Coding Standards

### Python Style

We follow [PEP 8](https://pep8.org/) with some modifications:

- **Line length**: 100 characters (not 79)
- **Quotes**: Double quotes for strings, single for dict keys
- **Imports**: Organized (stdlib, third-party, local)
- **Type hints**: Required for public APIs

**Example:**
```python
from typing import Dict, List, Optional

import numpy as np
import torch

from caterya.utils import normalize_scores


def calculate_fairness_energy(
    predictions: torch.Tensor,
    sensitive_attributes: torch.Tensor,
    groups: Optional[List[str]] = None
) -> Dict[str, float]:
    """
    Calculate the Fairness Energy Map for a model.
    
    Args:
        predictions: Model predictions (N,)
        sensitive_attributes: Demographic labels (N,)
        groups: Optional group names for interpretability
        
    Returns:
        Dictionary with energy scores per group
        
    Example:
        >>> preds = torch.rand(1000)
        >>> attrs = torch.randint(0, 2, (1000,))
        >>> energy = calculate_fairness_energy(preds, attrs)
        >>> print(energy['group_0'])
        0.23
    """
    # Implementation here
    pass
```

### Documentation

**All public functions must have docstrings** with:
- One-line summary
- Args (with types and descriptions)
- Returns (with type and description)
- Raises (if applicable)
- Example (for complex functions)

**Use NumPy/Google style docstrings**, not reStructuredText.

### Physics-Inspired Code

When implementing metrics with physics analogies:

```python
# Good: Clear physics connection
def ethical_energy_landscape(model, data):
    """
    Compute energy landscape where bias represents potential energy wells.
    
    Physics analogy: A ball rolling in a landscape will settle in valleys
    (local minima). High-bias configurations are deep wells that trap the
    model. This function maps the ethical terrain.
    """
    pass

# Avoid: Generic naming without conceptual grounding
def compute_bias_score(model, data):
    """Calculate some bias metric."""
    pass
```

---

## Testing Guidelines

### Types of Tests

1. **Unit Tests**: Test individual functions in isolation
2. **Integration Tests**: Test interactions between components
3. **Regression Tests**: Ensure bugs don't reappear
4. **Performance Tests**: Verify computational efficiency

### Writing Tests

```python
import pytest
import torch
from caterya.metrics import calculate_symmetry_index


def test_symmetry_index_perfect_fairness():
    """Test that perfectly fair predictions have symmetry index = 1.0"""
    predictions = torch.ones(1000) * 0.5  # All same prediction
    groups = torch.randint(0, 2, (1000,))
    
    index = calculate_symmetry_index(predictions, groups)
    
    assert abs(index - 1.0) < 1e-6, "Perfect fairness should give index=1.0"


def test_symmetry_index_complete_bias():
    """Test that completely biased predictions have symmetry index = 0.0"""
    predictions = torch.cat([torch.zeros(500), torch.ones(500)])
    groups = torch.cat([torch.zeros(500), torch.ones(500)])
    
    index = calculate_symmetry_index(predictions, groups)
    
    assert abs(index) < 1e-6, "Complete bias should give index≈0.0"


@pytest.mark.parametrize("n_samples", [100, 1000, 10000])
def test_symmetry_index_scales(n_samples):
    """Test that metric works across different dataset sizes"""
    predictions = torch.rand(n_samples)
    groups = torch.randint(0, 2, (n_samples,))
    
    index = calculate_symmetry_index(predictions, groups)
    
    assert 0 <= index <= 1, "Index must be in [0, 1]"
```

### Running Tests Locally

```bash
# All tests
pytest

# Specific file
pytest tests/test_metrics.py

# Specific test
pytest tests/test_metrics.py::test_symmetry_index_perfect_fairness

# With coverage
pytest --cov=caterya --cov-report=html tests/

# Verbose output
pytest -v tests/
```

---

## Documentation

### Writing Documentation

- **Be clear and concise**: No jargon unless necessary
- **Include examples**: Show, don't just tell
- **Explain the "why"**: Not just what the code does, but why it matters
- **Use visuals**: Diagrams, plots, animations when helpful

### Building Documentation Locally

(Future: Sphinx or MkDocs setup)

```bash
cd docs/
make html
open _build/html/index.html
```

---

## Community

### Getting Help

- **GitHub Discussions**: Ask questions, share ideas
- **Issues**: Report bugs, request features
- **Email**: aryhharyanto@proton.me for sensitive matters

### Stay Updated

- **Watch the repository**: Get notified of new releases
- **Star the project**: Show your support
- **Share with others**: Help grow the community

---

## Recognition

All contributors are recognized in:
- `AUTHORS` file (alphabetical order)
- Release notes for significant contributions
- Annual community report

We value all contributions—code, documentation, bug reports, ideas, advocacy.

---

## Questions?

If anything is unclear or you need help getting started, please ask! We were all beginners once, and we want this project to be accessible to everyone.

**Welcome to the CATERYA community. Let's build trustworthy AI together.**

---

*"Every line of code, every metric, every discussion—these are acts of hope that AI can be better."*

**— The CATERYA Community**
