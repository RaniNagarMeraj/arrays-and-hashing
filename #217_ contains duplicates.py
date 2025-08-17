def conatain(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False
nums=[1,2,3,4,1,5]
print(conatain(nums))