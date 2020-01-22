from evolutionary_algorithm import EAlgorithm
from multi_track_drifting import MultiInstanceEAlgorithm
from map import Map
from plotting import Plotter
import test
import configuration


class GUI:  # TODO całe GUI
    def __init__(self):
        print("Algorytm ewolucyjny analizujący trasę łazika z poborem próbek")
        print("Stworzony na zajęcia 'Matematyczne Metody Wspomagania Decyzji', III rok AiR I stopnia, WEAIiIB, AGH")
        print("Jacek Lichwa, Karolina Świerczek, Sonia Wittek")
        print()
        print("Wprowadź znak aby wybrać opcję z listy")
        configuration.load_config_file()
        pass

    def main_menu(self):
        print("1. Pojedyncze uruchomienie")
        print("2. Wielokrotne uruchomienie")
        print("3. Test algorytmu")
        print("Q - Zakończ")
        choice = input()
        if choice == "1":
            self.custom_instance_menu()
        elif choice == "2":
            self.multi_instance_menu()
        elif choice == "3":
            self.testing_menu()
        elif choice == "q" or "Q":
            pass
        else:
            self.main_menu()

    @staticmethod
    def multi_instance_menu():
        print("Wielokrotne uruchomienie dla:")
        print("1. Domyślnych wartości i losowych osobników startowych")
        choice = input()
        if choice == "1":
            print("Ile razy?")
            n = input()
            ea_map = Map()
            ea = EAlgorithm(ea_map)
            [ratings, routes, time] = ea.run_multiple_times(int(n))
            print()
            for i in range(len(routes)):
                print("TIME", time[i], "\tRATING", ratings[i], "\tROUTE", routes[i])
        pass

    def custom_instance_menu(self):
        print("Pojedynczy przypadek z parametrami:")
        print("1. Start")
        print("R - Powrót")
        choice = input()
        if choice == "1":
            ea_map = Map()
            ea = EAlgorithm(ea_map)
            ea.run()
            for elem in ea.generation.current_generation:
                print("Specimen:", elem.route, "rating:", elem.rating, elem.is_allowed)
            print("BEST:", ea.generation.select_best_allowed_specimen().route,
                  ea.generation.select_best_allowed_specimen().rating)
        elif choice == "R" or "r":
            self.main_menu()
        else:
            self.custom_instance_menu()
        pass

    def testing_menu(self):
        print("Testy:")
        print("1. Test pojedynczego uruchomienia algorytmu")
        print("2. Test wielokrotnego uruchomienia algorytmu")
        print("3. Wizualizacja map używanych w testach")
        print("R - Powrót")
        choice = input()
        if choice == "1":
            test.single_run_test()
        elif choice == "2":
            test.run_tests(100)
        elif choice == "3":
            test.maps_test()
        elif choice == "R" or "r":
            self.main_menu()
        else:
            self.testing_menu()
