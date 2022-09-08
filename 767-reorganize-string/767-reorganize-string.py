class Solution:
    def reorganizeString(self, s: str) -> str:
        c=[(-value,key) for key,value in Counter(s).items()]
        heapq.heapify(c)
        res=[]
        pre_a,pre_b=0,''
        while c:
            a,b=heapq.heappop(c)
            print((a,b))
            res.append(b)
            if pre_a<0:
                heapq.heappush(c,(pre_a,pre_b))
            a+=1
            pre_a,pre_b=a,b
        print(res)
        return '' if len(res)!=len(s) else ''.join(res)