from matplotlib import pyplot as plt

from data import APARTMENT_DATA
from classifiers import LinearRegression, NearestNeighbour
from abstractions import Review, ApartmentBuilding

test_apartment = True
test_rate_all = True
test_predict_ls = True
test_predict_nn = True

# Apartment test
def test_apartmentA():
    aptmin = ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 4), Review('COSMETIC', 1),
                                                       Review('OVERALL', 86)]).apartment_min_rating()
    assert (1 == aptmin[1])
    assert ('COSMETIC' == aptmin[0])

# Apartment test
def test_apartmentB():
    apt = ApartmentBuilding('SOCIAL HOUSING', 1, 1973, [Review('MODERATE RISK', 4), Review('COSMETIC', 1),
                                                       Review('OVERALL', 86)])
    assert (apt.num_ratings() == 3)  # should be an integer
    assert (type(apt.num_ratings()) == int)  # should be an integer
    assert (apt.apartment_overall_rating() == 86)  # should be a decimal
    assert (type(apt.apartment_overall_rating()) == int)  # should be a integer

# Regression test
def test_predictA1():
    lr = LinearRegression()
    apartments = APARTMENT_DATA[1:10]
    lr.train(apartments,'COSMETIC')

    apt = APARTMENT_DATA[11]

    assert (round(lr.predict(apt), 2) == 80.9)
    assert (round(lr.r_squared, 2) == 0.22)

# Regression test
def test_predictB1():
    lr = LinearRegression()
    apartments = APARTMENT_DATA[11:20]
    lr.train(apartments,'COSMETIC')

    apt = APARTMENT_DATA[21]

    assert (round(lr.predict(apt), 2) == 88.65)
    assert (round(lr.r_squared, 2) == 0.6)

# Regression test
def test_predictC1():
    lr = LinearRegression()
    apartments = APARTMENT_DATA[21:30]
    lr.train(apartments,'COSMETIC')

    apt = APARTMENT_DATA[31]

    assert (round(lr.predict(apt), 2) == 65.55)
    assert (round(lr.r_squared, 2) == 0.63)

# Nearest Neighbour test
def test_predictA2():
    apartments = APARTMENT_DATA[1:10]
    nn = NearestNeighbour(apartments)

    apt = APARTMENT_DATA[11]

    assert (round(nn.predict(apt), 2) == 80.9)

# Nearest Neighbour test
def test_predictB2():
    apartments = APARTMENT_DATA[1:10]
    nn = NearestNeighbour(apartments)

    apt = APARTMENT_DATA[21]

    assert (round(nn.predict(apt), 2) == 80.9)

# Nearest Neighbour test
def test_predictC2():
    apartments = APARTMENT_DATA[1:10]
    nn = NearestNeighbour(apartments)

    apt = APARTMENT_DATA[31]

    assert (round(nn.predict(apt), 2) == 80.9)

# Rate all test LS
def test_rateallA():
    training = APARTMENT_DATA[21:]
    to_rate = APARTMENT_DATA[:20]
    c = LinearRegression()

    c.train(training)

    predictions = [round(n, 1) for n in list(c.make_predictions(to_rate).values())]
    cosmetics = [r.apartment_cosmetic_rating() for r in to_rate]
    overall = [r.apartment_overall_rating() for r in to_rate]
    correct = [81.2, 91.4, 84.1, 75.0, 68.5, 68.5, 65.3, 89.5, 68.5, 89.9, 88.5, 89.9, 78.2, 92.7, 65.3, 71.7, 75.0, 83.0, 92.7, 84.6]

    plt.plot(cosmetics, predictions, 'bo')
    plt.plot(cosmetics, overall, 'ro')
    plt.xlabel('Cosmetic Rating for Apartment')
    plt.ylabel('Overall Ratings')
    plt.legend(['Predicted Rating', 'Actual Rating'])
    plt.show()

    for c in range(len(correct)):
        assert (abs(correct[c] - predictions[c]) < 0.5)

# Rate all test NN
def test_rateallB():
    training = APARTMENT_DATA[40:]
    to_rate = APARTMENT_DATA[20:40]
    c = NearestNeighbour(training)

    predictions = [round(n, 1) for n in list(c.make_predictions(to_rate).values())]
    cosmetics = [r.apartment_cosmetic_rating() for r in to_rate]
    overall = [r.apartment_overall_rating() for r in to_rate]
    correct = [78.2, 92.7, 89.5, 84.2, 72.6, 84.2, 88.5, 74.0, 88.5, 88.5, 88.5, 68.2, 84.2, 78.4, 90.0, 87.1, 88.5, 88.5, 76.9, 76.9]

    plt.plot(cosmetics, predictions, 'bo')
    plt.plot(cosmetics, overall, 'ro')
    plt.xlabel('Cosmetic Rating for Apartment')
    plt.ylabel('Overall Ratings')
    plt.legend(['Predicted Rating', 'Actual Rating'])
    plt.show()

    for c in range(len(correct)):
        assert (abs(correct[c] - predictions[c]) < 0.5)

if __name__ == '__main__':

    if test_apartment:
        test_apartmentA()
        test_apartmentB()
    if test_predict_ls:
        test_predictA1()
        test_predictB1()
        test_predictC1()
    if test_predict_nn:
        test_predictA2()
        test_predictB2()
        test_predictC2()
    if test_rate_all:
        test_rateallA()
        test_rateallB()
