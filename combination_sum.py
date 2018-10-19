class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates=sorted(list(set(candidates)))
        results = []
        self.dfs(candidates,target,0,[],results)
        return results

    def dfs(self,candidates,target,start,combination,results):
        if target ==0:
            results.append(list(combination))
            return

        for i in range(start,len(candidates)):
            if target<candidates[i]:
                return # in the for loop
            combination.append(candidates[i])
            #self.dfs(candidates,target-candidates[i],i,combination.append(candidates[i]),results) #make mistake here,cause list.append() excuted inplace,no return
            self.dfs(candidates,target-candidates[i],i,combination,results)

            combination.pop()

'''notes:
1,Target update its value every recursion call, target_star=target-new_added_ele
2,For loop to control the index move forward
3,in the for loop,every call the i remain the same,that is to say,the same index could keep calling
multiple times until the target < new_add_element
4,return and pop to move stack function to make for loop continue'''
