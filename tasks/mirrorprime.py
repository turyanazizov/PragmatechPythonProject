num1 = int(input())
num2 = int(input())


def reverse(n):
    n = str(n)
    n = n[::-1]
    n = int(n)
    return n


def Prime(n):
    for i in range(2, n):
        if n % i == 0:
            isprime = False
            break
        else:
            isprime = True
    return isprime


for n in range(num1, num2):
    if Prime(n) == True and Prime(reverse(n)) == True:
        print(n)
