from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            adj[from_i].append([to_i,price_i])
        costs = [float('inf')]*n
        # [node,cost,flights]
        queue = deque()
        queue.append([src,0,0])
        while (len(queue)>0):
            current_node, current_cost, current_flight_num = queue.popleft()
            if (current_cost < costs[current_node]):
                costs[current_node] = current_cost
                if (current_flight_num<=k):
                    for to_i, price_i in adj[current_node]:
                        queue.append([to_i,current_cost+price_i,current_flight_num+1])

        if (costs[dst]==float('inf')):
            return -1
        return costs[dst]
