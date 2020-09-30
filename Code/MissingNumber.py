class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        superset= set([i for i in range(0,len(nums)+1)])
        subset= set(nums)
        
        value = list(superset-subset)
        return value[0]
