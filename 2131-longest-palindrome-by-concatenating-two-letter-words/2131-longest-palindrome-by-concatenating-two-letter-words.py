class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        seen = set()
        exist = False
        pair = 0
        for word in count:
                rev = word[::-1]
                if rev == word:
                    if count[word] % 2 == 1:
                        exist = True
                    pair += count[word] // 2
                        
                    
                else:
                    if word not in seen:
                        pair += min(count[word], count[rev])
                        seen.add(rev)


        return 4 * pair + exist * 2
                
                
        