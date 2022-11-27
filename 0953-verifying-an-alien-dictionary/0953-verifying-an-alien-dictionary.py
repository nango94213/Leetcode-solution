class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(order):
            dic[v] = i
        
        for i in range(len(words)-1):
            j = 0
            while j < len(words[i]):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if dic[words[i][j]] < dic[words[i+1][j]]:
                        break
                    else:
                        return False
                j += 1
        return True
                