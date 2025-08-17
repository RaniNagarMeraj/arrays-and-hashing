def twosum(nums,target):
    hash={}
    for i,ele in enumerate(nums):
        diff=target-ele
        if diff in hash:
            return [hash[diff],i]
        hash[ele]=i
nums=[3,2,4]
target=7
print(twosum(nums,target))