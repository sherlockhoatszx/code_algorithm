class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        '''version1,naive,show the insitution but the o time is very big'''

        if m<0 or n<0:
            return 0
        if m==1 and n==1:
            return 1
        f=[[0 for _ in range(n+1)]for _ in range(m+1)]

        if f[m][n]>0:
            return f[m][n]

        left_paths=self.uniquePaths(m-1,n)
        top_paths=self.uniquePaths(m,n-1)

        f[m][n]=left_paths+top_paths

        return f[m][n]

    def c(self, m, n):
        mp = {}
        for i in range(m):
            for j in range(n):
                if(i == 0 or j == 0):
                    mp[(i, j)] = 1
                else:
                    mp[(i, j)] = mp[(i - 1, j)] + mp[(i, j - 1)]
        return mp[(m - 1, n - 1)]

    def uniquePaths2(self, m, n):
        '''version2'''
        return self.c(m, n)

    def uniquePaths3(self, m, n):
        '''version3'''
        import pdb
        pdb.set_trace()
        if m<=0 or n<=0:
            return 0
        paths=[0 for _ in range(n)]
        paths[0]=1

        for i in range(m):
            for j in range(1,n):
                paths[j]=paths[j-1]+paths[j]

        return paths[n-1]






s=Solution()
print(s.uniquePaths3(3,3))
