class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        num=0
        cache=""
        if len(s)==1:
            return 1
        for i in range (len(s)): #pwwkew 라 하면 0~5
            for j in range(i,len(s)):#i~5
                if s[j] in cache:
                    result=max(num,result)
                    cache=""
                    break
                else:
                    cache=s[i:j+1]
                    num=len(cache)
        return result                
            
        
        #i=0, j=0, cache=
            
