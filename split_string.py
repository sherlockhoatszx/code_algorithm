'''给一个字符串,你可以选择在一个字符或两个相邻字符之后拆分字符串,使字符串由仅一个字符或两个字符组成,输出所有可能的结果

样例
给一个字符串"123"
返回[["1","2","3"],["12","3"],["1","23"]]'''

import copy
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        ret=[]
        sp_list=[x for x in s]
        ret.append(sp_list)
        for idx,ch in enumerate(sp_list):
            if idx+1 == len(sp_list):
                break
            cmb_str = ch+sp_list[idx+1]
            temp_list = copy.deepcopy(sp_list)
            temp_list[idx+1]=cmb_str
            temp_list.pop(idx)
            ret.append(temp_list)

        return ret
