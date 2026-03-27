"""ADTS: Stacks and Queues

=== EECS 1516 Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we introduce two ADTs: Stacks and Queues.
A stack is a data structure that stores items in a last-in, first-out (LIFO).
A queue is a data structure that stores items in a first-in, first-out (FIFO).
We will explore the implementation of these ADTs using Python lists.
In the next lab, we will design and implement related ADTs using linked lists.

The data we use in this module is based on a record of
meeting attendance for the Toronto City Council. This record
is available on the internet, via the city's Open City Data Portal.
"""
from __future__ import annotations  # For type hints
from typing import Optional  # Optional indicates a variable can be of a certain type or None

from datetime import date
import csv


class Meeting:
    """A meeting represents a meeting of the Toronto city councillors."""
    _date: date
    _number: int
    _time: str

    def __init__(self, value: str, number: str, timing: str) -> None:
        """Initialize the Meeting.
        Note that input arguments are all strings, but we convert
        some of them to more useful types. For example, the date
        is converted to a date object and the meeting number is
        converted to an integer.  The timing of the meeting can be
        'Morning' or 'Afternoon'.
        """
        value = value.split('-')
        self._date = date(int(value[0]), int(value[1]), int(value[2]))
        self._number = int(number)
        self._timing = timing

    def get_date(self) -> date:
        """Return the date of this meeting."""
        return self._date

    def get_number(self) -> int:
        """Return the number of this meeting."""
        return self._number

    def get_timing(self) -> str:
        """Return the time of this meeting."""
        return self._timing

    def set_timing(self, param):
        """Set the time of this meeting."""
        self._timing = param


class EmptyStackError(Exception):
    """Exception raised when an error occurs."""


class MeetingStack:
    """A stack is a list-like structure that follows the LIFO (last-in,
    first-out) ordering. The last item added to the stack is the first one
    to be removed. We will implement a stack that stores Meeting objects.
    """
    _meeting_history: list[Meeting]

    def __init__(self) -> None:
        """Initialize a stack as an empty list."""
        self._meeting_history = []

    def is_empty(self) -> bool:
        """Return True if this stack contains no meetings.
        >>> s = MeetingStack()
        >>> s.is_empty()
        True
        >>> meeting = Meeting('2022-11-23','1','Afternoon')
        >>> s.push(meeting)
        >>> s.is_empty()
        False
        """
        return self._meeting_history == []

    def push(self, meeting: Meeting) -> None:
        """Add a new Meeting to the top of this stack."""
        self._meeting_history.append(meeting)

    def pop(self) -> Meeting:
        """Remove and return the Meeting at the top of this stack.

        Raise an EmptyStackError if this stack is empty.
        >>> s = MeetingStack()
        >>> meeting1 = Meeting('2022-11-23','1','Afternoon')
        >>> meeting2 = Meeting('2022-11-23','2','Morning')
        >>> s.push(meeting1)
        >>> s.push(meeting2)
        >>> s.pop().get_number()
        2
        """
        if self.is_empty():
            raise EmptyStackError
        else:
            return self._meeting_history.pop()


def remove_meetings(stack: MeetingStack, day: date) -> None:
    """Remove Meetings in <stack> that took place on <day>.
    Do not change the relative order of the other Meetings in the stack.
    >>> meetings = [Meeting('2022-12-15','2','Afternoon'), Meeting('2023-02-07','3','Afternoon'), Meeting('2023-02-08','4','Morning')]
    >>> s = MeetingStack()
    >>> for m in meetings: s.push(m)
    >>> remove_meetings(s, date(2023, 2, 8))
    >>> s.pop().get_number()
    3
    >>> s.pop().get_number()
    2
    >>> s.is_empty()
    True
    """
    temp = MeetingStack()

    while not stack.is_empty():
        meeting = stack.pop()
        if meeting.get_date() != day:
            temp.push(meeting)

    while not temp.is_empty():
        stack.push(temp.pop())


def change_meeting_times(stack: MeetingStack) -> MeetingStack:
    """Return a stack that contains swaps the meeting times of every meeting in <stack>.
    If an input meeting time is 'Afternoon', the output meeting time should be 'Morning', and vice versa.
    The input meeting stack should not be changed.

    >>> meetings = [Meeting('2022-12-15','2','Afternoon'), Meeting('2023-02-07','3','Afternoon'), Meeting('2023-02-08','4','Morning')]
    >>> s = MeetingStack()
    >>> for m in meetings: s.push(m)
    >>> s2 = change_meeting_times(s)
    >>> s.pop().get_number()  # s should be unchanged.
    4
    >>> s.pop().get_number()
    3
    >>> s.pop().get_number()
    2
    >>> s.is_empty()
    True
    >>> items = []
    >>> items.append(s2.pop())
    >>> items.append(s2.pop())
    >>> items.append(s2.pop())
    >>> [x.get_timing() for x in items]
    ['Afternoon', 'Morning', 'Morning']
    """
    temp = MeetingStack()
    new_stack = MeetingStack()

    while not stack.is_empty():
        temp.push(stack.pop())

    while not temp.is_empty():
        meeting = temp.pop()
        stack.push(meeting)

        timing = "Afternoon" if meeting.get_timing() == "Morning" else "Morning"
        meeting.set_timing(timing)
        new_stack.push(meeting) 

    return new_stack

###############################################################################
class MeetingQueue:
    """Queues also store items but in a different order. In a queue, the first
    item to be added is the first item to be removed. This is called a
    first-in-first-out (FIFO) or last-in-last-out (LILO) order.
    """
    _meeting_history: list[Meeting]

    def __init__(self) -> None:
        """Initialize a new empty queue."""
        self._meeting_history = []

    def is_empty(self) -> bool:
        """Return whether this queue contains no items.

        >>> q = MeetingQueue()
        >>> q.is_empty()
        True
        >>> s1 = Meeting('2022-11-23','1','Afternoon')
        >>> q.enqueue(s1)
        >>> q.is_empty()
        False
        """
        return self._meeting_history == []

    def enqueue(self, meeting: Meeting) -> None:
        """Add <item> to the back of this queue."""
        self._meeting_history.append(meeting)

    def dequeue(self) -> Optional[Meeting]:
        """Remove and return the meeting at the front of this queue.

        Return None if this Queue is empty.
        >>> q = MeetingQueue()
        >>> s1 = Meeting('2022-11-23','1','Afternoon')
        >>> s2 = Meeting('2022-12-15','2','Afternoon')
        >>> q.enqueue(s1)
        >>> q.enqueue(s2)
        >>> q.dequeue().get_number()
        1
        """
        if self.is_empty():
            return None
        else:
            return self._meeting_history.pop(0)


def count_meetings(queue: MeetingQueue, day: date) -> int:
    """Return a count of all the meetings in the queue
    that are on the day of <day>.

    Remove all these meetings from the queue.

    Precondition: queue contains only Meetings.
    >>> meetings = [Meeting('2022-12-15','2','Afternoon'), Meeting('2022-12-15','3','Afternoon'), Meeting('2023-02-08','4','Morning')]
    >>> q = MeetingQueue()
    >>> for m in meetings: q.enqueue(m)
    >>> count_meetings(q, date(2022, 12, 15))
    2
    >>> count_meetings(q, date(2023, 2, 8))
    1
    >>> q.is_empty()
    True
    """
    temp = MeetingQueue()
    count = 0

    while not queue.is_empty():
        m = queue.dequeue()

        if m.get_date() == day:
            count += 1
        else:
            temp.enqueue(m)

    while not temp.is_empty():
        queue.enqueue(temp.dequeue())

    return count


def safe_count_meetings(queue: MeetingQueue, day: date) -> int:
    """Return a count of all the meetings in the queue
    that are on the day of <day>.

    This time, do not alter the input queue.
    >>> meetings = [Meeting('2022-12-15','2','Afternoon'), Meeting('2022-12-15','3','Afternoon'), Meeting('2023-02-08','4','Morning')]
    >>> q = MeetingQueue()
    >>> for m in meetings: q.enqueue(m)
    >>> safe_count_meetings(q, date(2023, 2, 8))
    1
    >>> safe_count_meetings(q, date(2022, 12, 15))
    2
    >>> q.is_empty()
    False
    """
    temp = MeetingQueue()
    count = 0

    while not queue.is_empty():
        m = queue.dequeue()

        if m.get_date() == day:
            count += 1
        temp.enqueue(m)

    while not temp.is_empty():
        queue.enqueue(temp.dequeue())

    return count


def read_meeting_data(filename: str) -> dict[str, list[Meeting]]:
    """Accepts the name of a csv file.
    Returns a dict of CouncilMembers and the meetings
    that they attended since 2022.
    >>> members = read_meeting_data("city_council.csv")
    >>> len(members)
    27
    """
    retval = {}
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                name = row[0] + " " + row[1]
                if row[-1] == "Y":
                    meeting = Meeting(row[3], row[2], row[4])
                    if name in retval:
                        retval[name].append(meeting)
                    else:
                        retval[name] = [meeting]
            count += 1
    return retval


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # which city council member attended the most meetings since 2022?
    members = read_meeting_data("city_council.csv")
    max_meetings = 0
    max_member = ""
    for member in members:
        if len(members[member]) > max_meetings:
            max_meetings = len(members[member])
            max_member = member

    print("The city council member who attended the most meetings since 2022 is: ")
    print(max_member + ", who attended " + str(max_meetings) + " meetings.")