import random
import operator
from specimen import Specimen
import configuration
import map


class Population:
    def __init__(self, gen_num: int, max_point: int) -> None:
        self.size = configuration.values["population_size"]
        self.gen_num = gen_num
        self.max_point = max_point
        # wstepna inicjalizacja dla t=0
        self.current_generation = []
        self.old_generation = []

        temp_list = []
        for i in range(random.randrange(1, max_point, 1)):
            temp_list.append(random.randrange(1, max_point, 1))
        self.current_generation.append(Specimen(temp_list))

    def copy(self, previous_population) -> None:
        self.size = previous_population.size
        self.gen_num = previous_population.t + 1
        self.current_generation = []  # napisać funkcję tworzącą nową populację ze starej
        # TODO czy to robimy tutaj czy w klasie EA?

    def get_size(self) -> int:
        return self.size

    def get_solution(self, number) -> Specimen:
        return self.current_generation[number]

    def mutate(self, specimen: Specimen) -> Specimen:
        random.seed()
        for point in specimen.route:
            if random.randrange(0, 1) == 1:
                point = random.randrange(0, self.max_point) # mutowanie zachodzi losowo, do ustalenia rozkład losowania
        return specimen

    def cross_parents(self, parent_1: Specimen, parent_2: Specimen) -> list:
        random.seed()
        cross_length_1 = random.randrange(0, len(parent_1))
        cross_length_2 = random.randrange(0, len(parent_2))

        temp_1 = parent_1.route[:cross_length_1]  # krzyżowanie
        temp_2 = parent_2.route[:cross_length_2]
        temp_3 = parent_1.route[cross_length_1:]
        temp_4 = parent_1.route[cross_length_2:]

        child_1 = Specimen([temp_1, temp_3])
        child_2 = Specimen([temp_2, temp_4])

        return[child_1, child_2]

    def modify(self, parents: list) -> list:  # TODO coś trzeba ogarnąć z maksymalnym id wierzcholka grafu
        parents = random.shuffle(parents)  # pomieszanie wybranych rodziców
        children = []
        for specimen in parents:
            parents = self.mutate(specimen)  # mutowanie
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

    def next_generation(self) -> None:        # TODO
        pass
