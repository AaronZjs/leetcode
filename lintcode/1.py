# coding:utf-8
"""
http://www.lintcode.com/zh-cn/problem/remove-linked-list-elements/

给出链表 1->2->3->3->4->5->3, 和 val = 3, 你需要返回删除3之后的链表：1->2->4->5。

"""


class Solution:
    # @param int[]
    # @return int[]
    """docstring for Solution"""

    def sortIntegers(self, tree):
        l = len(tree)
        for i in xrange(l):
            for j in xrange(l - 1):
                if tree[j] > tree[i]:
                    temp = tree[i]
                    tree[i] = tree[j]
                    tree[j] = temp
        return tree


# tree = [3, 5, 7, 1, 4, 2]
# sort = Solution()
# n_sort = sort.sortIntegers(tree)
# print n_sort
