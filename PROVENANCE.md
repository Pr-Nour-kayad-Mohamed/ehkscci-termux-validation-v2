# PROVENANCE.md — EHK-SCCI / CATALYST — Validation Termux
Date: 2026-05-13
Platforme de reference: Termux ARM64 (aarch64)

## 1. Manuscrit EHK-SCCI
Statut: DRAFT v2 en cours - validation interne Termux
- Ce document est le seul etabli sur plateforme de reference
- Pas d'identifiant Razor Lake-AX revendique comme acquis

## 2. Contributions CATALYST / Holli Daye
Statut: Source a identifier et permission a documenter
- Toute contribution externe doit etre citee avec permission ecrite
- Ne pas presenter comme acquis ce qui est prospectif

## 3. Permissions
- Code interne: auteur present
- Dependances: numpy, networkx (licences MIT/BSD)
- Pas de donnees personnelles

## 4. Fichiers valides et SHA-256 — Mesures Termux corrigees selon Perplexity

### Code
- engine_gradient_v2.py: 8ffd10a0a69a92835f84510380a3a6237d218d2594c0fe798edec5736d494010
- bench_v2_corrected.py: 5b451c2a779cd4543c2f8db668fec353598f795fed2b2de2844f0312ae3ba21e

### Logs de validation
- results_v2_corrected.log: 45370fee7edc5d024dc46080b7518b65c954e95117ff058dd44687260ad780f0
  Contenu: Microbenchmark 20 iterations
  Median=1.57ms Max=61.47ms Min=1.23ms Miss>50ms 1/20
  Attention: ne mesure ni courbure Ollivier-Ricci ni estimation spectrale

- results_floor_corrected.log: 6c80ca848fc598f577ee01b1a288caf38df20de50de646590185918c1d993ff2
  Contenu: Test plancher corrige
  floor_inactive dTheta/dS=1.13e-12
  floor_active dTheta/dS=0
  target_raw_3.68e-13 dTheta/dS=3.67e-13

### Formulation validee Perplexity a inclure dans manuscrit
"Un microbenchmark synthetique a ete execute pendant 20 iterations sur Termux ARM64. La region chronometree comprend la generation d'un graphe 3-regulier 100 noeuds, l'extraction des aretes, la generation de valeurs pseudo-aleatoires substituees aux courbures, le calcul d'un score quadratique avec penalite spectrale inactive (lambda_2_adj=2.5 < 2*sqrt(2)) et l'evaluation d'une porte logistique ecretee. Les durees presentent une mediane de 1,57 ms et un maximum de 61,47 ms, avec 1 depassement de l'echeance de 50 ms sur 20. Ce test ne mesure ni le calcul de courbure Ollivier-Ricci ni l'estimation spectrale, et ne constitue pas une validation temporelle du systeme EHK-SCCI/CATALYST. Une derivee analytique locale de la branche d'ecretage est retournee a titre diagnostique. Aucune retropropagation automatique de bout en bout n'est evaluee par ce prototype."

## 5. Limites prospectives — Ne pas presenter comme acquis
- Razor Lake-AX 700 TOPS: plateforme prospective, pas plateforme de reference
- Calcul reel courbure Ollivier-Ricci (Wasserstein): non mesure
- Estimation spectrale lambda_2: non mesure (constante utilisee)
- Boucle complete CATALYST (acquisition, Vishon, Tora, Puller, Vault, decision): non mesuree
- Validation temporelle 50ms systeme: non constituee par ce test

Cette organisation reduit la dependance du calendrier scientifique a la disponibilite de Razor Lake-AX.

## Verification
sha256sum -c <<'SHA'
8ffd10a0a69a92835f84510380a3a6237d218d2594c0fe798edec5736d494010  /data/data/com.termux/files/home/engine_gradient_v2.py
5b451c2a779cd4543c2f8db668fec353598f795fed2b2de2844f0312ae3ba21e  /data/data/com.termux/files/home/bench_v2_corrected.py
45370fee7edc5d024dc46080b7518b65c954e95117ff058dd44687260ad780f0  /data/data/com.termux/files/home/results_v2_corrected.log
6c80ca848fc598f577ee01b1a288caf38df20de50de646590185918c1d993ff2  /data/data/com.termux/files/home/results_floor_corrected.log
SHA
