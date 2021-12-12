# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
#

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = [0]
        dic = collections.defaultdict(int)
        dic[0] += 1
        res = 0
        for i in nums:
            presum.append(presum[-1] + i)
            if dic[presum[-1] - k] != 0:
                res += dic[presum[-1] - k]
            dic[presum[-1]] += 1
        return res