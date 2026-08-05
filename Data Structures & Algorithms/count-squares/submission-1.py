class CountSquares:

    def __init__(self):
        self.points = dict()

    def add(self, point: List[int]) -> None:
        if point[0] not in self.points:
            self.points[point[0]] = defaultdict(int)
        self.points[point[0]][point[1]]+=1

    def count(self, point: List[int]) -> int:
        print(self.points)
        answer = 0
        if point[0] not in self.points:
            return 0
        for i in self.points[point[0]]:
            print(i)
            width = abs(i-point[1])
            if width == 0:
                continue
            if point[0]+width in self.points:
                if point[1] in self.points[point[0]+width] and i in self.points[point[0]+width]:
                    answer += self.points[point[0]][i]*self.points[point[0]+width][point[1]] * self.points[point[0]+width][i]
            if point[0]-width in self.points:
                if point[1] in self.points[point[0]-width] and i in self.points[point[0]-width]:
                    answer += self.points[point[0]][i]*self.points[point[0]-width][point[1]] * self.points[point[0]-width][i]
        return answer
