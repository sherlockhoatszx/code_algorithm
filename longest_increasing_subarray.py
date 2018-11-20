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
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)


    def longestIncreasingSubsequence3(self,nums):
        '''version3,the greedy+binary_search approach'''
        import sys
        n=len(nums)
        minLast=[sys.maxsize]*(n+1)
        minLast[0]=-sys.maxsize

        for idx,val in enumerate(nums):
            #find the first number in minLast >= nums[i]
            idx = self.binary_search(minLast,val)

            minLast[idx]=val

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

    def findLongestIncreasingSubsequence(self, nums):
        '''version1,to check how many elements can be adjoined after dpA[i]'''
        if not nums:
            return 0
        n=len(nums)
        dpA=[1]*n
        import sys
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    dpA[j]=max(dpA[j],dpA[i]+1)

        longest_amount = max(dpA)
        longest_arr=[sys.maxsize]* longest_amount
        for idx,val in enumerate(dpA):
            if val<=longest_amount:
                longest_arr[val]=nums[idx]

class Solution2:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    if we want to return the longest subarray also
    """


    def longestIncreasingSubsequence(self,nums):
        '''1.to check how many elements that dpA[i] can be added to
        2.add m to record the longest subarry,a new array to record
        index i's last position'''
        if not nums:
            return 0
        dp = [1] * len(nums)
        m,index=0,-1
        father=[-1]*len(nums)
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] < val:
                    if dp[prev]+1>dp[curr]:
                        dp[curr]=dp[prev]+1
                        father[curr]=prev
            if val>m:
                m=dp[curr]
                index=curr

        rets=[]

        for i in range(m):
            rets.append(nums[index])
            index=father[index]


        return max(dp),rets


testarr=[-7,10,9,2,3,8,8,1]
s=Solution2()
print(s.longestIncreasingSubsequence(testarr))
