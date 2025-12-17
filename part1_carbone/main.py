"""
Module pour calculer l'empreinte carbone basée sur les réponses de l'utilisateur concernant :
les aliments, équipements et énergie.

Ce module utilise des fichiers CSV pour charger les données nécessaires
et interagit avec l'utilisateur pour collecter les informations requises.

Fonctions principales :
- ans_aliments : Collecte les réponses de l'utilisateur sur les aliments.
- ans_equipements : Collecte les réponses de l'utilisateur sur les équipements.
- ans_energie : Collecte les réponses de l'utilisateur sur l'énergie.
- calc_aliments : Calcule les émissions de CO2 liées aux aliments.
- calc_equipements : Calcule les émissions de CO2 liées aux équipements.
- calc_energie : Calcule les émissions de CO2 liées à l'énergie.
- main : Point d'entrée principal pour exécuter le programme.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données depuis les fichiers CSV
aliments = pd.read_csv("data/Aliment_filtered.csv", sep=",")
equipments = pd.read_csv("data/Equipements_filtered.csv", sep=",")
energies = pd.read_csv("data/energie_filtered.csv", sep=",")

# Définition des questions posées à l'utilisateur
questions = {
    "aliments": {
        aliment: f"Combien de kilo de {aliment} avez-vous achetés ?\n"
        for aliment in aliments["Main_type"]
    },
    "energie": {
        type_energie : f"Combien de Kwh de {type_energie} avez-vous utilisés?\n"
        for type_energie in energies["Type"]
    },
    "equipements": {
        equipement: f"Combien de {equipement} avez-vous achetés ?\n"
        for equipement in equipments["Categorie"]
    }
}

# Fonction pour collecter les réponses sur les aliments
def ans_aliments():
    """
    Pose des questions à l'utilisateur sur les aliments consommés et collecte les réponses.

    Retourne :
        dict : Un dictionnaire contenant les catégories d'aliments et les quantités associées.
    """
    print("\n===== Questions : Nourriture =====\n")
    reponse_aliments = {}

    for categorie, question in questions["aliments"].items():
        while True:
            try:
                saisie = input(question).strip()

                # Entrée vide → 0
                if saisie == "":
                    quantite_aliment = 0.0
                else:
                    quantite_aliment = float(saisie)

                # Refus des valeurs négatives
                if quantite_aliment < 0:
                    print("Veuillez entrer un nombre positif ou laisser vide pour 0.")
                    continue

                reponse_aliments[categorie] = quantite_aliment
                break

            except ValueError:
                print("Veuillez entrer un nombre valide (ex : 5 ou 7.5).")

    return reponse_aliments


# Fonction pour collecter les réponses sur les équipements
def ans_equipements():
    """
    Pose des questions à l'utilisateur sur les équipements achetés et collecte les réponses.

    Retourne :
        dict : Un dictionnaire contenant les catégories d'équipements et les quantités associées.
    """
    print("\n===== Questions : Equipements =====\n")
    reponse_equipements = {}

    for categorie, question in questions["equipements"].items():
        while True:
            try:
                saisie = input(question).strip()

                # Entrée vide → 0
                if saisie == "":
                    quantite_equipement = 0.0
                else:
                    quantite_equipement = float(saisie)

                # Refus des valeurs négatives
                if quantite_equipement < 0:
                    print("Veuillez entrer un nombre positif ou laisser vide pour 0.")
                    continue

                reponse_equipements[categorie] = quantite_equipement
                break

            except ValueError:
                print("Veuillez entrer un nombre valide (ex : 5 ou 7.5).")

    return reponse_equipements


# Fonction pour collecter les réponses sur l'énergie
def ans_energie():
    """
    Pose des questions à l'utilisateur sur l'énergie utilisée et collecte les réponses.

    Retourne :
        dict : Un dictionnaire contenant le type d'énergie et la quantité associée.
    """
    print("\n===== Questions : Energie/Type =====\n")
    reponse_energie = {}

    for type_energie, question in questions["energie"].items():
        while True:
            try:
                saisie = input(question).strip()

                # Entrée vide → 0
                if saisie == "":
                    quantite_energie = 0.0
                else:
                    quantite_energie = float(saisie)

                # Refus des valeurs négatives
                if quantite_energie < 0:
                    print("Veuillez entrer un nombre positif ou laisser vide pour 0.")
                    continue

                reponse_energie[type_energie] = quantite_energie
                break

            except ValueError:
                print("Veuillez entrer un nombre valide (ex : 5 ou 7.5).")

    return reponse_energie


# Fonction pour calculer les émissions de CO2 liées aux aliments
def calc_aliments():
    """
    Calcule les émissions de CO2 basées sur les réponses de l'utilisateur concernant les aliments.

    Retourne :
        float : Le total des émissions de CO2 pour les aliments.
    """
    reponse_aliment = ans_aliments()
    total = 0
    details = {}
    for categorie, quantite in reponse_aliment.items():
        coef = aliments.loc[aliments["Main_type"] == categorie, "Moyenne_CO2"].iloc[0]
        emission = coef * quantite
        total += emission
        details[categorie] = emission

    return total,details

# Fonction pour calculer les émissions de CO2 liées aux équipements
def calc_equipements():
    """
    Calcule les émissions de CO2 basées sur les réponses de l'utilisateur
    concernant les équipements.

    Retourne :
        float : Le total des émissions de CO2 pour les équipements.
    """
    reponse_equipement = ans_equipements()
    total = 0
    details = {}
    for categorie, quantite in reponse_equipement.items():
        coef = equipments.loc[equipments["Categorie"] == categorie, "Moyenne_CO2"].iloc[0]
        emission = coef * quantite
        total += emission
        details[categorie] = emission

    return total,details

# Fonction pour calculer les émissions de CO2 liées à l'énergie
def calc_energie():
    """
    Calcule les émissions de CO2 basées sur les réponses de l'utilisateur concernant l'énergie.

    Retourne :
        float : Le total des émissions de CO2 pour l'énergie.
    """
    reponse_energie = ans_energie()
    total = 0
    details = {}
    for categorie, quantite in reponse_energie.items():
        coef = energies.loc[energies["Type"] == categorie, "CO2_Kwh"].iloc[0]
        emission = coef * quantite
        total += emission
        details[categorie] = emission

    return total,details



# Ajout d'une fonction pour générer un graphique

def generer_graphique(details_aliments, details_equipements, details_energies):
    """
    Génère un graphique en barres empilées des émissions de CO2
    pour les aliments, les équipements et l'énergie.
    """

    categories = ["Nourriture", "Équipements", "Énergie"]
    positions = range(len(categories))

    _, ax = plt.subplots(figsize=(16, 8))

    # ===== NOURRITURE =====
    cumul = 0
    legend_handles_aliments = []
    for categorie, emission in details_aliments.items():
        bar_aliment = ax.bar(0, emission, bottom=cumul, label=categorie)
        legend_handles_aliments.append(bar_aliment[0])
        cumul += emission
    total_aliments = cumul

    # ===== ÉQUIPEMENTS =====
    cumul = 0
    legend_handles_equipements = []
    for categorie, emission in details_equipements.items():
        bar_equipements= ax.bar(1, emission, bottom=cumul, label=categorie)
        legend_handles_equipements.append(bar_equipements[0])
        cumul += emission
    total_equipements = cumul

    # ===== ÉNERGIE =====
    cumul = 0
    legend_handles_energies = []
    for categorie, emission in details_energies.items():
        bar_energies = ax.bar(2, emission, bottom=cumul, label=categorie)
        legend_handles_energies.append(bar_energies[0])
        cumul += emission
    total_energie = cumul

    # ===== Totaux au-dessus des colonnes =====
    ax.text(0, total_aliments + 50, f"{total_aliments:.2f} kg",
            ha="center", fontweight="bold")
    ax.text(1, total_equipements + 50, f"{total_equipements:.2f} kg",
            ha="center", fontweight="bold")
    ax.text(2, total_energie + 50, f"{total_energie:.2f} kg",
            ha="center", fontweight="bold")

    # ===== Axes =====
    ax.set_xticks(positions)
    ax.set_xticklabels(categories)
    ax.set_ylabel("Émissions de CO2 (kg)")
    ax.set_title("Émissions de CO2 par catégorie")

    # ===== Légendes séparées =====
    legend_aliments = ax.legend(
        legend_handles_aliments,
        details_aliments.keys(),
        title="Nourriture",
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )
    ax.add_artist(legend_aliments)

    legend_equipements = ax.legend(
        legend_handles_equipements,
        details_equipements.keys(),
        title="Équipements",
        bbox_to_anchor=(1.02, 0.6),
        loc="upper left"
    )
    ax.add_artist(legend_equipements)

    ax.legend(
        legend_handles_energies,
        details_energies.keys(),
        title="Énergie",
        bbox_to_anchor=(1.02, 0.25),
        loc="upper left"
    )

    plt.tight_layout()
    plt.subplots_adjust(right=0.65)
    plt.savefig("Resultat.png")
    plt.show()



# Fonction principale pour exécuter le programme
def main():
    """
    Point d'entrée principal du programme.
    Collecte les réponses de l'utilisateur, calcule les émissions de CO2 et affiche les résultats.
    """
    print("============ Bienvenue dans le calculateur du Baratie ============")
    print()
    while True:
        choice = input(
            "Quelle type d'évaluation souhaitez-vous faire "
            "(hebdomadaire, mensuelle ou annuelle) ? \n"
        ).strip().lower()
        if choice in ["hebdomadaire", "mensuelle", "annuelle"]:
            break

        print("Indiquez hebdomadaire, mensuelle ou annuelle.")

    emission_aliments , details_aliments = calc_aliments()
    emission_equipements, details_equipements = calc_equipements()
    emission_energie , details_energies = calc_energie()

    emission_totale = emission_aliments + emission_equipements + emission_energie

    if choice == "hebdomadaire":
        emission_annuelle = emission_totale * 52

    if choice == "mensuelle":
        emission_annuelle = emission_totale * 12

    if choice == "annuelle":
        emission_annuelle = emission_totale * 1

    print(f"Votre empreinte carbone annuelle est de {emission_annuelle} Kg\n")

    print(f"Votre empreinte carbone {choice} est de {emission_totale} Kg")

    print("\n======= Détails =======\n")

    print(f"L'émission des aliments est {emission_aliments} Kg")
    print(f"L'émission des équipements est {emission_equipements} Kg")
    print(f"L'émission de l'énergie est {emission_energie} Kg")

    generer_graphique(details_aliments,details_equipements, details_energies)

    print("\n====== OREWA KAIZOKU ONI INARUUU ODOKODA ========")

if __name__ == "__main__":
    main()
