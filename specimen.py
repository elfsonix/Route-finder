import configuration
from rover import Rover


class Specimen:
    def __init__(self, route: list) -> None:
        self.route = route
        self.alpha: float = configuration.values["alpha"]
        self.rover = Rover()
        self.rating = self.rate()

    def get_length(self):
        return len(self.route)

    def get_item(self):
        return self.route

    def goal(self) -> float:
        return self.rover.go(self.route)

    def punishment(self) -> float:
        return 0

    def rate(self):
        return self.goal() + self.alpha * self.punishment()
