# 16. iki ədəd götürüb dəyişkənlərə mənimsədin. Əgər ədələrin fərqi bir-birlərinə olan nisbətin tam hissəsindən böyükdürsə, ekrana “Greater”, bərabərdirsə, “EQUAL” yox əgər kiçikdirsə, “SMALLER” yazılsın.
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a-b > a//b:
    print("Greater")
elif a-b == a//b:
    print("Equal")
elif a-b < a//b:
    print("Smaller")
