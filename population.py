import random
import operator
from copy import copy
from typing import List
from exceptions import *
from specimen import Specimen
import configuration
from map import Map


class Population:
    def __init__(self, my_map: Map, size: int = configuration.values["population_size"], gen_num: int = 0) -> None:
        self.size = size
        self.gen_num = gen_num                                  # aktualna generacja
        # wstepna inicjalizacja dla t=0
        self.current_generation = []                            # generacja obecna
        self.old_generation = []                                # generacja poprzednia
        self.map = my_map

        temp_list = []
        for j in range(0, configuration.values["population_size"]):
            for i in range(random.randrange(1, self.map.max_point, 1)):      # tworzę losowo generację początkową
                temp_list.append(random.randrange(1, self.map.max_point, 1))
            self.current_generation.append(Specimen(temp_list))
            # print(temp_list)
            temp_list = []
        for i in self.current_generation:
            i.rate(self.map)
        # print("start gen", len(self.current_generation))

    # działa
    def mutate_all(self, mutation_rate: float) -> None:
        # print("curr gen", len(self.current_generation))
        # print("size", self.get_size())
        for each in range(0, self.size-1):
            self.current_generation[each] = self.current_generation[each].mutate(mutation_rate, self.map.max_point)

    # prawie działa
    def cross_all(self) -> None:
        parent_list = copy(self.current_generation)
        # print(len(self.current_generation))
        child_list = []
        random.shuffle(parent_list)

        while len(parent_list) > 1:
            parent_1 = parent_list.pop(0)
            parent_2 = parent_list.pop(0)
            cross_length_1 = random.randrange(0, len(parent_1.route))
            cross_length_2 = random.randrange(0, len(parent_2.route))

            temp_1 = parent_1.route[:cross_length_1]  # krzyżowanie
            temp_2 = parent_2.route[:cross_length_2]
            temp_3 = parent_1.route[cross_length_1:]
            temp_4 = parent_1.route[cross_length_2:]

            child_1 = Specimen(temp_1 + temp_3)  # tworzenie potomków
            child_2 = Specimen(temp_2 + temp_4)
            child_list.append(child_1)
            child_list.append(child_2)
        parent_list.extend(child_list)
        self.current_generation = parent_list + child_list  # TODO selekcje z listy rodzice + dzieci, teraz jest progowo
        # TODO jest progowo, ale generujemy dokładną liczbe osobników więc nie ma różnicy
        if len(self.current_generation) < self.size:
            self.fix_incomplete_population()
        self.current_generation.sort()
        self.current_generation = self.current_generation[:self.size]

    def fix_incomplete_population(self):
        self.current_generation.append(Specimen(random.randrange(1, self.map.max_point, 1))) # TODO Zapytać czy można

    def rate_all(self) -> None:  # dokonuje oceny wszystich osobników w current generation
        for each in self.current_generation:
            if each.rating == 0:  # oceniamy tylko te nieocenione jeszcze osobniki
                each.rate(self.map)

    def modify(self, mutation_rate: float =50) -> None:
        self.mutate_all(mutation_rate)  # mutowanie
        self.select_parents()
        self.cross_all()
        self.rate_all()

    # SELEKCJA
    def select_parents(self, n_parents: int = None) -> None:  # Zmienia current gen na pule rodzicow po selekcji
        self.rate_all()
        self.current_generation.sort()  # sortowanie populacji od najlepszych do najgorszych

        # SELEKCJA PROGOWA 50%
        slicer = int(self.size*configuration.values["parent_group_size"]/100)
        self.current_generation = self.current_generation[:slicer]
        """
        # SELEKCJA RANKINGOWA
        parents = []
        ni_max = configuration.values["Ni_max"]
        ni_min = 2-ni_max
        probability = []
        n = len(self.current_generation)
        for i in range(n):
            probability[i] = (ni_max-(ni_max-ni_min)*(i-1)/(n-1))/n
        for j in range(n_parents)
            parents.append(random.choices(self.current_generation, probability))
        self.current_generation = parents
        """

    def select_best_specimen(self) -> Specimen:
        whole_population = copy(self.current_generation)
        whole_population.sort()             # sortowanie populacji od najlepszych do najgorszych
        return whole_population.pop()      # zwracam najlepszego

    def select_best_allowed_specimen(self) -> Specimen:
        whole_population = copy(self.current_generation)
        allowed_specimen = []
        for specimen in whole_population:
            if specimen.is_allowed == 1:
                allowed_specimen.append(specimen)
        if len(allowed_specimen) == 0:
            raise NoSpecimenFound
        allowed_specimen.sort()
        return allowed_specimen.pop()  # zwracam najlepszego

    def next_generation(self) -> None:  # modyfikuje starą populacje na nową
        self.modify()
        for i in self.current_generation:
            i.rate(self.map)
            # print("rating", i.rating)
        self.gen_num += 1


# test
# mypop = Population(Map())
# mypop.mutate_all(50)
# mypop.modify()
