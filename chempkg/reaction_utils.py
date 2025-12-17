"""
Module reaction_utils.

Ce module contient des fonctions permettant de modéliser des réactions
chimiques simples, notamment la vérification de la validité d'une réaction
et la modélisation de la cinétique d'une réaction de décomposition.

Le module fournit:
- Une fonction qui permet de savoir si une réaction est valide
- Une fonction qui calcule l'évolution de la concentration au cours du temps

"""


import numpy as np
import matplotlib.pyplot as plt
from chempkg.mol import Molecule


def valid_reaction(
    reactives: list[tuple[Molecule, int]],
    products: list[tuple[Molecule, int]],
) -> bool:

    """
    Vérifie si une réaction chimique est valide.

    Une réaction est valide si le nombre total d'atomes de chaque type
    est identique du côté des réactifs et des produits.

    Args:
        reactives (list[tuple[Molecule, int]]): Réactifs avec coefficients.
        products (list[tuple[Molecule, int]]): Produits avec coefficients.

    Returns:
        bool: True si la réaction est valide, False sinon.
    """
    reactives_count = {}
    for molecule, coeff in reactives:
        for atom, number in molecule.atoms.items():
            reactives_count[atom] = (
                reactives_count.get(atom, 0) + number * coeff
            )

    products_count = {}
    for molecule, coeff in products:
        for atom, number in molecule.atoms.items():
            products_count[atom] = (
                products_count.get(atom, 0) + number * coeff
            )

    return reactives_count == products_count

def kinetic_decomp(a0: float,
                   k: float,
                   t: float,
                   steps: int,
                   figure_path :str = None) :

    """
    Modélise la cinétique d'une réaction de décomposition A -> B + C.

    Calcule l'évolution de la concentration de A dans le temps selon
    la loi [A](t) = A0 * exp(-k * t).

    Args:
        A0 (float): Concentration initiale.
        k (float): Constante de réaction.
        T (float): Durée totale de la réaction.
        steps (int): Nombre de points de temps.
        figure_path (str | None): Chemin de sauvegarde de la figure.

    Returns:
        list[float]: Valeurs de la concentration au cours du temps.
    """
    temps = np.linspace(0, t, steps)
    a_t = a0 * np.exp(-k*temps)

    if figure_path is not None:
        plt.plot(temps,a_t)
        plt.xlabel("Temps en seconde")
        plt.ylabel("[A](t) en mol.L-1")
        plt.title("Evolution de [A](t)")
        plt.savefig(figure_path)
        plt.close()

    return a_t.tolist()
