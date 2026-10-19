import time, numpy as np, networkx as nx
from engine_gradient_v3 import compute_metrics

N=20
times=[]
ors=[]
l2s=[]
for i in range(N):
    G = nx.random_regular_graph(3, 100, seed=i)
    t0=time.perf_counter()
    or_m, l2, _ = compute_metrics(G)
    dt=(time.perf_counter()-t0)*1000
    times.append(dt)
    ors.append(or_m)
    l2s.append(l2)
    print(f"iter {i}: {dt:.2f}ms OR={or_m:.3f} l2={l2:.3f}")

print(f"\nMedian={np.median(times):.2f}ms Max={max(times):.2f} Min={min(times):.2f}")
print(f"OR mean={np.mean(ors):.3f} lambda2 mean={np.mean(l2s):.3f}")
print(f"Miss>50ms {sum(1 for x in times if x>50)}/{N}")
# Sauvegarde pour V3
with open("results_v3_real.log","w") as f:
    f.write(f"Median={np.median(times):.2f}ms Max={max(times):.2f} OR={np.mean(ors):.4f} L2={np.mean(l2s):.4f}\n")
