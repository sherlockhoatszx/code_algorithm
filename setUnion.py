class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def find(self, x, f):
        if x != f[x]:
            f[x] = self.find(f[x], f)
        return f[x]


    def setUnion(self, sets):
        # Write your code here
        f = {}
        for s in sets:
            first = s[0]
            for x in s:
                if not f.has_key(x):
                    f[x] = first
                else:
                    fFirst = self.find(first, f)
                    fx = self.find(x, f)
                    if fx != fFirst:
                        f[fx] = fFirst
        for s in sets:
            for x in s:
                self.find(x, f)
        hashSet = {}
        n = 0
        for val in f.values():
            if not hashSet.has_key(val):
                n += 1
                hashSet[val] = val
        return n
