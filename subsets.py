'''recursion and backtracking'''

class Solution:

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return


        self.search(nums, S + [nums[index]], index + 1)

        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
import copy
class Solution2:
    def subsets(self,nums):
        self.rets=[]
        def dfs(nums,temp,i):
            print(i)
            print('temp list is',temp)
            temp=copy.deepcopy(temp)
            self.rets.append(temp)
            print('rets',self.rets)
            for i in range(i,len(nums)):
                print('internal i is',i)
                print('appending to tmp is',nums[i])
                temp.append(nums[i])
                dfs(nums,temp,i+1)
                print('pop')
                temp.pop()
                print('after pop',temp)
        dfs(nums,[],0)
        return self.rets

class solution3:
    def subsets(self,nums):
        rets=[]
        self.dfs(nums,0,[],rets)
        return rets
    def dfs(self,nums,index,path,res):
        rests.append(path)
        print(rets)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,path+[nums[i]],res)

s = Solution2()
nums=[1,2,3]

rests = s.subsets(nums)
print(rests)
