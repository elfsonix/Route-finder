from map import Map
from population import Population
import configuration
from exceptions import *
from output_presentation import Plotter


class EAlgorithm:
    def __init__(self, my_map: Map, set_specimens: bool = False, save_info_per_iter: bool = False):
        self.avg_per_iter = []
        self.best_per_iter = []
        self.worst_per_iter = []
        self.avg_allwowed_per_iter = []
        self.best_allowed_per_iter = []
        self.worst_allowed_per_iter = []
        self.save_info_per_iter: bool = save_info_per_iter
        self.generation = Population(my_map, set_specimens=set_specimens)

    @staticmethod
    def stop(population, old_best):
        if population.gen_num > configuration.values["max_generation"]:  # przekroczenie max liczby generacji
            return 1
        elif population.select_best_specimen().rating > configuration.values["target_value"]:
            return 1
        elif old_best[-1] != 0:  # nie dziel przez 0 xd
            if (old_best[-1]-old_best[0])/old_best[-1] < 0.05:
                # jesli przez ostatnie 10 generacji nie poprawilo sie o 5% rating
                return 1
        else:
            return 0

    def run(self):
        self.generation.rate_all()
        old_best = [0, self.generation.select_best_allowed_specimen().rating]
        while not self.stop(self.generation, old_best):
            # wartosc 20 jest jeszcze do ustalenia -> wartosc docelowa funkcji celu
            # print("gen:", self.generation.gen_num)
            if self.save_info_per_iter:
                self.avg_per_iter.append(self.generation.get_average_specimen_rating())
                self.best_per_iter.append(self.generation.select_best_specimen().rating)
                self.worst_per_iter.append(self.generation.select_worst_specimen().rating)
                self.avg_allwowed_per_iter.append(self.generation.get_average_allowed_specimen_rating())
                self.best_allowed_per_iter.append(self.generation.select_best_allowed_specimen().rating)
                self.worst_allowed_per_iter.append(self.generation.select_worst_allowed_specimen().rating)

            self.generation.next_generation()
            # print("new best:", self.generation.select_best_allowed_specimen().rating)
            new_best = self.generation.select_best_allowed_specimen().rating
            if len(old_best) == 10:
                old_best.append(new_best)
                old_best.pop(0)
            else:
                old_best.append(new_best)

    def run_multiple_times(self, times: int = 10) -> list:
        routes = []
        best_ratings = []
        time = []
        for i in range(times):
            self.run()
            final_population = self.generation
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

    def plot_per_iteration(self):
        lst = [i for i in (range(len(self.best_per_iter)))]
        print("lst:", lst)
        Plotter().line_plot(lst, self.best_per_iter)
        Plotter().line_plot(lst, self.best_allowed_per_iter)
        Plotter().line_plot(lst, self.worst_per_iter)
        Plotter().line_plot(lst, self.worst_allowed_per_iter)
        Plotter().line_plot(lst, self.avg_per_iter)
        Plotter().line_plot(lst, self.avg_allwowed_per_iter)
