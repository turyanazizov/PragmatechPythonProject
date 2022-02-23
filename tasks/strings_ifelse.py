
# # ----------------------------------------------------------------------------------------------------------------------------------------
# # 1. 3 input daxil edin və daxil edilən ədələrin fərqini tapın
# num1=int(input('First number: '))
# num2=int(input('Second number: '))
# num3=int(input('Third number: '))
# a=num1-num2-num3
# print(a)
# # ----------------------------------------------------------------------------------------------------------------------------------------
# # 2. word = 'Python'. Verilen stringin uzerinde azı 5 dənə string method tətbiq edin
# word = 'Python'
# word.capitalize()
# word.center(10)
# word.count('t')
# word.find('n')
# word.split('t')
# word.swapcase()
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 3. math kitabxanasından istifadə edərək inputdan hələn ədədin kubunu tapın
# import math
# a=int(input('Enter number: '))
# cube=pow(a,3)
# print(cube)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 4. inputdan 3 ədəd götürün və o ədələrin kvadratını bir listə əlavə edin
# num1=int(input('First number: '))
# num2=int(input('Second number: '))
# num3=int(input('Third nunmber: '))
# list=[num1**2, num2**2, num3**2]
# print(list)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 5. Təsadüfi rəqəmlərdən ibarət olan listin rəqəmlərini kiçikdən böyüyə düzün
# list=[3,14,5,34,21,2,6]
# list.sort()
# print(list)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 6. Bir mesajı dəyişəndə saxlayın və sonra mesajı çapa verin
# msj=input('Enter message: ')
# print(msj)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 7. ad və soyad dəyişkənləri yaradın və onlara istədiyiniz kiçik hərflərdən ibarət dəyər verin. Sonra tam_ad adlı dəyərdə ad və soyadın ilk hərflərini böyük şəkildə çapa verərək həmin şəxsə Salam verin.
# ad="turyan"
# soyad="azizov"
# tam_ad=ad+' '+soyad
# print('Salam',tam_ad.title(),'!')
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 8. sep parametrindən istifadə edərək 4 müxtəlif şəhər adını * işarəsi ilə ayırın
# print('Baku','London','Paris','Madrid',sep='*')
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 9 .“ Macarıstan” sözünü tərsinə çapa verin
# word='Macaristan'
# print(word[::-1])
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 10. Bir sətir koddan istifadə edərək aşağıdakı yazını göründüyü kimi çapa verin. Languages: Python C JavaScript
# print('Languages:','Python', 'C', 'JavaScript',sep='\n')
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 11. Escape characterlərdən istifadə edərək ekrana bir cümlə çap edin.
# print("Salam, \nMenim adim \"Turyan\"dir...")
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 12. Istenilen bir mətnin tam yarısını çap edin.
# # Məsələn: 2 üstü 5 32-dir. (formattingfən istifadə edin)
# s='Hello, how old are you?'
# len=len(s)
# print(s[0:len//2])
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 13. x = 10, y = 55 “and”-dən istifadə edərək x və y müqayisə edərək boolen dəyərləri çapa verin.
# x=10
# y=55
# print(x>y and x>10)
# print(x<y and y<40)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 14. word = “istədiyiniz sözü yaza bilərsiz” məsələn word = ‘culture’ “Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"cüməsini bir dəyişkənə mənimsədin və həmin dəyişkəndə saxlayın və word-ə verdiyiniz sözün bu dəyişkəndə olub-olmamasını yoxlayın. Əgər söz varsa, ekranda belə bir nəticə çıxarın; “Culture” sözü mətndə var. Əgər yoxdursa, “Not found” çapa verin. 
# word='culture'
# sentence='Nineteet Eighty-Four does not present "art-as-culture" but "art-as-function"'
# if sentence.find(word)>0:
#     print('Word Found')
# else:
#     print("Word NOT Found")
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 15. 65 ədədinin 22 ədədinə olan qalığı ilə nisbətinin hasilini çapa verin. 
# a=65
# b=22
# print((a%b)*(a//b))
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 16. x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. X 10-dan böyükdürsə və cüt ədədirsə, ekrana “OKAY” yazılsın, əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın 
# x=int(input('Enter the number: '))
# if x>10 and x%2==0:
#     print("OKAY")
# elif x>10 or x%2==0:
#     print("NOT OKAY")
# else :
#     print("BAD")
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 17. iki ədəd götürüb dəyişkənlərə mənimsədin. Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, ekrana “Greater”, bərabərdirsə, “EQUAL” yox əgər kiçikdirsə, “SMALLER” yazılsın.
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))

# if a-b > a//b:
#     print("Greater")
# elif a-b == a//b:
#     print("Equal")
# elif a-b < a//b:
#     print("Smaller")
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 18. String data tipi yaradın və dəyərini 5.567-yə bərabər edin. Sonra bu dəyişkənin dəyərin 10- luqlara qədər yuvarlaqlaşdırın.
# s='5.567'
# num=float(s)
# print(round(num,1))
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 19. my_string = ‘f456.89ts’. my_stringin ədədə bərabər olan hissəsin ilə özündən sonra gələn ən kiçik tam ədədə olan qüvvətini tapın
# my_string = 'f4.5689ts'
# num=''
# for i in my_string:
#     if i.isdigit() or i=='.':
#         num+=i
# num=float(num)
# int_num=int(num)+1
# print(num**int_num)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 20. 1 və 8 arasında random bir ədəd götürsün proqram, sonra isə o ədədin kvadrat kökünü tapın (random kitabxansini research edin).
# import random
# num=random.randint(0,8)
# print(f"Random number: {num} \nSquare of number: {num**2}")
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 21. 0 və 1 arasında olan təsadüfi bir ədədin 1 və 10 arasında olan təsadüfi bir ədələ hasilini tapın.  (random kitabxansini research edin)
# import random
# num1=random.random()
# num2=random.randint(1,10)
# print(f'First Number: {num1} \nSecond Number 2: {num2} \nHasil: {num1*num2}')
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 22. x = “5.89” stringinin tam hissəsinin kubunu tapın.
# x='5.89'
# x=float(x)
# tam_x=int(x)
# cube=tam_x**3
# print(cube)
# #----------------------------------------------------------------------------------------------------------------------------------------
# # 23. y = “4.92” stringini integere cast edin.
# y='4.92'
# y=float(y)
# y=int(y)
# print(y)
# #----------------------------------------------------------------------------------------------------------------------------------------