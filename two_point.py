nums = [-5, -2, 4, 7, 8, 12, 16, 17, 32, 44, 48]


def two_point(iterable, k):
    l = 0
    r = len(nums) -1
    while l < r:
        if nums[l] + nums[r] == k:
            return [nums[l], nums[r]]
        elif nums[l] + nums[r] > k:
            r -= 1
        else:
            l += 1
    return []

print(two_point(nums, 44+48))
