import random #рандомайзер чисел

def randomizer():
    a=[random.randint(1,1000) for i in range(100)]
    print(a)

if __name__=='__main__':
    randomizer()
