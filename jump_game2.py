class Solution:
    def jump(self,A):
        '''naive version'''
        if not A:
            return -1

        n=len(A)

        import sys
        self.dp=[sys.maxsize]*n

        self.dp[0]=0

        for i in range(n):
            step=A[i]
            self.helper(i,step)

        return self.dp[n-1]

    def helper(self,idx,step):
        for i in range(idx,min(idx+step+1,len(self.dp))):
            self.dp[i]=min(self.dp[i],self.dp[idx]+1)






class Solution:
    def jump(self,A):
        '''dp version'''
        if not A:
            return -1

        n=len(A)

        import sys
        dp=[sys.maxsize]*n

        dp[0]=0

        for i in range(n):
            for prev in range(i):
                if prev+A[prev]>=i and dp[prev]!=sys.maxsize:
                    dp[i]=min(dp[i],dp[prev]+1)

        return dp[n-1]

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        p = [0]
        for i in range(len(A) - 1):
            while(i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)
        return p[-1]
