import Map
import Population
import abc
from solution import Solution
import random

class Evolutionary_algorithm(abc):
    def initiate(self, population_size: int) -> Population:
        pass
        # !!!!!! Jak wybrać rodziców? Jak dobrać rodziców w pary? Najpierw mutacja czy najpierw krzyzowanie?
        # Każdy z każdym, albo losowy z losowym

    def stop(self, P, t):
        #TODO warunek stopu
        pass

    def selectSpecimen(self, population: list): #ja bym to wypieprzyla TODO
        rating = 0
        best_specimen = population[0]
        for specimen in population:
            if specimen.rating>rating:
                rating = specimen.rating
                best_specimen = specimen
        return best_specimen

    def run(self, population_size):
        t: int = 0 # zmienić na zliczanie wywołania f oceny
        P = self.initiate(population_size)
        while (not self.stop(P, t)): # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            t = t + 1
            P = self.modify(self.selectParents(P))
            # czy musi być ocena tutaj?
            #ocena tylko tam gdzie trzeba
        return (P)
