class Solution:
    def addMinimum(self, word: str) -> int:
        i=0
        if "abc" in word:
            word=word.replace("abc"," ")

        two=["ab","bc","ac"]
        for s in two:   
            if s in word:
                i+=word.count(s)
                word=word.replace(s," ")

        one=["a","b","c"]
        for s in one:
            if s in word:
                i+=2*word.count(s)
                word=word.replace(s," ")

        return i