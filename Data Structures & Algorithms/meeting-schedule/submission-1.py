"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        endTime = 0
        for i in range(len(intervals)):
            if intervals[i].start<endTime:
                return False
            endTime = intervals[i].end
        return True