# An elegant solution: but Time Limit Exceeded :(
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        from functools import reduce
        
        return [reduce(lambda x,y: x*y, nums[:n]+nums[n+1::]) for n in range(len(nums))]
    

lista = [-1,1,0,-3,3]
sol = Solution()
print(sol.productExceptSelf(lista))
        