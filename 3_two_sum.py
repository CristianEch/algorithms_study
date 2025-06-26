class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            if nums[index] <= target:
                for other in range(index+1,len(nums)):
                    if nums[index] + nums[other] == target:
                        return [index, other]

nums= [3,3]
target = 6

sol = Solution()
print(sol.twoSum(nums=nums, target=target))

