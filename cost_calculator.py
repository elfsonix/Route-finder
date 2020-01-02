# from typing import List
import math
import abc
import configuration
# from map import Map


def calc_cost(point1: dict, point2: dict) -> float:
    cost = configuration.values["g"] * configuration.values["mi"] * \
           ((point1['x']-point2['x'])**2 + (point1['y'] - point2['y'])**2) * (point1['z'] - point2['z'])
    return abs(cost)


def calc_cost_matrix(points: list) -> list:
    temp = [[0 for x in points] for y in points]
    for i in range(len(points)):
        for j in range(len(points)):
            temp[i][j] = calc_cost(points[i], points[j])
    return temp


def calc_fuel_usage(mass: float, point1: int, point2: int, cost_matrix: list):
    return cost_matrix[point1][point2]*mass

    # if d == 0:
    #     return 0
    # slope = (math.atan(height / distance) * 50) / math.pi
    # return mass * slope * grav_acc * distance
