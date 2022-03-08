# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
#
# Return all the possible results. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s = "()())()"
# Output: ["(())()","()()()"]
# Example 2:
#
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]
# Example 3:
#
# Input: s = ")("
# Output: [""]
#
#
# Constraints:
#
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        self.remove(s, 0, 0, ('(', ')'), result)
        return result

    def remove(self, s, left, right, pars, res):
        stack = 0
        for i in range(right, len(s)):
            if s[i] == pars[0]:
                stack += 1
            elif s[i] == pars[1]:
                stack -= 1
            if stack >= 0:
                continue
            for j in range(left, i + 1):
                if s[j] == pars[1] and (j == left or pars[1] != s[j - 1]):
                    self.remove(s[:j] + s[j + 1:], j, i, pars, res)
            return
        reversed_s = s[::-1]
        if pars[0] == '(':
            self.remove(reversed_s, 0, 0, (')', '('), res)
        else:
            res.append(reversed_s)

