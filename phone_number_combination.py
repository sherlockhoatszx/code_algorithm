class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, '', results)

        return results

    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)
