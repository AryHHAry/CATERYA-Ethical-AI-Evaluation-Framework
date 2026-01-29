"""
Setup configuration for CATERYA - Ethical AI Evaluation Framework

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
else:
    requirements = [
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "torch>=2.0.0",
        "scikit-learn>=1.0.0",
        "shap>=0.41.0",
        "lime>=0.2.0",
        "plotly>=5.10.0",
        "matplotlib>=3.5.0",
        "streamlit>=1.20.0",
        "tqdm>=4.60.0",
        "pyyaml>=6.0",
    ]

setup(
    name="caterya",
    version="0.1.0",
    author="Ary HH",
    author_email="aryhharyanto@proton.me",
    description="Physics-inspired framework for quantifying AI trustworthiness",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework",
    project_urls={
        "Bug Tracker": "https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/issues",
        "Documentation": "https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/tree/main/docs",
        "Source Code": "https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "isort>=5.10.0",
        ],
        "full": [
            "transformers>=4.20.0",
            "datasets>=2.0.0",
            "onnx>=1.12.0",
            "onnxruntime>=1.12.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "caterya-demo=examples.run_demo:main",
        ],
    },
    include_package_data=True,
    package_data={
        "caterya": ["data/*.json", "data/*.csv"],
    },
    keywords=[
        "ai-ethics",
        "trustworthy-ai",
        "fairness",
        "interpretability",
        "robustness",
        "transparency",
        "physics-inspired",
        "evaluation-framework",
    ],
    license="Apache-2.0",
)
