"""Data Abstractions"""

#############################
# Phase 1: Data Abstractions #
#############################
class Review:
    """A review for an apartment building.  There are four types of reviews an apartment building can receive:
    -- a review of its cosmetic features (i.e. the cleanliness of the lobby, etc), which ranges from 0 to 1.
       the '_rating_type' for this kind of review is 'COSMETIC'.
    -- a review of moderate risk features (i.e. stairway railings, etc), which ranges from 0 to 1
       the '_rating_type' for this kind of review is 'MODERATE RISK'.
    -- a review of the apartment high risk features (i.e. fire doors, etc), which ranges from 0 to 1
       the '_rating_type' for this kind of review is 'HIGH RISK'.
    -- an overall review, which includes many features and ranges from 0 to 100
       the '_rating_type' for this kind of review is 'OVERALL'.
    """
    _rating_type: str
    _rating: float

    def __init__(self, rating_type: str, rating: float) -> None:
        """Return a Review abstraction."""
        self._rating_type = rating_type
        self._rating = rating

    @property
    def type(self) -> str:
        """Return the type of the `review`, which is a string. ('HIGH RISK', 'OVERALL', etc)"""
        return self._rating_type

    @property
    def rating(self) -> float:
        """Return the rating, which is an float that depends on the rating type."""
        return self._rating

    def __repr__(self):
        """Return a string representation of the review.
        This will be used anytime you print a Review object.
        The string representation should be in the following format:
        Review('<TYPE>', <RATING>)
        >>> Review("OVERALL", 86)
        Review('OVERALL', 86)
        """
        return f"Review('{self._rating_type}', {self._rating})"

# Apartments
class ApartmentBuilding:
    """An apartment, with a type (Private, TCHC, Social Housing), a location (or ward),
     a year of construction and one or more city reviews."""
    _type: str
    _ward: int
    _year: int
    _reviews: list[Review]

    def __init__(self, type: str, ward: int, year: int, reviews: list[Review]) -> None:
        """Return an apartment abstraction.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 11), Review('OVERALL', 86)]).type
        'SOCIAL HOUSING'
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, []).reviews
        []
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [88, 99, 10]).reviews
        Traceback (most recent call last):
        ...
        AssertionError: reviews must be a list of Reviews
        """
        assert isinstance(type, str) and (type in (["TCHC", "PRIVATE", "SOCIAL HOUSING"])), "type must be a string, either 'TCHC', 'PRIVATE', or 'SOCIAL HOUSING'"
        assert isinstance(ward, int), "ward must be an integer"
        assert isinstance(year, int), "year must be an integer"
        assert isinstance(reviews, list) and (all(isinstance(r, Review) for r in reviews) or len(reviews)==0), "reviews must be a list of Reviews"

        self._type = type
        self._ward = ward
        self._year = year
        self._reviews = reviews

    @property
    def type(self) -> str:
        return self._type

    @property
    def ward(self) -> int:
        return self._ward

    @property
    def year(self) -> int:
        return self.year

    @property
    def reviews(self) -> list[Review]:
        return self._reviews

    def get_all_ratings(self) -> list[float]:
        """Return a list of all ratings, which are numbers, for an `apartment` based on all reviews of the `apartment`.
        The doctest here should pass once you have written the constructor for ApartmentBuilding.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('APT_LOG', 6), Review('APT_SAFETY', 11), Review('APT_OVERALL', 86)]).get_all_ratings()
        [6, 11, 86]
        """
        return [r.rating for r in self.reviews]

    def num_ratings(self) -> int:
        """Return the number of ratings for the `apartment`.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('APT_LOG', 6), Review('APT_SAFETY', 11), Review('APT_OVERALL', 86)]).num_ratings()
        3
        >>> ApartmentBuilding('PRIVATE', 1, 2000, []).num_ratings()
        0
        """
        return len(self.reviews)

    def apartment_min_rating(self) -> tuple[str, float]:
        """Return the minimum rating for the apartment building.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 11), Review('OVERALL', 86)]).apartment_min_rating()
        ('MODERATE RISK', 6)
        >>> ApartmentBuilding('PRIVATE', 1, 2000, []).apartment_min_rating()
        """
        if len(self.reviews) == 0: 
            return None
        
        # placeholder
        min_rating = (None, max([r.rating for r in self.reviews]))

        # find the review with the min rating
        for r in self.reviews: 
            if r._rating < min_rating[1]:
                min_rating = (r.type, r.rating)

        return min_rating

    def apartment_overall_rating(self) -> float:
        """Return the overall rating for the apartment building.
        If there are no reviews for the building, return zero.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 11), Review('OVERALL', 86)]).apartment_overall_rating()
        86
        >>> ApartmentBuilding('PRIVATE', 1, 2000, []).apartment_overall_rating()
        0
        >>> ApartmentBuilding('PRIVATE', 1, 2000, [Review('MODERATE RISK', 10), Review('COSMETIC', 10)]).apartment_overall_rating()
        0
        """
        if len(self.reviews) == 0 or ("OVERALL" not in [r.type for r in self.reviews]): 
            return 0
        
        for r in self.reviews:
            if r.type == "OVERALL":
                return r.rating

    def apartment_cosmetic_rating(self) -> float:
        """Return the cosmetic rating for the apartment building.
        If there are no reviews for the building, return zero.
        >>> ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 11), Review('OVERALL', 86)]).apartment_cosmetic_rating()
        11
        >>> ApartmentBuilding('PRIVATE', 1, 2000, []).apartment_cosmetic_rating()
        0
        >>> ApartmentBuilding('PRIVATE', 1, 2000, [Review('MODERATE RISK', 10), Review('OVERALL', 10)]).apartment_cosmetic_rating()
        0
        """
        if len(self.reviews) == 0 or ("COSMETIC" not in [r.type for r in self.reviews]): 
            return 0
        
        for r in self.reviews:
            if r.type == 'COSMETIC':
                return r.rating


if __name__ == "__main__":
    import doctest
    doctest.testmod()
