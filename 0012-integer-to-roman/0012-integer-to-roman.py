class Solution:
    def intToRoman(self, num: int) -> str:
        
        M=0
        CM=0
        D=0
        CD=0

        if num>=1000:
            M=num//1000
            num=num%1000
        if num>=900:
            CM=1
            num-=900
        if num>=500:
            D=1
            num-=500
        if num>=400:
            CD=1
            num-=400
            
        C=0
        XC=0
        L=0
        XL=0
        
        if num>=100:
            C=num//100
            num%=100
        if num>=90:
            XC=1
            num-=90
        if num>=50:
            L=1
            num-=50
        if num>=40:
            XL=1
            num-=40
            
        X=0
        IX=0
        V=0
        IV=0
        I=0
        
        if num>=10:
            X=num//10
            num%=10
        if num>=9:
            IX=1
            num-=9
        if num>=5:
            V=1
            num-=5
        if num>=4:
            IV=1
            num-=4
            
        if num>=1:
            I=num
            
        out="M"*M+"CM"*CM+"D"*D+"CD"*CD+"C"*C+"XC"*XC+"L"*L+"XL"*XL+"X"*X+"IX"*IX+"V"*V+"IV"*IV+"I"*I
        
        return out