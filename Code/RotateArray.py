class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(k<len(nums)):
            nums[0:k],nums[k:len(nums)] = nums[-k:len(nums)],nums[0:len(nums)-k]
        
        #Naive Approach
        else:
            for i in range(0,k):
                temp=nums[len(nums)-1]
                for index in range(len(nums)-1,0,-1):
                    nums[index]=nums[index-1]
                nums[0]=temp
                
