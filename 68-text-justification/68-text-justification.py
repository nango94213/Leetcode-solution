class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, current, numbers = [], [], 0
        
        for w in words:
            if numbers + len(w) + len(current) > maxWidth:
                if len(current) == 1:
                    res.append(current[0]+' '*(maxWidth-numbers))
                else:
                    space = (maxWidth-numbers) // (len(current)-1)
                    extra_space = (maxWidth-numbers) % (len(current)-1)
                    
                    for i in range(extra_space):
                        current[i] += ' '
                    
                    res.append((space*' ').join(current))
                
                current, numbers = [], 0
            current.append(w)
            numbers += len(w)
        
        res.append(' '.join(current) + ' '*(maxWidth-numbers-(len(current)-1)))
        
        return res
                        
        