class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        left = newInterval[0]
        right = newInterval[1]
        for i in range(len(intervals)):
            if intervals[i][1]>=newInterval[0] and intervals[i][0]<=newInterval[1]:
                left = min(left,intervals[i][0])
                right = max(right,intervals[i][1])
            else:
                answer.append(intervals[i])
        answer.append([left,right])
        answer.sort()
        return answer
