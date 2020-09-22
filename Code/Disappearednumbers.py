class Solution:
  def disappearednums(self, nums:List[int])->List[int]:
    for value in nums:
      index = abs(value)-1
      nums[index] = -abs(nums[index])
    out = [i+1 for i in range(0,len(nums)) if nums[i]>0]
    return out
