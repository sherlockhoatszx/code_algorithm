class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange0(self, coins, amount):
        # naive version
        import sys
        if amount==0:
            return 0
        f=[[sys.maxsize for _ in range(amount+1)] for _ in range(len(coins)+1)]

        f[-1][0]=0

        for i in range(len(coins)-1,-1,-1):
            for j in range(amount+1):
                f[i][j]=f[i+1][j]
                maxK=j//coins[i]+1

                for k in range(1,maxK):
                    prev=f[i+1][j-k*coins[i]]

                    if prev<sys.maxsize:
                        f[i][j]=min(f[i][j],prev+k)
        #print(f)

        psob=min([row[-1] for row in f])
        return psob


    def coinChange1(self, coins, amount):
        # improve big o version，O(NM)time
        import sys
        if amount==0:
            return 0
        f=[[sys.maxsize for _ in range(amount+1)] for _ in range(len(coins)+1)]

        f[-1][0]=0

        for i in range(len(coins)-1,-1,-1):
            for j in range(amount+1):
                f[i][j]=f[i+1][j]
                if j >= coins[i]:

                    prev=f[i][j-coins[i]]

                    if prev<sys.maxsize:
                        f[i][j]=min(f[i][j],prev+1)

        psob=min([row[-1] for row in f])

        if posb<sys.maxsize:

            return posb

        return -1

    def coinChange2(self,coins,amount):

        #improve space complexity,o(nm) time and o(m) space
        import sys
        g=[sys.maxsize for _ in range(amount+1)]
        g[0]=0

        for i in range(len(coins)-1,-1,-1):
            for j in range(amount+1):
                if j>=coins[i]:
                    prev = g[j-coins[i]]

                    if prev<sys.maxsize:
                        g[j]=min(g[j],prev+1)
        if g[-1]<sys.maxsize:
            return g[-1]

        return -1





s=Solution()

print(s.coinChange2([1,2,5],11))
