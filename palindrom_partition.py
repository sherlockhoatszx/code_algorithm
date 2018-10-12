'''change based on the split string code and add the is_palidrom function'''

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        ret=[]
        self.dfs(ret,[],s)
        return ret

    def dfs(self,ret,stringList,s):
        if len(s)==0:
            ret.append(stringList)
            return
        for i in range(1,len(s)+1):
            prefix=s[:i]
            if self.ispalindrom(prefix):
                self.dfs(ret,stringList+[prefix],s[i:])

    def ispalindrom(self,s):
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:

                return False
            i+=1
            j-=1
        return True
    def is_palindrom(self,s):
        #this is more pythonic but doesn't help understand the algorithms
        return s==s[::-1]
