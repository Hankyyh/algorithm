# Given a string s, return the length of the longest substring that contains at most two distinct characters.
#
#
#
# Example 1:
#
# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:
#
# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of English letters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = collections.defaultdict(int)
        res = 0
        left = -1
        for i, c in enumerate(s):
            dic[c] += 1
            while len(dic) > 2:
                left += 1
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    dic.pop(s[left])
            if len(dic) <= 2:
                res = max(res, i - left)
        return res