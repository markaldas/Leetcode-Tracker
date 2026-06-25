class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        nums = {}
        for num in nums1:
            nums[num] = nums.get(num, 0)
        print(nums)
        
        for num in nums2:
            if num in nums:
                arr.append(num)
        
        # for num in nums:
        #     if nums[num] > 0:
        #         arr.append(num)
        print(nums)
        return list(set(arr))
