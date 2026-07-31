class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse=True)
        curTime = (target-cars[0][0])/cars[0][1]
        count = 1
        for i in range(len(cars)):
            time = (target-cars[i][0])/cars[i][1]
            if time>curTime:
                count+=1
                curTime = time
        return count
