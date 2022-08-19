import collections
class Leaderboard:

    def __init__(self):
        self.dic = collections.defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] += score

    def top(self, K: int) -> int:
        allScore = sorted(self.dic.values(), reverse=True)
        
        return sum(allScore[:K])
        

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)