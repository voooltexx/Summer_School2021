a=[1,1,1,3,4,4,5]
tmp = a[0] - 1
for n in a:
    if n != tmp:
        print(n)
        tmp = n
        
