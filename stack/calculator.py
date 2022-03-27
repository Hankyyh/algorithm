# 772. Basic Calculator III
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#
#
# Example 1:
#
# Input: s = "1+1"
# Output: 2
# Example 2:
#
# Input: s = "6-4/2"
# Output: 4
# Example 3:
#
# Input: s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21
#
#
# Constraints:
#
# 1 <= s <= 104
# s consists of digits, '+', '-', '*', '/', '(', and ')'.
# s is a valid expression.

class Solution:
    i = 0
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        op = '+'
        while self.i < len(s):
            c = s[self.i]
            self.i += 1
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            if c == '(':
                num = self.calculate(s)
            if self.i >= len(s) or c in ('+', '-', '*', '/', ')'):
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(num * stack.pop())
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
            if c == ')':
                break
        return sum(stack)
