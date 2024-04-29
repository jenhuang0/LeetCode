class TrieNode:
    def __init__(self):
        # array to store links to child nodes
        self.children = [None] * 26
        # flag to indicate if the node represents the end of a word
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # initialize the Trie with an empty root node
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        # start traversal from the root node
        for c in word:
            # calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # create a new node if the child does not exist
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            # move to the child node
            curr = curr.children[i]
        # mark the last node as the end of the inserted word
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        # start traversal from the root node
        for c in word:
            # calculate the index of the character in the children array
            i = ord(c) - ord("a")
            # return False if any character is missing in the trie
            if curr.children[i] == None:
                return False
            # move to the child node
            curr = curr.children[i]
        #return True if the lst node represents the end of a word
        return curr.isWord
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        # start traversal from the root node
        for c in prefix:
            i = ord(c) - ord("a")
            # return False if any charater is missing in the trie
            if curr.children[i] == None:
                return False
            # move to the child node
            curr = curr.children[i]
        # return True if the prefix exists in the trie
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)