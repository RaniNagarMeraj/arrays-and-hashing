def findmajor(nums):
    count=0
    candidate=None
    for ele in nums:
        if count==0:
            candidate=ele
            count+=(1 if ele==candidate else -1)
    return candidate
nums=[2,2,1,1,1,2,2]
print(findmajor(nums))