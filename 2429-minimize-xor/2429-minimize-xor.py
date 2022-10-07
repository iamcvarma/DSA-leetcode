class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        count_a,count_b,res = 0,0,a
        #get bit counts of a and b
        while a:
            count_a+=1
            a&=a-1
        while b:
            count_b+=1
            b&=b-1
        
        diff=count_b-count_a
        
        while diff:
            if diff>0:
                res|=(res+1) #adding bits
                diff-=1
            else:
                res&=(res-1) #removing bits
                diff+=1
        return res
                
                