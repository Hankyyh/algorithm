# We are given a list schedule of employees, which represents the working time for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
#
# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
#
#
#
# Example 1:
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
#
#
# Constraints:
#
# 1 <= schedule.length , schedule[i].length <= 50
# 0 <= schedule[i].start < schedule[i].end <= 10^8

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        # Flatten the given intervals.
        ints = []
        for i in schedule:
            [ints.append(x) for x in i]

        # Sort the intervals by starting time which is a key part of this soln. and indentifying overlap.
        ints.sort(key = lambda x:x.start)

        # Now we want to merge intervals (the continuous periods of being busy).
        merged = []
        for i in ints:
            # If we have no intervals in our list or the current task starts after the previous one ends.
            if not merged or i.start > merged[-1].end:
                merged.append(i)
            else:
                # We know that the start time intersects the start,end of the previous task, so we take the max ending time.
                # As this will be a merged, continuous busy period.
                merged[-1].end = max(i.end, merged[-1].end)

        # Now we have our merged intervals we can look at the time between the merged
        # intervals as these will be the free time for the employee.
        free = []
        for i in range(1, len(merged)):
            free.append(Interval(start=merged[i-1].end, end=merged[i].start))

        # Now we're left with intervals of free time.
        return free