class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = Counter(secret)
        b = Counter(guess)
        
        x = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
                a[secret[i]] -= 1
                b[secret[i]] -= 1
        y = 0
        for k in a:
            y += min(a[k], b[k])
        
        return str(x) + 'A' + str(y) + 'B'