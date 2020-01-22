from numpy import *
import population
import plotting
import configuration
from map import Map
import glob
from evolutionary_algorithm import EAlgorithm


class MultiInstanceEAlgorithm:

    def __init__(self, set_specimen: bool = False):
        self.best_ratings = []
        self.worst_ratings = []
        self.avg_ratings = []
        self.std_ratings = []
        self.best_ratings_len = []
        self.worst_ratings_len = []
        self.avg_ratings_len = []
        self.std_ratings_len = []
        self.maps = []
        self.cases = []
        self.specimens = []
        self.maps_names = []
        self.cases_names = []

        self.load_multiple_points()
        self.load_multiple_cases()
        self.set_specimen = set_specimen

    def load_multiple_points(self) -> None:     # wczytanie roznych map
        files_list = glob.glob('tests/maps/*points*.txt')
        self.maps_names = files_list
        for file in files_list:
            self.maps.append(Map(file))
        pass

    def load_multiple_cases(self) -> None:    # wczytanie roznych konfiguracji
        floats = ["g", "mi", "alpha", "rover_mass", "Ni_max"]
        files_list = glob.glob('tests/cases/*.txt')
        temp: dict = {}
        for file in files_list:
            f = open(file)
            self.cases_names = files_list
            for line in f:
                my_key, content = line.split()
                if my_key in floats:
                    temp[my_key] = float(content)
                else:
                    temp[my_key] = int(content)
            f.close()
            self.cases.append(temp)
        pass

    def execute_algorithm(self, times: int = 100):        # wykonanie algorytmu dla różnych konfiguracji
        for config_it in self.cases:
            print("@")
            for maps_in in self.maps:
                print("#")
                configuration.values = config_it
                ea = EAlgorithm(maps_in, set_specimens=self.set_specimen)
                [best_ratings, routes, time] = ea.run_multiple_times(times=times)
                best_ratings, routes = (list(t) for t in zip(*sorted(zip(best_ratings, routes))))
                route_lengths = []
                for route in routes:
                    route_lengths.append(len(route))
                self.best_ratings.append(best_ratings[-1])
                self.worst_ratings.append(best_ratings[0])
                self.avg_ratings.append(mean(best_ratings))
                self.std_ratings.append(std(best_ratings))
                self.best_ratings_len.append(route_lengths[-1])
                self.worst_ratings_len.append(route_lengths[0])
                self.avg_ratings_len.append(mean(route_lengths))
                self.std_ratings_len.append(std(route_lengths))
                print()
            print()
        print()
        print("BEST:", self.best_ratings)
        print("WORST:", self.worst_ratings)
        print("AVERAGE:", self.avg_ratings)
        print("STD:", self.std_ratings)

    def get_ratings(self):
        return self.best_ratings, self.worst_ratings, self.avg_ratings, self.std_ratings

    def get_ratings_lengths(self):
        return self.best_ratings_len, self.worst_ratings_len, self.avg_ratings_len, self.std_ratings_len
