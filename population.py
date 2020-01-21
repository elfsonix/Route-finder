import random
from copy import copy
from numpy import mean
from specimen import Specimen
import configuration
from map import Map
from exceptions import NoSpecimenFound


class Population:
    def __init__(self, my_map: Map, size: int = configuration.values["population_size"],
                 set_specimens: bool = False) -> None:
        self.size = size
        self.gen_num = 0                                  # aktualna generacja
        # wstepna inicjalizacja dla t=0
        self.current_generation: list = []                            # generacja obecna
        self.map = my_map
        self.set_specimens: bool = set_specimens
        if set_specimens:
            self.load_multiple_specimens()
        else:
            temp_list = []
            for j in range(0, configuration.values["population_size"]):
                for i in range(random.randrange(1, self.map.max_point, 1)):      # tworzę losowo generację początkową
                    temp_list.append(random.randrange(1, self.map.max_point, 1))
                self.current_generation.append(Specimen(temp_list))
                temp_list = []
        self.rate_all()

    def reset(self):
        self.current_generation = []
        self.gen_num = 0
        if self.set_specimens:
            self.load_multiple_specimens()
        else:
            temp_list = []
            for j in range(0, configuration.values["population_size"]):
                for i in range(random.randrange(1, self.map.max_point, 1)):      # tworzę losowo generację początkową
                    temp_list.append(random.randrange(1, self.map.max_point, 1))
                self.current_generation.append(Specimen(temp_list))
                temp_list = []
        self.rate_all()

    # działa
    def mutate_all(self, children: list) -> list:
        for each in children:
            mutate = random.randint(0, 100)
            if mutate <= configuration.values["mutation_probability"]:
                each.mutate(self.map.max_point)
        return children

    @staticmethod
    def cross_all(parent_list: list) -> list:
        child_list = []

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
        return child_list

    def rate_all(self) -> None:  # dokonuje oceny wszystich osobników w current generation
        for each in self.current_generation:
            each.rate(self.map)

    def modify(self) -> None:
        old_generation = copy(self.current_generation)
        parents = self.select_parents(self.size*configuration.values["parent_group_size"]/100)
        children = self.cross_all(parents)
        children = self.mutate_all(children)

        self.current_generation = children + old_generation
        self.rate_all()
        # for elem in children:
        #     print(elem.rating)
        # Obciecie do rozmiaru populacji
        self.current_generation.sort()
        self.current_generation = self.current_generation[:self.size]
        # if old_generation == self.current_generation:
        #     print("zjebałem")
        # if children not in self.current_generation:
        #     print("kurwa mać")

    # SELEKCJA
    def select_parents(self, n_parents: int = None) -> list:
        self.rate_all()
        self.current_generation.sort()  # sortowanie populacji od najlepszych do najgorszych

        # # SELEKCJA PROGOWA 50%
        # slicer = int(self.size*configuration.values["parent_group_size"]/100)
        # return self.current_generation[:slicer]

        # SELEKCJA RANKINGOWA
        parents = []
        ni_max = configuration.values["Ni_max"]
        ni_min = 2-ni_max
        probability = []
        n = len(self.current_generation)
        for el in range(n):
            probability.append((ni_max-(ni_max-ni_min)*(el-1)/(n-1))/n)  # Prawdopodobienstwo wyboru rodzica
        for j in range(int(n_parents)):
            [new_parent] = random.choices(self.current_generation, probability)  # Losowanie rodzicow
            # Trzeba tak rozpakować bo zwraca liste w liscie
            parents.append(new_parent)
        return parents

    def select_best_specimen(self) -> Specimen:
        whole_population = copy(self.current_generation)
        whole_population.sort()             # sortowanie populacji od najlepszych do najgorszych
        return whole_population.pop(0)      # zwracam najlepszego

    def select_best_allowed_specimen(self) -> Specimen:
        whole_population = copy(self.current_generation)
        allowed_specimen = []
        for specimen in whole_population:
            if specimen.is_allowed == 1:
                allowed_specimen.append(specimen)
        if len(allowed_specimen) == 0:
            raise NoSpecimenFound
            # return Specimen([0])
        allowed_specimen.sort()
        return allowed_specimen.pop(0)  # zwracam najlepszego

    def select_worst_specimen(self) -> Specimen:
        whole_population = copy(self.current_generation)
        whole_population.sort()  # sortowanie populacji od najlepszych do najgorszych
        return whole_population.pop()

    def select_worst_allowed_specimen(self):
        whole_population = copy(self.current_generation)
        allowed_specimen = []
        for specimen in whole_population:
            if specimen.is_allowed == 1:
                allowed_specimen.append(specimen)
        if len(allowed_specimen) == 0:
            # raise NoSpecimenFound
            return Specimen([0])
        allowed_specimen.sort()
        return allowed_specimen.pop()

    def get_average_specimen_rating(self):
        whole_population = copy(self.current_generation)
        whole_population_rating = []
        for specimen in whole_population:
            whole_population_rating.append(specimen.rating)
        return mean(whole_population_rating)

    def get_average_allowed_specimen_rating(self):
        whole_population = copy(self.current_generation)
        allowed_specimen = []
        for specimen in whole_population:
            if specimen.is_allowed == 1:
                allowed_specimen.append(specimen)
        if len(allowed_specimen) == 0:
            # raise NoSpecimenFound
            return 0
        allowed_specimen_rating = []
        for specimen in allowed_specimen:
            allowed_specimen_rating.append(specimen.rating)
        return mean(allowed_specimen_rating)

    def next_generation(self) -> None:  # modyfikuje starą populacje na nową
        self.modify()
        self.rate_all()
        self.gen_num += 1
        return None

    def load_multiple_specimens(self, file: str = "tests/start_specimens/specimens.txt"):
        f = open(file)
        for line in f:
            temp = []
            specimen_route = line.split()
            for elem in specimen_route:
                temp.append(int(elem))
            self.current_generation.append(Specimen(temp))
        f.close()
# TEST
# my_pop = Population(Map())
# for i in my_pop.current_generation:
#     print(i.route)
# parent = my_pop.select_parents(20)
# parent.sort()
# for each in parent:
#     print("Parent:", each.route, "rating:", each.rating)
