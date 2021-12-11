# Given an integer array nums, return the number of reverse pairs in the array.
#
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].
#
#
#
# Example 1:
#
# Input: nums = [1,3,2,3,1]
# Output: 2
# Example 2:
#
# Input: nums = [2,4,3,5,1]
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 5 * 104
# -231 <= nums[i] <= 231 - 1


def reversePairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return 0
    count = [0]

    def merge(nums):
        if len(nums) <= 1: return nums

        left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] <= 2 * right[r]:
                l += 1
            else:
                count[0] += len(left) - l
                r += 1
        return sorted(left+right)

    merge(nums)
    return count[0]