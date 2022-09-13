class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        count = list(Counter(s).values())

        
        sorted_count = sorted(count, reverse=True)
        res = 0
        digit = 0

        for i, v in enumerate(sorted_count):
            if i % 9 == 0:
                print(i)
                digit += 1
         
            res += digit * v
            
        return res
                