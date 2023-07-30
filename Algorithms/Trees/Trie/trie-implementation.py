## A Ready-to-use implementation of trie in python ##

class Trie:
    class Node:
        def __init__(self):
            self.letters = {}
            self.endsHere = False

        def add(self, char):
            self.letters[char] = Trie.Node()

        def contains(self, char):
            return char in self.letters

        def get(self, char):
            return self.letters[char]

        def end(self):
            self.endsHere = True

        def isEndsHere(self):
            return self.endsHere

    def __init__(self):
        self.head = self.Node()

    def addWord(self, word):
        node = self.head
        for char in word:
            if not node.contains(char):
                node.add(char)
            node = node.get(char)
        node.end()

    def search(self, word) -> bool:
        node = self.head
        for char in word:
            if not node.contains(char): return False
            node = node.get(char)
        return node.isEndsHere()