class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec=0
        b_dec=0
        for i in range(len(a)):          
            a_dec+=int(a[len(a)-1-i])*(2**i)
        for i in range(len(b)):          
            b_dec+=int(b[len(b)-1-i])*(2**i)
        c_dec=a_dec+b_dec
        
        
        c_bin = ''
        while c_dec > 0:
            c_bin = str(c_dec % 2) + c_bin
            c_dec //= 2
        
        if c_bin == '':
            c_bin = '0'
        
        return c_bin
        
        
        
            

            