# 1229. Meeting Scheduler
# Medium
#
# 575
#
# 25
#
# Add to List
#
# Share
# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.
#
# If there is no common time slot that satisfies the requirements, return an empty array.
#
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.
#
# It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.
#
#
#
# Example 1:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]
# Example 2:
#
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x:(x[0],x[1]))
        slots2.sort(key=lambda x:(x[0],x[1]))
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] <= slots2[j][0]:
                i += 1
            elif slots1[i][0] >= slots2[j][1]:
                j += 1
            else:
                overlap_left = max(slots1[i][0], slots2[j][0])
                overlap_right = min(slots1[i][1], slots2[j][1])
                if (overlap_right - overlap_left >= duration):
                    return [overlap_left, overlap_left + duration]
                if slots1[i][1] < slots2[j][1]:
                    i += 1
                else:
                    j += 1

        return []
