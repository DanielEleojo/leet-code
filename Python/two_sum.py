
def twoSum(self, nums: list[int], target: int) -> list[int]:
    dict = {}

    for i, val in enumerate(nums):
        lookup = target - val

        if lookup in dict:
            return [dict[lookup], i]
        
        dict[val] = i