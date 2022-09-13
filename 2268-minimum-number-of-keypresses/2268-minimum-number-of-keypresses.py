class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        count = list(Counter(s).items())
        dic = {}
        seen = 0
        
        sorted_count = sorted(count, key=lambda x: x[1], reverse=True)
        res = 0

        for k, v in sorted_count:
            if k not in dic:
                seen += 1
                if seen <= 9:
                    dic[k] = 1
                elif seen <= 18:
                    dic[k] = 2
                else:
                    dic[k] = 3
            
            res += dic[k] * v
            
        return res
                