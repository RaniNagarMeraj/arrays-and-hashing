def findmissing(nums):
    n=len(nums)
    missing=n
    for i in range(n):
        missing=missing^i^nums[i]

    return missing
nums=[3,0,1]
print(findmissing(nums))