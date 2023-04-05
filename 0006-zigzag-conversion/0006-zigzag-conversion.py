class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        #마디를 끊어서 저장, 각마디엔 numRows+numRows-2만큼 있음 2*numRows-2
        #마디별 첫번째들 먼저 붙이기
        #그다음 두번째, 2*numRows-2번째 번갈아서 붙이기
        #그다음 i번째, 2*numRows-2-i
        #i==numRows면 혼자 더하기
        result=""               #s=PAYPALISHIRING, numRows = 4 라하면
        length=2*numRows-2      #length = 6
        strlist = [s[i:i+length] for i in range(0, len(s), length)]
        #strlist["PAYPAL","ISHIRI","NG"]
#        for i in range(len(s)%length):
#            strlist[-1]+="_"
        #strlist["PAYPAL","ISHIRI","NG____"]
        for ss in strlist:
            result += ss[0]
        #result="PIN"
        for i in range(1, numRows-1):   #(1,3) 1,2 실행
            for ss in strlist:          #result=PIN+AL+SI+G_
                try:
                    result += ss[i]
                except:
                    pass                    
                try:
                    result += ss[length-i]
                except:
                    pass
                    

        for ss in strlist:
            try:
                result += ss[numRows-1]
            except:
                pass
        
        return result
#        return result.replace('_', '')