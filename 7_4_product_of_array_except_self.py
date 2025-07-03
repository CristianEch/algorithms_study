class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        result_2 = [0]*len(nums)
        result_2[len(nums)-1] = 1
        for n in range(len(nums)-2,-1,-1):
            result_2[n] = result_2[n+1]*nums[n+1]
        print(f"suffix product: {result_2}")

        result = [0]*len(nums)
        result[0] = 1
        final = [0]*len(nums)
        final[0] = result_2[0]
        for n in range(1,len(nums)):
            result[n] = result[n-1]*nums[n-1]
            final[n] = result[n-1]*nums[n-1]*result_2[n]
        print(f"prefix product: {result}")

        
    
        

        return final

            
    
lista = [1,2,3,4]
sol = Solution()
print(sol.productExceptSelf(lista))