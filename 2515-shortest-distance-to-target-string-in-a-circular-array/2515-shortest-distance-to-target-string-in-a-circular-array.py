class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        i = startIndex
        j = startIndex
        step = 0
        while words[i] != target and words[j] != target:
            i = (i - 1 + n) % n
            j = (j + 1) % n
            step += 1
            if step > n:
                return -1
        return step
        