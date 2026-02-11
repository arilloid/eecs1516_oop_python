from __future__ import annotations


class EventTicket:
    """ A ticket for an event. """
    _ticket_num: int
    _price: float

    def __init__(self, ticket_num: int, price: float = 100.00) -> None:
        self._ticket_num = ticket_num
        self._price = price

    def __str__(self):
        return f"Ticket: {self._ticket_num}"

    def __repr__(self):
        return f"Ticket: {self._ticket_num}"

    def get_price(self) -> float:
        """Return the price of this ticket."""
        return self._price


class DinnerTheatreTicket(EventTicket):
    """ A ticket for a dinner theatre event.
    Dinner theatre tickets include a meal, which increases the cost
    of each ticket.  Meals are $50.00 each, and can be any of the following:
    - "chicken", "beef", "vegetarian", "vegan", or "gluten-free".
    """
    _ticket_num: int
    _price: float
    _meal: str

    def __init__(self, ticket_num: int, price: float, meal: str) -> None:
        """Initialize a new dinner theatre ticket.
        Dinner theatre tickets include a meal, which increases the cost
        of each ticket."""
        super().__init__(ticket_num, price)
        self._meal = meal

    def __str__(self):
        return f"Ticket: {self._ticket_num} with {self._meal} meal"

    def __repr__(self):
        return f"Ticket: {self._ticket_num} with {self._meal} meal"

    def get_price(self) -> float:
        """Return the price of this ticket.
        Dinner theatre tickets include a meal, which increases the cos
        of each ticket.  Meals are $50.00 each.  Your code should therefore
        return the base price of the ticket, plus $50.00 for the meal.
        """
        return super().get_price() + 50


class EventManagementSystem:
    _available_tickets: list[EventTicket]
    _returned_tickets: list[EventTicket]

    def __init__(self, num_tickets: int, dinner_theatre: bool) -> None:
        """Initialize a new ticket system. Create a number of available tickets
            that is equal to num_tickets; store these in available_tickets.
            If dinner_theatre is True, then the tickets should be DinnerTheatreTickets, otherwise they should be
            EventTickets. All tickets should be created with a base price of $100.00.
            >>> system = EventManagementSystem(3, False)
            >>> system._available_tickets
            [Ticket: 1, Ticket: 2, Ticket: 3]
            >>> system = EventManagementSystem(1, True)
            >>> system._available_tickets
            [Ticket: 1 with vegetarian meal]
            """

        self._available_tickets = []
        self._returned_tickets = []

        # Note that these solutions assume that ticket numbers
        # start at 1 and increase by 1 for each ticket!!
        for t in range(1, num_tickets+1):
            if dinner_theatre:
                self._available_tickets.append(DinnerTheatreTicket(t, 100, "vegetarian"))
            else:
                self._available_tickets.append(EventTicket(t, 100))

    def tickets_exist(self) -> bool:
        """Indicates whether there are any available tickets.
        >>> system = EventManagementSystem(1, False)
        >>> system.tickets_exist()
        True
        >>> system.sell_ticket()
        Ticket: 1
        >>> system.tickets_exist()
        False
        """
        # Note the problem was a bit ambiguous about if we should just check _available_tickets or
        # both _available_tickets and _returned_tickets!!
        return len(self._available_tickets) > 0 or len(self._returned_tickets) > 0

    def sell_ticket(self) -> EventTicket:
        """Returns the next available ticket for sale. If there are no available
        tickets, return None.

        Note that the box office chooses to sell tickets in a particular order, as follows:
        If any tickets for seats have been returned, sell those tickets first and in the order
        in which they were returned. Then sell any other available seats.

        As an example, say we sell tickets 1, 2, 3, and 4. Then, ticket 2 is returned,
        and then ticket 1 is returned. The next ticket we will sell will be 2, followed by 1.
        After that (assuming no other ticket has been returned), we would then sell ticket
        5 next.
        >>> system = EventManagementSystem(500, False)
        >>> t1 = system.sell_ticket() # sell ticket 1-4
        >>> t2 = system.sell_ticket()
        >>> t3 = system.sell_ticket()
        >>> t4 = system.sell_ticket()
        >>> system.return_ticket(t2) # return ticket 2
        >>> system.return_ticket(t1) # return ticket 1
        >>> t5 = system.sell_ticket() # sell ticket 2, then 1
        >>> t5
        Ticket: 2
        >>> t6 = system.sell_ticket() # sell ticket 2, then 1
        >>> t6
        Ticket: 1
        >>> t7 = system.sell_ticket() # sell ticket 5
        >>> t7
        Ticket: 5
        """
        if len(self._returned_tickets) > 0:
            my_ticket = self._returned_tickets[0]
            self._returned_tickets.remove(my_ticket)
            # return self._returned_tickets.pop(0) # alternate solution
            return my_ticket
        elif len(self._available_tickets) > 0:
            my_ticket = self._available_tickets[0]
            self._available_tickets.remove(my_ticket)
            # return self._available_tickets.pop(0) # alternate solution
            return my_ticket
        else:
            return None

    def return_ticket(self, ticket: EventTicket) -> None:
        """Returns a ticket and stores this in the _returned_tickets
        list. Note that we will want the order in which tickets
        are returned to be the same as the order in which they were
        sold."""
        self._returned_tickets.append(ticket)


def get_ticket_prices(tickets: list[EventTicket]) -> list[float]:
    """ Answer to Q3!
    >>> tickets = [DinnerTheatreTicket(1,100,"chicken"), EventTicket(2,200)]
    >>> get_ticket_prices(tickets)
    [150, 200]
    """
    return [x.get_price() for x in tickets]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    ticket_system = EventManagementSystem(500, True)  # make 500 dinner theatre tickets
    print("Tickets for sale: " + str(ticket_system.tickets_exist()))  # should print True

    print("\n******\n")

    sold = []
    for i in range(0, 3):
        sold.append(ticket_system.sell_ticket())
        print("Selling: " + str(sold[-1]))
        print("Price is: " + str(sold[-1].get_price()) + " dollars.")

    print("\n******\n")

    sold = sold[::-1]  # reverse the order of the list
    for ticket in sold:
        print("Returning:" + str(ticket))
        ticket_system.return_ticket(ticket)

    print("\n******\n")

    print("Selling: " + str(ticket_system.sell_ticket()))  # Should be Ticket number 2
