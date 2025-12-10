from .metrics import summary_metrics
def evaluate(model, X, y, sensitive):
    y_pred = model.predict(X)
    return summary_metrics(y, y_pred, sensitive)
