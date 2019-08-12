class Solution:
    def wordDiff(self,word1,word2):
        count = 0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                count+=1
        return count
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not endWord in wordList:
            return 0
        visited = set(wordList)
        myQueue = [beginWord]
        step=1
        lastWord,nextWord = beginWord,beginWord
        while len(myQueue)!=0:
            element = myQueue[0]
            myQueue.pop(0)
            if element == endWord:
                return step
            for j in range(len(element)):
                for index in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = element[:j]+index+element[j+1:]
                    if new_word in visited:
                        myQueue.append(new_word)
                        nextWord = new_word
                        visited.remove(new_word)
            if element == lastWord:
                step+=1
                lastWord = nextWord
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not endWord in wordList:
            return 0
        visited = set(wordList)
        myQueue = [beginWord]
        step = 1
        lastWord, nextWord = beginWord, beginWord
        while len(myQueue) != 0:
            element = myQueue[0]
            myQueue.pop(0)
            if element == endWord:
                return step
            for word in wordList:
                if word in visited and  self.wordDiff(element,word)==1:
                    myQueue.append(word)
                    nextWord = word
                    visited.remove(word)
            if element == lastWord:
                step += 1
                lastWord = nextWord
        return 0

obj = Solution()
print(obj.ladderLength('hit','cog',['hot','dot','dog','lot','log','cog']))