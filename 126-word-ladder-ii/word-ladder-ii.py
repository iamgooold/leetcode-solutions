from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(set)
            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            next_level[new_word].add(word)
                            if new_word == endWord:
                                found = True

            level = next_level
            for w, p_set in next_level.items():
                parents[w].extend(p_set)

        if not found:
            return []

        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [word])

        backtrack(endWord, [])
        return res