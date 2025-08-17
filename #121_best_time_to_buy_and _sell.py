def findprofit(nums):
    min_price=nums[0]
    max_profit=0
    for price in nums[1:]:
        if price < min_price:
            min_price=price
        else:
            profit=price-min_price
            if profit > max_profit:
                max_profit=profit
    return max_profit
nums=[7,1,6,2,5,8]
print(findprofit(nums))