# coding:utf-8
"""

给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。
您在真实的面试中是否遇到过这个题？
样例

给定 [1,2,3] 表示 123, 返回 [1,2,4].

给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
"""


class Solution():
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, arr):
        # arr.reverse()
        n = ""
        for x in xrange(len(arr)):
            n += str(arr[x])
        n = str(int(n) + 1)

        for x in xrange(len(n)):
            print n[x]
            arr[x] = n[x]
        return arr


arr = [1, 2, 3, 9, 9, 9]
c = Solution()
c.plusOne(arr)

