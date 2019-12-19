import random
import operator
from typing import List

from specimen import Specimen
import configuration
from map import Map


class Population:
    def __init__(self, map: Map, size: int = configuration.values["population_size"], gen_num: int = 0) -> None:
        self.size = size
        self.gen_num = gen_num                                  # aktualna generacja
        # wstepna inicjalizacja dla t=0
        self.current_generation = []                            # generacja obecna
        self.old_generation = []                                # generacja poprzednia
        self.map = map

        temp_list = []
        for j in range(0, configuration.values["population_size"]):
            for i in range(random.randrange(1, self.map.max_point, 1)):      # tworzę losowo generację początkową
                temp_list.append(random.randrange(1, self.map.max_point, 1))
            self.current_generation.append(Specimen(temp_list))
            # print(temp_list)
            temp_list = []
        for i in self.current_generation:
            i.rate(self.map)

    def get_size(self) -> int:                                  # TODO czy potrzebne?
        return self.size

    def get_solution(self, number) -> Specimen:                 # TODO czy potrzebne?
        return self.current_generation[number]

    def mutate(self, specimen: Specimen) -> Specimen:
        random.seed()
        for point in specimen.route:
            if random.randrange(0, 1) == 1:
                point = random.randrange(0, self.map.max_point)
                # mutowanie zachodzi losowo, do ustalenia rozkład losowania
        return specimen

    def cross_parents(self, parent_1: Specimen, parent_2: Specimen) -> list:
        random.seed()
        cross_length_1 = random.randrange(0, len(parent_1.route))
        cross_length_2 = random.randrange(0, len(parent_2.route))

        temp_1 = parent_1.route[:cross_length_1]    # krzyżowanie
        temp_2 = parent_2.route[:cross_length_2]
        temp_3 = parent_1.route[cross_length_1:]
        temp_4 = parent_1.route[cross_length_2:]

        child_1 = Specimen([temp_1, temp_3])        # tworzenie potomków
        child_2 = Specimen([temp_2, temp_4])

        return[child_1, child_2]

    def modify(self, parents: list) -> list:
        # parents = random.shuffle(parents)  # pomieszanie wybranych rodziców # TODO cos nie dziala
        children = parents  # []
        # for specimen in parents:
        #     parents = self.mutate(specimen)  # mutowanie
        # for i in range(0, len(parents)):  # krzyżowanie
        #     parent_1 = parents.pop()
        #     parent_2 = parents.pop()
        #     offspring = self.cross_parents(parent_1, parent_2)
        #     children.append(offspring.pop())
        #     children.append(offspring.pop())
        return children

    def select_best_parents(self) -> list:
        whole_population = self.current_generation + self.old_generation
        whole_population.sort()                                     # sortowanie populacji od najlepszych do najgorszych
        return whole_population[:configuration.values["population_size"]]  # zwracam najlepszych

    def select_best_specimen(self) -> Specimen:
        whole_population = self.current_generation + self.old_generation
        whole_population.sort()             # sortowanie populacji od najlepszych do najgorszych
        return whole_population.pop()      # zwracam najlepszego

    def select_best_allowed_specimen(self):
        whole_population = self.current_generation + self.old_generation
        whole_population.sort()  # sortowanie populacji od najlepszych do najgorszych
        specimen = whole_population.pop()
        while not specimen.is_allowed:
            specimen = whole_population.pop()
        return specimen  # zwracam najlepszego

    def next_generation(self) -> None:
        new_generation: list = self.modify(self.select_best_parents())
        self.old_generation = self.current_generation
        self.current_generation = new_generation
        for i in self.current_generation:
            i.rate(self.map)
        self.gen_num += 1
