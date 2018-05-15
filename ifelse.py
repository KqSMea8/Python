a=input('symbol: ')
b=int(input('number: '))
c=int(input('number: '))
if a=='*':
    print(b*c)
elif a=='/':
    print(b/c)
elif a=='+':
    print(b+c)
elif a=='-':
    print(b-c)
else:
    print('error')

name=input('name: ')
yearsold=int(input('yearsold: '))
if name=='jimmy' and (yearsold==(21 or 22)):
    print('That is me')
elif name=='amy' and yearsold==23:
    print('That is the girl')
else:
    print('That is not us')



