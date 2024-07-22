class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = strs[0]
        for i in strs:
            if len(i) < len(shortest):
                shortest = i
                
        for i in range(len(shortest)):
            for j in strs:
                if shortest[i] != j[i]:
                    return prefix
            prefix += shortest[i]
        return prefix