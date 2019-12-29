from map import Map
from population import Population
import configuration
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
