'''use the mono decreasing deque to store the elements,find the largest elements
per window'''

from collections import deque

class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
        
        dq = deque([])
        pdb.set_trace()
        for i in range(k-1):
            self.push(dq,nums,i)
            
        rets = []
        
        for i in range(k-1,len(nums)):
            self.push(dq,nums,i)
            rets.append(nums[dq[0]])
            if dq [0] == i-k+1:
                dq.popleft()
                
        return rets
        
        
        
    def push(self,dq,nums,i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
            
import pdb           
s = Solution()
nums = [4,3,2,1,7,7,8]
k = 3

ret = s.maxSlidingWindow(nums=nums,k=3)
            
        
