from collections import defaultdict

class TrieNode:

	def __init__(self):
		self.isWord = False 
		self.children = defaultdict(TrieNode)


class Trie:

	def __init__(self):
		self.root = TrieNode()

	def insertWord(self, word):
		node = self.root
		for letter in word:
			node = node.children[letter]
		node.isWord = True

	def searchWord(self, word):
		node = self.root
		for letter in word:
			if letter not in node.children:
				return False
			node = node.children[letter]
		return node.isWord

	def searchPrefix(self, word):
		node = self.root
		for letter in word:
			if letter not in node.children:
				return False
			node = node.children[letter]
		return True


if __name__ == "__main__":

	t = Trie()
	t.insertWord("promoter")
	t.insertWord("programmer")
	t.insertWord("key")
	t.insertWord("keyword")

	print(t.searchWord("promoter"))
	print(t.searchWord("keys"))
	print(t.searchWord("pro"))

	print(t.searchPrefix("promoter"))
	print(t.searchPrefix("keys"))
	print(t.searchPrefix("pro"))