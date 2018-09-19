class Solution:
    '''根据字符串的中心镜像轴来循环，注意for m in len(s),find_longP(m,m)是对char的循环
    ，而，find_longP(m,m+1)是基于char与char之间的中心轴来循环'''
    def __init__(self):
        self.longest=0
        self.start=0
    def longestPalindrome(self,s):
        if not s:
            return ""
        for m in range(len(s)):
            #m means the middle
            self.find_pld_range(s,m,m)
            self.find_pld_range(s,m,m+1)

        return s[self.start:self.start+self.longest]



    def find_pld_range(self,s,left,right):
        '''this function return the start and longest length value '''

        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right +=1
        if self.longest < right-left-1:
            self.longest = right-left-1
            self.start =left +1
test_str ='ABACCABB'
s = Solution()
pld = s.longestPalindrome(test_str)
print(pld)
