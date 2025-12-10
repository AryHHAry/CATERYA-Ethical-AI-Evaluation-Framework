import numpy as np
from sklearn.metrics import roc_auc_score, accuracy_score
def demographic_parity_difference(y_true, y_pred, sensitive):
    groups = np.unique(sensitive)
    rates = []
    for g in groups:
        mask = (sensitive == g)
        rates.append(np.mean(y_pred[mask] == 1))
    return float(rates[0] - rates[1]) if len(rates)>1 else 0.0
def equalized_odds_difference(y_true, y_pred, sensitive):
    groups = np.unique(sensitive)
    tprs = []
    fprs = []
    for g in groups:
        mask = (sensitive == g)
        y_true_g = y_true[mask]
        y_pred_g = y_pred[mask]
        tp = np.sum((y_true_g==1) & (y_pred_g==1))
        fn = np.sum((y_true_g==1) & (y_pred_g==0))
        fp = np.sum((y_true_g==0) & (y_pred_g==1))
        tn = np.sum((y_true_g==0) & (y_pred_g==0))
        tpr = tp / (tp + fn) if (tp+fn)>0 else 0.0
        fpr = fp / (fp + tn) if (fp+tn)>0 else 0.0
        tprs.append(tpr)
        fprs.append(fpr)
    return float(max([abs(tprs[i]-tprs[j]) for i in range(len(tprs)) for j in range(len(tprs))] + [0.0])),)
def summary_metrics(y_true, y_pred, sensitive):
    return {
        'accuracy': float(accuracy_score(y_true, y_pred)),
        'roc_auc': float(roc_auc_score(y_true, y_pred)),
        'demographic_parity_diff': demographic_parity_difference(y_true, y_pred, sensitive),
        'equalized_odds_diff': equalized_odds_difference(y_true, y_pred, sensitive)
    }
