print ('Введите первое число ')
a=float(input())
print('Введите действие ')
sign=input()
print('Введите второе число ')
b=float(input())
if sign =='+':
    print('Сумма равна ')
    print(a+b)
elif sign =='-':
    print ('Разность равна ')
    print(a-b)
elif sign =='*' or 'x':
    if b==0:
        print ('На ноль делить нельзя! Введите другое число')
    if b>0 or b<0:
        print('Произведение равно ')
        print (a*b)
elif sign ==':' or '//':
    print ('Значение частного равно ')
    print (a//b)