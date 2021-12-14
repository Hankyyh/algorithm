# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
#
#
#
# Example 1:
#
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
# Example 2:
#
# Input: nums = [0]
# Output: 0
# Example 3:
#
# Input: nums = [2,4]
# Output: 6
# Example 4:
#
# Input: nums = [8,10,2]
# Output: 10
# Example 5:
#
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 105
# 0 <= nums[i] <= 231 - 1

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            node = root
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero

        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)

        return ans