class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Soln1: Naive Approach: O(n2)
        out = False
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    out = True
                    break
            if out==True:
                break
        return out
        """      
        
        
        #Soln2: Using extra memory ; O(n)
        d={}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]= 1
        return False
    
        """
        #Soln3: One liner
        return True if len(set(nums))<len(nums) else False
        """
      
          
