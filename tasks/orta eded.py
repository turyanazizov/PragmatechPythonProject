list=[11,3,7]

def Calc(nums):
    sum=0
    for num in nums:
        sum+=num
    return int(sum/len(nums))

print(Calc(list))