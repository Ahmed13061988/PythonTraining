val = 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]


# val = 3
# nums = [3, 2, 2, 3]


#
# def remove_element(list, value):
#     k = 0
#     for number in nums:
#         print(number)
#     #     if number == val:
#     #         nums.remove(number)
#     # print()
#
#
# remove_element(nums, val)

# new_nums = []
# for i in range(len(nums)):
#     if nums[i] != val:
#         new_nums.append(nums[i])
# print(new_nums)

def removeElement(nums, val):
    new_list = [value for value in nums if value != val]
    print(new_list)


removeElement(nums, val)
