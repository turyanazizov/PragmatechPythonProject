str=input('')
k=int(input(''))
code=''
for i in str:
    code+=chr(ord(i)+k)
print(code)

