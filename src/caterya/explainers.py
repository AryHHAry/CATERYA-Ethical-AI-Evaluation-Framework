# Minimal SHAP wrapper (requires shap installed)
import shap
def explain_model(model, X_sample):
    explainer = shap.Explainer(model, X_sample)
    return explainer(X_sample)
