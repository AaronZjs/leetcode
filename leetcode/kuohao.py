# coding:utf-8
"""
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。
括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
"""


class Solution():
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParenthesesbb(self, s):
        # if "{}" in s:
        #     return True
        #
        # if "[]" in s:
        #     return True
        #
        # if "()" in s:
        #     return True
        #
        # return False
        table = {"(": ")", "[": "]", "{": "}"}
        n = len(s)
        stack = []
        for i in s:
            if len(stack) > 0 and stack[-1] in table and table[stack[-1]] == i:
                print 'ha'
                stack.pop()
            else:
                print 'no'
                stack.append(i)
            # print  stack
            # print i
        return len(stack) == 0

    def isValidParentheses(self, s):
        table = {"(":")","[":"]","{":"}"}
        leng = len(s)
        stack = ''

        for i in s:
            print i


str = "({[()]})"
c = Solution()
print(c.isValidParenthesesbb(str))
