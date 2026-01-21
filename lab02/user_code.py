#!/usr/bin/env python
"""Object-Oriented Programming: Simple Objects

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module description ===
This module contains some examples of Python code
designed to explore the construction of simple objects.
We also override some inbuilt methods to provide more useful
string representations of objects, and to enable comparisons
between objects for the purpose of sorting and equality testing.
You may find list comprehensions, mapping and/or filtering
useful in this module.
"""
from __future__ import annotations
from datetime import date


class Sewer(object):
    """ a Sewer represents a sewer infrastructure item in a municipality.

     === Attributes ===
    _asset_id: the unique identifier of the sewer
    _asset_type: the type of sewer (catchbasin or manhole)
    _install_date: the date the sewer was installed
    _works_yard: the works yard that installed the sewer
    _ward: the ward in which the sewer is located
    _x_coord: the x coordinate of the sewer (longitude)
    _y_coord: the y coordinate of the sewer (latitude)
    === Sample Usage ===

     Creating a Sewer:
     >>> s = Sewer('2030569','Double Catchbasin','1753/01/01','MAVIS','3','-79.6211798370057','43.6238720598899')
     >>> s.get_asset_id()
     2030569
     >>> s.get_asset_type()
     'Double Catchbasin'
     """
    # Attribute types
    _asset_id: int
    _asset_type: str
    _install_date: date
    _works_yard: str
    _ward: int
    _lon: float
    _lat: float

    def __init__(self, asset_id: str, asset_type: str, install_date: str, works_yard: str, ward: str, lon: str,
                 lat: str) -> None:
        """Initialize this Sewer.
        Note that input arguments are all strings, but we convert
        some of them to more useful types. For example, the asset_id
        must converted to an int, and the install_date must converted to
        a date object.  Note that format of the string used to define any given
         date will always conform to the following format: YYYY/MM/DD.
        The values of x_coord and y_coord must be converted to floats.
         >>> s = Sewer('2030569','Double Catchbasin','1753/01/01','MAVIS','3','-79.6211798370057','43.6238720598899')
         >>> type(s.get_asset_id())
         <class 'int'>
         >>> type(s.get_install_date())
         <class 'datetime.date'>
         >>> type(s.get_lon())
         <class 'float'>
         >>> type(s.get_lat())
         <class 'float'>
        """
        install_date = install_date.split('/')
        install_date = [int(d) for d in install_date]

        # set the attributes
        self._asset_id = int(asset_id)
        self._asset_type = asset_type
        self._install_date = date(install_date[0], install_date[1], install_date[2])
        self._works_yard = works_yard
        self._ward = int(ward)
        self._lon = float(lon)
        self._lat = float(lat)

    def get_asset_id(self) -> int:
        """ return asset_id of sewer """
        return self._asset_id

    def get_asset_type(self) -> str:
        """ return asset_type of sewer """
        return self._asset_type

    def get_install_date(self) -> date:
        """ return install_date of sewer """
        return self._install_date

    def get_works_yard(self) -> str:
        """ return works_yard of sewer """
        return self._works_yard

    def get_ward(self) -> int:
        """ return ward of sewer """
        return self._ward

    def get_lon(self) -> float:
        """ return longitude of sewer """
        return self._lon

    def get_lat(self) -> float:
        """ return latitude of sewer """
        return self._lat

    def __lt__(self, other: Sewer):
        """ Compare sewers, for the purpose of sorting. Sewers should be ordered by their asset_id.
        A sewer that is 'less than' another sewer is one whose asset_id is less than the other sewer's asset_id.
        This will determine how sewers are sorted in lists.
        >>> s1 = Sewer('37742','Catchbasin','1955/01/01','CLARKSON','1','-79.5895934657861','43.5725163976989')
        >>> s2 = Sewer('37741','Pipe Inlet','1955/01/01','CLARKSON','1','-79.5906786543164','43.5724013172869')
        >>> s3 = Sewer('423','Manhole','1955/01/01','CLARKSON','1','-79.5780997842868','43.5915343992888')
        >>> s4 = Sewer('562','Manhole','1955/01/01','CLARKSON','1','-79.5786097434708','43.5910501086492')
        >>> l = sorted([s1, s2, s3, s4])
        >>> print([str(s) for s in l])
        ['ID 423: Manhole', 'ID 562: Manhole', 'ID 37741: Pipe Inlet', 'ID 37742: Catchbasin']
        >>> l.append(Sewer('1','Manhole','1955/01/01','CLARKSON','1','-79.5786097434708','43.5910501086492'))
        >>> l.sort()
        >>> str(l[0])
        'ID 1: Manhole'
        """
        return self._asset_id < other._asset_id

    def __str__(self) -> str:
        """ pretty print Sewer details
        When a Sewer is printed, it should be printed in the following format:
        ID <asset_id>: <asset_type>
        >>> s = Sewer('2030569','Double Catchbasin','1753/01/01','MAVIS','3','-79.6211798370057','43.6238720598899')
        >>> print(s)
        ID 2030569: Double Catchbasin
        >>> sewer = Sewer('111','Test Sewer','1753/01/01','MAVIS','3','-79.6211798370057','43.6238720598899')
        >>> print(sewer)
        ID 111: Test Sewer
        """
        return f'ID {self._asset_id}: {self._asset_type}'


def construct_sewers(sewers: list[list[str]]) -> list[Sewer]:
    """ make Sewer objects from list of input sewers.
    The input list contains lists of strings that represent the attributes of a sewer.
    This function should return a list of Sewer objects, one for each list in the input list.
    >>> sewers = [['37742','Catchbasin','1955/01/01','CLARKSON','1','-79.5895934657861','43.5725163976989'],['37741','Pipe Inlet','1955/01/01','CLARKSON','1','-79.5906786543164','43.5724013172869'],['423','Manhole','1955/01/01','CLARKSON','1','-79.5780997842868','43.5915343992888'],['562','Manhole','1955/01/01','CLARKSON','1','-79.5786097434708','43.5910501086492']]
    >>> sewers = construct_sewers(sewers)
    >>> sewers[0].get_asset_id()
    37742
    >>> sewers[1].get_asset_type()
    'Pipe Inlet'
    """
    return [Sewer(sewer_info[0], sewer_info[1], sewer_info[2], sewer_info[3], sewer_info[4], sewer_info[5], sewer_info[6]) for sewer_info in sewers]


def sewers_in_boundary(items: list[Sewer], boundary_box: list[float]) -> list[bool]:
    """Scan list of Sewer objects and return a list of booleans;
    each boolean indicates whether the corresponding Sewer is in the boundary box.
    The boundary box is parameterized as a list of four numbers:
    [min_longitude, min_latitude, longitude_span, latitude_span]
    >>> sewers = [['37742','Catchbasin','1955/01/01','CLARKSON','1','-79.6650648582618', '43.5286494728029'],['37741','Pipe Inlet','1955/01/01','CLARKSON','1','-79.6514228807402', '43.5286499880831'],['423','Manhole','1955/01/01','CLARKSON','1','-79.6368168487497', '43.5286516587731'],['562','Manhole','1955/01/01','CLARKSON','1','-79.6538693359683', '43.5286547813909'], ['564','Manhole','1955/01/01','CLARKSON','1','-79.86402398455755', '43.5286559094728']]
    >>> sewers = construct_sewers(sewers)
    >>> boundary_box = [-79.7, 43.5, 0.3, 0.2]
    >>> print(sewers_in_boundary(sewers, boundary_box))
    [True, True, True, True, False]
    
    single sewer - zero case
    >>> sewer = [['37742','Catchbasin','1955/01/01','CLARKSON','1','0','0']]
    >>> sewer = construct_sewers(sewer)
    >>> print(sewers_in_boundary(sewer, boundary_box))
    [False]
    """
    min_lon, min_lat = boundary_box[0], boundary_box[1]
    max_lon, max_lat = (boundary_box[0] + boundary_box[2]), (boundary_box[1] + boundary_box[3])

    return list(map(lambda i: (min_lon <= i.get_lon() <= max_lon) and (min_lat <= i.get_lat() <= max_lat), items))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
