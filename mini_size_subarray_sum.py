import pdb
'''同向双指针，慢指针遍历数组，快指针一路向前，直到sum>=target,停下来。
然后每次删掉左边的数字，只要当前和小于s，快指针继续向右，
每次pk min length'''
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        if nums is None or len(nums)==0:
            return -1

        n = len(nums)
        minLength = n + 1
        sum = 0
        fast = 0

        for i in range(n):
            sum_ret=[]
            while fast < n and sum < s:
                sum += nums[fast]
                sum_ret.append(nums[fast])
                #fast stop there,and wait for the slow index to judge
                #fast index start from where it stopped,not from the zero
                fast += 1
            if sum >= s:
                minLength = min(minLength, fast - i)
            #print and the sum_ret is only for show the process
            #not needed in the pure algorithms code
            print(i,sum_ret)
            sum -= nums[i]

        if minLength == n + 1:
            return -1

        return minLength


s=Solution()
print(s.minimumSize([1,2,3,4,5,6,7,8],11))
