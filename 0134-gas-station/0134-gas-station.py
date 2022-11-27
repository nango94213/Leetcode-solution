class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        c = 0
        start = 0
        
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            c += gas[i] - cost[i]
            if c < 0:
                start = i + 1
                c = 0
        return start