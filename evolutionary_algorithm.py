from map import Map
from population import Population
import abc
import configuration
from specimen import Specimen
import random


def stop(population):
    if population.gen_num > configuration.values["max_generation"]:
        return 1
    # elif population.select_best_specimen().rating > configuration.values["target_value"]:
    #     return 1
    else:
        return 0


def run(_map: Map):
    generation = Population(_map)
    while not stop(generation):  # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
        generation.next_generation()
        # czy musi być ocena tutaj?
        # ocena tylko tam gdzie trzeba
    return generation
