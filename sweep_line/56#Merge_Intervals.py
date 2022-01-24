# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
# Constraints:
#
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:(x[0],x[1]))
        res = []
        if len(intervals) == 0:
            return res
        cur_start, cur_end = -1, -1
        for i in intervals:
            if cur_start == -1:
                cur_start = i[0]
                cur_end = i[1]
            elif i[0] <= cur_end:
                cur_end = max(cur_end, i[1])
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = i[0], i[1]
        res.append([cur_start, cur_end])
        return res