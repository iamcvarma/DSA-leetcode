class Solution:
    def intToRoman(self, num: int) -> str:
        arr = [(1000,'M'),(500,'D'),(100,'C'),(50,'L'),(10,'X'),(5,'V'),(1,'I')]
        i=0
        res=[]
        while num:
            if num//arr[i][0]:
                s = str(num)
                fact = num//arr[i][0]
                if s[0]=='4':
                    res.append(arr[i][1])
                    res.append(arr[i-1][1])
                elif s[0]=='9':
                    res.append(arr[i+1][1])
                    res.append(arr[i-1][1])
                    fact = num//arr[i+1][0]
                else:
                    res.append(arr[i][1]*fact)
                num-=fact*arr[i][0]
            i+=1
        return "".join(res)