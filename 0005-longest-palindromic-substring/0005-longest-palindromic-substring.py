class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        st=0
        dic={}
        s="0"+s
        for j in range(1,len(s)):
            for i in range(len(s),st,-1):
                if s[j:i] == s[i-1:j-1:-1]:
                    dic[i-j] = s[j:i]
        return(dic[max(dic)])