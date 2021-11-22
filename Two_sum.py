# Brute Solution
# for each number X in list of numbers:
#     for each number Y in list of numbers starting from X:
#         if X+Y equal target number, return indices


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
#
# x = twoSum([1, 2, 3, 5], 4)
# print(x)

def twoSum(nums, target):
    dictionary = {}
    for i in range(len(nums)):
        secondNumber = target - nums[i]
        if secondNumber in dictionary.keys():
            secondIndex = nums.index(secondNumber)
            if i != secondIndex:
                return sorted([i, secondIndex])

        dictionary.update({nums[i]: i})


x = twoSum([1, 2, 3, 5], 6)
print(x)
