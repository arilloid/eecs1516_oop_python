from matplotlib import pyplot as plt

from data import APARTMENT_DATA, TESTING_DATA
from abstractions import *

##################################
# Phase 2: Nearest Neighbour
##################################
class NearestNeighbour:
    """A Nearest Neighbour model to predict ratings
     of an apartment."""
    _training_data: list[ApartmentBuilding]

    def __init__(self, training_data) -> None:
        """Return a NearestNeighbour abstraction."""
        self._training_data = training_data  # initialize the training data

    def predict(self, apartment: ApartmentBuilding) -> float:
        """Use the parameters of the nearest neighbour model to predict an overall rating for
        `apartment`.

        Arguments:
        apartment -- An apartment abstraction

        A nearest neighbour model uses the distance between apartments in the training
        data and the apartment whose rating is to be predicted in order to make predictions.
        You should search for the apartment in the training data whose COSMETIC score is NEAREST
        that of the apartment whose overall rating you seek to predict.  Your prediction should be
        the overall rating of that apartment which is the NEAREST NEIGHBOUR in the training set.
        If there is more than one NEAREST NEIGHBOUR, you can break ties any way you like.
        >>> apartment = ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('COSMETIC', 21)])
        >>> training = [ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 22), Review('OVERALL', 91)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 1), Review('OVERALL', 86)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 55), Review('OVERALL', 56)])]
        >>> r = NearestNeighbour(training)
        >>> round(r.predict(apartment), 1)
        91
        """
        pass  # replace with your code

    def make_predictions(self, apartments: list[ApartmentBuilding]) -> dict[ApartmentBuilding, float]:
        """Return the predicted rating for each apartment in `apartments`.
        You should return a dictionary wherein the keys are the Apartments in the
        input list and the values are the predicting rating for each apartment.

        Arguments:
        apartments -- A list of apartments to be rated
        >>> apartments = APARTMENT_DATA[:10]
        >>> training = [ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 1.6), Review('OVERALL', 91)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 1.0), Review('OVERALL', 86)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 2.1), Review('OVERALL', 56)])]
        >>> r = NearestNeighbour(training)
        >>> list(r.make_predictions(apartments).values())
        [56, 56, 56, 91, 86, 86, 86, 56, 86, 56]
        """
        pass  # replace with your code


##################################
# Phase 2: Linear Regression
##################################
class LinearRegression:
    """A linear regression model to predict ratings
    of an apartment."""
    _a: float
    _b: float
    _xs: list[float]
    _ys: list[float]
    _r_squared: float

    def __init__(self) -> None:
        """Return a LinearRegression abstraction."""
        self._a = 0  # intercept of regression line
        self._b = 0  # slope of regression line
        self._xs = []  # x values used to train model
        self._ys = []  # y values used to train model
        self._r_squared = 0  # r-squared value of model (how well it fits the training data)

    def train(self, apartments: list[ApartmentBuilding]) -> None:
        """Train a rating predictor (a function mapping COSMETIC apartment ratings
         onto OVERALL ratings), by performing least-squares linear regression.
         Save the R^2 value and the parameters of this model as attributes of `self`.

        Arguments:
        apartments -- A sequence of apartments
        >>> apartments = APARTMENT_DATA[:10]
        >>> r = LinearRegression()
        >>> r.train(apartments)
        >>> round(r._a,1)
        68.6
        >>> round(r._b,1)
        4.6
        """
        pass #replace with your code

    def predict(self, apartment: ApartmentBuilding) -> float:
        """Use the parameters of the regression model to predict an overall rating for
        `apartment`.

        Arguments:
        apartment -- An apartment abstraction

        A linear regression model is a function from apartment to evaluation.
        It can be calculated using the formula:
        y = b * x + a
        where x is the log rating of the apartment, y is the predicted evaluation,
        a is the intercept of the model, and b is the slope of the model.
        >>> apartment = ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 11), Review('OVERALL', 86)])
        >>> r = LinearRegression()
        >>> r._a = 1
        >>> r._b = 2
        >>> round(r.predict(apartment), 1)
        23
        """
        pass #replace with your code

    def make_predictions(self, apartments: list[ApartmentBuilding]) -> dict[ApartmentBuilding, float]:
        """Return the predicted rating of `apartments`.  Note
        that this method can only be called after `train` has been called.
        You will have to train the predictor using the apartments in
        the user has reviewed in the past; you will then use that model
        to predict the user's ratings for restaurants they have not
        reviewed. You should return a dictionary wherein the keys are the Apartments in the
        input list and the values are the predicting rating for each apartment.

        Arguments:
        apartments -- A list of apartments to be reviewed
        >>> apartments = APARTMENT_DATA[:10]
        >>> r = LinearRegression()
        >>> r._a = 1
        >>> r._b = 2
        >>> list(r.make_predictions(apartments).values())
        [5.2, 6.6, 5.6, 4.34, 3.44, 3.44, 3.0, 6.34, 3.44, 6.4]
        """
        pass #replace with your code


def calculate_mse(predictions: dict[ApartmentBuilding, float]) -> float:
    """Calculate the mean squared error between predicted ratings and actual ratings

     Arguments:
     predictions -- A dictonary wherein keys are apartment buildings (containing actual
     rating data) and values are predictions of the overall ratings for these buildings.
      >>> apartments = APARTMENT_DATA[:10]
      >>> training = [ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 1.6), Review('OVERALL', 91)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 1.0), Review('OVERALL', 86)]), ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 6), Review('COSMETIC', 2.1), Review('OVERALL', 56)])]
      >>> r = NearestNeighbour(training)
      >>> predictions = r.make_predictions(apartments)
      >>> round(calculate_mse(predictions),1)
      408.5
      >>> r = LinearRegression()
      >>> r._a = 1
      >>> r._b = 2
      >>> predictions = r.make_predictions(apartments)
      >>> round(calculate_mse(predictions),1)
      5310.2
      """
    pass  # replace with your code


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Uncomment the lines below to train and visualize a regression

    # c = LinearRegression()
    # c.train(APARTMENT_DATA)
    # ratings = c.make_predictions(TESTING_DATA)
    # print(f'MSE for regression is {calculate_mse(ratings)}')
    #
    # xs = [t.apartment_cosmetic_rating() for t in TESTING_DATA]
    # ys = [t.apartment_overall_rating() for t in TESTING_DATA]
    #
    # plt.plot(xs, ys, 'ro')
    # plt.plot(xs, ratings.values(), 'bo')
    # plt.title('Predicting Overall Ratings using Regression')
    # plt.xlabel('Cosmetic Rating for Apartment')
    # plt.ylabel('Overall Ratings')
    # plt.legend(['Actual Rating', 'Predicted Rating'])
    # plt.plot(xs, ratings.values(), 'b')
    # plt.show()
    #
    # c = NearestNeighbour(APARTMENT_DATA)
    # ratings = c.make_predictions(TESTING_DATA)
    # print(f'MSE for nearest neighbour is {calculate_mse(ratings)}')
    #
    # plt.plot(xs, ys, 'ro')
    # plt.plot(xs, ratings.values(), 'bo')
    # plt.title('Predicting Overall Ratings using Nearest Neighbours')
    # plt.xlabel('Cosmetic Rating for Apartment')
    # plt.ylabel('Overall Ratings')
    # plt.legend(['Actual Rating', 'Predicted Rating'])
    # plt.show()

