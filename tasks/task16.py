# 16. x-ə istənilən bir ədəd mənimsədin, sonra isə şərt verərək yoxlayın. X 10-dan böyükdürsə və cüt ədədirsə, ekrana “OKAY” yazılsın, əgər yuxarıdakı iki şərtdən biri ödənirsə “NOT OKAY” yazılsın, heç bir şərt ödənməzsə, “BAD” yazılsın 
x=int(input('Enter the number: '))
if x>10 and x%2==0:
    print("OKAY")
elif x>10 or x%2==0:
    print("NOT OKAY")
else :
    print("BAD")