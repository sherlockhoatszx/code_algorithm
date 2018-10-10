'''recursion and backtracking'''

class Solution:
    '''like inorder traverse'''

    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            print('appending array is',S)

            return
        print(S)
        print(index)

        #self.search(nums, S, index + 1)
        self.search(nums, S + [nums[index]], index + 1)
        print('right child')
        self.search(nums, S, index + 1)

    def subsets(self, nums):
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results
import copy
class Solution2:
    '''choose subtree''''
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
                print('after pop',temp)#backtracking
        dfs(nums,[],0)
        return self.rets


class Solution3:
    '''choose subtree，based on Solution2, use deepcopy in the for loop,then
    the pop will not be needed''''
    def subsets(self,nums):
        self.rets=[]
        def dfs(nums,temp,i):
            print(i)
            print('temp list is',temp)
            #temp=copy.copy(temp)
            self.rets.append(temp)
            print('rets',self.rets)
            for i in range(i,len(nums)):
                print('internal i is',i)
                print('appending to tmp is',nums[i])
                newset = copy.deepcopy(temp)
                newset.append(nums[i])
                dfs(nums,newset,i+1)
                #print('pop')
                #temp.pop()
                #print('after pop',temp)#backtracking
        dfs(nums,[],0)
        return self.rets

class solution4:
    def subsets(self,nums):
        rets=[]
        self.dfs(nums,0,[],rets)
        return rets
    def dfs(self,nums,index,path,res):
        rests.append(path)
        print(rets)
        for i in range(index,len(nums)):
            self.dfs(nums,i+1,path+[nums[i]],res)
#bfs
s = Solution()
nums=[1,2,3]

rests = s.subsets(nums)
print(rests)
