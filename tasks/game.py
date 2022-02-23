import random
num=random.randint(1,100)
print(num)
list=[]
list.append(num)
succes=False
i=0
boyuk=100
kicik=1
while succes==False:
    if i==0:
        texmin=int(input('Ilk texmininizi yazin: '))
        list.append(texmin)
        i+=1
    if texmin==num:
        print('Dogru texmin etdiniz - ',texmin)
        succes=True
    elif texmin<num:
        texmin=int(input('Yeniden texmininizi yazin: '))
        list.append(texmin)
        list.sort()
        print('Texmininiz Dogru ededden kicikdir.Araliq : ',list[list.index(num)-1],'-',list[list.index(num)+1])
        

    elif texmin>num:
        texmin=int(input('Yeniden texmininizi yazin: '))
        list.append(texmin)
        list.sort()
        print('Texmininiz Dogru ededden boyukdur.Araliq : ',list[list.index(num)-1],'-',list[list.index(num)+1])
    
