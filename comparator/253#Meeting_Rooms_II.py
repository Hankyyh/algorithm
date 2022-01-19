# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
#
#
#
# Example 1:
#
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:
#
# Input: intervals = [[7,10],[2,4]]
# Output: 1
#
#
# Constraints:
#
# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        list_cnt = []
        for i in intervals:
            list_cnt.append([i[0] ,1])
            list_cnt.append([i[1], -1])
        list_cnt.sort(key = lambda x : (x[0], x[1]))
        res, cnt = 0, 0
        for i in list_cnt:
            cnt = cnt + i[1]
            res = max(res, cnt)
        return res