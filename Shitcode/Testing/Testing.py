'''
###################
import random #рандомайзер чисел

def randomizer():
    a=[random.randint(1,1000) for i in range(100)]
    for n in a:
        if n%3==0:
            print(n)
    print(a)

if __name__=='__main__':
    randomizer()
###################


###################
def f(x):
    return 7*x+9
print(f(x))

for i in range(-10,11):
    print(f(i))
###################


###################
a=[]
a.append(6)
print(a)
###################


###################
a = [1,2,3,4,5,6]
ab= list(a)
print(ab)
###################

###################
f = open('Test.txt', 'a')

f.write('100 ')
f.close()

f2 = open ('Test.txt', 'r')
print(f2.read())
##################
'''


f = open('uidatabase.txt', 'r')
a = f.read().split('\n')
print(a)
for i in range (len(a)):
    a[i] = a[i].split()
print(a)
a.pop(len(a) - 1)
print(a)
















































































































































































































































