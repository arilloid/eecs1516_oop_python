#!/usr/bin/env python
"""Object-Oriented Programming: Python review examples

=== EECS 1516 ===
Lassonde School of Engineering

=== Module description ===
This module contains some examples of Python code.
We specifically review file reading and list comprehension.
We will read tree datafolder from a CSV file using methods in the csv package.

"""
from __future__ import annotations
import csv  # for reading csv files

def read_data(filename:str)->list[list[str]]:
    """Accepts the name of a csv file.
      Reads datafolder from the CSV file containing tree information
      and returns a list of lists. The input CSV has a header row and each
      subsequent row represents an individual tree using the following format:
      [tree_type, tree_diameter, tree_owner, tree_name, longitude, latitude]
      You will convert each row to a list of strings and return a list of lists.
    >>> trees = read_data("treelist.csv")
    >>> len(trees)
    99
    >>> trees[0]
    ['DECID', '19', 'MISS', 'NORWAY MAPLE', '-79.6650648582618', '43.5286494728029']
    """
    f = open(filename, 'r')
    trees_info = [tree_info[:-1].split(',') for tree_info in f][1:]
    f.close()

    return trees_info


def get_tree_names(mylist: list[list[str]]) -> list[str]:
    """Return a list of tree names from a list of lists.
    The input is assumed to represent tree datafolder, and each inner
    list is assumed to consiste of strings that represent
    an individual tree and conform to the following format:
    [tree_type, tree_diameter, tree_owner, tree_name, longitude, latitude]

    >>> trees = [['DECID', '19', 'MISS', 'NORWAY MAPLE', '-79.6650648582618', '43.5286494728029'], ['DECID', '17', 'MISS', 'NORWAY MAPLE', '-79.6514228807402', '43.5286499880831'], ['DECID', '6', 'MISS', 'SERVICEBERRY', '-79.6368168487497', '43.5286516587731'], ['DECID', '23', 'PEEL', 'HONEY LOCUST', '-79.6538693359683', '43.5286547813909'], ['DECID', '35', 'MISS', 'NORWAY MAPLE', '-79.6402398455755', '43.5286559094728']]
    >>> names = get_tree_names(trees)
    >>> print(names)
    ['NORWAY MAPLE', 'NORWAY MAPLE', 'SERVICEBERRY', 'HONEY LOCUST', 'NORWAY MAPLE']
    >>> print(names[0])
    NORWAY MAPLE
    >>> print(names[4])
    NORWAY MAPLE
    """
    return [tree[3] for tree in mylist]


def get_tree_coords(mylist: list[list[str]]) -> list[tuple[float, float]]:
    """Return a list of tree coordinates from a list of lists.
    The input is assumed to represent tree datafolder, and each inner
    list is assumed to consiste of strings that represent
    an individual tree and conform to the following format:
    [tree_type, tree_diameter, tree_owner, tree_name, longitude, latitude]
    The last two entries in each row are assumed to be
    the longitude and latitude of the tree.
    Make sure your method returns a list of **tuples** wherein
    each tuple consists of **floats** and **not strings**.
    >>> trees = [['DECID', '19', 'MISS', 'NORWAY MAPLE', '-79.6650648582618', '43.5286494728029'], ['DECID', '17', 'MISS', 'NORWAY MAPLE', '-79.6514228807402', '43.5286499880831'], ['DECID', '6', 'MISS', 'SERVICEBERRY', '-79.6368168487497', '43.5286516587731'], ['DECID', '23', 'PEEL', 'HONEY LOCUST', '-79.6538693359683', '43.5286547813909'], ['DECID', '35', 'MISS', 'NORWAY MAPLE', '-79.6402398455755', '43.5286559094728']]
    >>> coords = get_tree_coords(trees)
    >>> print(coords)
    [(-79.6650648582618, 43.5286494728029), (-79.6514228807402, 43.5286499880831), (-79.6368168487497, 43.5286516587731), (-79.6538693359683, 43.5286547813909), (-79.6402398455755, 43.5286559094728)]
    >>> type(coords[0][0]) == float
    True
    """
    return [(float(tree[-2]), float(tree[-1])) for tree in mylist]


def to_lower_case(mylist: list[str]) -> list[str]:
    """Accept a list of tree names, and return that list
    with the same tree names, but all in lower case.
    >>> trees = [['DECID', '19', 'MISS', 'NORWAY MAPLE', '-79.6650648582618', '43.5286494728029'], ['DECID', '17', 'MISS', 'NORWAY MAPLE', '-79.6514228807402', '43.5286499880831'], ['DECID', '6', 'MISS', 'SERVICEBERRY', '-79.6368168487497', '43.5286516587731'], ['DECID', '23', 'PEEL', 'HONEY LOCUST', '-79.6538693359683', '43.5286547813909'], ['DECID', '35', 'MISS', 'NORWAY MAPLE', '-79.6402398455755', '43.5286559094728']]
    >>> names = get_tree_names(trees)
    >>> print(names)
    ['NORWAY MAPLE', 'NORWAY MAPLE', 'SERVICEBERRY', 'HONEY LOCUST', 'NORWAY MAPLE']
    >>> lower = to_lower_case(names)
    >>> print(lower)
    ['norway maple', 'norway maple', 'serviceberry', 'honey locust', 'norway maple']
    >>> print(to_lower_case(['HI', 'THIS', 'IS', 'MY', 'LIST']))
    ['hi', 'this', 'is', 'my', 'list']
    """
    return [name.lower() for name in mylist]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

