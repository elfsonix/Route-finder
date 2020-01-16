from numpy import *
import population
import output_presentation
import configuration
from map import Map
import glob
from evolutionary_algorithm import EAlgorithm


class MultiInstanceEAlgorithm:

    def __init__(self):
        self.best_ratings = []
        self.worst_ratings = []
        self.avg_ratings = []
        self.std_ratings = []
        self.maps = []
        self.configs = []

    def load_multiple_points(self) -> None:     # wczytanie roznych map
        files_list = glob.glob('maps/points*.txt')
        for file in files_list:
            self.maps.append(Map(file))
        pass

    def load_multiple_configs(self) -> None:    # wczytanie roznych konfiguracji
        floats = ["g", "mi", "alpha", "rover_mass"]
        files_list = glob.glob('configs/config*.txt')
        temp: dict = {}
        for file in files_list:
            f = open(file)
            for line in f:
                key, content = line.split()
                if key in floats:
                    temp[key] = float(content)
                else:
                    temp[key] = int(content)
            f.close()
            self.configs.append(temp)
        pass

    def execute_algorithm(self):        # wykonanie algorytmu dla różnych konfiguracji
        for config_it in self.configs:
            for maps_in in self.maps:
                configuration.values = config_it
                [best_ratings, routes, time] = EAlgorithm().run_multiple_times(maps_in)
                best_ratings.sort()
                self.best_ratings.append(best_ratings[-1])
                self.worst_ratings.append(best_ratings[0])
                self.avg_ratings.append(mean(best_ratings))
                self.std_ratings.append(std(best_ratings))
        print()
        print("BEST:", self.best_ratings)
        print("WORST:", self.worst_ratings)
        print("AVERAGE:", self.avg_ratings)
        print("STD:", self.std_ratings)

        return self.best_ratings, self.worst_ratings, self.avg_ratings, self.std_ratings