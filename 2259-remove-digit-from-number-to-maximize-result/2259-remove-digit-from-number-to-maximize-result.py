class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = -1
        for i in range(len(number)):
            if number[i] == digit:
                if i != len(number)-1 and number[i+1] > number[i]:
                    return number[:i] + number[i+1:]
                last = i
        if last == -1:
            last = len(number) - 1
        return number[:last] + number[last+1:]
        