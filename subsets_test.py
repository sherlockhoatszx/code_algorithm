'''subsets is a very classical combination dfs,i rewrite it in the second time
and found out that the deepcopy and the append clause position is very tricky
this code is wrong,try to fix it'''

class Solution:
    def subsets(self,nums):
        if not nums:
            return -1

        self.rets=[]

        self.dfs_helper(nums,0,[])

        return self.rets

    def dfs_helper(self,nums,index,combines):
        #区分可变对象和不可变对象，区分python的应用方式
        import copy

        for i in range(index,len(nums)):
            combines=copy.deepcopy(combines)

            combines.append(nums[i])

            self.rets.append(combines)

            self.dfs_helper(nums,i+1,combines)



            combines.pop()

        return
