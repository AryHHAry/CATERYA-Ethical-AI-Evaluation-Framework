import numpy as np
import pandas as pd
def generate(n=1000, seed=0):
    np.random.seed(seed)
    gender = np.random.binomial(1, 0.45, size=n)
    region = np.random.choice([0,1,2], size=n, p=[0.6,0.25,0.15])
    x1 = np.random.normal(loc=0.0 + 0.5*gender, scale=1.0, size=n)
    x2 = np.random.normal(loc=1.0 - 0.3*region, scale=1.2, size=n)
    logits = -0.2 + 0.8*x1 - 0.5*x2 + 0.6*gender - 0.4*(region==2)
    prob = 1 / (1 + np.exp(-logits))
    y = (np.random.rand(n) < prob).astype(int)
    df = pd.DataFrame({'x1':x1,'x2':x2,'gender':gender,'region':region,'y':y})
    return df
if __name__ == '__main__':
    df = generate(1000)
    df.to_csv('data/synthetic/sample.csv', index=False)
    print('Synthetic dataset written to data/synthetic/sample.csv')
