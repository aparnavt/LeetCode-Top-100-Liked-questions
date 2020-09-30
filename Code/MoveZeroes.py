class Solution:
     def moveZeroes(self, nums:List[int])->List[int]:
            zero = 0  # records the position of "0"
            for i in range(len(nums)):
                if nums[i] != 0:
                    print(i)
                    nums[i], nums[zero] = nums[zero], nums[i]
                    print(nums,zero)
                    zero += 1
