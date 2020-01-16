from evolutionary_algorithm import EAlgorithm
from map import Map
import configuration
from output_presentation import Plotter
from multi_track_drifting import MultiInstanceEAlgorithm
from gui import GUI


def main():

    # configuration.load_config_file()
    # alg_map = Map()
    # data = EAlgorithm().run_multiple_times(alg_map, 1)
    # print("DONE")
    # [best_ratings, routes, time] = data
    # for element in range(len(best_ratings)):
    #     print("Try", time[element], ":", best_ratings[element], routes[element])
    # routes_len = []
    # for route in routes:
    #     routes_len.append(len(route))
    #
    # Plotter().style_setup()
    # Plotter().histogram(best_ratings)
    # Plotter().scatter_plot(routes_len, best_ratings, x_axis_name="Długość genotypu", y_axis_name="Rating")
    # Plotter().scatter_and_histogram(routes_len, best_ratings)

    menu = GUI()
    menu.main_menu()

    # ea = MultiInstanceEAlgorithm()
    # ea.load_multiple_configs()
    # ea.load_multiple_points()
    # best, worst, average, std = ea.execute_algorithm()
    # dataset_names = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']
    # xlabels = ['Best', 'Worst', 'Average', 'Standart Deviation']
    # title = 'Ratings'
    #
    # Plotter().grouped_barplot(best, worst, average, std, dataset_names, xlabels, 'Rating', title)
    # Plotter().barplot(best, dataset_names, "Rating", title)


if __name__ == '__main__':
    # TODO wywołanie algorytmu
    main()
    pass
