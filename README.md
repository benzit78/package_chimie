# Package Chimie – Atomes, Molécules et Réactions

Ce projet est un **package Python dédié à la modélisation de concepts chimiques de base**.
Il permet de représenter des atomes, de construire des molécules à partir de formules chimiques
et de fournir des outils utilitaires pour manipuler des réactions simples.

Le projet est conçu dans un objectif **pédagogique**, avec une attention particulière portée à :
- la structure d’un package Python,
- la programmation orientée objet,
- les tests unitaires,
- la lisibilité et la qualité du code.

---

## 📦 Contenu du package

Le package est organisé autour des modules suivants :

### 🔹 `atom.py`
- Représentation d’un atome chimique
- Gestion du symbole chimique et de la masse atomique
- Validation des éléments

### 🔹 `mol.py`
- Représentation d’une molécule à partir d’une formule brute (ex: `H2O`, `CO2`)
- Décomposition de la molécule en atomes
- Calcul de la masse moléculaire

### 🔹 `reaction_utils.py`
- Fonctions utilitaires liées aux réactions chimiques
- Aide à la manipulation et à l’analyse des équations chimiques

---

## 🧪 Tests

Les tests unitaires sont regroupés dans le dossier `tests/` et permettent de vérifier :
- le bon fonctionnement des classes `Atom` et `Molecule`,
- la validité des calculs,
- la robustesse face aux entrées incorrectes.

Pour lancer les tests :

```bash
pytest