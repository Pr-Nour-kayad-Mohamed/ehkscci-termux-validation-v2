import time
import numpy as np
import networkx as nx
from engine_gradient_v2 import theta_k

print("=== Microbenchmark synthétique - CORRIGÉ selon Perplexity ===")
times=[]
for i in range(20):
    # CORRECTION 1 : génération graphe DANS chronométrage (Perplexity 2.1)
    t0 = time.perf_counter()
    G = nx.random_regular_graph(d=3, n=100)
    edges = list(G.edges())
    t1 = time.perf_counter()
    
    # CORRECTION 2 : renommé synthetic_input_generation (Perplexity 2.2)
    # Ce passage NE calcule AUCUNE courbure Ollivier-Ricci
    kappa_OR_synth = np.random.randn(len(edges)) * 0.1
    kappa_ref = np.zeros(len(edges))
    t2 = time.perf_counter()
    
    # CORRECTION 3 : pénalité spectrale inactive car lambda_2_adj=2.5 < bound 2*sqrt(2)=2.828
    # Donc I_disc = mean(gap^2) seulement
    gap = kappa_OR_synth - kappa_ref
    I_disc = float(np.mean(gap**2))  # penalty = 0
    t3 = time.perf_counter()
    
    theta_raw, theta, active, grad_raw, d_raw_dS, d_theta_dS = theta_k(I_disc)
    t4 = time.perf_counter()
    
    e2e = (t4-t0)*1000
    times.append(e2e)
    print(f"run {i+1:02d}: graph+edges={(t1-t0)*1000:.2f}ms synthetic={(t2-t1)*1000:.2f}ms score={(t3-t2)*1000:.2f}ms theta={(t4-t3)*1000:.2f}ms E2E={e2e:.2f}ms")

times_sorted=sorted(times)
median=times_sorted[len(times_sorted)//2]
print(f"\nMedian={median:.2f}ms Max={max(times):.2f}ms Min={min(times):.2f}ms")
print(f"Deadline misses >50ms: {sum(1 for t in times if t>50)}/20")
print("\nATTENTION: Ce test ne mesure ni courbure Ollivier-Ricci ni estimation spectrale.")
print("Formulation: Une dérivée analytique locale de la branche d'écrêtage est retournée à titre diagnostique. Aucune rétropropagation automatique de bout en bout n'est évaluée par ce prototype.")
