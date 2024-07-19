class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        clen = 0
        for i in s:
            if i not in lst:
                lst.append(i)
            elif i in lst:
                k = 0
                for z in lst:
                    k+=1
                if k>clen:
                    clen = k
                while lst[0] is not i:
                    lst.pop(0)
                lst.pop(0)
                lst.append(i)
        k = 0
        for z in lst:
            k+=1
        if clen<k:
            clen = k        
        return clen