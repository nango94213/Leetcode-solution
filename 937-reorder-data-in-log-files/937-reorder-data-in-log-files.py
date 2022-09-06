class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def order(log):
            first, second = log.split(' ', 1)
            
            return [2] if second[0].isnumeric() else [1, second, first]
        
        logs.sort(key=order)
        return logs
        