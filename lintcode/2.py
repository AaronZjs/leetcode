# coding:utf-8
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if (n == 1):
            return 0
        if (n == 2):
            return 1

        n1 = 0
        n2 = 1

        count = 2
        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        # write your code here
        return n2

# t = Solution()
# t.fibonacci(10)
