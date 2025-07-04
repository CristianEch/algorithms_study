class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if len(nums)== 0:
            return 0
        else:      

            lista = sorted(nums)
            print(lista) 
            holder = {}
            holder[lista[0]] = lista[0]
            
            result = [1]*len(lista)
                       
            
            for index in range(1,len(lista)):
                if lista[index] == lista[index-1] + 1 or lista[index] == lista[index-1]:
                    if lista[index] == lista[index-1] +1:
                        print(f"ok with {lista[index]}")
                        holder[lista[index]] = lista[index]
                else:
                    print(f"partial holder {holder}")
                    result[index]= len(holder)
                    holder = {}
                    holder[lista[index]]= lista[index]
                result[index]= len(holder)

            return max(result)
array = [9,1,4,7,3,-1,0,5,8,-1,6]
sol = Solution()
print(sol.longestConsecutive(array))




