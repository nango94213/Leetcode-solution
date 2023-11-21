class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = collections.defaultdict(list)
        
        def key(word):
            count = [0] * 26
            
            for c in word:
                count[ord(c)-ord('a')] += 1
    
            return str(count)
        
        for s in strs:
            dic[key(s)].append(s)
        
        return dic.values()
        