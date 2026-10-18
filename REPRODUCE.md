# Reproduction du microbenchmark synthétique v2

## Périmètre
Microbenchmark synthétique. Ne calcule ni Ollivier-Ricci ni spectre.
Ne constitue pas validation système EHK-SCCI/CATALYST.

## 1. Identifier la révision
git rev-parse HEAD
git status --short

## 2. Vérifier les fichiers déposés
sha256sum --check --strict SHA256SUMS

## 3. Documenter l'environnement
uname -a
python --version
python -m pip freeze

## 4. Exécuter le benchmark
python bench_v2_corrected.py > reproduction_bench.log 2>&1

## 5. Interpréter
Valeurs rapportées: 20 iter, median 1.57ms, max 61.47ms, 1 depassement 50ms.
