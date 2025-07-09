class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
            result = 0
            l = len(nums)
            map_sumas = {}
            suma = 0
            
            
            
        
            for index in range(l):
                suma += nums[index]
                
                
                    
                
                if suma - k in map_sumas:
                    
                    #print(f"suba (suma-k): {suba}")
                    result += 1
        
                if suma == k:
                    result += 1
                map_sumas[suma] = index
                
                
            
            return result
    

sol = Solution()
print(sol.subarraySum([1],0))