# from typing import List
import math
# Initiate
mass = 20.5  # mass in kilograms
current_location = {'x': 0, 'y': 0, 'z': 0}

# Read file of points
plik = open('points.txt')
point_list = []
for linia in plik:
    linia = linia.split()
    dictionary: dict = {'x': int(linia[0]), 'y': int(linia[1]), 'z': int(linia[2])}
    point_list.append(dictionary)
print(point_list)
plik.close()

# Calculate cost for each point
cost = []
for elem in point_list:
    distance = math.sqrt((current_location['x'] - elem['x'])**2 + (current_location['y'] - elem['y'])**2)
    height = current_location['z'] - elem['z']
    point_cost = distance  # unfinished
    cost.append(point_cost)
print(cost)
# print(point_list[0]['y'])  # Print y coordinate of 0. point
