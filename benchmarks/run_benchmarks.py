import json
from caterya.dataset import load_synthetic
from caterya.models import SimpleModel
from caterya.evaluation import evaluate
if __name__ == '__main__':
    df = load_synthetic()
    X = df[['x1','x2']].values
    y = df['y'].values
    s = df['gender'].values
    model = SimpleModel()
    model.fit(X,y)
    res = evaluate(model, X, y, s)
    with open('benchmarks/results.json','w') as f:
        json.dump(res,f,indent=2)
    print('Benchmarks saved to benchmarks/results.json')
