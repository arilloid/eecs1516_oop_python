"""Priority Queue Implementations ... with Linked Lists!

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we will compare implementations of a Queue
that relies on Linked Lists. The data we will be using
relates to the public's use of city websites.

We will compare Queue implementations that make use of
both singly and doubly linked lists.  More specifically,
we will be comparing the time required to enqueue and dequeue
elements from each of these implementations.  You should notice
that the singly linked list is slower for dequeue operations.
Ask yourself why this is the case!  And consider what the
difference in time complexity might be for other operations,
or for implementations that make use of Python's built-in
data structures.

As before, you will need to have the package matplotlib installed
to run this module. You can install it by running
`pip3 install matplotlib` in your terminal, or by using the
package manager in your IDE.
"""
from __future__ import annotations

from typing import Optional
from timeit import timeit
import matplotlib.pyplot as plt
import random

import csv


class CityWebsite:
    """Information about the pages that users visit on city run websites

    === Attributes ===
    _name: the name of the website
    _sessions: the number of individual viewing sessions on the website
    _views: the number of individual pages viewed on the website
    _view_time: the average time, in seconds, spent on the website
    _bounce_rate: the number of users who left the website after viewing only one page
    """
    _name: str  # the name of the website
    _sessions: int  # the number of individual viewing sessions on the website
    _views: int  # the number of page views on the website
    _view_time: float  # the average time, in seconds, spent on the website
    _bounce_rate: float  # the bounce rate of the website

    def __init__(self, name: str, sessions: str, views: str, vtime: str, bounce: str) -> None:
        """Initialize a new fire object with the given information.  The time
        of the fire is a string in the format 'YYYY-MM-DDTHH:MM:SS'.
        """
        self._name = name
        self._sessions = int(sessions)
        self._views = int(views)
        self._view_time = float(vtime)
        self._bounce_rate = float(bounce)

    def __repr__(self):
        return f'{self._views} views: {self._name}'

    @property
    def views(self):
        return self._views


class PriorityQueue1:
    """ A priority queue is a data structure that stores elements in order of priority.
    In this case, we will determine priority by the number of views that are
    associated with a CityPageView object. We will encode two different varieties
    of priority queues: one that is built with a singly linked list, and another that uses
    a doubly linked list. This one is the singly linked list implementation.

    === Attributes ===
    _rear: The back node in the PQ, or None if the PQ is empty.
    """
    _rear: Optional[PriorityQueue1Node]

    def __init__(self) -> None:
        self._rear = None  # Initially, the queue is empty

    def __str__(self):
        """Return a string representation of this Priority Queue."""
        if self._rear is None:
            return 'PQ is empty!'
        else:
            ptr = self._rear
            retval = ""
            while ptr is not None:
                retval += str(ptr.city_website)
                if ptr.next is not None:
                    retval += " -> \n"
                ptr = ptr.next
            return retval

    def build_pq(self, websites: list[CityWebsite]) -> None:
        for i in websites:
            self.enqueue(i)

    def enqueue(self, city_site: CityWebsite) -> None:
        """Add the given city_site to the queue.
        Make sure to insert the item so that the queue
        is ordered in ascending order, based on the number of views.
        This means you will have to traverse the queue from the rear
        to the front to find the correct position to insert each new item.
        You will be comparing the number of views associated with city_site with
        the number of views associated with the other items in the queue
        as you traverse it.
        >>> pq = PriorityQueue1()
        >>> websites = read_city_data('city_websites.csv')[0:5]
        >>> for site in websites:
        ...     pq.enqueue(site)
        >>> print(pq)  # doctest: +NORMALIZE_WHITESPACE
        1129983 views: Parking Violations||www.toronto.ca/services-payments/tickets-fines-penalties/pay/parking-violations/ ->
        1961673 views: Pay Your Parking Violation||www.toronto.ca/services-payments/tickets-fines-penalties/pay/pay-your-parking-violation/ ->
        2366612 views: Search Results||find.toronto.ca/searchblox/servlet/searchservlet ->
        2692846 views: Services & Payments, Parking Violation Notice Lookup||secure.toronto.ca/webapps/parking/ ->
        5764191 views: City Of Toronto||www.toronto.ca/
        """
        new_node = PriorityQueue1Node(city_site)

        if self._rear is None:
            self._rear = new_node
            return
        
        if city_site.views <= self._rear.city_website.views:
            new_node.next = self._rear
            self._rear = new_node
        else:
            curr_node = self._rear
            while curr_node.next and curr_node.next.city_website.views <= city_site.views:
                curr_node = curr_node.next

            new_node.next = curr_node.next
            curr_node.next = new_node
        
        
    def dequeue(self) -> CityWebsite:
        """Remove and return the first item that was inserted
        into the queue (i.e. the item with the most page views
        in the entire queue). The item should be removed from the
        queue when it is dequeued. You will have to traverse the queue
        from the rear to the front to find the correct item to remove.
        If the queue is empty, raise an IndexError.
        >>> pq = PriorityQueue1()
        >>> websites = read_city_data('city_websites.csv')[0:5]
        >>> for site in websites:
        ...     pq.enqueue(site)
        >>> print(pq.dequeue()) # doctest: +NORMALIZE_WHITESPACE
        5764191 views: City Of Toronto||www.toronto.ca/
        >>> print(pq) # doctest: +NORMALIZE_WHITESPACE
        1129983 views: Parking Violations||www.toronto.ca/services-payments/tickets-fines-penalties/pay/parking-violations/ ->
        1961673 views: Pay Your Parking Violation||www.toronto.ca/services-payments/tickets-fines-penalties/pay/pay-your-parking-violation/ ->
        2366612 views: Search Results||find.toronto.ca/searchblox/servlet/searchservlet ->
        2692846 views: Services & Payments, Parking Violation Notice Lookup||secure.toronto.ca/webapps/parking/
        """
        if self._rear is None:
            raise IndexError("Queue is empty")
        
        if self._rear.next is None:
            site = self._rear.city_website
            self._rear = None
            return site
        
        curr_node = self._rear
        # find second to last node
        while curr_node.next.next:
            curr_node = curr_node.next
        
        site = curr_node.next.city_website
        curr_node.next = None   

        return site


class PriorityQueue1Node:
    """We will be encoding two different types of queues using linked lists.
    This first queue will be a singly linked list. Each node will store a
    CityPageView object, and will point to the next node in the queue. The
    entire queue will be represented as a chain of linked list nodes;
    the first node in the chain will be the front of the queue, and the last
    node will be the back of the queue.

    === Attributes ===
    _city_website: The fire information stored in this node.
    _next: The next node in the list, or None if there are no more nodes.
    """
    _city_website: Optional[CityWebsite]
    _next: Optional[PriorityQueue1Node]

    def __init__(self, city_site: CityWebsite = None) -> None:
        """Initialize a new node to store a CityPageView object,
        with no next node."""
        if city_site is None:
            self._city_website = None  # An empty node
            self._next = None  # Initially, point to nothing
        else:
            self._city_website = city_site
            self._next = None  # Initially, point to nothing

    @property
    def next(self):
        return self._next

    @property
    def city_website(self):
        return self._city_website

    @next.setter
    def next(self, value):
        self._next = value

    @city_website.setter
    def city_website(self, value):
        self._city_website = value

    def __str__(self):
        """Return a string representation of this LinkedListNode."""
        return f'{self._city_website}'


class PriorityQueue2:
    """We will be encoding two different types of queues using linked lists.

    === Attributes ===
    _front: The front node in the PQ, or None if the PQ is empty.
    _back: The rear node in the PQ, or None if the PQ is empty.
    """
    _rear: Optional[PriorityQueue2Node]
    _front: Optional[PriorityQueue2Node]

    def __init__(self) -> None:
        self._front = None  # Initially, the queue is empty
        self._rear = None  # Initially, the queue is empty

    def __str__(self):
        """Return a string representation of this PQ."""
        if self._rear is None:
            return 'PQ is empty'
        else:
            ptr = self._rear
            retval = ""
            while ptr is not None:
                retval += str(ptr.city_website)
                if ptr.next is not None:
                    retval += " -> \n"
                ptr = ptr.next
            return retval

    def print_backwards(self):
        if self._rear is None:
            print('PQ is empty')
        else:
            ptr = self._front
            retval = ""
            while ptr is not None:
                retval += str(ptr.city_website)
                if ptr.previous is not None:
                    retval += " -> \n"
                ptr = ptr.previous
            print(retval)

    def build_pq(self, websites: list[CityWebsite]) -> None:
        for i in websites:
            self.enqueue(i)

    def enqueue(self, item: CityWebsite) -> None:
        """Add the given city_site to the queue.
        Make sure to insert the item so that the queue
        is ordered in ascending order, based on the number of views.
        This means you will have to traverse the queue to find
        the correct position to insert each new item.  You will be
        comparing the number of views associated with city_site with
        the number of views associated with the other items in the queue
        as you traverse it. You can traverse the queue from the front
        or the rear, but you must be consistent in your implementation.
        >>> pq = PriorityQueue2()
        >>> websites = read_city_data('city_websites.csv')[0:5]
        >>> for site in websites:
        ...     pq.enqueue(site)
        >>> print(pq)  # doctest: +NORMALIZE_WHITESPACE
        1129983 views: Parking Violations||www.toronto.ca/services-payments/tickets-fines-penalties/pay/parking-violations/ ->
        1961673 views: Pay Your Parking Violation||www.toronto.ca/services-payments/tickets-fines-penalties/pay/pay-your-parking-violation/ ->
        2366612 views: Search Results||find.toronto.ca/searchblox/servlet/searchservlet ->
        2692846 views: Services & Payments, Parking Violation Notice Lookup||secure.toronto.ca/webapps/parking/ ->
        5764191 views: City Of Toronto||www.toronto.ca/
        >>> pq.print_backwards()  # doctest: +NORMALIZE_WHITESPACE
        5764191 views: City Of Toronto||www.toronto.ca/ ->
        2692846 views: Services & Payments, Parking Violation Notice Lookup||secure.toronto.ca/webapps/parking/ ->
        2366612 views: Search Results||find.toronto.ca/searchblox/servlet/searchservlet ->
        1961673 views: Pay Your Parking Violation||www.toronto.ca/services-payments/tickets-fines-penalties/pay/pay-your-parking-violation/ ->
        1129983 views: Parking Violations||www.toronto.ca/services-payments/tickets-fines-penalties/pay/parking-violations/
        """
        new_node = PriorityQueue2Node(item)

        if self._rear is None:
            self._rear = new_node
            self._front = new_node
            return
        
        if item.views <= self._rear.city_website.views:
            new_node.next = self._rear
            self._rear.previous = new_node
            self._rear = new_node
        else:
            curr_node = self._rear
            while curr_node.next and curr_node.next.city_website.views <= item.views:
                curr_node = curr_node.next
            
            new_node.next = curr_node.next
            new_node.previous = curr_node
            if curr_node.next:
                curr_node.next.previous = new_node
            else:
                self._front = new_node
            
            curr_node.next = new_node
        

    def dequeue(self) -> CityWebsite:
        """Remove and return the first item that was inserted
        into the queue (i.e. the item with the most page views
        in the entire queue). The item should be removed from the
        queue when it is dequeued. You should be able to do this
        in O(1) time!!
        If the queue is empty, raise an IndexError.
        >>> pq = PriorityQueue1()
        >>> websites = read_city_data('city_websites.csv')[0:5]
        >>> for site in websites:
        ...     pq.enqueue(site)
        >>> print(pq.dequeue()) # doctest: +NORMALIZE_WHITESPACE
        5764191 views: City Of Toronto||www.toronto.ca/
        >>> print(pq) # doctest: +NORMALIZE_WHITESPACE
        1129983 views: Parking Violations||www.toronto.ca/services-payments/tickets-fines-penalties/pay/parking-violations/ ->
        1961673 views: Pay Your Parking Violation||www.toronto.ca/services-payments/tickets-fines-penalties/pay/pay-your-parking-violation/ ->
        2366612 views: Search Results||find.toronto.ca/searchblox/servlet/searchservlet ->
        2692846 views: Services & Payments, Parking Violation Notice Lookup||secure.toronto.ca/webapps/parking/
        """
        if self._front is None:
            raise IndexError("Queue is empty")

        site = self._front.city_website

        if self._front.previous is None:
            self._rear = None
            self._front = None
        else:
            self._front = self._front.previous
            self._front.next = None
            
        return site 


class PriorityQueue2Node:
    """A node in a doubly linked list.

    We have seen linked lists, which are a collection of nodes
    where each node points to the next node in the list. In a
    doubly linked list, each node also points to the previous
    node in the list.

    === Attributes ===
    _city_website: The city website information stored in this node.
    _next: The next node in the list, or None if there are no more nodes.
    _previous: The previous node in the list, or None if there are no preceding nodes.
    """
    _city_website: Optional[CityWebsite]
    _next: Optional[PriorityQueue2Node]
    _previous: Optional[PriorityQueue2Node]

    def __init__(self, city_site: CityWebsite = None) -> None:
        """Initialize a new node to store a CityPageView object,
        with no next node."""
        if city_site is None:
            self._city_website = None  # An empty node
            self._next = None  # Initially, point to nothing
            self._previous = None  # Initially, point to nothing
        else:
            self._city_website = city_site
            self._next = None  # Initially, point to nothing
            self._previous = None  # Initially, point to nothing

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    @property
    def city_website(self):
        return self._city_website

    @next.setter
    def next(self, value):
        self._next = value

    @previous.setter
    def previous(self, value):
        self._previous = value

    @city_website.setter
    def city_website(self, value):
        self._city_website = value

    def __str__(self):
        """Return a string representation of this LinkedListNode."""
        return f'{self._city_website}'


def read_city_data(filename: str) -> list[CityWebsite]:
    """Accepts the name of a csv file.
    Returns a list of CityPageView objects in the file
    """
    fires = []
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                building = CityWebsite(*row)
                fires.append(building)
            count += 1
    return fires


if __name__ == '__main__':

    import doctest
    num = doctest.testmod()

    if num[0] == 0:

        num_websites = [50, 100, 175, 250]
        enqueue1_times, enqueue2_times = [], []
        dequeue1_times, dequeue2_times = [], []
        build_queue1_times, build_queue2_times = [], []

        city_websites = read_city_data("city_websites.csv")

        for index in num_websites:

            pq1 = PriorityQueue1()
            pq2 = PriorityQueue2()
            build_queue1_times.append(timeit('pq1.build_pq(city_websites[0:index])', number=1, globals=locals()))
            build_queue2_times.append(timeit('pq2.build_pq(city_websites[0:index])', number=1, globals=locals()))

            pq1_times = []
            pq2_times = []
            for i in range(1, 100):  # test 100 insertions

                num = random.randint(0, len(city_websites)-1) # pick a random fire
                website = city_websites[num]

                time = timeit('pq1.enqueue(website)', number=1, globals=locals())
                pq1_times.append(time)
                time = timeit('pq2.enqueue(website)', number=1, globals=locals())
                pq2_times.append(time)

            enqueue1_times.append(sum(pq1_times) / len(pq1_times))
            enqueue2_times.append(sum(pq2_times) / len(pq2_times))

            pq1_times = []
            pq2_times = []
            for i in range(1, 100):  # test 100 insertions
                time = timeit('_ = pq1.dequeue()', number=1, globals=locals())
                pq1_times.append(time)
                time = timeit('_ = pq2.dequeue()', number=1, globals=locals())
                pq2_times.append(time)

            dequeue1_times.append(sum(pq1_times) / len(pq1_times))
            dequeue2_times.append(sum(pq2_times) / len(pq2_times))

            # Uncomment the following lines to see the average time to insert into a linked list and a tree
            # if index == 50:
            #     print(f'Average time in seconds to dequeue from ....')
            # print(f'a singly linked list PQ: {sum(pq1_times) / len(pq1_times)}')
            # print(f'a doubly linked list PQ: {sum(pq2_times) / len(pq2_times)}')

        #plot the data
        f, (ax1, ax2, ax3) = plt.subplots(1, 3)

        # subplot 1 (build time)
        ax1.plot(num_websites, build_queue1_times, label='PQ1')
        ax1.plot(num_websites, build_queue2_times, label='PQ2')
        ax1.set_ylabel('Time (in secs)')
        ax1.set_title('Build PQ Time')
        ax1.legend()

        # subplot 2 (enqueue time)
        ax2.plot(num_websites, enqueue1_times, label='PQ1')
        ax2.plot(num_websites, enqueue2_times, label='PQ2')
        ax2.set_xlabel('Num Websites in ADT')
        ax2.set_title('Enqueue Time')
        ax2.legend()

        #subplot 3 (dequeue time)
        ax3.plot(num_websites, dequeue1_times, label='PQ1')
        ax3.plot(num_websites, dequeue2_times, label='PQ2')
        ax3.set_title('Dequeue Time')
        ax3.legend()

        plt.show()
