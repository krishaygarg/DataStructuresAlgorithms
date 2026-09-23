import heapq
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        # set of accessible points
        # add edges and update set of accessible points
        # costs: [cost, (x,y)]
        n = len(grid)
        costs = [[grid[0][0],(0,0)]]
        total_cost = 0
        visited = set()
        while (len(costs)>0):
            current_cost, current_point = heapq.heappop(costs)
            visited.add(current_point)
            total_cost = max(total_cost, current_cost)
            if (current_point == (n-1,n-1)):
                return total_cost
            if (current_point[0]>0):
                new_point = (current_point[0]-1, current_point[1])
                if (new_point not in visited):
                    heapq.heappush(costs, [grid[current_point[0]-1][current_point[1]],new_point])
            if (current_point[0]<n-1):
                new_point = (current_point[0]+1, current_point[1])
                if (new_point not in visited):
                    heapq.heappush(costs, [grid[current_point[0]+1][current_point[1]],new_point])          
            if (current_point[1]>0):
                new_point = (current_point[0], current_point[1]-1)
                if (new_point not in visited):
                    heapq.heappush(costs, [grid[current_point[0]][current_point[1]-1],new_point])
            if (current_point[1]<n-1):
                new_point = (current_point[0], current_point[1]+1)
                if (new_point not in visited):
                    heapq.heappush(costs, [grid[current_point[0]][current_point[1]+1],new_point])