'''给出一个由小写字母组成的矩阵和一个字典。找出所有同时在字典和矩阵中出现的单词。一个单词可
以从矩阵中的任意位置开始，可以向左/右/上/下四个相邻方向移动。一个字母在一个单词中只能被使用一次。且字典中不存在重复单词'''
'''There were 2 way to implement it.Using Trie or Hash set .'''
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.word=None

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def add(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()

            node = node.children[c]

        node.is_word=True
        node.word=word

    def find(self,word):
        node=self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []

        trie = Trie()
        for word in words:
            trie.add(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(
                    board,
                    i,
                    j,
                    trie.root.children.get(c),
                    set([(i, j)]),
                    result,
                )

        return list(result)

    def search(self, board, x, y, node, visited, result):
        if node is None:
            return

        if node.is_word:
            result.add(node.word)

        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y

            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue

            visited.add((x_, y_))
            self.search(
                board,
                x_,
                y_,
                node.children.get(board[x_][y_]),
                visited,
                result,
            )
            visited.remove((x_, y_))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
#todo: use the hash set to implement it again. and compare them
