[题目链接](https://leetcode-cn.com/problems/implement-trie-prefix-tree/submissions/)
### 题目分析
此题的关键在于理解字典树的数据结构，字典树每一个结点下面有26个指针，分别对应'a'-'z'字母，当插入时，我们首先检查对应字母的指针是否为空，为空就新建结点将其挂载父节点的下面，注意我们要设置一个成员变量，来判断当前的节点是不是单词的最后一个字母所对应的节点，代码如下：
```Python
class TrieNode:
    def __init__(self,isWord=False):
        self.isWord = isWord
        self.trie = [None for i in range(26)]
class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pcur = self.root
        for i in range(len(word)):
            if pcur.trie[ord(word[i])-ord('a')] is None:
                pcur.trie[ord(word[i])-ord('a')] = TrieNode() 
            if i == len(word)-1:
                pcur.trie[ord(word[i])-ord('a')].isWord = True            
            pcur = pcur.trie[ord(word[i])-ord('a')]                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pcur = self.root
        for i in range(len(word)):
            if pcur.trie[ord(word[i])-ord('a')] is None:
                return False
            pcur = pcur.trie[ord(word[i])-ord('a')]
        if pcur.isWord == True:
            return True
        return False
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pcur = self.root
        for i in range(len(prefix)):
            if pcur.trie[ord(prefix[i])-ord('a')] is None:
                return False
            pcur = pcur.trie[ord(prefix[i])-ord('a')]
        return True
```
