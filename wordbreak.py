#dynamic programming
'''
solution1:TopDown,wordBreak('leetcode')=inDict('leetcode')
||wordBreak('l')&&inDict('eetcode')
||wordBreak('le')&&inDict('etcode')
....

solution2 TopDown+Memoization:
wordBreak('l')=False
wordBreak('le')=False
..
wordBreak('leet')=True
solution3:bottomup

solution3 Bottom up

1 Define subproblems
dp[i]:whether s[0...i-1]can be segmented
2,guess,the break point:number of choice O(i)orO(n)
3,dp[i]=dp[0]&&inDict(s[0..i-1])||dp[1]&&inDict(s[1..i-1])
corner case dp[0]=True time per problem o(i^2),
orgininal problem dp[n]

solution4 bottom up ,pre count the max length in the dictionary
j=i-1...max(0,i-maxlen),this is a pruning trick'''
#wordbreakI
class Solution:
    def wordBreak(self,s,dic):
        if len(dic)==0:
            return len(s)==0

        n = len(s)
        #dp Memoization
        f = [False]*(n+1)
        f[0]=True
        #for pruning
        maxLen=max([len(w) for w in dic])

        for i in range(1,n+1):
            for j in range(1,min(i,maxLen)+1):
                if not f[i-j]:
                    continue
                if s[i-j:i] in dic:
                    f[i]=True
                    break

        return f[n]
