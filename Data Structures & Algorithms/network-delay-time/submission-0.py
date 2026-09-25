import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')]*n
        adj = [[] for _ in range(n)]
        heap = []
        for ui, vi, ti in times:
            adj[ui-1].append([vi-1,ti])
        furthest = 0
        heap.append([0,k-1])
        distances[k-1]=0
        reached = 0
        while (len(heap)>0):
            current_dist, current_node = heapq.heappop(heap)
            print(current_dist, current_node)
            if (distances[current_node]==current_dist):
                reached+=1
                furthest = max(furthest,current_dist)
                for vi, ti in adj[current_node]:
                    if (current_dist+ti<distances[vi]):
                        distances[vi] = current_dist+ti
                        heapq.heappush(heap,[distances[vi],vi])
        if reached == n:
            return furthest
        return -1
        # add all non infinity values to heap
        # pop smallest element from heap and relax all edges
        # add to heap
