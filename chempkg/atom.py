"""
Module atom.

Ce module définit les outils nécessaires à la représentation d'un atome
chimique. Il implémente la classe Atom ainsi que des fonctions permettant
de calculer la configuration électronique d'un atome à partir de son
nombre d'électrons, selon la règle de Klechkowski.

Le module fournit :
- une liste ordonnée de sous-couches électroniques,
- une fonction de calcul du nombre maximal d'électrons par sous-couche,
- une fonction de calcul des orbitales occupées,
- une fonction générant une configuration électronique lisible,
- la classe Atom avec ses méthodes spéciales (__repr__, __str__, __eq__).
"""

# pylint: disable=invalid-name


sous_couches = [
    (1, 0),  # 1s
    (2, 0),  # 2s
    (2, 1),  # 2p
    (3, 0),  # 3s
    (3, 1),  # 3p
    (4, 0),  # 4s
    (3, 2),  # 3d
    (4, 1),  # 4p
    (5, 0),  # 5s
    (4, 2),  # 4d
    (5, 1),  # 5p
    (6, 0),  # 6s
    (4, 3),  # 4f
    (5, 2),  # 5d
    (6, 1),  # 6p
    (7, 0),  # 7s
    (5, 3),  # 5f
    (6, 2),  # 6d
    (7, 1),  # 7p
]

lettre = {0: "s", 1: "p", 2: "d", 3: "f"}


def num_elec(l):

    """
    Calcule le nombre maximal d'électrons pour une sous-couche donnée.

    Args:
        l (int): Indice de la sous-couche (0=s, 1=p, 2=d, 3=f).

    Returns:
        int: Nombre maximal d'électrons.
    """

    return (l * 2 + 1) * 2

def get_orbitales(z: int) :
    """
    Calcule les orbitales électroniques pour un atome ayant z électrons.

    Args:
        z (int): Nombre total d'électrons dans l'atome.

    Returns:
        list: Liste des orbitales sous forme de tuples (n, l, nombre d'électrons).
    """

    atoms_free = z
    orbitales_atom = []
    i = 0
    while atoms_free > 0 and i< len(sous_couches):

        n, l  = sous_couches[i]

        atoms_couche = num_elec(l)

        if atoms_free >= atoms_couche:
            num_atom = atoms_couche
        else:
            num_atom = atoms_free

        atoms_free -= num_atom

        orbitales_atom.append((n, l, num_atom))

        i += 1
    return orbitales_atom



def elec_config(z: int):
    """
    Renvoie une configuration électronique lisible pour un atome ayant z électrons.

    Args:
        z (int): Nombre total d'électrons dans l'atome.

    Returns:
        tuple: Configuration électronique sous forme de chaînes lisibles.
    """
    orbitales = get_orbitales(z)
    config = []

    for n, l, num_atom in orbitales :
        lettre2 = lettre[l]
        config.append(f"{n}{lettre2}{num_atom}")

    return tuple(config)


class Atom :

    """
    Représente un atome chimique.

    Un atome est défini par son symbole, son nombre d'électrons,
    sa masse atomique et sa configuration électronique.

    """


    def __init__(self, name : str, num_electron : int , weight : float):
        """
        Initialise une instance de la classe Atom.

        Args:
            name (str): Nom de l'atome (ex: "Hydrogène").
            num_electron (int): Nombre d'électrons dans l'atome.
            weight (float): Masse atomique de l'atome.
        """
        self.name = name
        self.num_electron = num_electron
        self.weight = weight
        self.elec_config = elec_config(self.num_electron)


    def __repr__(self):
        """
        Représentation officielle de l'atome.

        Returns:
            str: Nom de l'atome.
        """
        return self.name

    def __str__(self) -> str:
        """
        Représentation lisible de l'atome.

        Returns:
            str: Nom, masse atomique et nombre d'électrons de l'atome.
        """
        return f"{self.name} ({self.weight}, {self.num_electron})"

    def __eq__(self, other) :
        """
        Vérifie l'égalité entre deux atomes.

        Args:
            other (Atom): Autre instance de la classe Atom.

        Returns:
            bool: True si les atomes sont égaux, False sinon.
        """
        if not isinstance (other, Atom):
            return NotImplemented
        return (
            self.name == other.name
            and self.num_electron == other.num_electron
            and self.weight == other.weight
        )

    def __hash__(self) -> int:
        return hash(self.name)


ATOM_REGISTRY = {
    "H": Atom("H", 1, 1),      # Hydrogen
    "C": Atom("C", 6, 12),     # Carbon
    "O": Atom("O", 8, 16),     # Oxygen
    "N": Atom("N", 7, 14),     # Nitrogen
    "Ca": Atom("Ca", 20, 40),  # Calcium
    "P": Atom("P", 15, 31),    # Phosphorus
    "K": Atom("K", 19, 39),    # Potassium
    "S": Atom("S", 16, 32),    # Sulfur
    "Na": Atom("Na", 11, 23),  # Sodium
    "Cl": Atom("Cl", 17, 35),  # Chlorine
    "Fe": Atom("Fe", 26, 56),  # Iron
    "I": Atom("I", 53, 127),   # Iodine
    "F": Atom("F", 9, 19),     # Fluorine
    "Co": Atom("Co", 27, 59),  # Cobalt
    "Mo": Atom("Mo", 42, 96),  # Molybdenum
}


#Association symbole à l'instance

H  = ATOM_REGISTRY["H"]
C  = ATOM_REGISTRY["C"]
O  = ATOM_REGISTRY["O"]
N  = ATOM_REGISTRY["N"]
Ca = ATOM_REGISTRY["Ca"]
P  = ATOM_REGISTRY["P"]
K  = ATOM_REGISTRY["K"]
S  = ATOM_REGISTRY["S"]
Na = ATOM_REGISTRY["Na"]
Cl = ATOM_REGISTRY["Cl"]
Fe = ATOM_REGISTRY["Fe"]
I  = ATOM_REGISTRY["I"]
F  = ATOM_REGISTRY["F"]
Co = ATOM_REGISTRY["Co"]
Mo = ATOM_REGISTRY["Mo"]
