
# 1.Write a Python function to find the Max of three numbers.

# nums = [3,6,2]

# def FindThreeMax(list):
#     for i in range(len(list)):
#         j = i+1
#         for j in range(3):
#             if list[i] > list[j]:
#                 list[i], list[j] = list[j], list[i]
#     return list[0]

# print("Maximum number:", FindThreeMax(nums))
# -------------------------------------------------------------------------------------------------------------------------------
# 2.Write a Python function to sum all the numbers in a list. Go to the editor Sample List : (8, 2, 3, 0, 7) Expected Output : 20

# list=[8,2,3,0,7]

# def CalculateSum(nums):
#     result=0
#     for num in nums:
#         result += num
#     return result

# print("Sum of numbers:",CalculateSum(list))
# -------------------------------------------------------------------------------------------------------------------------------
# 3.Write a Python function to multiply all the numbers in a list. Go to the editor Sample List : (8, 2, 3, -1, 7) 
# Expected Output : -336

# list=[8,2,3,-1,7]

# def CalculateProduct(nums):
#     result=1
#     for num in nums:
#         result *= num
#     return result

# print("Multiply of numbers:",CalculateProduct(list))
# -------------------------------------------------------------------------------------------------------------------------------
# 4. Write a Python program to reverse a string. Go to the editor Sample String : "1234abcd" Expected Output : "dcba4321"

# txt = "1234abcd"

# def ReverseOfString(text):
#     return text[::-1]

# print("Reversed String:",ReverseOfString(txt))