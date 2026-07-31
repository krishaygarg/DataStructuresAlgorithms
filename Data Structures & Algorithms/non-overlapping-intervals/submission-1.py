class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        total = 0
        prevEnd = float('-inf')
        for i in range(len(intervals)):
            if intervals[i][0]>=prevEnd:
                total+=1
                prevEnd = intervals[i][1]
        return len(intervals)-total