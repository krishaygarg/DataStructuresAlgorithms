import copy
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        original = copy.deepcopy(queries)
        queries.sort()
        answer = defaultdict()
        lengths = []
        i = 0
        for q in queries:
            while i<len(intervals) and intervals[i][0]<=q:
                heapq.heappush(lengths,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            while len(lengths)>0 and lengths[0][1]<q:
                heapq.heappop(lengths)
            if len(lengths)==0:
                answer[q]=-1
            else:
                answer[q]=lengths[0][0]

        final = [0]*len(queries)
        for i in range(len(original)):
            final[i] = answer[original[i]]
        return final
    
