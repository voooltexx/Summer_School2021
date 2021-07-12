#Составное/не составное число

a=int(input())
count=0
for i in range (2,a):
    if a% i==0:
        count=count+1
if count:
    print('составное')
else:
    print('не составное')
    