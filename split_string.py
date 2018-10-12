'''给一个字符串,你可以选择在一个字符或两个相邻字符之后拆分字符串,使字符串由仅一个字符或两个字符组成,输出所有可能的结果

样例
给一个字符串"123"
返回[["1","2","3"],["12","3"],["1","23"]]'''

import copy


def test_i(n):
    def printi(n,i):
        for idx in range(i,n):
            print(idx)
            printi(n,idx+1)
            print('pop')
    printi(n,0)

test_i(3)

'''the important thing is,1st figiure out how to draw the tree,2nd,how many options
for the combination:for i in range(len(nums)),or for i in range(2)'''

class cutStringSolution:
    def subsets(self,s):
        ret=[]
        self.dfs(ret,[],s)
        return ret

    def dfs(self,result,path,s):
        if s=='':
            result.append(path[:])
            return

        for i in range(2):
            if i<=len(s[:i+1])-1:
                path.append(s[:i+1])
                self.dfs(result,path,s[i+1:])
                path.pop()


s=cutStringSolution()
print(s.subsets('1234'))
