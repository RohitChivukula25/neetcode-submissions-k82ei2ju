class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        DS = set()
        for i in nums:
            if(i in DS):
                return True
            DS.add(i)
        return False