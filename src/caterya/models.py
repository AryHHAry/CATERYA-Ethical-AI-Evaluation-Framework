from sklearn.linear_model import LogisticRegression
class SimpleModel:
    def __init__(self):
        self.model = LogisticRegression(max_iter=200)
    def fit(self, X, y, sample_weight=None):
        self.model.fit(X, y, sample_weight=sample_weight)
    def predict(self, X):
        return self.model.predict(X)
    def predict_proba(self, X):
        return self.model.predict_proba(X)[:,1]
