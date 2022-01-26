class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        
        while l<r:
            mid=(l+r)//2
            total=0
            day=1
            for w in weights:
                if total+w>mid:
                    day+=1
                    total=w
                else:
                    total+=w
                
            if day>days:
                    l=mid+1
            else:
                    r=mid
        return l