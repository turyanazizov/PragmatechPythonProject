money=int(input("Cekilecek meblegi daxil edin: "))

def fnc(n):
    res = 0
    while(n>0):
        if n%10!=0 or n<=0:
            return -1
        elif n-500>=0:
            n-=500
            res+=1
        elif n-200>=0:
            n-=200
            res+=1
        elif n-100>=0:
            n-=100
            res+=1
        elif n-50>=0:
            n-=50
            res+=1
        elif n-20>=0:
            n-=20
            res+=1
        elif n-10>=0:
            n-=10
            res+=1
    return res

print(fnc(money))