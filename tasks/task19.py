# 19. my_string = ‘f456.89ts’. my_stringin ədədə bərabər olan hissəsin ilə özündən sonra gələn ən kiçik tam ədədə olan qüvvətini tapın
my_string = 'f4.5689ts'
num=''
for i in my_string:
    if i.isdigit() or i=='.':
        num+=i
num=float(num)
int_num=int(num)+1
print(num**int_num)
