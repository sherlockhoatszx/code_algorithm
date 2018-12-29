class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        # 滚动哈西
        seed = 33
        mod = 1000000007
        ans = 0
        mxLen = -1
        aHash = []
        sHash = []
        base = []
        for i in a:
            ans = 1
            mxLen = max(mxLen, len(i))
            for j in i:
                ans = (ans * seed + ord(j) - ord('a')) % mod
            aHash.append(ans)
        ans = 1
        sHash.append(ans)
        mxLen = max(mxLen, len(s))
        for i in s:
            ans = (ans * seed + ord(i) - ord('a')) % mod
            sHash.append(ans)
        ans = 1
        base.append(ans)
        for i in range(mxLen):
            ans = ans * seed % mod
            base.append(ans)
        ret = [i for i in s]
        i = 0
        while i < len(s):
            maxLen = -1
            index = 0
            for j in range(len(a)):
                lenaj = len(a[j])
                l = i + 1
                r = i + lenaj
                if r > len(s):
                    continue
                sHashValue = (sHash[r] - base[r - l + 1] * sHash[l - 1] % mod + mod) % mod
                aHashValue = (aHash[j] - base[lenaj] + mod) % mod
                if sHashValue == aHashValue and lenaj > maxLen:
                    maxLen = lenaj
                    index = j
            if maxLen != -1:
                for j in range(maxLen):
                    ret[i + j] = b[index][j]
                i = i + maxLen - 1
            i = i + 1
        return "".join(ret)
