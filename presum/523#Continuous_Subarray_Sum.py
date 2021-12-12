# 523. Continuous Subarray Sum
# Medium
#
# 1128
#
# 173
#
# Add to List
#
# Share
# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
#
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
#
#
#
# Example 1:
#
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:
#
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:
#
# Input: nums = [23,2,6,4,7], k = 13
# Output: false

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        preindex = {0:-1}
        for i, a in enumerate(nums):
            prefix = (prefix + a) % k
            if prefix in preindex and i - preindex[prefix] > 1:
                return True
            if prefix not in preindex :
                preindex[prefix] = i

        return False

