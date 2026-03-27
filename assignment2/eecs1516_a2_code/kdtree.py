from __future__ import annotations
from typing import Optional, Tuple

from abstractions import Apartment, ApartmentReader

import math  # This may be useful!
import pickle  # for test cases in doctests

class _KDTNode:
    """A node to store some data in a KD-tree. A KD-tree is a binary tree
    that will be built of these nodes.

    === Attributes ===
    Information stored in a node:
    _apartment: The Apartment data that is stored in this node.
    _pivot: The pivot value of this node. At alternating levels of a KD tree,
            this will be a cosmetic, moderate or high risk assessment. All nodes in the left subtree
            will have a value strictly less than the pivot, and all nodes in the right subtree
            will have a value greater than or equal to the pivot.

    Children of this node:
    _left: the left subtree of this node.
    _right: the right subtree of this node.
    """
    _apartment: Apartment
    _pivot: float  # the pivot value of this node, this will be either the lon or lat coordinate
    _left: Optional[_KDTNode]
    _right: Optional[_KDTNode]

    def __init__(self, apt: Apartment, pivot: float) -> None:
        """Initialize a new _KDTNode storing <tree>, with no left or right nodes. """
        self._apartment = apt
        # all the nodes in the right subtree will have a value greater than the pivot
        self._pivot = pivot  # all the nodes in the left subtree will have a value less than the pivot
        self._left = None  # Initially pointing to nothing
        self._right = None  # Initially pointing to nothing

    def distance(self, c: float, m: float, h: float) -> float:
        """Return the distance between the _apartment in this node
        and a point (at c, m, h). Use euclidian distance in 3D as a distance measure.
        >>> node = _KDTNode(Apartment( '1805','PRIVATE','43.65','-79.39','2.8','2.6','2.7','87' ),0)
        >>> round(node.distance(1, 1, 1),1)
        2.9
        >>> round(node.distance(1, 2, 1),1)
        2.5
        >>> round(node.distance(3, 1, 1),1)
        2.3
        """
        pass  # Replace this!

    #Useful getter and setter methods below!
    @property
    def apartment(self) -> Apartment:
        return self._apartment

    @property
    def left(self) -> _KDTNode:
        return self._left

    @property
    def right(self) -> _KDTNode:
        return self._right

    @property
    def pivot(self) -> float:
        return self._pivot

    @left.setter
    def left(self, node) -> None:
        self._left = node

    @right.setter
    def right(self, node) -> None:
        self._right = node

    @pivot.setter
    def pivot(self, value):
        self._pivot = value


class KDTree:
    """A KDTree that stores information about Apartments.
    It is made up of _KDTNode objects, and each _KDTNode object
    contains apartment objects.

    === Attributes ===
    _KDTreeRoot: The root of the KDTree.
    _average_build_year: The average year the apartments in the tree were built

    """
    _KDTreeRoot: _KDTNode  # the root of the KD tree
    _average_build_year: int

    def __init__(self, data: list[Apartment]) -> None:
        """Initialize a new KD Tree (KDTree) using the input data.
        If <KDTree> is None, the KDTree is empty.
        """
        # build the tree from the apartment list, starting at depth 0
        self._KDTreeRoot = self.build_tree(data, 0)
        self._average_build_year= self.calculate_year_average() #initialize

    def calculate_year_average(self) -> int:
        """
        Calculate the average year of construction for the apartment buildings contained
        within the tree. Round your estimate to the nearest integer value.
        You may want to write a recursive helper function for this!
        >>> with open('kdtree.pkl', 'rb') as file: loaded_object = pickle.load(file)
        >>> print(loaded_object.calculate_year_average())
        1971
        """
        pass  # Replace this!

    def display_tree(self) -> None:
        """ Recursive method to DISPLAY (i.e. print to the console) a KDTREE.
        You may want to study this code in order to see how to write your own recursive
        HELPER methods. """
        lines, *_ = self._display_helper(self._KDTreeRoot)
        for line in lines:
            print(line)

    def _display_helper(self, node: _KDTNode) -> tuple[list[str], int, int, int]:
        """ Recursive helper method to DISPLAY a KDTREE."""
        # No child.
        if node.right is None and node.left is None:
            line = f'{round(float(node.apartment.get_cosmetic()), 2)},{round(float(node.apartment.get_mod_risk()), 2)},{round(float(node.apartment.get_high_risk()), 2)}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_helper(node.left)
            s = f'{round(float(node.apartment.get_cosmetic()), 2)},{round(float(node.apartment.get_mod_risk()), 2)},{round(float(node.apartment.get_high_risk()), 2)}'

            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '|' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_helper(node.right)
            s = f'{round(float(node.apartment.get_cosmetic()), 2)},{round(float(node.apartment.get_mod_risk()), 2)},{round(float(node.apartment.get_high_risk()), 2)}'

            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '|' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_helper(node.left)
        right, m, q, y = self._display_helper(node.right)
        s = f'{round(float(node.apartment.get_cosmetic()), 2)},{round(float(node.apartment.get_mod_risk()), 2)},{round(float(node.apartment.get_high_risk()), 2)}'

        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '|' + (n - x - 1 + u + y) * ' ' + '|' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def build_tree(self, data: list[Apartment], depth: int) -> Optional[_KDTNode]:
        """Build a KDTree from the input data. Build the tree using the median
        of the data at each level of the tree. The depth of the tree is used to
        determine whether to split the data by the cosmetic, moderate or high risk
        score of the apartment. Split by cosmetic score if depth mod 3 is 0, and by
        moderate risk score if depth mod 3 is 1; otherwise split by high risk score.
        Your implementation will be recursive.
        >>> t = KDTree([Apartment( '1805','PRIVATE','43.65','-79.39','2.8','2.6','2.7','87' ) , Apartment( '1910','PRIVATE','43.65','-79.39','2.9','1.6','1.7','87' ), Apartment( '2010','PRIVATE','43.65','-79.39','2.0','2.0','2.0','87' )])
        >>> t.display_tree() # doctest: +NORMALIZE_WHITESPACE
              _____2.8,2.6,2.7_____
             |                     |
        2.0,2.0,2.0           2.9,1.6,1.7
        """
        pass  # Replace this!

    def lookup(self, c: float, m: float, h: float) -> bool:
        """Return True if there is a tree with the given coordinates is
        in the KDTree.  Otherwise return False.
        >>> with open('kdtree.pkl', 'rb') as file: loaded_object = pickle.load(file)
        >>> print(loaded_object.lookup(1,1,1))
        False
        >>> print(loaded_object.lookup(2.7,2.8,2.7))
        True
        """
        pass  # Replace this!

    def get_closest_point(self, c: float, m: float, h: float) -> Optional[Apartment]:
        """ Return the nearest apartment to the given input set of coordinates
        >>> with open('kdtree.pkl', 'rb') as file: loaded_object = pickle.load(file)
        >>> print(loaded_object.get_closest_point(2,2,2))
        At (-79.422, 43.687) and owned by SOCIAL HOUSING
        Item scores: (2.0, 2.6, 2.2) and overall score: 82.0
        >>> print(loaded_object.get_closest_point(3,3,3))
        At (-79.325, 43.663) and owned by SOCIAL HOUSING
        Item scores: (2.7, 2.8, 2.7) and overall score: 90.0
        """
        pass  # Replace this!

    def predict(self, test_data: list[Apartment]) -> list[str]:
        """ Classify each apartment building in the input list test_data as being either `SOCIAL HOUSING'
        `TCHC' or `PRIVATE'. Make classifications by finding the nearest apartment
        in the tree to the (cosmetic, moderate and high risk assessments) of each input
        apartment in test_data.  Classifications should be stored in a list of strings that is returned.
        >>> with open('kdtree.pkl', 'rb') as file: loaded_object = pickle.load(file)
        >>> apt_list = [Apartment( '1805','PRIVATE','43.65','-79.39','2.8','2.6','2.7','87' )]
        >>> loaded_object.predict(apt_list)
        ['SOCIAL HOUSING']
        """
        pass  # Replace this!

    @staticmethod
    def arg_sort(seq: list[int]) -> list[int]:
        """Return the indices of values in a sequence such that the values at each index are
        in ascending order. You don't need to use this function, but it may be helpful to
        find median values and partition data sets when you construct a KDTree.
        >>> KDTree.arg_sort([3, 1, 2])
        [1, 2, 0]
        >>> KDTree.arg_sort([8, 6, 7, 5, 3, 0, 9])
        [5, 4, 3, 1, 2, 0, 6]
        """
        pass  # Replace this!

def get_ground_truth(apartments: list[Apartment]) -> list[str]:
    """
    Get ground truth owner labels from a list of apartments.
    """
    return [apt.owner for apt in apartments]

def calculate_accuracy(predictions: list[str], truth: list[str]) -> int:
    """
    Helper method to allow you to calculate the accuracy of predictions.
    Input is a list of ground truth labels and a list of predicted labels.
    Output is a number between 0 and 100 representing the percent of predicted
    labels that are correct. Round to the nearest integer value for percentages
    >>> p = ['A','A','A','A','A','A','A','A','A','A']
    >>> t = ['A','A','A','A','A','A','A','A','A','B']
    >>> calculate_accuracy(p,t)
    90
    """
    pass # Replace this!

if __name__ == '__main__':

    # print("Below is an example of a KD Tree:")
    with open('kdtree.pkl', 'rb') as file:
        loaded_object = pickle.load(file)
        loaded_object.display_tree()

    # Once you write code to build your own KD Tree,
    # you can test it using the doctests below.
    import doctest
    doctest.testmod()

    # # You can also test your implementation using the following code.
    # # Step 1: Build a Tree with 'Training Data'
    # training_data = ApartmentReader.read_apartments('apartment-data/training-2026.csv')
    # kd = KDTree(training_data)
    #
    # # Step 2: Use tree to Predict the owners of apartments in a 'Test Set'
    # test_data = ApartmentReader.read_apartments('apartment-data/testing-2026.csv')
    # predictions = kd.predict(test_data)
    #
    # # Step 3: Ask ... do our predictions seem ok?
    # # NOTE THAT ACCURACY IS NOT ALWAYS THE BEST MEASURE OF GOODNESS
    # # What other measures might be more appropriate?  Or better?  Why?
    # ground_truth = get_ground_truth(test_data)
    # accuracy = calculate_accuracy(predictions, ground_truth)
    # print("\nThe raw accuracy of your classifier is: " + str(round(accuracy,2)) + " percent.\n")

