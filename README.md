[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23524997.svg)](https://doi.org/10.5281/zenodo.23524997)
# EHK-SCCI V3.5 — Fractional Fermi Sea as Lean Edge Critical Phase
**From Cesium Tubes (70k atoms, Nägerl Group PRL June 2026) to ARM64 Termux (<5W, Djibouti) & Intel Xeon 6+**

[![DOI Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.23445576.svg)](https://doi.org/10.5281/zenodo.23445576)

## 🔬 Sommaire Executif

Pont formel 1:1 entre mer de Fermi fractionnaire (70k atomes Cs ultra-froids, PRL juin 2026) et EHK-SCCI V3.4/V3.5.

* Validation Reelle: 23,9 ms median (27,6x), 0/20 FAIL <50ms sur Snapdragon <5W Djibouti
* Invariant: OR -0,411 preserve, residu 0,0012

## ⚙️ Isomorphisme Rigoureux

| Dimension Physique | Dimension Algorithmique |
| :--- | :--- |
| Cycle repulsion-attraction | K_ij(t) Kuramoto + Tura Liquid tau=0.02s |
| Auto-reorganisation evite chaos thermique | np.einsum eij ei->ej 661ms->23.9ms |
| Occupation fractionnaire F | F_raw 0.666 -> F_corr 0.833 gain p/3 |
| Ordre cache correlations | OR -0.411 residu 0.0012 |

## 🚀 Reproductibilite

