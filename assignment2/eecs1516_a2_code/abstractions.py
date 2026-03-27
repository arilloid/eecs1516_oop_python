"""Data Abstractions"""
import csv

#############################
# Data Abstractions #
#############################
# Locations
class Location:
    _lon: float
    _lat: float

    def __init__(self, lat: float, lon: float) -> None:
        self._lon = lon
        self._lat = lat

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon

# Apartments
class Apartment:
    """An apartment, with a location (or ward), and a city review.
    You can decide on the names and attribute types."""
    _owner: str
    _year: int
    _loc: Location
    _overall_score: float
    _score_subset: tuple[float,float,float]

    def __init__(self, year: str, type: str, lat: str, lon: str, c: str, m: str, h: str, score: str ) -> None:
        """Return a apartment abstraction.
        >>> Apartment( '1805','PRIVATE','43.65','-79.39','2.8','2.6','2.7','87' ).owner
        'PRIVATE'
        >>> Apartment( '1805','PRIVATE','43.65','-79.39','2.8','2.6','2.7','87' ).year
        1805
        """
        self._owner = type
        self._loc = Location(float(lon), float(lat))
        if year != '':
            self._year = int(year)
        else:
            self._year = 1900
        self._overall_score = float(score)
        self._score_subset = (float(c),float(m),float(h))

    def __str__(self) -> str:
        """ Return a string representation of this apartment.
        Format: At (a, b) and owned by c\nItem scores: [d,e,f] and overall score: g
        """
        a = round(float(self._loc.lat), 3)
        b = round(float(self._loc.lon), 3)
        return f'At ({a}, {b}) and owned by {self._owner}\nItem scores: {self._score_subset} and overall score: {self._overall_score}'

    def __repr__(self) -> str:
        """ Return a string representation of this apartment.
        Format: At (a, b) and owned by c\nItem scores: [d,e,f] and overall score: g
        """
        return f'\nAt ({self._loc.lat}, {self._loc.lon}) and owned by {self._owner}\nItem scores: {self._score_subset} and overall score: {self._overall_score}'

    @property
    def score(self) -> float:
        return self._overall_score

    @property
    def year(self) -> int:
        return self._year

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def score_subset(self) -> tuple[float, float, float]:
        return self._score_subset

    def get_cosmetic(self) -> float:
        return self._score_subset[0]

    def get_mod_risk(self) -> float:
        return self._score_subset[1]

    def get_high_risk(self) -> float:
        return self._score_subset[2]

# ApartmentReader
class ApartmentReader:
    """A class to read the apartment data from a csv file.
    We will use static methods to read the data,
    so there will be no need to create an instance of
    this class."""

    @staticmethod  # static! We do not need an instance of this class to use this method.
    def read_apartments(filename: str) -> list[Apartment]:
        """Read the tree data from the csv file and return a
        list of trees."""
        apartments = []

        with open(filename, newline='') as csvfile:
            a_reader = csv.reader(csvfile, delimiter=',')
            count = 0
            for row in a_reader:
                if count > 0:
                    apartments.append(Apartment(*row))
                count += 1

        return apartments

if __name__ == "__main__":
    import doctest
    doctest.testmod()
