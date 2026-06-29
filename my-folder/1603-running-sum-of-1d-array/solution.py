class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        new_arr = []

        for num in nums:
            curr_sum += num
            new_arr.append(curr_sum)

        return new_arr 

