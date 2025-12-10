import pandas as pd
from pathlib import Path
def load_synthetic(path='data/synthetic/sample.csv'):
    p = Path(path)
    if not p.exists():
        from data.synthetic.generate_synthetic import generate
        df = generate(1000)
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(p, index=False)
    return pd.read_csv(p)
