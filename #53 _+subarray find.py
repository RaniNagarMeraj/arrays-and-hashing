def findmax(nums):
    max_sum=nums[0]
    current_sum=nums[0]
    start=0
    end=0
    temp=0
    for i in range(1,len(nums)):
        if nums[i]>current_sum+nums[i]:
            current_sum=nums[i]
            temp=i
        else:
            current_sum=current_sum+nums[i]
        if current_sum>max_sum:
            max_sum=current_sum
            start=temp
            end=i
    return max_sum,nums[start:end+1]
nums=[3,4,2,1]
max_sum,subarray=findmax(nums)
print(max_sum,subarray)