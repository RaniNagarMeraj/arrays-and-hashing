def singlr(nums):
    res=0
    for ele in nums:
        res^=ele
    return res
nums=[4,1,2,1,2]
print(singlr())
