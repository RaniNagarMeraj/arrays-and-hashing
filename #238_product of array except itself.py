def findproduct(nums):
    n=len(nums)
    result=[1]*n
    left_product=1
    for i in range(n):
        result[i]=left_product
        left_product=left_product*nums[i]
    right_product=1
    for i in range(n-1,-1,-1):
        result[i]=result[i]*right_product
        right_product=right_product*nums[i]

    return result
nums=[1,2,3,4]
print(findproduct(nums))




# #brute force
# nums=[1,2,3,4]
# n=len(nums)
# result=[]
# for i in range(n):
#     product=1
#     for j in range(n):
#         if i!=j:
#             product=product*nums[j]
#     result.append(product)
# print(result)