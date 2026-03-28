"""BST Trees and Fire Data

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we make our own ADTs to help us organize
Fire objects.  We continue to look at BSTs!  This time,
however, we explore the difference between BSTs that are
balanced and those that are not.  Of note, there are several
sub-varieties of trees that self-balance, including AVL trees
and Red-Black trees.  We will not be exploring these trees
in this module, but they are worth looking into if you are
interested in the topic. Your assignment focuses on KD-Trees,
which are a type of BST tree that is particularly
useful for organizing spatial data.  There are self-balancing
varieties of KD-Trees, as well.
"""
from __future__ import annotations

from typing import Optional

from datetime import datetime
import csv


class Fire:
    """Information about a fire incident in the GTA

    === Attributes ===
    _loss: the estimated dollar loss resulting from the fire
    _responding_personnel: the number of personnel who responded to the fire
    _cause: the possible cause of the fire
    _time: the time that the Toronto Fire Services arrived at the scene
    _lon: longitude of the fire
    _lat: latitude of the fire
    """
    _loss: int  # the estimated dollar loss resulting from the fire
    _responding_personnel: int  # the number of personnel who responded to the fire
    _cause: str  # the cause of the fire
    _time: datetime  # the time of the fire
    _lon: float  # the longitude of the fire
    _lat: float  # the latitude of the fire

    def __init__(self, loss: str, num: str, cause: str, when: str, lon: str, lat: str) -> None:
        """Initialize a new fire object with the given information.  The time
        of the fire is a string in the format 'YYYY-MM-DDTHH:MM:SS'.
        """
        self._loss = int(loss)
        self._responding_personnel = int(num)
        self._cause = cause
        self._time = datetime.strptime(when, '%Y-%m-%dT%H:%M:%S')
        self._lon = float(lon)
        self._lat = float(lat)

    def __repr__(self):
        return f'({self._lat},{self._lon}) at {self._time}: {self._loss}'

    @property
    def loss(self):
        return self._loss

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon


class BSTTree:
    """A Binary Search tree

    === Attributes ===
    _fire: The fire information stored in the root node of the tree
    _left: The left subtree of the root node.  The estimated loss from fires in
    this subtree will all be less than the estimated loss from the fire
    at the root.
    _right: The right subtree of the root node.  The estimated loss from fires in
    this subtree will all be greater than or equal to the estimated loss from the fire
    at the root.
    """
    _fire: Optional[Fire]
    _left: Optional[BSTTree]
    _right: Optional[BSTTree]

    def __init__(self, fire: Optional[Fire] = None) -> None:
        """Initialize a new node to store a Fire object, with no subtrees."""
        if fire is None:
            self._fire = None
            self._left = None
            self._right = None
        else:
            self._fire = fire
            self._left = BSTTree(None)  # a leaf points to two empty trees!
            self._right = BSTTree(None)  # this can be useful when you traverse the tree.

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def fire(self):
        return self._fire

    @left.setter
    def left(self, value):
        self._left = value

    @right.setter
    def right(self, value):
        self._right = value

    @fire.setter
    def fire(self, value):
        self._fire = value

    def is_empty(self) -> bool:
        """Return true if this tree is empty."""
        return self._fire is None

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
            answer = depth * '  ' + str(self._fire) + '\n'
            answer += self._left._str_helper(depth + 1)
            answer += self._right._str_helper(depth + 1)
            return answer

    def build_tree(self, items: list[Fire]) -> None:
        """Build a tree from the given list of fires.
        This method calls your insert method.
        The parameter 'items' is a list of Fire objects.
        """
        for i in items:
            self.insert(i)  # all we do is insert each item into the tree

    def count_nodes(self) -> int:
        """Return the number of nodes in this tree."""
        if self.is_empty():
            return 0
        else:
            return 1 + self._left.count_nodes() + self._right.count_nodes()

    def insert(self, fire: Fire) -> None:
        """Insert <fire> into this tree as follows:

            1. If the tree is empty, place <fire> at the root (i.e. in the _data attribute) of this tree.
            2. If the root of the tree is populated and the estimated loss from the <fire> is less
            than the loss located the root (i.e. in the _data attribute), insert the <fire> into the left subtree.
            3. If the root of the tree is populated and the estimated loss from the <fire> is greater
            than or equal to the loss located the root (i.e. in the _data attribute), insert the <fire> into the right subtree.
            >>> bst = BSTTree()
            >>> fires = read_fire_data('fires.csv')[0:5]
            >>> for f in fires: bst.insert(f)
            >>> bst._fire.loss
            20000
            >>> bst._left._fire.loss
            500
            >>> bst._right._fire.loss
            50000
            """
        if self.is_empty():
            self.fire = fire
            self.right = BSTTree()
            self.left = BSTTree()
        else:
            if self.fire.loss > fire.loss:
                self.left.insert(fire)
            else:
                self.right.insert(fire)

    def in_order_loss(self) -> str:
        """Print the estimated loss from all fires in this tree in order.
        You will need to do an in-order traversal of the tree to do this.
        >>> bst = BSTTree()
        >>> fires = read_fire_data('fires.csv')[0:5]
        >>> for f in fires: bst.insert(f)
        >>> print(bst.in_order_loss().strip())
        100 100 500 20000 50000
        """
        if self.is_empty():
            return ''
        else:
            # recursively print the left subtree
            result = self.left.in_order_loss()
            # print the current value
            result += str(self.fire.loss) + ' '
            # recursively print the right subtree
            result += self._right.in_order_loss()
            return result


    def pre_order_loss(self) -> str:
        """Print the estimated loss from all fires in this tree in pre-order.
        You will need to do a pre-order traversal of the tree to do this.
        >>> bst = BSTTree()
        >>> fires = read_fire_data('fires.csv')[0:5]
        >>> for f in fires: bst.insert(f)
        >>> print(bst.pre_order_loss().strip())
        20000 500 100 100 50000
        """
        if self.is_empty():
            return ''
        else:
            # print the current value
            result = str(self.fire.loss) + ' '
            # recursively print the left subtree
            result += self.left.pre_order_loss()
            # recursively print the right subtree
            result += self._right.pre_order_loss()
            return result

    def post_order_loss(self) -> str:
        """Print the estimated loss from all fires in this tree in post-order.
        You will need to do a post-order traversal of the tree to do this.
        >>> bst = BSTTree()
        >>> fires = read_fire_data('fires.csv')[0:5]
        >>> for f in fires: bst.insert(f)
        >>> print(bst.post_order_loss().strip())
        100 100 500 50000 20000
        """
        if self.is_empty():
            return ''
        else:
            # recursively print the left subtree
            result = self.left.post_order_loss()
            # recursively print the right subtree
            result += self._right.post_order_loss()
            # print the current value
            result += str(self.fire.loss) + ' '
            return result


def build_balanced_tree(items: list[Fire]) -> BSTTree:
    """
    Return a balanced BSTTree built from the given list of fires.
    The parameter 'items' is a list of Fire objects.
    In order to build a balanced tree, you should first sort the list of fires by estimated loss.
    Then, you should build the tree using a divide and conquer approach, as follows:
    1. Insert the middle element of the list into the tree.
    2. Recursively build the left subtree using the left half of the list.
    3. Recursively build the right subtree using the right half of the list.
    4. Return the tree.
    >>> bst = build_balanced_tree(read_fire_data('fires.csv')[0:1000])
    >>> bst.count_nodes()
    1000
    >>> abs(bst.left.count_nodes() -  bst.right.count_nodes()) < 2
    True
    >>> bst = BSTTree()
    >>> bst.build_tree(read_fire_data('fires.csv')[0:1000])
    >>> abs(bst.left.count_nodes() -  bst.right.count_nodes()) < 2
    False
    """
    if len(items) == 0:
        return BSTTree(None)
    
    items.sort(key=lambda x: x.loss)
    middle_idx = len(items) // 2

    bst = BSTTree(items[middle_idx])
    
    bst.left = build_balanced_tree(items[:middle_idx])
    bst.right = build_balanced_tree(items[middle_idx + 1:])
    
    return bst


def read_fire_data(filename: str) -> list[Fire]:
    """Accepts the name of a csv file.
    Returns a list of Fire Incidents in the file
    """
    fires = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                building = Fire(*row)
                fires.append(building)
            count += 1
    return fires


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    # There should be a difference in the number of nodes in the left and right subtrees
    # of the unbalanced tree. But the number of nodes in the left and right subtrees
    # of the balanced tree should be the same (within a node).

    # Make sure you know why this is the case.

    # Moreover, make sure you have a sense as to the benefit
    # of a balanced tree.  If you search for a node in a balanced tree,
    # how many comparisons will you need to make in the worst case?
    # How about in the average case?  How about in the best case?
    # What about for an unbalanced tree?

    unbalanced = BSTTree() # make an empty tree
    unbalanced.build_tree(read_fire_data('fires.csv'))
    print("\nIn an unbalanced tree there are ....")
    print(str(unbalanced.left.count_nodes()) + " nodes in the left subtree")
    print(str(unbalanced.right.count_nodes()) + " nodes in the left subtree")

    balanced = build_balanced_tree(read_fire_data('fires.csv'))
    print("\nIn a balanced tree there are ....")
    print(str(balanced.left.count_nodes()) + " nodes in the left subtree")
    print(str(balanced.right.count_nodes()) + " nodes in the left subtree")

    # Some questions you might want answer for yourself using your BST:

    # What was the total estimated loss from all fires in the file?
    # What was the average estimated loss from all fires in the file?
    # What was the estimated loss from the fire with the highest loss?
    # What was the estimated loss from the fire with the lowest loss?
    # How many fires were estimated to have a loss of at least $1,000,000?


