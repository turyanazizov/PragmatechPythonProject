il=2022
ay=2
gun=20
aylar=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def isPalindrome(gun,ay,il):
    d=str(gun)
    m=str(ay)
    if gun<10:
        d="0"+str(gun)
    if ay<10:
        m="0"+str(ay)
    date=d+m+str(il)
    if date==date[::-1]:
        print(d+'.'+m+'.'+str(il))
        return True

g=gun
a=ay
i=il
for i in range(il,4000):
    if isPalindrome(g,a,i):
        break

    for a in range(1,12):
        if isPalindrome(g,a,i):
            break

        for g in range(1,aylar[int(a)]):
            if isPalindrome(g,a,i):
                break
            