class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = {}
        end = True
        for i, v in enumerate(words):
            current = trie
            for c in v:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current[end] = i
        
        stack = list(trie.values())
        
        res = ''
        while stack:
            now = stack.pop()
            if end in now:
                word = words[now[end]]
                if len(word) > len(res) or len(word) == len(res) and word < res:
                    res = word
                
                stack += [now[i] for i in now if i != end]
        
        return res
            