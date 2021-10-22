def minimulPerk(nums:list) -> int:
    if len(nums) == 1:
        return nums[0]

    res = float('inf')
    for i, num in enumerate(nums):
        if ((i - 1) < 0 and num > nums[i + 1])\
            or ((i + 1) == len(nums) and nums[i - 1] < num)\
            or (nums[i - 1] < num and num > nums[i + 1]):
            res = min(res, num)
    return res

nums = [2, 4]
print(minimulPerk(nums))