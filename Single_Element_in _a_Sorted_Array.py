def singleNonDuplicate(nums):
    for x in nums:
        if nums.count(x) == 1:
            return x


l = [1, 1, 2, 3, 3, 4, 4, 8, 8]
a = singleNonDuplicate(l)
print(a)
