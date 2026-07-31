class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while (len(heap)>1):
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if (x<y):
                heapq.heappush(heap,x-y)
        if len(heap)==0:
            return 0
        else:
            return -heap[0]
