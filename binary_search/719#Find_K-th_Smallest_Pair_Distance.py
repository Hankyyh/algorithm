# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
#
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
#
#
#
# Example 1:
#
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Example 2:
#
# Input: nums = [1,1,1], k = 2
# Output: 0
# Example 3:
#
# Input: nums = [1,6,1], k = 3
# Output: 5


def smallestDistancePair(nums, k):
    # Return: Is there k or more pairs with distance <= guess? i.e. are
    # there enough?
    def possible(guess_dist):
        i = count = 0
        j = 1
        # Notice that we never decrement j or i.
        while i < len(nums):
            # If the distance calculated from j-i is less than the guess,
            # increase the window on `j` side.
            while (j < len(nums)) and ((nums[j] - nums[i]) <= guess_dist):
                j += 1
            # Count all places between j and i
            count += j - i - 1
            i += 1
        return count >= k

    nums.sort()
    lo = 0
    hi = nums[-1] - nums[0]

    while lo < hi:
        mid = (lo + hi) // 2
        # If `mid` produced `k` or more results we know it's the upper bound.
        if possible(mid):
            # We don't set to `mid - 1` because we found a number of distances
            # bigger than *or equal* to `k`. If this `mid` ends up being
            # actually equal to `k` then it's a correct guess, so let's leave it within
            # the guess space.
            hi = mid
        # If `mid` did not produce enouh results, let's increase  the guess
        # space and try a higher number.
        else:
            lo = mid + 1

    # `lo` ends up being an actual distance in the input, because
    # the binary search mechanism waits until the exact lo/hi combo where
    # 2nd to last `mid` did not produce enough results (k or more), but
    # the last `mid` did.
    return lo