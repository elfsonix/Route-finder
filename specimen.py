from copy import copy

import configuration
import random
from map import Map


class Specimen:
    def __init__(self, route: list) -> None:
        if isinstance(route, list):
            self.route = route
        elif isinstance(route, int):
            self.route = [route]
        else:
            pass  # todo exception handling?

        self.rating = 0
        self.is_allowed = 0

    def __lt__(self, other):  # sprawia, że sortowanie jest możliwe
        return self.rating < other.rating

    def __len__(self):  # sprawia, że len(specimen) zwraca długość self.route
        return len(self.route)

    def mutate(self, max_point, mutation_rate=configuration.values["mutation_rate"]):
        random.seed()
        for point in range(0, len(self)): # iteracja po indeksach genow zamiast po genach
            if random.randrange(0, 100 / mutation_rate) == 1:
                # wylosowanie nowego genu na miejsce starego z listy dostepnych punktow
                self.route[point] = random.randrange(0, max_point)  # TODO rozkład losowania
        self.rating = 0
        return self

    def is_route_allowed(self, cost: float) -> None:  # sprawdzenie czy rozwiązanie jest poprawne
        if configuration.values["fuel"] < cost:  # sprawdzenie czy przekroczylismy ograniczenie
            self.is_allowed = 0
        else:
            self.is_allowed = 1

    def rate(self, my_map: Map) -> None:
        previous_point = 0
        weight = configuration.values["rover_mass"]
        points_covered = []
        cost = 0
        profit = 0
        for current_point in self.route:  # obliczenie kosztu przejazdu
            cost += my_map.calc_fuel_usage(weight, previous_point, current_point)
            previous_point = copy(current_point)
            if current_point not in points_covered:  # sprawdzenie czy punkt byl odwiedzony
                weight += my_map.get_weight(current_point)  # zwiększenie wagi łazika
                profit += my_map.get_profit(current_point)  # zwiększenie zysku
                cost += configuration.values["init_fuel_need"]  # dodanie kosztu rozpoczęcia ruchu
                points_covered.append(current_point)
            self.is_route_allowed(cost)
        cost += my_map.calc_fuel_usage(weight, previous_point, 0)
        self.is_route_allowed(cost)
        # obliczenie wartości funkcji optymalizacji
        self.rating = profit - configuration.values["alpha"] * (0 if self.is_allowed else cost)
