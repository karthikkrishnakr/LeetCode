class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            shortest = str1
            largest = str2
        else:
            shortest = str2
            largest = str1
        prefix = ""
        for i in range(len(shortest)):
            k = len(largest)//(len(shortest)-i)
            l = len(shortest)//(len(shortest)-i)
            if shortest[:len(shortest)-i]*k == largest and shortest[:len(shortest)-i]*l == shortest:
                return shortest[:len(shortest)-i]
        return ""