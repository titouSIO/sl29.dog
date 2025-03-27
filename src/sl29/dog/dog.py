"""Module providing an implementation of a dog"""
from typing import Optional
import random

# Définition de l'exception personnalisée MatingError
class MatingError(Exception):
    """Exception levée lorsque deux chiens de même sexe tentent de s'accoupler."""
    pass


class Dog:
    """
    Une classe représentant un chien.

    Attributes:
        _race (str): La race du chien (protected).
        _sex (str): Le sexe du chien (protected).
        name (str): Le nom du chien (public).
    """

    def __init__(self, race: str, sex: str, name: str = "") -> None:
        """
        Initialise un chien avec une race, un sexe et un nom.

        Args:
            race (str): La race du chien.
            sex (str): Le sexe du chien ('M' ou 'F').
            name (str, optional): Le nom du chien. Par défaut, une chaîne vide.
        """
        self._race = race  # Attribut protégé pour la race
        self._sex = sex    # Attribut protégé pour le sexe
        self.name = name   # Attribut public pour le nom
        self._mother = None
        self._father = None
        self._puppies = []


    @property
    def race(self) -> str:
        """
        Retourne la race du chien.

        Returns:
            str: La race du chien.
        """
        return self._race

    @property
    def sex(self) -> str:
        """
        DOCSTRINGS A COMPLETER
        """
        return self._sex 

    def __str__(self) -> str:
        """
        DOCSTRINGS A COMPLETER
        """
        return f"Chien: {self.name}, Race: {self._race}, Sexe: {self._sex}"

    
    
    
    def bark(self, n=1):
        return "Woff" * n

    def chew(self, stuff):
        a_stuff = stuff[:-1]
        return a_stuff

   

    @property
    def mother(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.
        
        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        return self._mother

    @property
    def father(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.
        
        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        return self._father


    @property
    def puppies(self) -> Optional['Dog']:
        """
        Retourne la mère du chien ou None.
        
        Returns:
            Optional[Dog]: La mère du chien ou None.
        """
        return self._puppies


    def mate(self, other: 'Dog') -> 'Dog':
        """
        Fait s'accoupler deux chiens et retourne un chiot.

        Args:
            other (Dog): L'autre chien avec lequel s'accoupler.

        Returns:
            Dog: Le chiot issu de l'accouplement.

        Raises:
            MatingError: Si les deux chiens sont de même sexe.
        """
        # Vérification des sexes
        # Détermination du père et de la mère
        # Détermination de la race du chiot
        # Détermination du sexe du chiot (aléatoire)
        # Création du chiot
        # Assignation des parents
        # Ajout du chiot à la liste des chiots des parents
        if self._sex == other._sex:
            raise MatingError("Ils sont du même sexe, donc l'accouplement est impossible.")
        else:
            father = self if self._sex == "M" else other
            mother = self if self._sex == "F" else other

            if father.race == mother.race:
                race = father.race
            else:
                race= "bâtard"

            puppies_sex = random.choice(["M", "F"])

            puppies = Dog( race=race,sex=puppies_sex, name="chiotA")

            puppies._father = father.name
            puppies._mother = mother.name

            father._puppies.append(puppies)
            mother._puppies.append(puppies)

        return puppies
