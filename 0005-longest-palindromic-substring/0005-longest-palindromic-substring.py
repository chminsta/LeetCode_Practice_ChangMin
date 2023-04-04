class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=len(s)
        if m==1:
            return s
        while m>=0:
            
            for i in range(0,len(s)-m+1):
                test=s[i:i+m]
            
                if test==test[::-1]:
                    return test
            m-=1
                
        