import argparse
from caterya.dataset import load_synthetic
from caterya.models import SimpleModel
from caterya.evaluation import evaluate
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='demo')
    args = parser.parse_args()
    df = load_synthetic()
    X = df[['x1','x2']].values
    y = df['y'].values
    s = df['gender'].values
    model = SimpleModel()
    model.fit(X,y)
    res = evaluate(model, X, y, s)
    print(res)
if __name__ == '__main__':
    main()
