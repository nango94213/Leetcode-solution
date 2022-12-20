class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i = 0
 
        players.sort()
        trainers.sort()
        
        res = 0
        
        for j in range(len(trainers)):
            if i < len(players) and trainers[j] >= players[i]:
                res += 1
                i += 1
        return res