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

    def __repr__(self):
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


class BSTTree:
    """A Binary Search tree

    === Attributes ===
    _building: The building information stored in the root node of the tree
    _left: The left subtree of the root node.  The evaluation scores of buildings in
    this subtree will all be less than the evaluation score of the building
    at the root.
    _right: The right subtree of the root node.  The evaluation scores of buildings in
    this subtree will all be less than the evaluation score of the building
    at the root.
    """
    _apartment: Optional[ApartmentBuilding]
    _left: Optional[BSTTree]
    _right: Optional[BSTTree]

    def __init__(self, apartment: Optional[ApartmentBuilding] = None) -> None:
        """Initialize a new node to store an Apartment Building object, with no subtrees."""
        if apartment is None:
            self._apartment = None
            self._left = None
            self._right = None
        else:
            self._apartment = apartment
            self._left = BSTTree(None)  # a leaf points to two empty trees!
            self._right = BSTTree(None)  # this can be useful when you traverse the tree.

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def apartment(self):
        return self._apartment

    @left.setter
    def left(self, value):
        self._left = value

    @right.setter
    def right(self, value):
        self._right = value

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
        """Return a string representation of this tree."""
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._apartment) + '\n'
            answer += self._left._str_helper(depth + 1)
            answer += self._right._str_helper(depth + 1)
            return answer

    def build_tree(self, apartments: list[ApartmentBuilding]) -> None:
        """Build a tree from the given list of apartment buildings.
        This method calls your insert method.
        The parameter 'apartments' is a list of ApartmentBuilding objects.
        """
        for i in apartments:
            self.insert(i)  # all we do is insert each item into the tree

    def insert(self, apartment: ApartmentBuilding) -> None:
        """Insert <apartment> into this tree as follows:
            1. If the tree is empty, place <apartment> at the root (i.e. in the _data attribute) of this tree.
            Make the left and right subtrees empty BST Nodes.
            2. If the root of the tree is populated and the evaluation score of <apartment> is less
            than the score of the apartment located the root (i.e. in the _data attribute), insert the
            <apartment> into the left subtree.
            3. If the root of the tree is populated and the evaluation score of <apartment> is greater
            than or equal to the score of the apartment located the root (i.e. in the _data attribute), insert the
            <apartment> into the right subtree.
            >>> bst = BSTTree(ApartmentBuilding('PRIVATE','1955','36','42','43.689555816','-79.3860183305'))
            >>> bst.insert(ApartmentBuilding('TCHC','1995','38','22','43.589555816','-79.4860183305'))
            >>> bst.insert(ApartmentBuilding('PRIVATE','1965','76','82','43.789555816','-79.2860183305'))
            >>> bst._apartment
            PRIVATE: 42
            >>> bst._left._apartment
            TCHC: 22
            >>> bst._right._apartment
            PRIVATE: 82
            """
        pass  # TO DO: implement this method

    def apartments_in_range(self, start: int, end: int) -> list[ApartmentBuilding]:
        """Return the apartments in this BST with evaluation scores between <start> and <end>, inclusive.
        The apartments should be returned in sorted order, based on their evaluation.
        >>> bst = BSTTree(ApartmentBuilding('PRIVATE', '1955', '36', '42', '43.689555816', '-79.3860183305'))
        >>> left = BSTTree(ApartmentBuilding('TCHC', '1965', '38', '22', '43.589555816', '-79.4860183305'))
        >>> left._left = BSTTree(ApartmentBuilding('PRIVATE', '1975', '75', '19', '43.789555816', '-79.2860183305'))
        >>> left._right = BSTTree(ApartmentBuilding('PRIVATE', '1985', '76', '25', '43.789555816', '-79.2860183305'))
        >>> right = BSTTree(ApartmentBuilding('TCHC', '1995', '38', '83', '43.589555816', '-79.4860183305'))
        >>> right._left = BSTTree(ApartmentBuilding('PRIVATE', '2005', '65', '70', '43.789555816', '-79.2860183305'))
        >>> right._right = BSTTree(ApartmentBuilding('PRIVATE', '2015', '76', '84', '43.789555816', '-79.2860183305'))
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.apartments_in_range(70, 100)
        [PRIVATE: 70, TCHC: 83, PRIVATE: 84]
        >>> bst.apartments_in_range(0, 30)
        [PRIVATE: 19, TCHC: 22, PRIVATE: 25]
        """
        pass  # TO DO: implement this method

    def best_apartment(self) -> None:
        """Return (one of) the apartment(s) with the best evaluation
        score in the BSTTree.
        >>> apartments = read_apartment_data("apartments.csv")[0:300]
        >>> bst = BSTTree()
        >>> bst.build_tree(apartments)
        >>> bst.best_apartment()
        PRIVATE: 80
        """
        pass  # TO DO: implement this method

    def worst_apartment(self) -> None:
        """Return (one of) the apartment(s) with the worst evaluation
        score in the BSTTree.
        >>> apartments = read_apartment_data("apartments.csv")[0:300]
        >>> bst = BSTTree()
        >>> bst.build_tree(apartments)
        >>> bst.worst_apartment()
        PRIVATE: 17
        """
        pass  # TO DO: implement this method

    def depth(self) -> int:
        """Return the depth of this tree. Calculate depth
        as the number of nodes on the longest path in the BSTTree.
        >>> apartments = read_apartment_data("apartments.csv")[0:300]
        >>> apartments.sort(key=lambda x: x.eval_score)
        >>> bst = BSTTree()
        >>> bst.build_tree(apartments)
        >>> bst.depth() == 300
        True
        >>> random.shuffle(apartments)
        >>> bst = BSTTree()
        >>> bst.build_tree(apartments)
        >>> bst.depth() < 300
        True
        """
        pass  # TO DO: implement this method


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

