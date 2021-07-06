#! Программа для обмена валют

print('Приветствуем в программе обмена валют!')
print('Чтобы выйти, нажмите N')
EUR = 87
USD = 73
print ('Доступные варианты: Рубли, Евро, Доллары')
while True:
    type = input('Укажите, какую валюту вы хотите обменять: ')
    if type.lower() == 'n' or type.lower()=='N':
        break
    if type.lower()=='рубли' or type.lower()== 'rubles':
        print('Укажите, на какую валюту вы хотите обменять: ')
        if type.lower()=='доллары' or type.lower()=='dollars':
            data=int(input('Введите сумму в рублях: ')
    money=int(data)
    if money < 0:
        print ('Сумма не может быть отрицательной!')
        continue
    cache = round(money / 73,4)
print('Работы программы завершена.')
