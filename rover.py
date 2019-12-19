# from specimen import Specimen
import math
import configuration
import cost_calculator
from map import Map


class Rover:
    def __init__(self, start_weight: float = configuration.values["rover_mass"],
                 start_location: int = configuration.values["base_id"]) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

    # zwraca koszt przebytej trasy w danym Solution, tj. osobniku
    def go(self, route: list, map: Map):
        previous_point = 0
        cost = 0
        for elem in route:
            cost += cost_calculator.calc_fuel_usage(self.current_weight, previous_point, elem, map.cost_matrix)
            previous_point = elem
        cost += cost_calculator.calc_fuel_usage(self.current_weight, 0, map.cost_matrix)
        return cost
