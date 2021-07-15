import random
a=[]
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append([random.randint(1,100)])
for i in range(3):
    a[i][i]=0
print(a)
