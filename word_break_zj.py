'''a DP problem,using depth first search with Memoization
search prefix and recursive search the rest
wordBreak('catsanddog')=in_dict('catsanddog')
U combine('c',wordBreak('atsanddog'))
U combine('ca',wordbreak('tsanddog'))
U combine('cat',wordbreak('sanddog'))
    U combine('s',wordBreak('anddog'))
    U combine('sa',wordBreak('nddog'))
    ...
    U combine('sand',wordBreak('dogs'))
        memo{'dogs':'dogs'}
        partitions=dogs
        return ['dogs']
    #call stack pop
    memo{'sanddogs':['sand','dogs']}
    return ['sand','dogs']
U combine('cats',wordBreak('anddog'))
...


=['cat sand dog','cats and dog']
'''
#create by hezhijian
#top down memo here, bottom up(not implemented) also works
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        rets = self.dfs(s, wordDict, {})
        #add the elements with double quotation marks
        dqm_rets = [['"'+wd+'"' for wd in ret.split(" ") ]for ret in rets]

        ret_str=''
        for ret in dqm_rets:
            #comma join element and change line in the end
            sub_s = ','.join(ret)+'\n'
            ret_str += sub_s

        return ret_str

    # find out all possible segment ways
    def dfs(self, s, wordDict, memo):
        #Memoization to save dupliacate computation results to decrease O(t)
        #such as {'sanddog': ['sand dog'], 'dog': ['dog']}
        import pdb
        #pdb.set_trace()
        if s in memo:
            return memo[s]
        #corner case judge
        if len(s) == 0:
            return []
        #to save temp segmented words
        partitions = []
        #traverse the string from s[0]
        for i in range(1, len(s)):
            prefix = s[:i]
            #judge if break
            if prefix not in wordDict:
                continue
            #depth first search
            #sub_partions is backwards partition's return value from call stack pop
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            pdb.set_trace()
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
        #judge if s in word dictionary
        if s in wordDict:
            partitions.append(s)
        #save the possible segmentation in memo(a hash dict)
        memo[s] = partitions
        #return partition per dfs
        return partitions

if __name__=="__main__":
    test_s = "长春市长春节致辞好"
    dic = {"长","长春","长春市","市长","春节","致辞"}

    wb = Solution()
    print(wb.wordBreak(test_s,dic))
