class Solution:    
    def countPrimes(self, n: int) -> int:
        nums= [i for i in range(2,n)]
        for index,num in enumerate(nums):
            if num*num > n:
                break
            elif num!=-1:
                for j in range(index+num, len(nums),num):
                    nums[j]=-1
        out = [num for num in nums if num!=-1]
        return len(out)
