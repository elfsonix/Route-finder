import configuration
import cost_calculator
import random
from map import Map


class Specimen:
    def __init__(self, route: list) -> None:
        self.route = route
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

    def mutate(self, mutation_rate, max_point):
        # print("pre mutation", self.route)
        random.seed()
        for point in range(0, self.get_length()): # iteracja po indeksach genow zamiast po genach
            if random.randrange(0, 100 / mutation_rate) == 1:
                # wylosowanie nowego genu na miejsce starego z listy dostepnych punktow
                self.route[point] = random.randrange(0, max_point)  # TODO rozkład losowania
        # print("post mutation", self.route)
        self.rating = 0
        return self

    def rate(self, my_map: Map) -> None:
        previous_point = 0
        weight = configuration.values["rover_mass"]
        points_covered = []
        cost = 0
        profit = 0

        for elem in self.route:  # obliczenie kosztu przejazdu
            cost += cost_calculator.calc_fuel_usage(weight, previous_point, elem, my_map.cost_matrix)
            previous_point = elem
            if elem not in points_covered:  # sprawdzenie czy punkt byl odwiedzony
                weight += my_map.get_weight(elem)  # zwiększenie wagi łazika
                profit += my_map.get_profit(elem)  # zwiększenie zysku
                cost += 1  # dodanie kosztu rozpoczęcia ruchu
                points_covered.append(elem)
        # przejazd do bazy - funkcja kary
        punishment = cost_calculator.calc_fuel_usage(weight, previous_point, 0, my_map.cost_matrix)

        if configuration.values["fuel"] - cost < 0:  # sprawdzenie czy przekroczylismy ograniczenie
            self.is_allowed = 0
        else:
            self.is_allowed = 1

        # obliczenie wartości funkcji optymalizacji
        self.rating = profit - configuration.values["alpha"] * punishment


# test
# myspec = Specimen([1, 2, 3, 4, 5, 6])
# myspec.mutate(50, 9)
# myspec.rate(Map())
# print(myspec.rating)
