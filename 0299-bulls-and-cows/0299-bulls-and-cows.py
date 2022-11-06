class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = Counter(secret)
        b = Counter(guess)
        first = 0
        for i in range(len(secret)):
            if  secret[i] == guess[i]:
                first += 1
                a[secret[i]] -= 1
                b[secret[i]] -= 1
        
        second = 0
        
        for k in a:
            if  k in b:
                second += min(a[k], b[k])
        
        return str(first) + 'A' + str(second) + 'B'