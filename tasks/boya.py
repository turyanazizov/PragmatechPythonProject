n=int(input('Sifaris sayini qeyd edin: '))

def CalculatePerimetr():
    perimetrs=[]
    for i in range(n):
        L=int(input())
        W=int(input())
        H=int(input())
        p=2*L*H+2*W*H
        perimetrs.append(p)
    return perimetrs

def CalculatePaint(list):
    for perimetr in list:
        b1=perimetr/16
        b2=perimetr//16
        if b1>b2:
            print(b2+1)
        else:
            print(b2)

CalculatePaint(CalculatePerimetr())