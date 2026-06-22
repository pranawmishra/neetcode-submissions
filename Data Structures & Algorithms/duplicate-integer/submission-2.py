class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i, j = 0, 0
        nums_sorted = sorted(nums)

        for n in range(len(nums_sorted)-1):
            if nums_sorted[n] == nums_sorted[n+1]:
                return True

        return False
        