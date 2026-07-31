class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i]+=1
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap,(-value,key))
        answer = []
        while (len(answer)<k):
            answer.append(heapq.heappop(heap)[1])
        return answer
        # bucket sort
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        print(buckets)
        return []