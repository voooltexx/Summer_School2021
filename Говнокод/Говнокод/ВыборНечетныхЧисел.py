print('Введите числа и я выберу только нечётные: ')
a=input().split()
print('Нечетные числа: ')
for num in a:
    if (not int(num)%2) and (not int(num)%3):
        print(num)
