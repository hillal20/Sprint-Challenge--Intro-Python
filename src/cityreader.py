import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.

# TODO


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# Use Python's built-in "csv" module to read this file so that each record is
# imported into a City instance. (You're free to add more attributes to the City
# class if you wish, but this is not necessary.) Google "python 3 csv" for
# references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
# file = csv.reader('cities.csv')

cities = []

file = open("cities.csv", newline='')

# read file
reader = csv.reader(file)
# remove header
header = next(reader)
# get city data
data = [row for row in reader]

# loop over data and create city for each line
for city in data:
    newCity = City(city[0], city[3], city[4])
    cities.append(newCity)
# Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city.name, city.latitude, city.longitude)


# cities = []
# with open('cities.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         cities.append(' '.join(row))

# newArray = []


# # # TODO
# for i in cities[1:]:
#     print(i.split('\n')[0].split(',')[0], i.split('\n')[
#           0].split(',')[3], i.split('\n')[0].split(',')[4])
# newArray.append(i.split('\n')[0].split(',')[0] + "," + i.split('\n')[
#     0].split(',')[3] + "," + i.split('\n')[0].split(',')[4])

# # Print the list of cities (name, lat, lon), 1 record per line.


# print
# print(newArray)
# # TODO


# *** STRETCH GOAL! ***
# c = input('please type 2  cordinats for the 1st point  :')
# d = input('please type 2  cordinats for the 2st point  :')


# a = c.split(' ')
# b = d.split(' ')
# print('point a is===>', a)
# print('point b is ===>', b)

# length= a[0] -

#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Output the cities that fall
# within this square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO
