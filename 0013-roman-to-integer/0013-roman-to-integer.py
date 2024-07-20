class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        s = s.replace("IV","G")
        s = s.replace("IX","N")
        s = s.replace("XL","A")
        s = s.replace("XC","B")
        s = s.replace("CD","E")
        s = s.replace("CM","F")
        for i in s:
            if i=="M":
                result+=1000
            elif i=="F":
                result+=900
            elif i=="D":
                result+=500
            elif i=="E":
                result+=400
            elif i=="C":
                result+=100
            elif i=="B":
                result+=90
            elif i=="L":
                result+=50
            elif i=="A":
                result+=40
            elif i=="X":
                result+=10
            elif i=="N":
                result+=9
            elif i=="V":
                result+=5
            elif i=="G":
                result+=4
            elif i=="I":
                result+=1
        return result