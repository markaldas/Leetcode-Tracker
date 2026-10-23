class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        prod_left = 1

        for i in range(len(nums)):
            result.append(prod_left)
            prod_left *= nums[i]

        prod_right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= prod_right
            prod_right *= nums[i]
    

        return result
                



        
