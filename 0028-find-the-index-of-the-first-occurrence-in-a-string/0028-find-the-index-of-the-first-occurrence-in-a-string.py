class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack)-len(needle)+1):
                if needle==haystack[i:i+len(needle)]:
                    return i
        else:
            return -1