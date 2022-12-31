class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        default = 'abcdefghijklmnopqrstuvwxyz'
        j = 0
        dic = {}
        for i in range(len(key)):
   
            if key[i] != ' ' and key[i] not in dic:
                dic[key[i]] = default[j]
                j += 1
        dic[' '] = ' '
        res = ''
        for c in message:
            res += dic[c]
        return res