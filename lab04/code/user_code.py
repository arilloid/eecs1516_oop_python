"""Object-Oriented Programming: Visualization example

=== EECS Winter 2024 ===
Lassonde School of Engineering

=== Module Description ===
In this module we visualize watermain breaks around York using matplotlib.
We will use a software design pattern that is a version of a Model-View-Controller (MVC)
design. This separates our data model from our visualization.
"""
from __future__ import annotations
from datetime import date
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import csv  # for reading the data file, you will need this!

draw = True  # change this when you are ready to draw the map


class MapView:  # the visualization class

    def __init__(self) -> None:
        """Initialize a new MapView object.
        Attributes:
        _h: height of the map
        _w: width of the map
        _urx: upper right x coordinate of the map
        _ury: upper right y coordinate of the map
        _llx: lower left x coordinate of the map
        _lly: lower left y coordinate of the map
        _fig: the figure
        _ax: the axes
        """
        self._h, self._w = 300, 670  # dimensions of the map
        self._urx, self._ury = 43.781322, -79.533667  # coordinate boundaries of the map
        self._llx, self._lly = 43.745431, -79.424748
        self._fig = None
        self._ax = None

    def draw(self, breaks: list[WatermainBreak], years: list[int]) -> None:
        """Draw the water main breaks in 'breaks' on the map.
        The title of the plot will contain the number of breaks
        and the years in which they occurred.
        """
        title = "York University"
        if breaks is not None:
            title = f"{len(breaks)} watermain breaks"
        if years is not None and len(years) > 0:
            title = f"{len(breaks)} watermain breaks in years: {years}"

        self._fig, self._ax = plt.subplots()
        self._draw_map()
        self._fig.canvas.draw()
        if breaks is not None:
            self._draw_breaks(breaks)
        plt.title(title)
        plt.show()

    def _draw_map(self):
        """ helper function to draw the map."""
        img = mpimg.imread('york.png')
        self._ax.imshow(img)
        self._ax.autoscale(False)

    def _draw_breaks(self, breaks: list[WatermainBreak], color: str = 'ro'):
        """ helper function to draw watermain breaks.
        breaks: a list of WatermainBreak objects.
        color: the color to use to illustrate the breaks.
        Note that to draw a break we need to convert its coordinates,
        which are longitude and latitude, to pixel coordinates.
        """
        ylim = self._ax.get_ylim()
        xlim = self._ax.get_xlim()
        self._h = math.floor(max(ylim))
        self._w = math.floor(max(xlim))

        filtered_breaks = list(
            filter(lambda x: self._lly >= x.get_lon() >= self._ury and self._urx >= x.get_lat() >= self._llx, breaks))
        x_values = list(
            map(lambda x: self._w - self._w * ((x.get_lon() - self._lly) / (self._ury - self._lly)), filtered_breaks))
        y_values = list(
            map(lambda x: self._h - self._h * ((x.get_lat() - self._llx) / (self._urx - self._llx)), filtered_breaks))
        self._ax.plot(x_values, y_values, color)


class BreakException(Exception):
    """A custom exception class for watermain breaks."""

    def __init__(self, message: str = "BreakException"):
        """ Initialize a new BreakException."""
        super().__init__(message)


class WatermainBreak:
    """A watermain break
    === Attributes ===
    _date: The complete date of the break (year, month, day)
    _year: The year of the break
    _lon: longitude
    _lat: latitude
    """
    _date: date
    _year: int
    _lon: float
    _lat: float

    def __init__(self, when: date, year: int, lon: float, lat: float) -> None:
        """Initialize a new WatermainBreak object.
        Note that this constructor expects the date to be a 'date' object,
        the year to be an int, and the longitude and latitude to be floats.
        This code will be similar to what you have seen
        in prior labs save that we want you to throw a
        BreakException if the year attribute is less than 1990 or
        greater than 2016. In this case, raise a BreakException
        with the following message:
        "No data before 1990 or after 2016"
        Also raise an error if the longitude or latitude are not floats,
        the year is not an int, or the date is not a date object. You
        can generate any error message you like in these cases.
        >>> wm = WatermainBreak(date(1990,2,7),1990,-79.4423175852,43.7400136761)
        >>> isinstance(wm.get_date(), date)
        True
        >>> wm.get_year()
        1990
        >>> wm = WatermainBreak(date(1972,2,7),1972,-79.4423175852,43.7400136761)
        Traceback (most recent call last):
        ...
        BreakException: No data before 1990 or after 2016
        """
        pass  # TODO: Implement this function

    def get_year(self):
        return self._year

    def get_date(self):
        return self._date

    def get_lon(self):
        return self._lon

    def get_lat(self):
        return self._lat

    def __repr__(self):
        """Return a representation of this water main break (str)."""
        return f"WatermainBreak('{self._date}', {self._year}, {self._lon}, {self._lat})"


class BreakFilter:
    """A filter for watermain breaks."""
    _filter_years: list[int]
    _breaks: list[WatermainBreak]

    def __init__(self, filter_years: list[int], breaks: list[WatermainBreak]) -> None:
        """ Initialize a new watermain break filter.
        breaks is an input list of WatermainBreak that we will filter.
        filter_years is a list containing all the years of
        watermain breaks that we want to keep.
        Save filtered breaks in self._breaks.
        Save the filter_years list in the attribute self._filter_year.
        If filter_years is empty, save all the breaks in self._breaks.
        >>> breaks = [WatermainBreak(date(1990,2,7),1990,-79.4423175852,43.7400136761), WatermainBreak(date(1990,2,7),1990,-79.4423175852,43.7400136761), WatermainBreak(date(1991,2,7),1991,-79.4423175852,43.7400136761)]
        >>> filtered = BreakFilter([1990], breaks)
        >>> len(filtered.get_breaks())
        2
        >>> filtered = BreakFilter([1991], breaks)
        >>> len(filtered.get_breaks())
        1
        >>> filtered = BreakFilter([], breaks)
        >>> len(filtered.get_breaks())
        3
        """
        pass  # TODO: Implement this function

    def get_breaks(self):
        if hasattr(self, '_breaks'):
            return self._breaks

    def get_filter_years(self):
        if hasattr(self, '_filter_years'):
            return self._filter_years


def read_breaks_file(filename: str) -> list[WatermainBreak]:
    """Read <filename> and return a list containing the water main breaks
    in this file. Each line in <filename> contains data about a single
    water main break in this format:

    date, year, longitude, latitude

    The date will be a string in the format YYYY/MM/DD
    >>> breaks = read_breaks_file('york_breaks.csv')
    >>> len(breaks)
    2933
    >>> isinstance(breaks[0], WatermainBreak)
    True
    """
    pass  # TODO: Implement this function


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Once you pass all the doctests, set the flag on line 19 to True.
    # This should draw a map with watermain breaks on it.
    if draw:
        break_list = read_breaks_file("york_breaks.csv")  # Read the trees from the file
        input_years = input(
            "See all the watermain breaks for which years?\n"
            "Enter years as a comma delimited list, e.g. 1990, 1991, 1992\n")
        input_years = [int(x) for x in input_years.strip().split(",")]
        t_filter = BreakFilter(input_years, break_list)  # Filter the trees based on the user's input
        treeView = MapView()  # Create a map view
        treeView.draw(t_filter.get_breaks(), t_filter.get_filter_years())  # Attach it to the data and draw it
