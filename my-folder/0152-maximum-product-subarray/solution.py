class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            candidate = (num, curr_max * num, curr_min * num)
            curr_max = max(candidate)
            curr_min = min(candidate)
            result = max(result, curr_max)

        return result 

        
