from map import Map
from population import Population
import configuration
from exceptions import *
import abc


class EAlgorithm(abc.ABC):

    @staticmethod
    def stop(population, old_best):
        if population.gen_num > configuration.values["max_generation"]:  # przekroczenie max liczby generacji
            return 1
        # elif population.select_best_specimen().rating > configuration.values["target_value"]:
        #     return 1
        elif (old_best[-1]-old_best[0])/old_best[-1] < 0.05:
            # jesli przez ostatnie 10 generacji nie poprawilo sie o 5% rating
            return 1
        else:
            return 0

    def run(self, my_map: Map):
        generation = Population(my_map)
        old_best = [1, generation.select_best_allowed_specimen().rating]
        while not self.stop(generation, old_best):
            # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            print("Pre:", generation.select_best_allowed_specimen().rating)
            generation.next_generation()
            print("Post:", generation.select_best_allowed_specimen().rating)
            new_best = generation.select_best_allowed_specimen().rating
            if len(old_best) == 10:
                old_best.append(new_best)
                old_best.pop(0)
                # print(old_best)
            else:
                old_best.append(new_best)
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
