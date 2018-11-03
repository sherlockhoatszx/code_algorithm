import sys
import pdb
class Solution:

    def maxSubarray(self,nums):
        min_sum,max_sum=0,-sys.maxsize

        prefix_sum = 0

        pdb.set_trace()

        for num in nums:
            #print(num)
            prefix_sum += num
            #print('####',prefix_sum)
            max_sum = max(max_sum,prefix_sum-min_sum)
            #print('#######',max_sum)
            min_sum = min(min_sum,prefix_sum)
            #print('#######',min_sum)

        return max_sum

class Solution2:
    '''dp'''
    def maxSubarray(self,nums):
        dp=[0]*len(nums)
        res=dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
            res = max(res,dp[i])
        return res





arr=[1,-3,-2,5,400,-3,4]
s=Solution2()
print(s.maxSubarray(arr))
