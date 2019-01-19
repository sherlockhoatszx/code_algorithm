class Solution:
    # @param num, a list of integer
    # @return an integer
    '''O(nlogn)
    use classmethod cause I want to save typeing...normaly it should be
    instance's method'''
    @classmethod
    def longestConsecutive1(cls, num):
        num.sort()
        l = num[0]
        ans = 1
        tmp = 1
        for n in num:
            if(n - l == 0):
                continue;
            elif(n - l == 1):
                tmp += 1
            else:
                if tmp > ans:
                    ans = tmp
                tmp = 1
            l = n
        if tmp > ans:
            ans = tmp
        return ans

    ''''O(n),dict to store the element and x+1 x-1 check if in'''
    @classmethod
    def longestConsecutive2(cls, num):

        dict={}

        for x in num:
            dict[x] = 1

        ans = 0

        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len

        return ans

testNums = [100, 4, 200, 1, 3, 2]
print(Solution.longestConsecutive2(testNums))
