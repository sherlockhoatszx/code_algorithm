class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            f[i][0] = i
        for j in range(m + 1):
            f[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j] + 1, f[i][j - 1] + 1)
                    # equivalent to f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1

        return f[n][m]


    def minDistance2(self, word1, word2):
        n, m = len(word1), len(word2)
        f = [[0] * (m + 1), [0] * (m + 1)]

        for j in range(m + 1):
            f[0][j] = j

        for i in range(1, n + 1):
            f[i % 2][0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i % 2][j] = min(f[(i - 1) % 2][j - 1], f[(i - 1) % 2][j] + 1, f[i % 2][j - 1] + 1)
                    # equivalent to f[i % 2][j] = f[(i - 1) % 2][j - 1]
                else:
                    f[i % 2][j] = min(f[(i - 1) % 2][j - 1], f[(i - 1) % 2][j], f[i % 2][j - 1]) + 1

        return f[n % 2][m]
