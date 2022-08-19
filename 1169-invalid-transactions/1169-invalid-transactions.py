
import collections
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        seen = collections.defaultdict(list)
        res = []
        
        for t in transactions:
            
            info = t.split(',')
            seen[info[0]].append((int(info[1]), info[3]))
        
        
        for t in transactions:
            
            info = t.split(',')
            
            
            if int(info[2]) > 1000:
                res.append(t)
                continue
                
                
            for item in seen[info[0]]:
                    if abs(item[0]-int(info[1])) <= 60 and item[1] != info[3]:
                        res.append(t)
                        break
                
            
     
        return res