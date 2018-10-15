class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        self.rets=[]
        self.numbers=[i for i in range(1,n+1)]
        self.dfs(k,0,n)
        return self.rets

    def dfs(self,k,idx,n):

        for i in range(idx,n):
            if i+1 ==i+k:
                subsets=[self.numbers[idx]]
                self.rets.append(subsets)
                break

            elif i<=n-k:

                subsets=[self.numbers[idx]]+self.numbers[i+1:i+k]

                self.rets.append(subsets)
        if idx <=n:
            self.dfs(k,idx+1,n)


s=Solution()
import pdb
pdb.set_trace()
print(s.combine(2,1))
print(s.combine(5,3))#did not pass
print(s.combine(4,2))#pass
