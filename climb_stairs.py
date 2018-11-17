
class Solution:
    """
    @param n: An integer
    @return: An integer
    step is 1 or 2
    """

    def climbStairs(self, n):
        # naive version 1
        if n<=1:
            return n
        last,lastlast,now=1,1,0
        for i in range(2,n+1):
            now=last+lastlast
            lastlast=last
            last=now

        return now

    def climbStairs2(self,n):
        '''version2,prons:demonstrate the road map
        cons:'''
        if n==0:
            return 0
        self.rets=[-1 for _ in range(n+1)]
        self.helper(n)
        return self.rets[n]

    def helper(self,x):
        if self.rets[x]!=-1:
            return
        if x==0 or x==1:
            self.rets[x]=1
        self.helper(x-1)
        self.helper(x-2)
        self.rets[x]=self.rets[x-1]+self.rets[x-2]


    def climbStairs3(self, n):
        # write your code here
        if n == 0:
            return 0
        if n <= 2:
            return n
        result=[1,2]
        for i in range(n-2):
            result.append(result[-2]+result[-1])
        return result[-1]
