"""

Module mol.

Ce module permet de représenter des molécules chimiques à partir de leur
formule brute, d’identifier les atomes qui les composent et de calculer
leur masse moléculaire.

"""

from chempkg.atom import Atom
from chempkg.atom import ATOM_REGISTRY

def sep_atom(formula)->dict[Atom , int]:
    """
    Analyse une formule chimique et retourne les atomes qui la composent.

    La fonction convertit la formule en un dictionnaire dont:
    les clés sont des objets Atom et les valeurs sont leurs nombres d'occurences.

    Args:
        formula(str) : Formule chimique (Molecule)

    returns :
        dict[Atom, int] : Dictionnaire des atomes et de leurs quantités
    """
    atoms = {}
    i = 0

    while i < len(formula):
        symbol = formula[i]
        i += 1

        if i < len(formula) and formula[i].islower():
            symbol += formula[i]
            i += 1

        if symbol not in ATOM_REGISTRY:
            raise ValueError(f"Atome inconnu : {symbol}")

        atom = ATOM_REGISTRY[symbol]

        number = ""
        while i < len(formula) and formula[i].isdigit():
            number += formula[i]
            i += 1

        count = int(number) if number else 1

        atoms[atom] = atoms.get(atom, 0) + count

    return atoms



def weight(formula: str)-> float:
    """
    Calcule la masse de la molécule, correspondant à la somme des masses des atomes.

    Args:
        formula(str) : Formule chimique (Molecule)

    Returns:
        float : Masse de la molécule
    """

    atoms = sep_atom(formula)
    total_weight = 0.0

    for atom, number in atoms.items():
        total_weight += number * atom.weight

    return float(total_weight)




class Molecule():
    """
    Représente une molécule.

    Une molécule est définie par sa formule brute, les atomes qui la composent et sa masse.
    Les atomes sont stockés sous la forme d'un dictionnaire
    """
    def __init__(self, formula: str):
        """
        Initialise une molécule à partir de sa formule chimique.

        Args:
            formula (str): Formule brute de la molécule.
        """
        self.formula = formula
        self.atoms = sep_atom(self.formula)
        self.weight = weight(self.formula)


    def __repr__(self) :
        """
        Représentation de la molécule
        """
        return self.formula

    def __str__(self):
        """
        Représentation lisible de la molécule
        """
        return self.formula


    def __eq__(self, other) -> bool:
        """Compare deux molécules."""
        if not isinstance(other, Molecule):
            return NotImplemented
        return self.atoms == other.atoms
