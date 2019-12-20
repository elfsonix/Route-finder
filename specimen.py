import configuration
import cost_calculator
from map import Map


class Specimen:
    def __init__(self, route: list) -> None:
        self.route: list = route
        self.rating = 0
        self.is_allowed = 0

    def __lt__(self, other):
        return self.rating < other.rating

    def __len__(self):
        return len(self.route)

    def get_length(self):
        return len(self.route)

    def get_item(self):
        return self.route

    def rate(self, map: Map) -> None:
        previous_point = 0
        weight = configuration.values["rover_mass"]
        points_covered = []
        cost = 0

        for elem in self.route:  # obliczenie kosztu przejazdu
            cost += cost_calculator.calc_fuel_usage(weight, previous_point, elem, map.cost_matrix)
            previous_point = elem
            if elem not in points_covered:  # sprawdzenie czy punkt byl odwiedzony
                weight += map.get_profit(elem)  # zwiększenie wagi łazika
                cost += 10  # dodanie kosztu rozpoczęcia ruchu
                # print(weight)
            points_covered.append(elem)

        cost += cost_calculator.calc_fuel_usage(weight, previous_point, 0, map.cost_matrix) # przejazd do bazy

        if configuration.values["fuel"] - cost > 0:  # sprawdzenie czy przekroczylismy ograniczenie
            cost = 0
            self.is_allowed = 0
        else:
            cost = configuration.values["fuel"] - cost
            self.is_allowed = 1

        # obliczenie wartości funkcji optymalizacji
        self.rating = weight - configuration.values["rover_mass"] - configuration.values["alpha"] * cost

