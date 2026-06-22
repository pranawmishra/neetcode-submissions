class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        d = {}
        for i in range(len(nums)):
            k2 = target - nums[i]
            if k2 not in d:
                d[nums[i]] = i

            else:
                return [d[k2], i]