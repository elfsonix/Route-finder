from solution import Solution

class Rover:
    def __init__(self, start_weight: float, start_location: int) -> None:
        self.current_weight = start_weight
        self.current_location = start_location

    def go(self, route: Solution):
        return 1 # koszt przebytej trasy
