class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        map = {}

        for num in nums:
            if num in map:
                return True
            map[num] = None
        return False

        
