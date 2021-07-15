print('Привет! Я помогу тебе отсортировать любые числа, которые ты ввёдешь, по возрастанию! Введи любые числа: ')
a=input()
a=a.split()
for i in range(len(a)):
    a[i]=int(a[i])
for i in range (len(a)):
    for j in range (len(a)-1):
        if a[j]>a[j+1]:
            t=a[j+1]
            a[j+1]=a[j]
            a[j]=t
print('Hoba!',a)
