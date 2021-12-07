class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        res = []
        for i in range(len(nums2) -1, -1, -1):
            # print(i)
            while len(stack) > 0 and stack[-1] < nums2[i]:
                stack.pop()
            if len(stack) == 0:
                dic[nums2[i]] = -1
            else:
                dic[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        for i in nums1:
            res.append(dic.get(i))
        return res
