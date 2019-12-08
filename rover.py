from solution import Solution
import math


class Rover:
    def __init__(self, start_weight: float, start_location: int) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

    # zwraca koszt przebytej trasy w danym Solution, tj. osobniku
    def go(self, route: Solution):
        cost = 0
        for i in (1, route.get_length()):
            # odleglosc w linii prostej miedzy punktami, dodac wspolczynnik do sumy?
            cost += math.sqrt(((route.get_item()[i]['x']-route.get_item()[i-1]['x'])**2) +
                              ((route.get_item()[i]['y']-route.get_item()[i-1]['y'])**2) +
                              ((route.get_item()[i]['z']-route.get_item()[i-1]['z'])**2))
        return cost
