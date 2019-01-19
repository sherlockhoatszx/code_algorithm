#add and search word data structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node = node.children[c]

        node.is_word=True
