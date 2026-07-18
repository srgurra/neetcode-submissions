"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda meeting: meeting.start)

        room_end_times = []

        for meeting in intervals:
            if room_end_times and meeting.start >= room_end_times[0]:
                heapq.heappop(room_end_times)

            heapq.heappush(room_end_times, meeting.end)

        return len(room_end_times)