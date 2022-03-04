n=int(input('Enter the number of numbers: '))
nums=[]

def Preparelist(n):
    for i in range(n):
        nums.append(int(input()))
    return findMissingNumber(nums)

def findMissingNumber(nums):
    for i in range(len(nums)-1):
        if nums[i]+1 != nums[i+1]:
            print(f"Missing number(s): {nums[i]+1}")

Preparelist(n)
