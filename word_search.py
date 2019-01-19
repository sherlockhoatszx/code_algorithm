class Solution:
    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # edge case
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False
        # edge case
        if len(word) == 0:
            return True

        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if self.dfs(board, x, y, 0, word):
                        return True
        return False


    def dfs(self, board, x , y, index, word):
        # stopping case(base case)
        if index == len(word):
            return True
        # stopping case(base case)
        if not self.is_bound(x, y, board) or board[x][y] != word[index]:
            return False

        board[x][y] = '#'
        is_finded = \
        self.dfs(board, x - 1, y, index + 1, word) or \
        self.dfs(board, x + 1, y, index + 1, word) or \
        self.dfs(board, x, y - 1, index + 1, word) or \
        self.dfs(board, x, y + 1, index + 1, word)
        board[x][y] = word[index]

        return is_finded


    def is_bound(self, x, y, board):
        m, n = len(board), len(board[0])
        return 0 <= x <= m - 1 and 0 <= y <= n - 1
