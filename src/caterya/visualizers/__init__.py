"""
Visualization module for CATERYA.

Created and maintained by Ary HH (aryhharyanto@proton.me)
"""

from pathlib import Path
from typing import Union
import json


def generate_all_visualizations(results, output_dir: Union[str, Path] = './reports'):
    """
    Generate HTML visualizations for evaluation results.
    
    Args:
        results: EvaluationResults object
        output_dir: Directory to save visualizations
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save results as JSON
    results_path = output_dir / 'results.json'
    results.save(results_path)
    
    # Generate simple HTML report
    html_content = generate_html_report(results)
    report_path = output_dir / 'report.html'
    with open(report_path, 'w') as f:
        f.write(html_content)
    
    print(f"✓ Visualizations saved to {output_dir}")
    print(f"  - Results JSON: {results_path}")
    print(f"  - HTML Report: {report_path}")


def generate_html_report(results):
    """Generate a simple HTML report."""
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>CATERYA Evaluation Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }}
        .score {{
            font-size: 48px;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin: 30px 0;
        }}
        .pillar {{
            background: #ecf0f1;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }}
        .metric {{
            padding: 8px;
            margin: 5px 0;
            background: white;
            border-left: 3px solid #3498db;
        }}
    </style>
</head>
<body>
    <h1>CATERYA Evaluation Report</h1>
    <div class="score">
        Trust Score: {results.open_score:.1f}/100
    </div>
    
    <h2>Pillar Scores</h2>
    {"".join([f'<div class="pillar"><strong>{name.title()}:</strong> {score:.2f}</div>' 
              for name, score in results.pillar_scores.items()])}
    
    <h2>Metric Details</h2>
    {"".join([f'<div class="metric">{name}: {score:.3f}</div>' 
              for name, score in results.metric_scores.items()])}
</body>
</html>
"""
    return html


__all__ = ['generate_all_visualizations', 'generate_html_report']
