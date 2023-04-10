class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        data=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        out=[]
        new=[]
        #let digits"23"
        for num in digits:
            #num "2"
            if out == []:
                for s in data[int(num)]:                 
                    out.append(s)
            else:   #out=["a","b","c"]
                for o in out:
                    for s in data[int(num)]:
                        new.append(o+s)
                out=new
                new=[]
                    
        return out