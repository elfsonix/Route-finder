from solution import Solution


class Rover:
    def __init__(self, start_weight: float, start_location: int) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

    # zwraca koszt przebytej trasy w danym Solution, tj. osobniku
    def go(self, route: Solution):
        #for dict in route:
            #dict[i] dokoncze wieczorem
        return 1