class Solution:
    '''print binary'''
    def prt_bi(self,n):
        self.ret=[]
        self.dfs(n,'')
        return self.ret
    def dfs(self,i,prefix):
        if i==0:
            self.ret.append(prefix)

            return

        self.dfs(i-1,prefix+'0')
        self.dfs(i-1,prefix+'1')
import copy
class Solution2:
    '''print binary'''
    def prt_bi(self,n):
        #self.ret=[]
        return self.dfs(n,'')
        #return self.ret
    def dfs(self,i,prefix):
        if i==0:
            #self.ret.append(prefix)
            print('i equals 0,the prefix is',prefix)
            #why return none !!
            return prefix
            #return self.ret
        #prefix = copy.deepcopy(prefix)
        #print(i)
        #print(prefix)
        self.dfs(i-1,prefix+'0')
        self.dfs(i-1,prefix+'1')

s=Solution()
import pdb
pdb.set_trace()
print(s.prt_bi(2))
