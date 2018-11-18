"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):

        import heapq
        data, res, last = [], [], None
        for l in intervals:
            for i in l:
                heapq.heappush(data, (i.start, i.end))
        while data:
            cur = heapq.heappop(data)
            cur = Interval(cur[0], cur[1])
            if not last or last.end < cur.start:
                res += [cur]
                last = cur
            elif last.end > cur.end:
                continue
            else:
                last.end = cur.end
        return res

#
