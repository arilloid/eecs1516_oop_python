"""Linked Lists

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we make our own ADTs to help us organize
Apartment objects.  This time, we will implement a
tree to store apartment information.
"""
from __future__ import annotations

from typing import Optional

import csv
import random  # you can use this to generate random numbers


class ApartmentBuilding:
    """Information about an apartment building in the GTA

    === Attributes ===
    btype: the type of the building (e.g. Private, Toronto City Housing, Social Housing)
    year_built: year the building was built
    num_units: # of apartments in the building
    eval_score: evaluation score of the building, out of 100
    lon: longitude of the building
    lat: latitude of the building
    """
    _btype: str
    _year_built: int
    _num_units: int
    _eval_score: int
    _lon: float
    _lat: float

    def __init__(self, type_build: str, year: str, units: str, score: str, lon: str, lat: str) -> None:
        """Initialize a new apartment building"""
        self._btype = type_build
        self._year_built = int(year)
        self._num_units = int(units)
        self._eval_score = int(score)
        self._lon = float(lon)
        self._lat = float(lat)

    def __str__(self):
        return f'{self._btype}: {self._eval_score}'

    @property
    def btype(self):
        return self._btype

    @property
    def year_built(self):
        return self._year_built

    @property
    def eval_score(self):
        return self._eval_score

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon


class TreeNode:
    """A node in a tree

    === Attributes ===
    _building: The building information stored in this node.
    _subtrees: The subtrees, or branches, of the node.  These are references
    additional TNodes (if there are branches).
    """
    _apartment: ApartmentBuilding
    _subtrees: list[TreeNode]

    def __init__(self, apartment: ApartmentBuilding, subtrees: Optional[list[TreeNode]]) -> None:
        """Initialize a new node to store an Apartment Building object, with no subtrees."""
        self._apartment = apartment
        self._subtrees = subtrees if subtrees is not None else []

    @property
    def subtrees(self):
        return self._subtrees

    @property
    def apartment(self):
        return self._apartment

    @subtrees.setter
    def subtrees(self, value):
        self._subtrees = value

    @apartment.setter
    def apartment(self, value):
        self._apartment = value

    def is_empty(self) -> bool:
        """Return true if this tree is empty."""
        return self._apartment is None

    def __str__(self) -> str:
        """Return a string representation of this tree.
        You may find this method helpful for debugging.
        """
        return self._str_helper()

    def _str_helper(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree."""
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._apartment) + '\n'
            for subtree in self.subtrees:
                s += subtree._str_helper(depth + 1)
            return s

    def build_tree(self, items: list[ApartmentBuilding]) -> None:
        """Build a tree from the given list of apartment buildings.
        This method calls your insert method.
        The parameter 'items' is a list of ApartmentBuilding objects.
        """
        for i in items:
            self.insert(i) # all we do is insert each item into the tree

    def insert(self, apartment: ApartmentBuilding) -> None:
        """Insert <apartment> into this tree as follows:

            1. If the tree is empty, place <apartment> at the root of the tree.
            2. If the root of the tree is populated and it has **less than 3 subtrees**,
            create a new TreeNode containing the apartment, and place the new TreeNode among the
            subtrees of the original.
            3. Otherwise, pick a random number between 0 and 2,
            and insert the apartment into the subtree with this index in the
            list of subtrees. So, if you pick 0, you should insert the item into
            the first subtree.  If you pick 1, you should insert
            the item into the second subtree, and so on.

        >>> t = TreeNode(None, [])
        >>> s1 = ApartmentBuilding('Private', '2000', '100', '80', '7.0', '8.0')
        >>> s2 = ApartmentBuilding('Private', '2000', '100', '70', '7.0', '8.0')
        >>> s3 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> s4 = ApartmentBuilding('Private', '2000', '100', '50', '7.0', '8.0')
        >>> s5 = ApartmentBuilding('Private', '2000', '100', '40', '7.0', '8.0')
        >>> for s in [s1, s2, s3, s4, s5]: t.insert(s)
        >>> t.subtrees[0].apartment.eval_score
        70
        >>> t.subtrees[2].apartment.eval_score
        50
        """
        #1 tree is empty
        if self.is_empty():
            self._apartment = apartment
        #2 less than 3 subtrees
        elif len(self._subtrees) < 3:
            self._subtrees.append(TreeNode(apartment, []))
        #3 pick a random subtree tree and recurse
        else:
            index = random.randint(0, 2)
            self.subtrees[index].insert(apartment)

    def depth(self) -> int:
        """Return the depth of this tree.
        >>> t = TreeNode(None, [])
        >>> t.build_tree(read_apartment_data('apartments.csv'))
        >>> t.depth()
        9
        """
        if self.is_empty():
            return 0
        elif self.subtrees == []:
            return 1
        else:
            return 1 + max([sub.depth() for sub in self.subtrees])

    def average_evaluation_score(self) -> float:
        """Return a float that represents
        the average evaluation score of all the apartment
        buildings in this tree.

        Return 0.0 if the tree is empty.
        >>> TreeNode(None, []).average_evaluation_score()
        0.0
        >>> s1 = ApartmentBuilding('Private', '2000', '100', '80', '7.0', '8.0')
        >>> s2 = ApartmentBuilding('Private', '2000', '100', '70', '7.0', '8.0')
        >>> s3 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> lt = TreeNode(s1, [TreeNode(s2, []), TreeNode(s3, [])])
        >>> round(lt.average_evaluation_score(), 1)
        70.0
        >>> s4 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> s5 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> s6 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> rt = TreeNode(s4, [TreeNode(s5, []), TreeNode(s6, [])])
        >>> s0 = ApartmentBuilding('Private', '2000', '100', '60', '7.0', '8.0')
        >>> t = TreeNode(s0, [lt, rt])
        >>> round(t.average_evaluation_score(), 2)
        64.29
        """
        def get_totals(node: TreeNode) -> tuple[float, float]:
            count = 1
            total = node.apartment.eval_score

            for sub in node.subtrees:
                sub_total, sub_count = get_totals(sub)
                count += sub_count
                total += sub_total
            
            return total, count
        
        if self.is_empty():
            return 0.0
        
        total, count = get_totals(self)
        return total/count

    
        

def read_apartment_data(filename: str) -> list[ApartmentBuilding]:
    """Accepts the name of a csv file.
    Returns a list of Apartment Buildings in the file
    """
    buildings = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                building = ApartmentBuilding(*row)
                buildings.append(building)
            count += 1
    return buildings


if __name__ == '__main__':
    import doctest
    doctest.testmod()
  