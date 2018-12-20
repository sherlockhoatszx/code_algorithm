'''在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]'''



class Solution:
    '''2d dynamic programming'''

    def backPack(self, m, A):
        n = len(A)
        f = [[False] * (m + 1) for _ in range(n + 1)]

        f[0][0] = True
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = f[i - 1][j] or f[i - 1][j - A[i - 1]]
                else:
                    f[i][j] = f[i - 1][j]

        for i in range(m, -1, -1):
            if f[n][i]:
                return i
        return 0

class Solution2:
    '''1d array dp'''
    def backPack(self,m,A):
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >= 0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1

        return ans

if __name__=='__main__':
    tw=10
    items=[3,4,8,5]
    pack=Solution2()
    print(pack.backPack(tw,items))
