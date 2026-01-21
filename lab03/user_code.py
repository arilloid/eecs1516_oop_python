#!/usr/bin/env python

"""Object-Oriented Programming: SimpleObject example

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we go back to working wth MunicipalTree Objects.
This time, we touch on the ideas of composition and inheritance
in the way we make MunicipalTrees.  More specifically, will make **Location**
objects to store the locations of trees; MunicipalTree objects will
therefore contain or be **composed** of Locations. In addition, we will
use inheritance to make different types of trees, e.g. White Ash or Beech.
A default MunicipalTree will have allometric coefficients for a 'generic'
tree, while a White Ash will have allometric coefficients specific to a White Ash
and a Beech will have allometric coefficients specific to a Beech tree.
Allometric coefficients are used to estimate the biomass and carbon content
of specific kinds of trees from the tree's diameter at breast height (DBH).
"""

class Location:
    """ a Location captures a longitude and latitude
    location. """

    # Attribute types
    _lon: float
    _lat: float

    def __init__(self, lon: float, lat: float) -> None:
        """Initialize a new Location.
        'lon' is the longitude of the location.
        'lat' is the latitude of the location.
         >>> l = Location(43.4723, -79.7087)
         >>> l.get_lon()
         43.4723
         >>> l.get_lat()
         -79.7087
         """
        self._lon = lon
        self._lat = lat

    def get_lon(self) -> float:
        """ return the longitude of the location"""
        return self._lon

    def get_lat(self) -> float:
        """ return the latitude of the location"""
        return self._lat

    def __str__(self) -> str:
        """ pretty print tree details.
         We will use the format (lon, lat) """
        return "(" + str(self.get_lon()) + ", " + str(self.get_lat()) + ")"

    def __hash__(self) -> int:
        """ return a hash of the Location object.
            A hash is a unique integer that is used to compare objects.
            It is used in conjunction with the __eq__ method.
            We will discuss this in class!
            >>> l1 = Location(43.4723, -79.7087)
            >>> l2 = Location(43.4723, -79.7087)
            >>> hash(l1) == hash(l2)
            True
            """
        return hash(self._lon) + hash(self._lat)

    def __eq__(self, other) -> bool:
        """ Test for the equality of two Location objects.
            We will consider two locations equal if they have the same
            longitude and latitude.
         >>> l1 = Location(43.4723, -79.7087)
         >>> l2 = Location(43.4723, -79.7087)
         >>> l1 == l2
         True
         >>> l3 = Location(43, -79.7087)
         >>> l1 == l3
         False
         """
        return (self._lat == other.get_lat() and self._lon == other.get_lon())


class MunicipalTree(object):
    """ a MunicipalTree represents a tree in a municipality.

     === Attributes ===
     type: the type of tree (deciduous or coniferous)
     diameter: the diameter of the tree (in cm)
     owner: the owner of the tree (peel, york, mississauga)
     name: the botanical name of the tree
     Location: the location of the tree
     """

    # Attribute types
    _type: str
    _diameter: int
    _owner: str
    _name: str
    _loc: Location
    _wood_params: list[float]

    def __init__(self, type: str, diameter: str, owner: str, name: str, longitude: str, latitude: str) -> None:
        """Initialize this Municipal Tree based on an input of strings and numbers.
            'type' is the type of tree (deciduous or coniferous)
            'diameter' is the diameter of the tree (in cm)
            'owner' is the owner of the tree (peel, york, mississauga)
            'name' is the botanical name of the tree
            'longitude' is the longitude of the tree
            'latitude' is the latitude of the tree
            Make sure to convert the diameter to an **int** and the longitude and latitude to a **Location**
            before storing them in the instance variables.
            Default allometric coefficients are provided for you, and have been
            stored in the _wood_params attribute.
          >>> s = MunicipalTree('DECID', '19', 'MISS', 'NORWAY MAPLE', '-79.6650648582618', '43.5286494728029')
          >>> s.get_diameter()
          19
          >>> t = MunicipalTree('DECID', '22', 'Peel', 'ASH', '43.4723', '-79.7087')
          >>> type(t.get_loc())
          <class '__main__.Location'>
          >>> print(t.get_loc())
          (43.4723, -79.7087)
          >>> type(t.get_diameter())
          <class 'int'>
          >>> print(t.get_diameter())
          22
          """
        self._wood_params = [0.15, 2.15]  # default allometreic parameters
        self._type = type
        self._diameter = int(diameter)
        self._owner = owner
        self._name = name
        self._loc = Location(float(longitude), float(latitude))

    def calculate_carbon_content(self) -> float:
        """ Calculate the carbon content of this tree in kg, based on biomass of wood.

            The tree's Biomass can be estimated using this formula:
            B = p*diameter^q, where diameter is the tree diameter.
            p and q are the **wood parameters**. p is the same as
            the first element in the _wood_params attribute and q is the
            same as the second element in the _wood_params attribute.
            The variables p and q are called allometric coefficeints.
            Allometric coefficeints for different species of trees can be found here:
            https://www.researchgate.net/publication/249535320_Canadian_national_tree_aboveground_biomass_equations

            Carbon content of a tree in kg can be calculated with the wood parameters using this formula:
            Carbon = a*B, where B is the tree's Biomass and a = 0.474.  We use
            a = 0.474, as this was the mean wood carbon fraction for tree species
            surveyed by the USDA Forest Service Forest Inventory and Analysis (FIA)
            program (https://www.fs.usda.gov/nrs/highlights/2256).

            Return the kg of carbon sequestered in the wood of the tree.

            >>> t = MunicipalTree('Deciduous', '22', 'Peel', 'Ash', '43.4723', '-79.7087')
            >>> print(t.get_loc())
            (43.4723, -79.7087)
            >>> t.get_name()
            'Ash'
            >>> abs(round(t.calculate_carbon_content(),2)-54.71) < 1
            True
            >>> print(t.calculate_carbon_content())
            54.71146758653036
            """
        a = 0.474
        p, q = self._wood_params[0], self._wood_params[1]

        biomass = p*(self._diameter**q)
        carbon = a*biomass

        return carbon

    def set_wood_params(self, params: list[float]) -> None:
        """ setWoodParams of tree """
        self._wood_params = params

    def set_diameter(self, param: int) -> None:
        """ setDiameter of tree """
        self._diameter = param

    def set_name(self, name: str) -> None:
        """ setName of tree """
        self._name = name

    def get_wood_params(self) -> list[float]:
        """ getWoodParams of tree """
        return self._wood_params

    def get_type(self) -> str:
        """ get type of tree """
        return self._type

    def get_owner(self) -> str:
        """ return owner of tree """
        return self._owner

    def get_diameter(self) -> int:
        """ return diameter of tree """
        return self._diameter

    def get_name(self) -> str:
        """ return name of tree """
        return self._name

    def get_loc(self) -> Location:
        """ return location of tree """
        return self._loc

    def __str__(self) -> str:
        """ pretty print tree details
        Format: name: location
        >>> t = MunicipalTree('Deciduous', '22', 'Peel', 'Ash', '43.4723', '-79.7087')
        >>> print(t)
        Ash: (43.4723, -79.7087)
        """
        return self.get_name() + ": " + str(self.get_loc())


class Beech(MunicipalTree):
    """ A Beech is a type of MunicipalTree.
    It has the same attributes and methods as a MunicipalTree.
    But, its allometric coefficients are different than a
    default MunicipalTree. For a Beech, the allometric
    coefficients should be set to [0.15, 2.25].
    """

    def __init__(self, type: str, diameter: str, owner: str, name: str, longitude: str, latitude: str) -> None:
        """ initialize beech tree
        >>> t = MunicipalTree('Deciduous', '22', 'Peel', 'Ash', '43.4723', '-79.7087')
        >>> s = Beech('Deciduous', '22', 'Peel', 'Beech', '43.4723', '-79.7087')
        >>> abs(round(t.calculate_carbon_content(),3)-54.71) < 1
        True
        >>> abs(round(s.calculate_carbon_content(),3)-74.528) < 1
        True
        >>> isinstance(s, Beech)
        True
        >>> isinstance(s, MunicipalTree)
        True
        >>> isinstance(s, WhiteAsh)
        False
        >>> type(s) == type(t)
        False
        """
        MunicipalTree.__init__(self, type, diameter, owner, name, longitude, latitude)
        self._wood_params = [0.15, 2.25]


class WhiteAsh(MunicipalTree):
    """ A WhiteAsh is a type of MunicipalTree.
    It has the same attributes and methods as a MunicipalTree.
    But, its allometric coefficients are different than a
    default MunicipalTree. For a WhiteAsh, the allometric
    coefficients should be set to [0.19, 2.17].
    """

    def __init__(self, type: str, diameter: str, owner: str, name: str, longitude: str, latitude: str) -> None:
        """ initialize ah tree
        >>> t = MunicipalTree('Deciduous', '22', 'Peel', 'Ash', '43.4723', '-79.7087')
        >>> s = WhiteAsh('Deciduous', '22', 'Peel', 'White Ash', '43.4723', '-79.7087')
        >>> abs(round(t.calculate_carbon_content(),3)-54.711) < 1
        True
        >>> abs(round(s.calculate_carbon_content(),3)-73.721) < 1
        True
        >>> isinstance(s, WhiteAsh)
        True
        >>> isinstance(s, MunicipalTree)
        True
        >>> isinstance(s, Beech)
        False
        >>> type(s) == type(t)
        False
        """
        MunicipalTree.__init__(self, type, diameter, owner, name, longitude, latitude)
        self._wood_params = [0.19, 2.17]


if __name__ == '__main__':
    import doctest
    doctest.testmod()