class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap,(math.sqrt(point[0]**2+point[1]**2),point[0],point[1]))

        answer = []
        for i in range(k):
            element = heapq.heappop(heap)
            answer.append([element[1],element[2]])
        return answer