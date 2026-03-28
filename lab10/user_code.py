"""BST Trees and Fire Data

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we will compare Linked Lists and BSTs that
are again used to store Fire objects. While last time
we organized our Fire objects according to the loss
associated with each fire, this time we will organize
our data according to the number of personnel who
responded to each fire.

We will then compare the time it takes to construct a
BST and a Linked List, and the time it takes to insert
Fire objects into each ADT. You should see that the BST
is faster for both operations. Ask yourself why this
is the case!  And consider what the difference in time
complexity might be for other operations, such as
searching for a Fire object or deleting an object
from the collection.

You will need to have the package matplotlib installed
to run this module. You can install it by running
`pip3 install matplotlib` in your terminal, or by using the
package manager in your IDE.
"""
from __future__ import annotations

from typing import Optional
from timeit import timeit
import matplotlib.pyplot as plt
import random

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
        return f'{self._time}: {self._responding_personnel}'

    @property
    def responding_personnel(self):
        return self._responding_personnel


class LinkedListNode:
    """A node in a linked list.

    We will represent a linked list as a chain of linked list nodes.
    Each node will store a Fire object.

    === Attributes ===
    _fire: The fire information stored in this node.
    _next: The next node in the list, or None if there are no more nodes.
    """
    _fire: Optional[Fire]
    _next: Optional[LinkedListNode]

    def __init__(self, fire: Fire = None) -> None:
        """Initialize a new node to store a Fire object,
        with no next node."""
        if fire is None:
            self._fire = None  # An empty node
            self._next = None  # Initially, point to nothing
        else:
            self._fire = fire
            self._next = None  # Initially, point to nothing

    @property
    def next(self):
        return self._next

    @property
    def fire(self):
        return self._fire

    @next.setter
    def next(self, value):
        self._next = value

    @fire.setter
    def fire(self, value):
        self._fire = value

    def __str__(self):
        """Return a string representation of this LinkedListNode."""
        retval = f'{self._fire}'
        ptr = self._next
        while ptr is not None:
            retval += f' -> {ptr._fire}'
            ptr = ptr._next
        return retval

    def is_empty(self) -> bool:
        """Return whether this linked list is empty.
        """
        return self._fire is None

    def count_nodes(self) -> int:
        """Return the number of nodes in the linked list.
        """
        if self.is_empty():
            return 0
        else:
            count = 0
            ptr = self
            while ptr is not None:
                count += 1
                ptr = ptr._next
            return count

    def build_list(self, items: list[Fire]) -> None:
        """Build a tree from the given list of fires.
        This method calls your insert method.
        The parameter 'items' is a list of Fire objects.
        """
        for i in items:
            self.insert(i)  # all we do is insert each item into the tree

    def insert(self, item: Fire) -> None:
        """Insert a new Fire object into the LinkedList.
        The parameter 'item' is a Fire object.
        You should insert items in the list such that they are in ascending order
        by the number of personnel who responded to the fire.
        >>> ll = LinkedListNode()
        >>> ll.build_list(read_fire_data('fires.csv')[0:5])
        >>> ll._fire.responding_personnel
        4
        >>> ll._next._fire.responding_personnel
        4
        >>> ll._next._next._fire.responding_personnel
        22
        >>> ll._next._next._next._fire.responding_personnel
        47
        """
        if self.is_empty():
            self.fire = item
            return
        
        new_node = LinkedListNode(item)

        if item.responding_personnel < self._fire.responding_personnel:
            # insert in the front
            new_node.fire = self.fire
            new_node.next = self.next
            self.fire = item
            self.next = new_node
            return
        else:
            # insert in the middle/end
            curr_node = self
            # search for the right position
            while curr_node.next and curr_node.next.fire.responding_personnel <= item.responding_personnel:
                curr_node = curr_node.next
            # insert the node
            new_node.next = curr_node.next
            curr_node.next = new_node
        

    def build_linked_list_from_tree(self, firetree: BSTTree):
        """Populate a linked list from the given BSTTree of Fire objects.
        Note that as a part of this method, you will want to extract all
        fires from the input tree.  You can write a helper method
        to make this happen, as you see fit!! The tree traversal code
        that you wrote in your last lab may be useful here.
        >>> bst = BSTTree()
        >>> bst.build_tree(read_fire_data('fires.csv')[0:5])
        >>> ll = LinkedListNode()
        >>> ll.build_linked_list_from_tree(bst)
        >>> print(ll) # note this prints in order of responding personnel!
        2020-01-01 01:28:08: 4 -> 2020-01-01 02:17:49: 4 -> 2020-01-01 00:55:17: 22 -> 2020-01-01 00:46:05: 47 -> 2020-01-01 02:07:19: 73
        """
        if firetree.is_empty():
            return None

        # recurse left
        self.build_linked_list_from_tree(firetree.left)
        # insert current node
        self.insert(firetree.fire)
        # recurse right                         
        self.build_linked_list_from_tree(firetree.right)


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

    def count_nodes(self) -> int:
        """Return the number of nodes in this tree."""
        if self.is_empty():
            return 0
        else:
            return 1 + self._left.count_nodes() + self._right.count_nodes()

    def build_tree(self, items: list[Fire]) -> None:
        """Build a tree from the given list of fires.
        This method calls your insert method.
        The parameter 'items' is a list of Fire objects.
        """
        for i in items:
            self.insert(i)  # all we do is insert each item into the tree

    def insert(self, fire: Fire) -> None:
        """Note this method is very much like one from the last lab!!
        Insert a <fire> into this tree as follows:

            1. If the tree is empty, place <fire> at the root (i.e. in the _data attribute) of this tree.
            2. If the root of the tree is populated and the number of responding personnel to the <fire> is less
            than the loss located the root (i.e. in the _data attribute), insert the <fire> into the left subtree.
            3. If the root of the tree is populated and the number of responding personnel to the <fire> is greater
            than or equal to the loss located the root (i.e. in the _data attribute), insert the <fire> into the right subtree.
        >>> bst = BSTTree()
        >>> bst.build_tree(read_fire_data('fires.csv')[0:5])
        >>> bst._fire.responding_personnel
        47
        >>> bst._right._fire.responding_personnel
        73
        >>> bst._left._fire.responding_personnel
        22
        >>> bst._left._left._fire.responding_personnel
        4
        """
        if self.is_empty():
            self.fire = fire
            self.left = BSTTree()
            self.right = BSTTree()
        else:
            if fire.responding_personnel < self._fire.responding_personnel:
                self.left.insert(fire)
            else:
                self.right.insert(fire)

    def build_tree_from_linked_list(self, firelist: LinkedListNode):
        """Return a BSTTree built from the given linked list of Fire objects.
        The parameter 'firelist' is a linked list of Fire objects.
        Watch out though! If the linked list is sorted, the resulting
        tree will be unbalanced (why??). You may therefore want to shuffle the
        items in the linked list before inserting them into the tree.
        Note the doctests do NOT test for balance. But you may
        want to test for balance in your own tests!  A balanced tree allows
        for O(log n) search times.
        >>> bst = BSTTree()
        >>> ll = LinkedListNode()
        >>> ll.build_list(read_fire_data('fires.csv')[0:10])
        >>> ll.count_nodes()
        10
        >>> bst.build_tree_from_linked_list(ll)
        >>> bst.count_nodes()
        10
        """
        fires = []

        # traverese the linked list
        curr_node = firelist
        while curr_node:
            fires.append(curr_node.fire)
            curr_node = curr_node.next

        # shuffle to avoid unbalanced tree
        random.shuffle(fires)

        # build tree
        for fire in fires:
            self.insert(fire)


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
    num = doctest.testmod().failed

    if num > 0:
        print('\nOnce you pass all the tests in this file,\nthis code will time and plot the performance of your methods!')
        exit(0)

    num_fires = [1000, 2000, 3000, 4000, 5000]
    insert_list_times = []  # list to store the time taken to insert a fire into a linked list
    insert_tree_times = []  # list to store the time taken to insert a fire into a BST
    build_list_times = []  # list to store the time taken to build a linked list
    build_tree_times = []  # list to store the time taken to build a BST
    fire_list = read_fire_data("fires.csv")

    for index in num_fires: # test for different numbers of fires in our collections

        linked_list = LinkedListNode()
        build_list_times.append(timeit('linked_list.build_list(fire_list[0:index])', number=1, globals=locals()))
        bst_tree = BSTTree()
        build_tree_times.append(timeit('bst_tree.build_tree(fire_list[0:index])', number=1, globals=locals()))

        list_times = []
        tree_times = []
        for i in range(1, 100):  # test 100 insertions
            num = random.randint(0, len(fire_list)) # pick a random fire
            fire = fire_list[num]
            time = timeit('bst_tree.insert(fire_list[num])', number=1, globals=locals())
            tree_times.append(time)
            time = timeit('linked_list.insert(fire_list[num])', number=1, globals=locals())
            list_times.append(time)

        insert_list_times.append(sum(list_times) / len(list_times))
        insert_tree_times.append(sum(tree_times) / len(tree_times))

        # Uncomment the following lines to see the average time to insert into a linked list and a tree
        if index == 1000: print(f'Average time in seconds to insert into ....')
        print(f'a linked list with {index} elements: {sum(insert_list_times) / len(insert_list_times)}')
        print(f'a binary search tree with {index} elements: {sum(insert_tree_times) / len(insert_tree_times)}')

    # plot the data
    f, (ax1, ax2) = plt.subplots(1, 2)

    # subplot 1 (insertion time)
    ax1.plot(num_fires, insert_list_times, label='Linked List')
    ax1.plot(num_fires, insert_tree_times, label='BST Tree')
    ax1.set_xlabel('Num Fires in ADT')
    ax1.set_ylabel('Time (in secs)')
    ax1.set_title('Insertion Time')
    ax1.legend()

    # subplot 2 (construction time)
    ax2.plot(num_fires, build_list_times, label='Linked List')
    ax2.plot(num_fires, build_tree_times, label='BST Tree')
    ax2.set_xlabel('Num Fires in ADT')
    ax2.set_title('Construction Time')
    ax2.legend()
    plt.show()





