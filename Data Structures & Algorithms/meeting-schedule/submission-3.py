"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        curr_start, curr_end = -1,-1
        for interval in intervals:
            if curr_start < interval.start and curr_end <= interval.start \
               and curr_start < interval.end and curr_end < interval.end:
                curr_start, curr_end = interval.start, interval.end
            else:
                return False
        return True
