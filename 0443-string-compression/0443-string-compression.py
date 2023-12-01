class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count=1
        i=1
        while i<len(chars):
            if chars[i]!=chars[i-1]:
                if count!=1:
                    chars[i-count:i]=[chars[i-1]]+list(str(count))
                    
                    i=i-count+2 if count<10 else i-count+3
                count=1
            else:
                count+=1
                if i==len(chars)-1:
                    chars[i-count+1:i+1]=[chars[i-1]]+list(str(count))

                
            i+=1
    
        return len(chars)