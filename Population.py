import random
import operator
from solution import Solution
import Map


class Population:
    def __init__(self, t: int, points: list, size: int = 30) -> None:
        self.size = size
        self.t = t
        # wstepna inicjalizacja dla t=0
        self.current_generation = []
        self.old_generation = []
        for i in range(len(points)):
            self.current_generation.append(random.randrange(1, len(points), 1))
        # korzystam z  random.randrange(start, stop[, step])

    def copy(self, previous_population) -> None:
        self.size = previous_population.size
        self.t = previous_population.t + 1
        self.current_generation = []  # napisać funkcję tworzącą nową populację ze starej
        # TODO czy to robimy tutaj czy w klasie EA?

    def get_size(self) -> int:
        return self.size

    def get_solution(self, number) -> Solution:
        return self.current_generation[number]

    def mutate(self, specimen: Solution, points: Map.Points) -> Solution:
        random.seed()
        for point in specimen.route:
            if random.randrange(0, 1) == 1:
                point = random.randrange(0, len(points)) # mutowanie zachodzi losowo, do ustalenia rozkład losowania
        return specimen

    def cross_parents(self, parent_1: Solution, parent_2: Solution) -> list:
        random.seed()
        cross_length_1 = random.randrange(0, len(parent_1))
        cross_length_2 = random.randrange(0, len(parent_2))

        temp_1 = parent_1.route[:cross_length_1]  # krzyżowanie
        temp_2 = parent_2.route[:cross_length_2]
        temp_3 = parent_1.route[cross_length_1:]
        temp_4 = parent_1.route[cross_length_2:]

        child_1 = Solution([temp_1, temp_3])
        child_2 = Solution([temp_2, temp_4])

        return[child_1, child_2]

    def modify(self, parents: list) -> list:  # TODO coś trzeba ogarnąć z maksymalnym id wierzcholka grafu
        parents = random.shuffle(parents)  # pomieszanie wybranych rodziców
        children = []
        for specimen in parents:
            parents = self.mutate(specimen, )  # mutowanie
        for i in range(0, len(parents)):  # krzyżowanie
            parent_1 = parents.pop()
            parent_2 = parents.pop()
            offspring = self.cross_parents(parent_1, parent_2)
            children.append(offspring.pop())
            children.append(offspring.pop())
        return children

    def selectParents(self) -> list:
        whole_population = [self.current_generation, self.old_generation]
        whole_population.sort(key=operator.attrgetter('rating'))  # sortowanie populacji od najlepszych do najgorszych



        # TODO wybranie rodzicow
        pass

    def next_generation(self):        # TODO
        pass
