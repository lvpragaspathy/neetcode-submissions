class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        out = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            out.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0], newInterval[1] = min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])
            i += 1
            
        out.append([newInterval[0], newInterval[1]])

        while i < len(intervals):
            out.append(intervals[i])
            i += 1

        return out
