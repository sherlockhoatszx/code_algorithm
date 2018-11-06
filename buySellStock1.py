class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    condition:only one time transition
    """
    def maxProfit(self, prices):

        import sys
        if prices is None or len(prices)==0:
            return 0
        minp,maxp=0,-sys.maxsize
        total=0
        for i in range(1,len(prices)):
            pft=prices[i]-prices[i-1]
            total=total+pft
            maxp=max(maxp,total-minp)
            minp=min(minp,total)

        return maxp if maxp>=0 else 0
