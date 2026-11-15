"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_meeting = (float('-inf'),float('-inf'))
        intervals_sorted = sorted(intervals,key=lambda x:x.start)
        for interval in intervals_sorted:
            if (interval.start>prev_meeting[0] and interval.end>prev_meeting[0]) and (interval.start>=prev_meeting[1] and interval.end>prev_meeting[1]):
               prev_meeting = (interval.start,interval.end)
            else:
               return False     
                
        return True  
              