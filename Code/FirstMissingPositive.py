class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        postive_numbers= [x for x in nums if x>0]
        
        try:
            missing_nums = set(range(1,len(nums)+2))-set(postive_numbers)
            return min(missing_nums)
        except:
            return 1
