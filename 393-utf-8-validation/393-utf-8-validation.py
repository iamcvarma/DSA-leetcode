class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i, n = 0, len(data)
        while i<n:
            if data[i]>>7==0:i+=1
            elif data[i]>>5==6 and i+1<n and data[i+1]>>6==2:i+=2
            elif data[i]>>4==14 and i+2<n and data[i+1]>>6==2 and data[i+2]>>6==2:i+=3
            elif data[i]>>3==30 and i+3<n and data[i+1]>>6==2 and data[i+2]>>6==2 and data[i+3]>>6==2:i+=4
            else:return False
        return True