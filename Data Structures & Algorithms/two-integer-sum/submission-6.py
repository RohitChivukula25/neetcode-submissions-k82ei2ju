class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,val in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[val] = i
