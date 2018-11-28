class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):

        if nums is None:
            return

        results=[]
        permutation=[]
        visited=[0]*len(nums)

        self.dfs(nums,results,permutation,visited)
        return results

    def dfs(self,nums,results,permutations,visited):

        if len(nums)==len(permutations):
            #attention, permutation copy here
            
            permutations=permutations[:]

            print(permutations)
            results.append(permutations)
            return

        for i in range(0,len(nums)):
            print('i is',i)

            if visited[i]==1:
                continue
            permutations.append(nums[i])
            print(permutations)

            visited[i]=1

            self.dfs(nums,results,permutations,visited)
            print('dfs end')
            visited[i]=0
            permutations.pop()


s=Solution()
print(s.permute([1]))


class Solution2:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        #
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

        if nums is None:
            return []

        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result
