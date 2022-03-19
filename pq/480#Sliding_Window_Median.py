# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
#
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
# You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.
#
#
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
# 1 [3  -1  -3] 5  3  6  7       -1
# 1  3 [-1  -3  5] 3  6  7       -1
# 1  3  -1 [-3  5  3] 6  7        3
# 1  3  -1  -3 [5  3  6] 7        5
# 1  3  -1  -3  5 [3  6  7]       6
# Example 2:
#
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1

def medianSlidingWindow(nums, k):
    small, large = [], []
    for i, x in enumerate(nums[:k]):
        heapq.heappush(small, (-x,i))
    for _ in range(k-(k>>1)):
        move(small, large)
    ans = [get_med(small, large, k)]
    for i, x in enumerate(nums[k:]):
        if x >= large[0][0]:
            heapq.heappush(large, (x, i+k))
            if nums[i] <= large[0][0]:
                move(large, small)
        else:
            heapq.heappush(small, (-x, i+k))
            if nums[i] >= large[0][0]:
                move(small, large)
        while small and small[0][1] <= i:
            heapq.heappop(small)
        while large and large[0][1] <= i:
            heapq.heappop(large)
        ans.append(get_med(small, large, k))
    return ans

def move(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))

def get_med(h1, h2, k):
    return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.