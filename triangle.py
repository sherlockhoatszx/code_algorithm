class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    #version 1
    def minimumTotal(self, triangle):
        # bottom up more easy

        if triangle is None or len(triangle)==0:
            return -1

        if triangle[0] is None or len(triangle[0])==0:
            return -1

        n=len(triangle)
        f=[[-1 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            f[n-1][i]=triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                f[i][j]=min((f[i+1][j],f[i+1][j+1]))+triangle[i][j]

        return f[0][0]


    #version2

    def minimumTotal2(self, triangle):
        #  up down
        res=[triangle[0]]
        N = len(triangle)
        for i in range(1,len(triangle)):
            res.append([])
            for j in range(len(triangle[i])):
                if j-1>=0 and j< len(triangle[i-1]):
                    res[i].append(min(res[i-1][j-1],res[i-1][j])+triangle[i][j])
                elif j-1>=0:
                    res[i].append(res[i-1][j-1]+triangle[i][j])
                else:
                    res[i].append(res[i-1][j]+triangle[i][j])

        minvalue = min(res[N-1])
        return minvalue

    #version3

    def minimumTotal3(self, triangle):
        #bottom up

        if triangle is None  or len(triangle)==0:
            return -1

        if triangle is None or len(triangle[0])==0:
            return -1

        res=[triangle[-1]]

        n=len(triangle)

        for i in range(1,n):
            res.append([])
            for j in range(n-i):
                res[i].append(min(res[i-1][j],res[i-1][j+1])+triangle[n-1-i][j])

        return res[-1][-1]


    def minimumTotal4(self, triangle):
        #  1d list,O(n**2)time,O(n) space
        if triangle is None  or len(triangle)==0:
            return -1

        if triangle is None or len(triangle[0])==0:
            return -1

        n=len(triangle)
        dp=[triangle[n-1][i] for i in range(n)]

        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                dp[j]=triangle[i][j]+min(dp[j],dp[j+1])

        return dp[0]
