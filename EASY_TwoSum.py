class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetList = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (target == (nums[i] + nums[j])):
                    targetList.append(i)
                    targetList.append(j)
                    return targetList
