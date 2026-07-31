"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        best = 0
        current = 0
        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]
        startTimes.sort()
        endTimes.sort()
        start = 0
        end = 0
        while (start<len(startTimes)):
            if (startTimes[start]<endTimes[end]):
                current+=1
                start+=1
            else:
                current-=1
                end+=1
            best = max(best,current)
        return best
