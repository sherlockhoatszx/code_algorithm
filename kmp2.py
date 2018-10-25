class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            jj = ret[i - 1]
            while jj > 0 and pattern[jj] != pattern[i]:
                jj = ret[jj - 1]
            ret.append(jj + 1 if pattern[jj] == pattern[i] else jj)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, jj = self.partial(P), [], 0
        print(partial)
        for i in range(len(T)):
            while jj > 0 and T[i] != P[jj]:
                jj = partial[jj - 1]
            if T[i] == P[jj]: jj += 1
            if jj == len(P):
                ret.append(i - (jj - 1))
                jj = 0

        return ret

import pdb
pdb.set_trace()
kmp = KMP()
ret = kmp.search('ababbabababa','abab')
print(ret)
