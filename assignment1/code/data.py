import os
import csv

from abstractions import *

DATA_DIRECTORY = 'datafolder/'

def load_data(apartments_dataset):

    types = ['COSMETIC', 'MODERATE RISK', 'HIGH RISK', 'OVERALL']
    apartments = []
    with open(os.path.join(DATA_DIRECTORY, apartments_dataset)) as csvfile:
        apartment_data = csv.reader(csvfile, delimiter=',')
        line_no = 0
        for row in apartment_data:
            if line_no > 0:
                reviews = []
                count = 0
                for i in [3,4,5,6]:
                    reviews.append(Review(types[count], float(row[i])))
                    count += 1
                apartments.append(ApartmentBuilding(row[1], int(row[2]), int(row[0]), reviews))
            line_no += 1

    return apartments

APARTMENT_DATA = load_data('apartments.csv') #TRAIN on some apartment data
TESTING_DATA = load_data('testset.csv') #TEST on a DIFFERENT set of apartment data

