class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        result = 0

        while i < len(s) and s[i].isspace():
            i += 1


        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1


        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1


        result = max(-2**31, min(sign * result, 2**31 - 1))

        return result

                
                    
            