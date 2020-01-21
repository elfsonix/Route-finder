from multi_track_drifting import MultiInstanceEAlgorithm
from plotting import Plotter
from evolutionary_algorithm import EAlgorithm
from map import Map
import configuration as cnfg


def case_naming(name):
    if "default" in name:
        return "Default\ncase"
    elif "alpha_big" in name:
        return "Alpha\nbig"
    elif "alpha_small" in name:
        return "Alpha\nsmall"
    elif "rate_big" in name:
        return "Mutation\nrate\nbig"
    elif "rate_small" in name:
        return "Mutation\nrate\nsmall"
    elif "size_big" in name:
        return "Parent\ngroup\nsize\nbig"
    elif "size_small" in name:
        return "Parent\ngroup\nsize\nsmall"
    else:
        return None


def map_naming(name):
    if "arrangement_bad" in name:
        return "Bad point arrangement"
    elif "arrangement_good" in name:
        return "Good point arrangement"
    elif "arrangement_middle" in name:
        return "Average point arrangement"
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

        print(iteretion, "baprlot values", best[iteretion*7:iteretion*7+7])
        iteretion += 1

    return None


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
        Plotter.scatter_plot(x, y)
        x = []
        y = []
        z = []


if __name__ == "__main__":
    single_run_test()
    # run_tests(10)
    # maps_test()
