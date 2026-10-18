import numpy as np

def sigmoid_negative_stable(x):
    x = np.asarray(x, dtype=np.float64)
    out = np.empty_like(x)
    pos = x >= 0
    neg = ~pos
    out[pos] = 1/(1+np.exp(-x[pos]))
    exp_x = np.exp(x[neg])
    out[neg] = exp_x/(1+exp_x)
    return out

def theta_k(I_disc, S=0.0, epsilon=1e-15):
    # I_disc entre, theta_raw = sigmoid(-I_disc + S)
    theta_raw = float(sigmoid_negative_stable(np.array(-I_disc + S)))
    is_floor_active = theta_raw < epsilon
    # Au raccord r=epsilon, convention documentée = 1.0 si égalité détectée (non diff classique)
    # Pour test honnête, grad = 0 si actif, 1 si inactif
    grad_wrt_raw = 0.0 if is_floor_active else 1.0
    theta = epsilon if is_floor_active else theta_raw
    # dérivée analytique locale par rapport à S
    d_raw_dS = theta_raw * (1.0 - theta_raw)  # dérivée sigmoid
    d_theta_dS = grad_wrt_raw * d_raw_dS
    return theta_raw, theta, is_floor_active, grad_wrt_raw, d_raw_dS, d_theta_dS
