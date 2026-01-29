# CATERYA - Ethical AI Evaluation Framework
# Created and maintained by Ary HH (aryhharyanto@proton.me)

FROM python:3.10-slim

LABEL maintainer="Ary HH <aryhharyanto@proton.me>"
LABEL description="CATERYA - Physics-Inspired Ethical AI Evaluation Framework"
LABEL version="0.1.0"

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install CATERYA in development mode
RUN pip install -e .

# Create directories for outputs
RUN mkdir -p /app/reports /app/data

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Default command: Run Streamlit app
CMD ["streamlit", "run", "examples/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Alternative: Run demo script
# CMD ["python", "examples/run_demo.py"]
