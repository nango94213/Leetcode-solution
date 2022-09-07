class Solution:
    def numberOfWays(self, s: str) -> int:
        
        dp = {'0': 0, '01': 0, '010': 0, '1': 0, '10': 0, '101': 0}
        
        for c in s:
            if c == '0':
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            
            if c == '1':
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
        
        return dp['101'] + dp['010']