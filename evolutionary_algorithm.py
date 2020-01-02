from map import Map
from population import Population
import configuration
from exceptions import *
import random


def stop(population):
    if population.gen_num > configuration.values["max_generation"]:  # przekroczenie max liczby generacji
        return 1
    # elif population.select_best_specimen().rating > configuration.values["target_value"]:
    #     return 1
    else:
        return 0


def run(my_map: Map):
    generation = Population(my_map)
    while not stop(generation):  # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
        generation.next_generation()
        # czy musi być ocena tutaj?
        # ocena tylko tam gdzie trzeba
    return generation


def run_multiple_times(my_map: Map, t: int = 10) -> list:
    best_ratings = []
    for i in range(t):
        final_population = run(my_map)
        try:
            best_ratings.append([i+1, final_population.select_best_allowed_specimen().rating,
                                 final_population.select_best_allowed_specimen().route])
        except NoSpecimenFound:
            print("!", end=" ")
            pass
        else:
            print(".", end=" ")
    return best_ratings
