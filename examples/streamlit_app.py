#!/usr/bin/env python3
"""
CATERYA Interactive Dashboard (Streamlit)

Web interface for CATERYA evaluation framework.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import streamlit as st
import numpy as np
import plotly.graph_objects as go
from caterya import CATERYAEvaluator
from caterya.utils import generate_synthetic_dataset


# Page config
st.set_page_config(
    page_title="CATERYA - Ethical AI Evaluation",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">⚛️ CATERYA</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Physics-Inspired Ethical AI Evaluation Framework</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎛️ Configuration")
st.sidebar.markdown("---")

# Dataset parameters
st.sidebar.subheader("Dataset Parameters")
n_samples = st.sidebar.slider("Number of samples", 100, 5000, 1000, 100)
n_groups = st.sidebar.slider("Number of demographic groups", 2, 5, 2)

# Evaluation settings
st.sidebar.subheader("Evaluation Settings")
selected_pillars = st.sidebar.multiselect(
    "Select pillars to evaluate",
    ['bias', 'interpretability', 'robustness', 'transparency'],
    default=['bias', 'interpretability', 'robustness', 'transparency']
)

aggregation_method = st.sidebar.selectbox(
    "Aggregation method",
    ['geometric_mean', 'arithmetic_mean', 'harmonic_mean']
)

# Run evaluation button
run_evaluation = st.sidebar.button("🚀 Run Evaluation", type="primary", use_container_width=True)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### About
CATERYA evaluates AI trustworthiness through four physics-inspired pillars:
- **Energy Landscape** (Bias & Fairness)
- **Information Principle** (Interpretability)
- **Stability Principle** (Robustness)
- **Entanglement** (Transparency)

**Created by:** Ary HH  
**Email:** aryhharyanto@proton.me
""")

# Main content
if run_evaluation:
    with st.spinner("🔬 Running CATERYA evaluation..."):
        # Generate dataset
        dataset = generate_synthetic_dataset(n_samples=n_samples, n_groups=n_groups)
        
        # Mock model
        class MockModel:
            def predict(self, data):
                return data['predictions']
        
        model = MockModel()
        
        # Run evaluation
        evaluator = CATERYAEvaluator(config={'aggregation_method': aggregation_method})
        results = evaluator.evaluate(
            model=model,
            dataset=dataset,
            pillars=selected_pillars
        )
    
    # Display results
    st.success("✅ Evaluation completed!")
    st.markdown("---")
    
    # Main score
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🎯 CATERYA Open Score")
        
        # Create gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=results.open_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Trustworthiness", 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 30], 'color': '#ffcccc'},
                    {'range': [30, 50], 'color': '#ffe6cc'},
                    {'range': [50, 70], 'color': '#ffffcc'},
                    {'range': [70, 90], 'color': '#ccffcc'},
                    {'range': [90, 100], 'color': '#ccffee'}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)
        
        # Interpretation
        if results.open_score >= 80:
            st.success("🌟 Excellent - System demonstrates strong trustworthiness")
        elif results.open_score >= 60:
            st.warning("⚠️ Good - Minor improvements recommended")
        elif results.open_score >= 40:
            st.warning("⚠️ Moderate - Significant improvements needed")
        else:
            st.error("❌ Poor - Critical ethical issues detected")
    
    st.markdown("---")
    
    # Pillar scores
    st.markdown("### 📊 Pillar Scores")
    
    pillar_cols = st.columns(len(selected_pillars))
    pillar_names = {
        'bias': ('🔋', 'Bias & Fairness', 'Energy Landscape'),
        'interpretability': ('💡', 'Interpretability', 'Information'),
        'robustness': ('🛡️', 'Robustness', 'Stability'),
        'transparency': ('🔗', 'Transparency', 'Entanglement')
    }
    
    for col, pillar in zip(pillar_cols, selected_pillars):
        icon, name, principle = pillar_names.get(pillar, ('📋', pillar.title(), ''))
        score = results.pillar_scores.get(pillar, 0.0)
        
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{icon} {name}</h3>
                <p style="color: #666; font-size: 0.9em;">{principle}</p>
                <h2 style="color: #1f77b4;">{score:.3f}</h2>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed metrics
    st.markdown("### 🔍 Detailed Metrics")
    
    # Create bar chart
    metrics_data = list(results.metric_scores.items())
    metrics_data.sort(key=lambda x: x[1], reverse=True)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[m[1] for m in metrics_data],
        y=[m[0].replace('_', ' ').title() for m in metrics_data],
        orientation='h',
        marker=dict(
            color=[m[1] for m in metrics_data],
            colorscale='RdYlGn',
            showscale=True,
            cmin=0,
            cmax=1
        )
    ))
    
    fig.update_layout(
        title="Metric Scores (0-1 scale)",
        xaxis_title="Score",
        yaxis_title="Metric",
        height=400,
        margin=dict(l=200, r=50, t=50, b=50)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Raw data
    with st.expander("📋 View Raw Data"):
        st.json(results.to_dict())
    
    # Download results
    st.markdown("---")
    st.markdown("### 💾 Export Results")
    
    col1, col2 = st.columns(2)
    with col1:
        json_str = str(results.to_dict())
        st.download_button(
            label="📥 Download JSON",
            data=json_str,
            file_name="caterya_results.json",
            mime="application/json"
        )
    with col2:
        st.info("HTML report generation coming soon!")

else:
    # Welcome screen
    st.markdown("""
    ## Welcome to CATERYA! 👋
    
    CATERYA (Contextual, Authentic, Transparent, Ethical, Responsible, Yield-focused) 
    is a physics-inspired framework for quantifying AI trustworthiness.
    
    ### 🚀 Getting Started
    
    1. **Configure** evaluation parameters in the left sidebar
    2. **Select** which pillars you want to evaluate
    3. **Click** "Run Evaluation" to begin analysis
    4. **Explore** interactive visualizations of results
    
    ### 🔬 The Four Pillars
    
    #### 1. Bias & Fairness → Energy Landscape Principle
    AI systems, like physical systems, seek local minima. Bias represents energy 
    wells that trap models in unfair configurations.
    
    #### 2. Interpretability → Information Principle
    True understanding requires information authenticity—distinguishing genuine 
    comprehension from statistical pattern matching.
    
    #### 3. Robustness → Stability Principle
    Ethical AI must remain stable across contexts, like fundamental constants in physics.
    
    #### 4. Transparency & Accountability → Entanglement Principle
    Every AI output is entangled with its training data, model architecture, and human decisions.
    
    ---
    
    ### 📚 Learn More
    
    - [GitHub Repository](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework)
    - [Documentation](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/tree/main/docs)
    - [Contributing Guide](https://github.com/AryHHAry/CATERYA-Ethical-AI-Evaluation-Framework/blob/main/CONTRIBUTING.md)
    
    ---
    
    *"Between the particles of computation and the singular star of human consciousness, we measure trust."*
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>CATERYA v0.1.0 | Created and maintained by Ary HH | Apache 2.0 License</p>
    <p>⚛️ Physics-Inspired AI Ethics | 🌍 Open Source | 🤝 Community-Driven</p>
</div>
""", unsafe_allow_html=True)
