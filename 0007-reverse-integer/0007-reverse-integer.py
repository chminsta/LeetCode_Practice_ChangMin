class Solution:
    def reverse(self, x: int) -> int:
        s=int(str(abs(x))[::-1])
        if s<-(2**(31)) or s>2**31-1:
            return 0
        elif x<0:
            return -1*s
        else:
            return s
            