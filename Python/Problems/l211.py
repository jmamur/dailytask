class TrieNode:
    def __init__(self):
        self.IsEnd = False
        self.children = dict()
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()

            curr_node = curr_node.children[c] 
        curr_node.IsEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr_node = self.root

        for c in word:
            if c in curr_node.children:
                curr_node = curr_node.children[c]
            elif c is ".":
                continue
            else:
                return False
            
            
        return curr_node.IsEnd
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
word = WordDictionary()
word.addWord("bad")
word.addWord("dad")
word.addWord("mad")
print(word.search("pad"))
print(word.search(".ad"))
print(word.search("b.."))