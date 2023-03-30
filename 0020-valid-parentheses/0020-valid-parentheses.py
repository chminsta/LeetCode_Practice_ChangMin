class Solution:
    def isValid(self, s: str) -> bool:
        
        char=["()" , "{}" , "[]"]
        
        point=0
        i=0
        while True:
            while i<3:
                
                if char[i] in s:
                    s=s.replace(char[i],'')
                    point+=1
                i+=1
                
            i=0
            if s=="":
                return True
            else:
                
                if point == 0:
                    return False
                else:
                    point=0
            
                

        
            