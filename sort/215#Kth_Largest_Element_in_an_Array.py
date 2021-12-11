# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        k = min(k, len(nums))
        pos = self.partition(nums, left, right)
        while pos != len(nums) - k:
            if pos < len(nums) - k:
                left = pos + 1
            else:
                right = pos - 1
            pos = self.partition(nums, left, right)
        return nums[pos]

    def partition(self, nums, left, right) -> int:
        pivot, wall = nums[right], left
        for i in range(left, right):
            if nums[i] < pivot:
                self.swap(nums, i, wall)
                wall += 1
        self.swap(nums, wall, right)
        return wall

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp