import configuration


class Map:
    def __init__(self, file: str = "points.txt") -> None:
        f = open(file)
        self.map = []
        for line in f:
            line = line.split()
            dictionary: dict = {'x': int(line[0]), 'y': int(line[1]), 'z': int(line[2]), 'profit': float(line[3]),
                                'weight': float(line[4])}
            self.map.append(dictionary)
        f.close()
        self.max_point = len(self.map)

        self.cost_matrix = self.calc_cost_matrix(self.map)

    def get_z(self, point_id: int) -> int:
        return self.map[point_id]['z']

    def get_profit(self, point_id: int):
        return self.map[point_id]['profit']

    def get_weight(self, point_id: int):
        return self.map[point_id]['weight']

    @staticmethod
    def calc_cost(point1: dict, point2: dict) -> float:
        cost = configuration.values["g"] * configuration.values["mi"] * \
               ((point1['x']-point2['x'])**2 + (point1['y'] - point2['y'])**2) * (point1['z'] - point2['z'])
        return abs(cost)

    def calc_cost_matrix(self, points: list) -> list:
        temp = [[0 for x in points] for y in points]
        for i in range(len(points)):
            for j in range(len(points)):
                temp[i][j] = self.calc_cost(points[i], points[j])
        return temp

    def calc_fuel_usage(self, mass: float, point1: int, point2: int):
        return self.cost_matrix[point1][point2] * mass
