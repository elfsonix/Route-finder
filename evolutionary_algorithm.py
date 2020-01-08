from map import Map
from population import Population
import configuration
from exceptions import *


class EAlgorithm:

    def stop(self, population):
        if population.gen_num > configuration.values["max_generation"]:  # przekroczenie max liczby generacji
            return 1
        # elif population.select_best_specimen().rating > configuration.values["target_value"]:
        #     return 1
        else:
            return 0

    def run(self, my_map: Map):
        generation = Population(my_map)
        while not self.stop(generation):  # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            generation.next_generation()
        return generation

    def run_multiple_times(self, my_map: Map, times: int = 10) -> list:
        routes = []
        best_ratings = []
        time = []
        for i in range(times):
            final_population = self.run(my_map)
            try:
                routes.append(final_population.select_best_allowed_specimen().route)
                best_ratings.append(final_population.select_best_allowed_specimen().rating)
                time.append(i+1)
            except NoSpecimenFound:
                print("!", end=" ")
                pass
            else:
                print(".", end=" ")
        return [best_ratings, routes, time]
