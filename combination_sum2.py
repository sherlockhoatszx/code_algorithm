class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here

        num=sorted(list(num))
        results=[]
        combination=[]

        self.dfs(num,target,combination,0,results)

        return results

    def dfs(self,num,target,combination,start_index,results):

        if target==0:
            results.append(list(combination))
            return

        for i in range(start_index,len(num)):
            if i!=start_index and num[i]==num[i-1]:
                continue

            if target<num[i]:
                return

            combination.append(num[i])

            self.dfs(num,target-num[i],combination,i+1,results)
            combination.pop()


class Solution2:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
        self.ans, tmp, use = [], [], [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans
    def dfs(self, can, target, p, now, tmp, use):
        if now == target:
            self.ans.append(tmp[:])
            return
        for i in range(p, len(can)):
            if now + can[i] <= target and (i == 0 or can[i] != can[i-1] or use[i-1] == 1):
                tmp.append(can[i])
                use[i] = 1
                self.dfs(can, target, i+1, now + can[i], tmp, use)
                tmp.pop()
                use[i] = 0


'''notes,solution is based on combination_sum and amended a little
solution2 is a new method'''
