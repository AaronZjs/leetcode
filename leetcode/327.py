# coding:utf-8
"""


给一个整型数组 nums , 返回 一个在 lower 和 upper 之间的数字


例子：
给一个 nums = [-2, 5, -1] , lower = -2  , upper = 2
返回 3
这三个范围是 : [0, 0], [2, 2], [0, 2]  和各自的和 : -2, -1, 2


"""


class Ymb():

	# def __init__(self,nums,lower,upper):
	# 	n = len(nums)
	# 	sums = [0.0] * (n+1)
	# 	for i in xrange(n):
	# 		sums[i+1] = sums[i] + nums[i]

	# 	# print sums

	# 	return self.countWhileMergeSort(sums,0,n+1,lower,upper)
	def countRangeSum(self, nums, lower, upper):
		n = len(nums)
		sums = [0.0] * (n + 1)
		for i in xrange(n):
			sums[i + 1] = sums[i] + nums[i]
		print sums
		return self.countWhileMergeSort(sums, 0 , n + 1, lower, upper)
	

	def countWhileMergeSort(self, sums, start, end, lower, upper):
		if end - start <= 1:
			return 0
		mid = (start + end) / 2
		count = self.countWhileMergeSort(sums, start, mid, lower, upper)\
				+ self.countWhileMergeSort(sums, mid, end, lower, upper)
		j = k = t = mid
		cache = [0.0]*(end - start)
		r = 0
		for i in xrange(start, mid):
			while k < end and sums[k] - sums[i] < lower:
				k += 1
			while j < end and sums[j] - sums[i] <= upper:
				j += 1
			while t < end and sums[t] < sums[i]:
				cache[r] = sums[t]
				r += 1
				t += 1
			cache[r] = sums[i]
			r += 1
			count += j - k
		for i in xrange(r):
			sums[start + i] = cache[i]
		return count

nums = [-2,5,-1]
lower = -2
upper = 2

ymb = Ymb()
res = ymb.countRangeSum(nums,lower,upper)
print res
		



























