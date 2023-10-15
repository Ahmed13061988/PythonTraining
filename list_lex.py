def check(nums):
    result = 0
    for i in nums:
        value = i
        nums.remove(i)
        if value in nums:
            result += 1
    return result


print(check([10, 20, 30, 40, 30, 20]))
