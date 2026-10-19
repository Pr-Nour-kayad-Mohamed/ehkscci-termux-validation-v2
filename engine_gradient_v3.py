"""
EHK-SCCI V3 Lite - Real OR + Spectral sans POT
- OR: Wasserstein approx via scipy.optimize.linprog (exact pour petits supports)
- Fallback si linprog absent: distance de transport approx
- Lambda2: Laplacian eigh
Fonctionne sur Termux pur.
"""
import numpy as np, networkx as nx
from scipy.optimize import linprog

def wasserstein_exact(a, b, D):
    # EMD exact via linear programming: min <D,P> s.t. P*1=b, P^T*1=a
    n, m = D.shape
    # variables: P.flatten()
    c = D.flatten()
    # contraintes égalité
    A_eq = []
    b_eq = []
    # sum_j P_ij = a_i  (n contraintes)
    for i in range(n):
        row = np.zeros(n*m)
        row[i*m:(i+1)*m] = 1
        A_eq.append(row)
        b_eq.append(a[i])
    # sum_i P_ij = b_j (m contraintes)
    for j in range(m):
        row = np.zeros(n*m)
        row[j::m] = 1
        A_eq.append(row)
        b_eq.append(b[j])
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    bounds = [(0, None)]*(n*m)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    if not res.success:
        # fallback approx: moyenne D
        return np.mean(D)
    return res.fun

def ollivier_ricci_edge(G, u, v, lengths):
    Nu = list(G.neighbors(u)) + [u]
    Nv = list(G.neighbors(v)) + [v]
    D = np.zeros((len(Nu), len(Nv)))
    for i, x in enumerate(Nu):
        lx = lengths[x]
        for j, y in enumerate(Nv):
            D[i,j] = lx.get(y, 10)
    a = np.ones(len(Nu))/len(Nu)
    b = np.ones(len(Nv))/len(Nv)
    W = wasserstein_exact(a, b, D)
    return 1 - W/1.0

def compute_metrics(G):
    lengths = dict(nx.all_pairs_shortest_path_length(G))
    or_vals = [ollivier_ricci_edge(G, u, v, lengths) for u,v in G.edges()]
    or_mean = float(np.mean(or_vals))
    L = nx.laplacian_matrix(G).todense()
    vals = np.linalg.eigvalsh(L)
    lambda2 = float(sorted(vals)[1])
    return or_mean, lambda2, len(or_vals)

if __name__ == "__main__":
    G = nx.random_regular_graph(3, 100, seed=0)
    or_m, l2, m = compute_metrics(G)
    print(f"OR_mean={or_m:.4f} lambda2={l2:.4f} edges={m}")
