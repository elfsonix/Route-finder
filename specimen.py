from copy import copy

import configuration
import cost_calculator
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

    def __lt__(self, other): # sprawia, że sortowanie jest możliwe
        return self.rating < other.rating

    def __len__(self): # sprawia, że len(specimen) zwraca długość self.route
        return len(self.route)

    def mutate(self, mutation_rate, max_point):
        # print("pre mutation", self.route)
        random.seed()
        for point in range(0, len(self)): # iteracja po indeksach genow zamiast po genach
            if random.randrange(0, 100 / mutation_rate) == 1:
                # wylosowanie nowego genu na miejsce starego z listy dostepnych punktow
                self.route[point] = random.randrange(0, max_point)  # TODO rozkład losowania
        # print("post mutation", self.route)
        self.rating = 0
        return self

    def is_route_allowed(self, cost: float) -> None: # sprawdzenie czy rozwiązanie jest poprawne
        if configuration.values["fuel"] < cost:  # sprawdzenie czy przekroczylismy ograniczenie
            # print("fafarafa", configuration.values["fuel"] - cost)
            self.is_allowed = 0
            # print("NOT", self.is_allowed)
        else:
            # print("pycipyci", configuration.values["fuel"] - cost)
            self.is_allowed = 1
            # print("YE", self.is_allowed)

    def rate(self, my_map: Map) -> None:
        previous_point = 0
        weight = configuration.values["rover_mass"]
        points_covered = []
        cost = 0
        profit = 0
        # print("route", self.route)
        for current_point in self.route:  # obliczenie kosztu przejazdu
            # print("ccc", current_point, previous_point)
            cost += my_map.calc_fuel_usage(weight, previous_point, current_point)
            previous_point = copy(current_point)
            if current_point not in points_covered:  # sprawdzenie czy punkt byl odwiedzony
                # print("current_point", current_point)
                weight += my_map.get_weight(current_point)  # zwiększenie wagi łazika
                profit += my_map.get_profit(current_point)  # zwiększenie zysku
                cost += configuration.values["init_fuel_need"]  # dodanie kosztu rozpoczęcia ruchu
                points_covered.append(current_point)
            self.is_route_allowed(cost)
            # print("COST:", cost, "ALLOWED", self.is_allowed)
        # przejazd do bazy - funkcja kary
        cost += my_map.calc_fuel_usage(weight, previous_point, 0)
        self.is_route_allowed(cost)
        # obliczenie wartości funkcji optymalizacji
        # print("profit:", profit, "punishment:", punishment, "cost:", cost, "is allowed:", self.is_allowed)
        self.rating = profit - configuration.values["alpha"] * (0 if self.is_allowed else cost)


# test
# myspec = Specimen([1, 2, 3, 4, 5, 6])
# myspec.mutate(50, 9)
# myspec.rate(Map())
# print(myspec.rating)
