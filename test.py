from multi_track_drifting import MultiInstanceEAlgorithm
from output_presentation import Plotter
from evolutionary_algorithm import EAlgorithm
from map import Map
import configuration as cnfg


def case_naming(name):
    if "default" in name:
        return "Default case"
    elif "alpha_big" in name:
        return "Alpha big"
    elif "alpha_small" in name:
        return "Alpha small"
    elif "rate_big" in name:
        return "Mutation rate big"
    elif "rate_small" in name:
        return "Mutation rate small"
    elif "size_big" in name:
        return "Parent group size big"
    elif "size_small" in name:
        return "Parent group size small"
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
    best, worst, avg, std = mea.execute_algorithm(times=times)
    case_names = []
    map_names = []
    iteretion = 0
    for name in mea.cases_names:
        case_names.append(case_naming(name))
    for name in mea.maps_names:
        map_names.append(map_naming(name))
    for name1 in map_names:
        Plotter().barplot(best[iteretion*7:iteretion*7+7], case_names, "Rating", name1)
        iteretion += 1
    # Plotter().barplot(best, bar_names, "Rating", "BEST")
    return best, worst, avg, std


def single_run_test():
    cnfg.load_config_file()
    alg_map = Map()
    ea = EAlgorithm(alg_map, save_info_per_iter=True)
    ea.run()
    ea.plot_per_iteration()
    print(ea.generation.select_best_allowed_specimen().rating)
    pass


if __name__ == "__main__":
    single_run_test()
    run_tests(100)
