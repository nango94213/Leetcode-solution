class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        for i in range(int(area**(0.5)), -1, -1):
            if area % i == 0:
                return [area//i , i]
        return [area, 1]
        