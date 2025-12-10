from caterya.metrics import demographic_parity_difference
import numpy as np
def test_demo_parity():
    y_pred = np.array([1,0,1,0])
    s = np.array([0,0,1,1])
    diff = demographic_parity_difference(None, y_pred, s)
    assert abs(diff - ((1/2)-(1/2))) < 1e-6
