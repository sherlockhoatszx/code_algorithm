class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares1(self, n):
        '''version1,dp'''
        dp = [n for _ in range(n+1)]
        for i in range(n+1):
            if i**2 <= n:
                dp[i**2] = 1
            j = 1
            while j**2 < i:
                dp[i] = min(dp[i], dp[i-j**2] + 1)
                j +=1
        return dp[n]

    def numSquares2(self, n):
        '''version2,math'''
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in xrange(n+1):
            temp = i * i
            if temp <= n:
                if int((n - temp)** 0.5 ) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3
