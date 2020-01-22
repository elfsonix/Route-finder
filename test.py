from multi_track_drifting import MultiInstanceEAlgorithm
from plotting import Plotter
from evolutionary_algorithm import EAlgorithm
from map import Map
import configuration as cnfg


def case_naming(name):
    if "default" in name:
        return "G0"
    elif "alpha_big" in name:
        return "G1"
    elif "alpha_small" in name:
        return "G2"
    elif "probability_big" in name:
        return "G3"
    elif "probability_small" in name:
        return "G4"
    elif "size_big" in name:
        return "G5"
    elif "size_small" in name:
        return "G6"
    else:
        return None


def map_naming(name):
    if "arrangement_bad" in name:
        return "Bad point arrangement"
    elif "arrangement_good" in name:
        return "Good point arrangement"
    elif "default" in name:
        return "Default map"
    elif "weight_bad" in name:
        return "Bad weight arrangement"
    elif "weight_good" in name:
        return "Good weight arrangement"
    elif "weight_middle" in name:
        return "Average weight arrangement"
    else:
        return None


def run_tests(times: int = 1):
    mea = MultiInstanceEAlgorithm(set_specimen=True)
    mea.execute_algorithm(times=times)
    best, worst, avg, std = mea.get_ratings()
    best_len, worst_len, avg_len, std_len = mea.get_ratings_lengths()
    case_names = []
    map_names = []
    y_data = []
    iteretion = 0
    for name in mea.cases_names:
        case_names.append(case_naming(name))
    for name in mea.maps_names:
        map_names.append(map_naming(name))
    for name1 in map_names:
        Plotter().barplot_threeway(best[iteretion*7:iteretion*7+7],
                                   avg[iteretion*7:iteretion*7+7],
                                   worst[iteretion*7:iteretion*7+7],
                                   case_names, "Rating", name1, ["Best", "Avg", "Worst"])
        # Plotter().scatter_plot(best[iteretion*7:iteretion*7+7],
        #                        best_len[iteretion*7:iteretion*7+7],
        #                        "Ratings", "Genome lengths", name1)
        y_data.append(best[iteretion*7:iteretion*7+7])
        print(iteretion, "baprlot values", best[iteretion*7:iteretion*7+7])
        iteretion += 1
    return None


def run_test_percentage(times: int = 1):
    mea = MultiInstanceEAlgorithm(set_specimen=True)
    mea.execute_precengage_values(times)
    best, worst, avg, std = mea.get_ratings()
    # best_len, worst_len, avg_len, std_len = mea.get_ratings_lengths()
    case_names = []
    map_names = []
    # y_data = []
    x_data = [10*x for x in range(5, 15)]
    print(len(best)/11)
    iteretion = 0
    # print("best len", len(best))
    for name in mea.cases_names:
        case_names.append(case_naming(name))
    for name in mea.maps_names:
        map_names.append(map_naming(name))
    for name1 in map_names:
        print("XXX")
        # Plotter().barplot_threeway(best[iteretion * 7:iteretion * 7 + 7],
        #                            avg[iteretion * 7:iteretion * 7 + 7],
        #                            worst[iteretion * 7:iteretion * 7 + 7],
        #                            case_names, "Rating", name1, ["Best", "Avg", "Worst"])
        # Plotter().scatter_plot(best[iteretion*7:iteretion*7+7],
        #                        best_len[iteretion*7:iteretion*7+7],
        #                        "Ratings", "Genome lengths", name1)
        Plotter().multiline_plot(x_data, best[10*iteretion:10*iteretion + 10],
                                 best[10*iteretion + 10:10*iteretion + 20],
                                 best[10*iteretion + 20:10*iteretion + 30],
                                 x_axis_name="Default parameter pecentage",
                                 y_axis_name="Rating",
                                 plot_title=name1,
                                 legend=["alpha", "mutation_probability", "parent_group_size"])
        # y_data.append(best[iteretion * 7:iteretion * 7 + 7])
        # print(iteretion, "baprlot values", best[iteretion * 7:iteretion * 7 + 7])
        iteretion += 1

def single_run_test():
    cnfg.load_config_file()
    alg_map = Map()
    ea = EAlgorithm(alg_map, set_specimens=True, save_info_per_iter=True)
    ea.run()
    ea.plot_per_iteration()
    print("Single run best rating:\t", ea.generation.select_best_allowed_specimen().rating)
    print("Single run worst rating:\t", ea.generation.select_worst_allowed_specimen().rating)
    print("Single run average rating:\t", ea.generation.get_average_allowed_specimen_rating())
    pass


def maps_test():
    mea = MultiInstanceEAlgorithm()
    mea.load_multiple_points()
    x = []
    y = []
    z = []
    for _map in mea.maps:
        for d in _map.map:
            x.append(d["x"])
            y.append(d["y"])
            z.append(d["z"])
            print(".", end=" ")
        print("#")
        print(x)
        print(y)
        Plotter.scatter_plot(x, y)
        x = []
        y = []
        z = []


if __name__ == "__main__":
    # single_run_test()
    # run_tests(100)
    # maps_test()
    run_test_percentage(10)
