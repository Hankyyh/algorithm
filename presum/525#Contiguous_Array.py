# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        presum = [0]
        preindex = {0:-1}
        res = 0
        for i, n in enumerate(nums):
            if n == 0:
                presum.append(presum[-1] - 1)
            else:
                presum.append(presum[-1] + 1)
            if presum[-1] in preindex:
                res = max(res, i - preindex[presum[-1]])
            else:
                preindex[presum[-1]] = i
        return res
