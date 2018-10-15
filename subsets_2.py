'''recursion and remove duplicate
S = [1,2,2]
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]'''
import copy
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here

        self.rets=[]
        nums.sort()
        self.dfs(nums,[],0)
        return self.rets

    def dfs(self,nums,subsets,startindex):
        subsets = copy.deepcopy(subsets)
        self.rets.append(subsets)
        for i in range(startindex,len(nums)):
            #i>0 to avoid out of range
            #nums[i]==nums[i-1] duplicate elements
            #i >startindex,i-1 did not push into the list, and nums[i]==nums[i-1]
            #then there is duplicate
            if i>0 and nums[i]==nums[i-1] and i>startindex:
                continue
            subsets.append(nums[i])
            self.dfs(nums,subsets,i+1)
            subsets.pop()

'''version 2, try the BFS'''
from queue import Queue
class Solution_BFS:
    def subsetsWithDup(self,nums):
        slef.rets=[]
        nums.sort()
        
