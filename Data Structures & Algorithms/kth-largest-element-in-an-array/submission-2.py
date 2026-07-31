class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            if (i<k):
                heapq.heappush(heap,nums[i])
            elif (nums[i]>heap[0]):
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
        return heap[0]
            

        