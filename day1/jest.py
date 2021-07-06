a=input().split()
sum1=0
sum2=0
for num in a:
    if int(num)%2:
        sum1=sum1+int(num) #сумма нечетных чисел
    if not int(num)%2:
        sum2=sum2+int(num) #сумма четных чисел
print(sum1,sum2)
