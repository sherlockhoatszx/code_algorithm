class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence1(self, nums):
        '''version1,to check how many elements can be adjoined after dpA[i]'''
        if not nums:
            return 0
        n=len(nums)
        dpA=[1]*n
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    dpA[j]=max(dpA[j],dpA[i]+1)

        return max(dpA)

    def longestIncreasingSubsequence2(self,nums):
        '''version2,to check how many elements that dpA[i] can be added to'''
        if not nums:
            return 0
        dp = [1] * len(nums)
        for curr, val in enumerate(nums):
            for prev in xrange(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence3(self,nums):
        '''version3,the greedy+binary_search approach'''
        import sys
        n=len(nums)
        minLast=[sys.maxsize]*(n+1)
        minLast[0]=-sys.maxsize

        for idx,val in enumerate(nums):
            #find the first number in minLast >= nums[i]
            idx = self.binary_search(minLast,val)
            print(idx)
            minLast[idx]=val
            print(minLast)

        for i in range(n,0,-1):
            if minLast[i]!=sys.maxsize:
                return i

        return 0
    #find the first number in minLast>num
    def binary_search(self,arr,num):
        start,end=0,len(arr)-1
        while start+1<end:
            mid=(end-start)//2+start

            if arr[mid]<num:
                start=mid
            else:
                end=mid

        return end
