from rover import Rover

class Solution:
    def __init__(self, points: list) ->None:
        self.route = points
        self.rating = self.rate()

    def get_length(self):
        return len(self.route)

    def goal(self) -> float:
        return Rover.go(self)

    def punishment(self) -> float:
        pass

    def rate(self, alfa: float = 1, beta: float = 1):
        return alfa*self.goal() + beta*self.punishment()