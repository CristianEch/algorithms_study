class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        flag = False
        lista_2 = []
        for n in range(len(nums)):
            if nums[n] in lista_2:
                flag = True
                print(f"El número que ya está en la lista es {nums[n]}")
                break
            else:
                print(f"Number who's going to be append to the list: {nums[n]}")
                lista_2.append(nums[n])
        return flag

nums = [11,11, 2, 3, 4, 6, 6]      
sol = Solution()
print(sol.hasDuplicate(nums))
#make the same with dictionaries and it will be faster, with less memory consumption