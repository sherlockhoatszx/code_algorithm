"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#brutal force or use min_heap
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        '''version1,brutal force'''
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))

        meeting_rooms = 0
        ongoing_meetings = 0
        for _, delta in sorted(points):
            ongoing_meetings += delta
            meeting_rooms = max(meeting_rooms, ongoing_meetings)

        return meeting_rooms

    def minMeetingRooms(self,intervals):

        """
        first sort by the start time
        then maintain the min_heap of the end time
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        import heapq
        heap = []
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]:
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)
        return len(heap)
