class Solution:
    '''print binary'''
    def prt_bi(self,n):
        self.ret=''
        self.dfs(n,'')
        return self.ret
    def dfs(self,i,prefix):
        if i==0:
            print('i equals 0,the prefix is',prefix)
            self.ret=self.ret+prefix

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


'''Why Solution2 is wrong

During the recursion, last call first return,and first call last return,
in Solution2,the final return is a recursion call,not the base case,so
the return is None
The scripts below demonstrate why'''

t = {}

def ex(x):
    global t
    if x > 1:
        x -= 1
        t[x] = ex(x)
    else:
        return x

ex(10)
print(t)

'''the output is {1: 1, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}'''
