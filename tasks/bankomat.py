n=int(input("Cekilecek meblegi daxil edin: "))

res=0
while(n>0):
    if n%10!=0 or n<=0:
        print(-1)
        break
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

print(res)