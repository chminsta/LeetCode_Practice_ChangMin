class Solution:
    def removeStars(self, s: str) -> str:
        if "*" not in s:
            return s
        
        i=1
        while True:
            if s[i]=="*":
                s=s[0:i-1]+s[i+1:]
                i-=1
            else:
                i+=1
            if i==len(s):
                return s
                