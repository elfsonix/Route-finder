from map import Map
from population import Population
import configuration
from exceptions import *
from plotting import Plotter


class EAlgorithm:
    def __init__(self, my_map: Map, set_specimens: bool = False, save_info_per_iter: bool = False):
        self.avg_per_iter = []
        self.best_per_iter = []
        self.worst_per_iter = []
        self.avg_allwowed_per_iter = []
        self.best_allowed_per_iter = []
        self.worst_allowed_per_iter = []
        self.save_info_per_iter: bool = save_info_per_iter
        self.my_map = my_map
        self.set_specimens = set_specimens
        self.generation = Population(self.my_map, set_specimens=self.set_specimens)

    @staticmethod
    def stop(population, old_best):
        if population.gen_num > configuration.values["max_generation"]:  # przekroczenie max liczby generacji
            return True
        elif population.select_best_specimen().rating > configuration.values["target_value"]:
            return True
        elif old_best[-1] != 0:  # nie dziel przez 0 xd
            if (old_best[-1]-old_best[0])/old_best[-1] < 0.05:
                # jesli przez ostatnie 10 generacji rating nie poprawil sie o 5%
                return True
            else:
                return False
        else:
            return False

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
            self.generation.reset()
            self.run()
            final_population = self.generation
            try:
                routes.append(final_population.select_best_allowed_specimen().route)
                best_ratings.append(final_population.select_best_allowed_specimen().rating)
                time.append(i+1)
            except NoSpecimenFound:
                print("!", end=" ")
                continue
            else:
                print(self.generation.gen_num, end=" ")
        return [best_ratings, routes, time]

    def plot_per_iteration(self):
        lst = [i for i in (range(len(self.best_per_iter)))]
        print("lst:", lst)
        print(self.best_allowed_per_iter)
        # Plotter().line_plot(lst, self.best_per_iter, plot_title="Best")
        # Plotter().line_plot(lst, self.best_allowed_per_iter, plot_title="Best allowed")
        # Plotter().line_plot(lst, self.worst_per_iter, plot_title="Worst")
        # Plotter().line_plot(lst, self.worst_allowed_per_iter, plot_title="Worst allowed")
        # Plotter().line_plot(lst, self.avg_per_iter, plot_title="Average")
        # Plotter().line_plot(lst, self.avg_allwowed_per_iter, plot_title="Average allowed")
        Plotter().multiline_plot(lst,
                                 self.best_allowed_per_iter,
                                 self.avg_allwowed_per_iter,
                                 self.worst_allowed_per_iter,
                                 x_axis_name="Iteration",
                                 y_axis_name="Rating",
                                 legend=["Best", "Average", "Worst"],
                                 plot_title="Allowed ratings")
        Plotter().multiline_plot(lst,
                                 self.best_per_iter,
                                 self.avg_per_iter,
                                 self.worst_per_iter,
                                 x_axis_name="Iteration",
                                 y_axis_name="Rating",
                                 legend=["Best", "Average", "Worst"],
                                 plot_title="All ratings")
        # x=[]
        # y=[]
        # for d in self.my_map.map:
        #     x.append(d["x"])
        #     y.append(d["y"])
        # Plotter.scatter_plot(x, y, plot_title="Mapa")
