# from typing import List
import math

# Initiate
m = 20.5  # mass in kilograms
current_location = {'x': 0, 'y': 0, 'z': 0}
g = 3.71  # gravitational acceleration in m/s^2
init_fuel_need = 10 # fuel needed to start moving


# Fuel usage function
def fuel_usage(mass, grav_acc, height, distance):
    if d == 0:
        return 0
    slope = (math.atan(height / distance) * 50) / math.pi
    return mass * slope * grav_acc * distance


# Read file of points
plik = open('points.txt')
point_list = []
for linia in plik:
    linia = linia.split()
    dictionary: dict = {'x': int(linia[0]), 'y': int(linia[1]), 'z': int(linia[2])}
    point_list.append(dictionary)
print(point_list)
plik.close()
# print(point_list[0]['y'])  # Print y coordinate of 0. point

# Calculate cost for each point
cost = []
for elem in point_list:
    d = math.sqrt((current_location['x'] - elem['x']) ** 2 + (current_location['y'] - elem['y']) ** 2)
    h = elem['z'] - current_location['z']
    point_cost = init_fuel_need + fuel_usage(m, g, h, d)
    cost.append(point_cost)
print(cost)
