class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        default = 'abcdefghijklmnopqrstuvwxyz'
        j = 0
        dic = {}
        dic[' '] = ' '
        
        for k in key:
            if k not in dic:
                dic[k] = default[j]
                j += 1
        res = ''
        for c in message:
            res += dic[c]
        return res