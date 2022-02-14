from decimal import Clamped


list=[11,3,7]

def Calc(nums):
    sum=0
    for num in nums:
        sum+=num
    return sum/3

print(Calc(list))