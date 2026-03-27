"""Linked Lists

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we make our own ADTs to help us organize
Shelter objects.  The data about Shelters is, as ever,
drawn from Open City Data for the city of Toronto; it contains
information about the number of available beds at each shelter
and the sector of the population (Men, Women, Families, Youth)
that the Shelter serves.  We will implement a
linked list to store shelter information.
"""
from __future__ import annotations

from typing import Optional

import csv


class Shelter:
    """Information about an overnight shelter in the GTA

    === Attributes ===
    name: the name of the organization
    sector: sector served e.g. Mixed Adult, Youth, Women
    occupied: # of occupied beds in the shelter
    unoccupied: # of unoccupied beds in the shelter
    """
    _name: str
    _sector: str
    _occupied: int
    _unoccupied: int

    def __init__(self, name: str, sector: str, occupied: str, unoccupied: str) -> None:
        """Initialize a new shelter"""
        self._name = name
        self._sector = sector
        self._occupied = int(occupied)
        self._unoccupied = int(unoccupied)

    def __str__(self):
        return f'{self._name}: (occupied {self._occupied}, unoccupied {self._unoccupied})'

    @property
    def occupied(self):
        return self._occupied

    @property
    def unoccupied(self):
        return self._unoccupied

    @property
    def name(self):
        return self._name

    @property
    def sector(self):
        return self._sector


class _Node:
    """A node in a linked list.  We will wrap the information
    we care about (i.e. about each Shelter) inside of this node.

    Note that Node is considered a "private class", i.e. one which is only meant
    to be used in this module by the LinkedList class. This is why the name of
    the class is prefixed with an underscore.

    === Attributes ===
    _shelter: The shelter information stored in this node.
    _next: The next node in the list, or None if there are no more nodes.
    """
    _shelter: Shelter
    _next: Optional[_Node]

    def __init__(self, shelter: Shelter) -> None:
        """Initialize a new node to store a Shelter object, with no next node."""
        self._shelter = shelter
        self._next = None  # Initially, point to nothing

    # The following are "getters" and "setters" for the attributes.
    # We are using Python's 'property' decorator to define these methods.
    # In languages like Java, these would be defined using explicit getter and
    # setter methods.
    @property
    def next(self):
        return self._next

    @property
    def shelter(self):
        return self._shelter

    @next.setter
    def next(self, value):
        self._next = value

    @shelter.setter
    def shelter(self, value):
        self._shelter = value


class LinkedList:
    """A linked list. A linked list stores Node objects.  Each
    Node object contains a shelter object as well as a reference
    to another Node object. This reference is used to link the
    Node objects together to form a list.
    """
    _first: Optional[_Node]  # The first node in the linked list; None if the list is empty.

    def __init__(self, shelters: list[Shelter]) -> None:
        """Initialize a new linked list containing the given shelters.
        This will convert the list of shelters into a linked list
        of Node objects; each Node will contain one shelter from
        the incoming list. The first Node in the linked list
        will contain the first shelter in <shelters>.  This first node
        will also contain a reference to the second Node, which will
        contain the second shelter in <shelters>, and so on.
        """
        if not shelters:  # No shelters in an empty list!
            self._first = None
        else:  # Convert the list of shelters into a linked list
            self._first = _Node(shelters[0])
            curr = self._first
            for shelter in shelters[1:]:
                curr.next = _Node(shelter)
                curr = curr.next

    def is_empty(self) -> bool:
        """Return true if linked list is empty. Otherwise, return false."""
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of the shelters in this list.
        The string representation will have the following format:
        '[shelter1 | shelter2 | ... | shelterN]'.
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.shelter))
            curr = curr.next
        return '[' + ' | '.join(items) + ']'

    def __getitem__(self, index):
        """Return the Shelter at the given index."""
        curr = self._first
        curr_index = 0
        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1
        if curr is None:
            raise IndexError
        return curr.shelter

    def __len__(self) -> int:
        """Return the number of Nodes in this linked list.
        To implement this method, you will need to traverse the
        linked list and count the number of Nodes within it.
        Note that within each _Node is a Shelter object.
        >>> lst = LinkedList(read_shelter_data("shelters.csv"))
        >>> len(lst)
        4874
        """
        curr_node = self._first
        count = 0

        while curr_node:
            count +=1
            curr_node = curr_node.next
        
        return count

    def occupancy_rate(self, sector: Optional[str] = None) -> float:
        """Return the percentage of occupied beds among the
        shelters in this linked list. Calulate this as the
        total number of occupied beds divided by the total
        number of beds. Round the result to two decimal places.

        If sector is provided as a parameter, then return the
        occupancy rate just for shelters that serve the given
        sector.

        >>> lst = LinkedList(read_shelter_data("shelters.csv"))
        >>> lst.occupancy_rate('Women')
        99.59
        >>> lst.occupancy_rate('Men')
        99.05
        >>> lst.occupancy_rate('Youth')
        98.18
        >>> lst.occupancy_rate()
        98.89
        """
        curr_node = self._first
        total_occupied = 0
        total_unoccupied = 0

        while curr_node:
            if sector is None or curr_node.shelter.sector == sector:
                total_occupied += curr_node.shelter.occupied
                total_unoccupied += curr_node.shelter.unoccupied
            curr_node = curr_node.next
        
        return round((total_occupied/(total_occupied+total_unoccupied)*100), 2)

    def sector_index(self, sector: str) -> int:
        """Return the index of the first occurrence of a shelter
         that serves the given sector in this linked list.

        Raise a 'ValueError' if no shelter serving the sector <sector>
        is present in the list.

        >>> s1 = Shelter('Christie Ossington Neighbourhood Centre','Mixed Adult','6', '16')
        >>> s2 = Shelter('City of Toronto','Mixed Adult','16', '6')
        >>> s3 = Shelter('Covenant House Toronto','Youth','6', '26')
        >>> lst = LinkedList([s1, s2, s3])
        >>> lst.sector_index('Mixed Adult')
        0
        >>> lst.sector_index('Youth')
        2
        >>> lst.sector_index('Frogs')
        Traceback (most recent call last):
        ValueError
        """
        curr_node = self._first
        index = 0

        while curr_node:
            if curr_node.shelter.sector == sector:
                return index
            
            curr_node = curr_node.next
            index += 1

        raise ValueError


def read_shelter_data(filename: str) -> list[Shelter]:
    """Accepts the name of a csv file.
    Returns a list of Shelters in the file
    >>> retval = read_shelter_data("shelters.csv")
    >>> len(retval)
    4874
    """
    shelters = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                shelter = Shelter(*row)
                shelters.append(shelter)
            count += 1
    return shelters


if __name__ == '__main__':
    import doctest
    doctest.testmod()
