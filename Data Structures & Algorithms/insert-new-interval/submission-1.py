class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        start, end = newInterval[0], newInterval[1]
        out = []

        i = 0
        while i < len(intervals) and intervals[i][1] < start:
            out.append(intervals[i])
            i += 1

        # now end >= i_start

        while i < len(intervals) and intervals[i][0] <= end:
            start, end = min(intervals[i][0], start), max(end, intervals[i][1])
            i += 1
            
        out.append([start, end])

        while i < len(intervals):
            out.append(intervals[i])
            i += 1


        return out
