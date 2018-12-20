'''滚动数组
W for total weight/volumn limit
i for Ith element
rule:
#
if Weight[i]>W:
    #don't add in Ith element
    Value[i,w]=Value[i-1,w]
else:
    #add in,max the current max and the Ith elements' value + depart the Ith weights'
    #best choice
    Value[i,w]=max(V[i-1,w],Value[i]+Value[i-1,w-wt[i]])
#notes1:Beacause Value[i-1,w] will be required to compute anyway, so Value[i-1,w]
clause out the second loop
notes2: Beacause the DP Matrix row i only depend on the last row i-1,
so, to decrease the space,only two row rolling arrays,not full n*m matrix
will satisfy
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        n = len(A)

        dp = [[0] * (m + 1), [0] * (m + 1)]
        for i in range(1, n + 1):
            dp[i % 2][0] = 0
            for j in range(1, m + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if A[i - 1] <= j:
                    #注意这里A的下标i-1，V的下标都是i-1
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - A[i - 1]] + V[i-1])
        return dp[n % 2][m]
