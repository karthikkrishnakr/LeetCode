class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        output = ""
        g1 = (numRows-1)*2 if numRows>1 else 1
        g2 = 0
        ind = 0
        if length<=numRows:
            return s
        while ind<length:
            output+=s[ind]
            ind+=g1
        if length>1 and g1!=1:
            for i in range(1,numRows-1):
                g1-=2
                g2+=2
                output+=s[i]
                ind = i
                pos = 1
                while True:
                    if pos%2!=0:
                        ind+=g1
                        pos+=1
                        if ind>=length:
                            break
                        output+=s[ind]
                    else:
                        ind+=g2
                        pos+=1
                        if ind>=length:
                            break
                        output+=s[ind]
            g2 = (numRows-1)*2
            ind = numRows-1
            while ind<length:
                output+=s[ind]
                ind+=g2
        return output