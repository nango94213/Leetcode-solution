class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        word_set = set([''])
        longest_word = ''
        
        for w in words:
            if w[:-1] in word_set:
                word_set.add(w)
                
                if len(w) > len(longest_word):
                    longest_word = w
                    
        return longest_word
        