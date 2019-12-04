from classes import *
import abc

class Evolutionary_algorithm(abc):
    def initiate(self, population_size: int) -> Population:
        pass

    def mutate(self):
        pass

    def cross(self):
        pass

    def modify(self, parents: list) -> list:
        for parent in parents:
            pass
        #!!!!!! Jak wybrać rodziców? Jak dobrać rodziców w pary? Najpierw mutacja czy najpierw krzyzowanie?
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

    def evolutionary_algorithm(self, population_size):
        t: int = 0 # zmienić na zliczanie wywołania f oceny
        P = self.initiate(population_size)
        while (not self.stop(P, t)): # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            t = t + 1
            P = self.modify(self.selectParents(P))
            # czy musi być ocena tutaj?
            #ocena tylko tam gdzie trzeba
        return (P)

