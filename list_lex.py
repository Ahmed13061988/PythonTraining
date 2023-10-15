# def check(nums):
#     result = 0
#     for i in nums:
#         value = i
#         nums.remove(i)
#         if value in nums:
#             result += 1
#     return result

def check(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
    return count


print(check([1, 1, 5, 100, -20, -20, 6, 0, 0]))
