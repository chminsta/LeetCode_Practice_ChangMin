class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss=s.split(" ")
        while "" in ss:
            ss.remove("")
        return len(ss[len(ss)-1])