class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for number in nums:
            key = number
            if key not in counter:
                counter[key]= 0
            counter[key] += 1
        print(sorted(counter.items(), key=lambda x:-x[1]))
        return [n[0] for n in sorted(counter.items(), key=lambda x:-x[1])][:k+1]
        
        



        
        


lista = [4,1,1,1,2,2,3]
sol = Solution()
print(sol.topKFrequent(lista,5))
