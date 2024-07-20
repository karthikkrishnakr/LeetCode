class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s=="":
            return 0
        result = ""
        sign = True
        if s[0]=="-":
            sign = False
            s = s[1::]
        elif s[0] =="+":
            s = s[1::]
        for i in s:
            if i not in "0123456789":
                break
            result += i
        if result =="":
            return 0
        result = int(result)
        if not sign:
            result *= -1
        if result >= 2**31:
            return (2**31)-1
        elif result < -2**31:
            return -2**31
        return result