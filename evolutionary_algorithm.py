from map import Map
from population import Population
import abc
import configuration
from specimen import Specimen
import random


def stop(population, gen_num):
    # TODO warunek stopu
    pass


def run(_map: Map):
    gen_num: int = 0  # zmienić na zliczanie wywołania f oceny
    generation = Population(gen_num, _map.max_point)
    while not stop(generation, gen_num):  # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
        gen_num = gen_num + 1
        generation.next_generation()
        # czy musi być ocena tutaj?
        # ocena tylko tam gdzie trzeba
    return generation
