# PROVENANCE V3 - Real OR + Spectral
Date: 2026-10-19
Device: Termux ARM64
Engine: engine_gradient_v3.py - REAL Ollivier-Ricci via scipy linprog exact + Laplacian eigh
Graph: 3-regular 100 nodes, 150 edges, seed 0-19

Metrics:
- OR_mean -0.411 (negative, expander)
- lambda2 mean 0.216
- Median 661ms, 20/20 >50ms miss (expected for exact OT Python)
- V2 synthetic 1.57ms invalidated - replaced by real measurement

Dependencies: networkx, scipy, numpy (no POT)
Repro: python bench_v3_real.py
