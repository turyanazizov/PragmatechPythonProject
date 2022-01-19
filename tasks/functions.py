# --------------------------------------------------------------------------------------------------------------------------------------------
# 1.Write a Python program to select the odd items of a list.

# list = [1,2,3,4,5,6,7,8,9,10]

# def SelectOdd(list):
#     oddList=[]
#     for item in list:
#         if item%2==0:
#             oddList.append(item)
#     return oddList

# print(SelectOdd(list))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 2.Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0, 7) Expected Output : 20

# list=[1,2,3,4,5,6,7,8,9,10]

# def sumFunc(list):
#     sum=0
#     for item in list:
#         sum+=item
#     return sum

# print(sumFunc(list))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 3.Write a Python function to multiply all the numbers in a list.Sample List : (8, 2, 3, -1, 7) Expected Output : -336

# list = [1,2,3,4,5]

# def multiplyFunc(list):
#     result=1
#     for item in list:
#         result=result*item
#     return result

# print(multiplyFunc(list))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 4.Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.

# number=int(input('Enter the Number: '))

# def returnDay(number):
#     if number>7 or number<1:
#         return None
#     if number == 1:
#         return 'Monday'
#     if number == 2:
#         return 'Tuesday'
#     if number == 3:
#         return 'Wednesday'
#     if number == 4:
#         return 'Thursday'
#     if number == 5:
#         return 'Friday'
#     if number == 6:
#         return 'Saturday'
#     if number == 7:
#         return 'Sunday'

# print(returnDay(number))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 5.Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website.Loop through the list, and print a greeting to each user: • If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report? • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

# usernames=['admin','turyan','ali','ulvi','sabina','tahir']

# def loginFunc(list):
#     username=input('Enter your username: ')
#     found=False
#     for user in usernames:
#         if username==user:
#             found=True
    
#     if username=='admin' and found==True:
#         return 'Hello admin, would you like to see a status report?'
#     elif found==True :
#         return f'Hello {username}, thank you for logging in again.'
#     else:
#         return 'Error occured. Please Sign up website later Sign in...'
# print(loginFunc(usernames))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 6.len() funksiyasini ozunuz yazmaga calishin.

# item=[1,4,4,56,7,9]
# def lenof(item):
#     count=0
#     for i in item:
#         count+=1
#     return count
# print(lenof(item))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 7.funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin.      Mes: [1,2,3,1] bu halda True qaytaracag

# list = [1,2,3,4,5,6,7,8,9,10,1]

# def checkFunc(list):
#     if list[0]==list[-1]:
#         return True
#     else:
#         return False

# print(checkFunc(list))
# --------------------------------------------------------------------------------------------------------------------------------------------
# 8.Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.

# list = [1, 3, 5, 6, 7, 8]
# dict = {
#     'tural': 1,
#     'elcin': 2,
#     'turyan': 3,
#     'aga': 4,
#     'ferid': 5,
#     'ulvi':6
# }

# def deleteFunc(list, dict):
#     newList=[]
#     for num in list:
#         for item in dict:
#             if num == dict[item]:
#                 newList.append(num)
#     return newList

# print(deleteFunc(list,dict))
# --------------------------------------------------------------------------------------------------------------------------------------------
