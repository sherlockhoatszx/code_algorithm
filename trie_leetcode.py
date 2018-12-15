class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()

            node = node.children[c]

        node.is_word=True

    def find(self,word):
        node = self.root
        for c in word:
            node = node.children.get(c)

            if node is None:
                return None
        return node

    def search(self,word):

        node = self.find(word)

        return node is not None and node.is_word

    def startsWith(self,prefix):
        return self.find(prefix) is not None

if __name__=="__main__":
    tr=Trie()
    tr.insert('ab')
