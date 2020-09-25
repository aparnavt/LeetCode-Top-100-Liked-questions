class Solution:
    def reverse(self, x: int) -> int:
        
        if x>0:
            ans = int(str(x)[::-1]) 
            return ans if ans<(2**31 -1) else 0
        else:
            ans = -int(str(-x)[::-1]) 
        return ans if abs(ans)<2**31 else 0
        
        
        """
        Naive Approach 
        n = abs(x)
        i=0
        dig={}
        while(x>0):
            dig[i] = n%10
            i+=1
            n=n/10
        for j in range(len(dig)) :
            reverse+= dig[j] * pow(10,len(dig)-1-j)
            
        reverse = reverse * x/abs(x)
        return reverse
        """
            
