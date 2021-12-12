# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array.
#
#
#
# Example 1:
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
#     [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:
#
# Input: nums = [5], k = 9
# Output: 0

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        count = [1] + [0] * k
        for a in nums:
            prefix = (prefix + a) % k
            res += count[prefix]
            count[prefix] += 1
        return res