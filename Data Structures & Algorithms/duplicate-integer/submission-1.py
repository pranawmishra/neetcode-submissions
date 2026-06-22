class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i, j = 0, 0
        d = {}

        for n in nums:
            if n in d:
                # d[n] += 1
                return True
            else:
                d[n] = 1

        return False
        