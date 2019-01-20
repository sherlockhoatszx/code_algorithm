class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        hash = {}
        n = len(s)
        j = 0
        longest = 0

        for i in range(n):
            while j < n and (len(hash) < k or len(hash) == k and s[j] in hash):
                hash[s[j]] = hash.get(s[j], 0) + 1
                j += 1

            # len(hash) must be smaller or equal to k after while
            longest = max(longest, j - i)

            if s[i] in hash:
                hash[s[i]] -= 1
                if hash[s[i]] == 0:
                    del hash[s[i]]

        return longest
