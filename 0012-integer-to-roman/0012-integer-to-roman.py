class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        while num >= 1000:
            num-=1000
            result += "M"
        if str(num).startswith("4") and num >= 400:
            num-=400
            result += "CD"
        elif str(num).startswith("9") and num >= 900:
            num-=900
            result += "CM"
        while num >= 500:
            num-=500
            result += "D"
            
        while num >= 100:
            num-=100
            result += "C"
        if str(num).startswith("4") and num >= 40:
            num-=40
            result+="XL"
        elif str(num).startswith("9") and num >= 90:
            num-=90
            result+="XC"
            
        while num >= 50:
            num-=50
            result += "L"
        while num >= 10:
            num-=10
            result+="X"
        if str(num).startswith("4"):
            num-=4
            result += "IV"
        elif str(num).startswith("9"):
            num-=9
            result += "IX"
        while num >= 5:
            num-=5
            result += "V"
        while num >= 1:
            num-=1
            result+="I"
        return result