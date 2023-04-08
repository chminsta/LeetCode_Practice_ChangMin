class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if len(s)<=2:
            if s=="01":
                return 2
            else:
                return 0
        #add two pointers L,R
        l=0
        if len(s)%2:
            r=len(s)-2
        else:
            r=len(s)-1
        while r>0:
            for i in range(len(s)-r):
                #check
                halfpoint=i+(r-l+1)//2
                
                if "1" not in s[i:halfpoint] and  "0" not in s[halfpoint:i+r+1]:

                    return r-l+1                 
                
                
            r-=2
        return 0