import Map
import Population
import abc
from solution import Solution
import random

class Evolutionary_algorithm(abc):
    def initiate(self, population_size: int) -> Population:
        pass

    def mutate(self, specimen: Solution, points: Map.Points) -> Solution:
        random.seed()
        for point in specimen.route:
            if random.randrange(0, 1) == 1:
                point = random.randrange(0, len(points)) # mutowanie zachodzi losowo, do ustalenia rozkład losowania
        return specimen

    def cross_parents(self, parent_1: Solution, parent_2: Solution) -> list:
        random.seed();
        cross_length_1 = random.randrange(0, len(parent_1))
        cross_length_2 = random.randrange(0, len(parent_2))

        temp_1 = parent_1.route[:cross_length_1] # krzyżowanie
        temp_2 = parent_2.route[:cross_length_2]
        temp_3 = parent_1.route[cross_length_1:]
        temp_4 = parent_1.route[cross_length_2:]

        child_1 = temp_1 + temp_3
        child_2 = temp_2 + temp_4

        return[child_1, child_2]

    def modify(self, parents: list) -> list:
        parents = random.shuffle(parents) # pomieszanie wybranych rodziców
        children = []
        for specimen in parents:
            parents = self.mutate(parents) # mutowanie
        for i in range(0, len(parents)): # krzyżowanie
            parent_1 = parents.pop()
            parent_2 = parents.pop()
            offspring = self.cross_parents(parent_1, parent_2)
            children.append(offspring.pop())
            children.append(offspring.pop())
        return children

        # !!!!!! Jak wybrać rodziców? Jak dobrać rodziców w pary? Najpierw mutacja czy najpierw krzyzowanie?
        # Każdy z każdym, albo losowy z losowym

    def stop(self, P, t):
        pass

    def selectParents(self, old_population: list) -> list:
        pass

    def rate(self):
        pass

    def selectSpecimen(self, population: list): #ja bym to wypieprzyla
        rating = 0
        bestSpecimen = population[0]
        for specimen in population:
            if self.rate(specimen)>rating:
                self.rate = rating(specimen)
                bestSpecimen = specimen
        return bestSpecimen

    def run(self, population_size):
        t: int = 0 # zmienić na zliczanie wywołania f oceny
        P = self.initiate(population_size)
        while (not self.stop(P, t)): # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            t = t + 1
            P = self.modify(self.selectParents(P))
            # czy musi być ocena tutaj?
            #ocena tylko tam gdzie trzeba
        return (P)
