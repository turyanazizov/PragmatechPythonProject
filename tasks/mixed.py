
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
# -------------------------------------------------------------------------------------------------------------------------------
# 5. Kvadrat tenliyi hell eden funksiya yazin

# import math
# print("A*x^2+B*x+C=0")
# a=int(input('Enter A parametr:'))
# b=int(input('Enter B parametr:'))
# c=int(input('Enter C parametr:'))

# def QuadraticEquationCalculator(a,b,c):
#     d=b**2-4*a*c
#     if d>0:
#         x1= -1*b + math.sqrt(d)
#         x2= -1*b - math.sqrt(d)
#         return x1,x2
#     elif d==0:
#         x= -1*b + math.sqrt(d)
#         return x
#     elif d<0:
#         return "There are no real roots..."

# print(QuadraticEquationCalculator(a,b,c))