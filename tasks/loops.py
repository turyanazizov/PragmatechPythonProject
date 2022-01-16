# Tapshiriqlar
# 1.Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

# num1 = int(input('1st: '))
# num2 = int(input('2nd: '))
# num3 = int(input('3rd: '))
# num4 = int(input('4th: '))

# if num1 == num2 and num3 == num4 and num1 == num3:
#     print(num1**2)
# else:
#     print(num1+num2+num3+num4)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 2.Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

# num1 = int(input('1st: '))
# num2 = int(input('2nd: '))
# num3 = int(input('3rd: '))
# num4 = int(input('4th: '))

# list=[num1,num2,num3,num4]
# print(max(list))
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 3.Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

# meyveler={
#     'alma':10,
#     'banan':20,
#     'armud':25,
#     'nar':32,
#     'gilas':27
# }
# print(meyveler.keys())
# meyve=input('Meyve daxil edin: ')
# print(meyveler[meyve])
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 4.Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.

# ad=input('Adinizi daxil edin: ')
# while len(ad)<3 or len(ad)>11:
#     ad=input('Adinizi dogru daxil edin: ')

# soyad=input('Soyadinizi daxil edin: ')
# while len(soyad)<5 or len(soyad)>15:
#     soyad=input('Soyadinizi dogru daxil edin: ')

# il=input('Dogum ilinizi daxil edin: ')
# while len(il)!=4:
#     il=input('Dogum ilinizi dogru daxil edin: ')

# email=input('Emailinizi daxil edin: ')
# while len(email)<10 or len(email)>22 or email[len(email)-len('@gmail.com')::] != '@gmail.com':
#     email=input('Emailinizi dogru daxil edin: ')

# password=input('Password daxil edin: ')
# while len(password)<6 or len(password)>13:
#     password=input('Password dogru daxil edin: ')

# print('Qeydiyyatiniz tamamlandi!!!')
# print('Qeydiyyatin detallarina baxmaq isterdiniz?')

# cavab=input('yes/no: ')
# if cavab=='yes':
#     print(f'Ad: {ad}\nSoyad: {soyad}\nYaş: {2022-int(il)}\nEmail: {email}\nParol: {password}')
# if cavab=='no':
#     print(f'{ad},{soyad} Ugurlar!!!')
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 5.Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

# list=[12,34,2,4,7,23]
# sum=0
# for eded in list:
#     sum+=eded
# print(sum)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 6.Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

# list=[12,34,2,4,7,245,23]
# m=list[0]
# for i in list:
#     if i>m:
#         m=i
# print(m)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 7.Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.

# list=[12,34,2,4,7,245,1,23]
# m=list[0]
# for i in list:
#     if i<m:
#         m=i
# print(m)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 8.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

# list=['abc', 'xyz', 'aba', '1221']
# count=0
# for item in list :
#     if item[0]==item[-1]:
#         count+=1
# print(count)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 9.Write a Python program to check a list is empty or not.

# list=[]
# if len(list)==0:
#     print('List is empty...')
# else:
#     print('List is NOT empty...')
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 10.my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.

# my_text = 'Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.'
# list=my_text.split(' ')
# list.sort()
# for item in list:
#     print(item,end=' ')
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 11.Write a Python program to select the odd items of a list.

# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2==0:
#         print(i)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# 12.dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"} Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. Bunun ucun userden input alin. Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user ne sorushmaq isteyir. Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” sualina cavab axtarir. Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” “. Bu suali sorushduqda yes ve no secimleri verin. Eger yes yazsa dictionarydeki datadan istifade ederek Platonun doguldugu ili usere gosterin.Meselen country daxil etse proqram texmin etsin ki user platonun doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin. Eger mentiqsiz soz daxil edilse not found verin ekrana.

# dict={"name": "Plato",
#     "country": "Ancient Greece",
#     "born": -427,
#     "teacher": "Socrates",
#     "student": "Aristotle"
# }

# sual=input('Sualinizi daxil edin: ')

# if sual.find('when')>=0 or sual.find('born')>=0:
#     print('Maybe did you mean “When was Plato born?”')
#     cavab=input('Your answer (yes/no): ')
#     if cavab=='yes':
#         print('Plato born date is:',dict['born'])

# elif sual.find('country')>=0:
#     print('Maybe did you mean “Where was Plato born?”')
#     cavab=input('Your answer (yes/no): ')
#     if cavab=='yes':
#         print('Plato born place is:',dict['country'])

# elif sual.find('name')>=0:
#     print('Maybe did you mean “What was name?”')
#     cavab=input('Your answer (yes/no): ')
#     if cavab=='yes':
#         print('Name is:',dict['name'])

# elif sual.find('student')>=0:
#     print('Maybe did you mean “Who was Platos student?”')
#     cavab=input('Your answer (yes/no): ')
#     if cavab=='yes':
#         print('Platos student is:',dict['student'])

# elif sual.find('teacher')>=0:
#     print('Maybe did you mean “Who was Platos teacher?”')
#     cavab=input('Your answer (yes/no): ')
#     if cavab=='yes':
#         print('Platos teacher is:',dict['teacher'])
# ---------------------------------------------------------------------------------------------------------------------------------------------