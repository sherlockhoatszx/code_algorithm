class Solution:
    """
    @param s: a string
    @return: an integer
    """
    @classmethod
    def lengthOfLongestSubstring(cls, s):
        # two pointers,and use set([]) to store results
        unique_chars=set([])
        j=0
        ans=0
        for i in range(len(s)):
            while j<len(s) and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            ans = max(ans,j-i)
            unique_chars.remove(s[i])

        return ans

print(Solution.lengthOfLongestSubstring('abcbcdb'))
