class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        answer = []
        for i in range(len(intervals)):
            if intervals[i][0]>right:
                answer.append([left,right])
                left = intervals[i][0]
                right = max(right,intervals[i][1])
            else:
                right = max(right,intervals[i][1])
        answer.append([left,right])
        return answer