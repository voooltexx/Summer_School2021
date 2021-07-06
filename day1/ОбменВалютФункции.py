'''
def get_currency_key(currency_cods):
    for cod in currency_cods:
        print(cod)
    print('Введите код валюты, на которую хотите обменять: ', end=' ')

    key=input()

    if key in currency_cods:
        return key
    else:
        return 0
'''
print('Приветствуем в программе обмена валюты!')

def get_money():
      money=int(input('Введите сумму денег, которые вы хотите обменять: '))
      if money > 0:
          return money
      return 0

def get_first_money_cod(currency_cods):
    for cod in currency_cods:
        print(cod)    
    cod1=int(input('Введите код валюты, которую хотите обменять: ', end=' '))
    return cod1


def get_second_money_cod(currency_cods):
    for cod in currency_cods:
        print(cod)    
    cod2=int(input('Введите код валюты, на которую хотите обменять: ', end=' '))
    return cod2

def exchange_engine(cod1, cod2):

    money = get_money()
    if not money:
        print('ERROR!')
        return

    EUR=87
    USD=73
    YEN=1.5
    YUAN=11
    RUB=1
    currency_cods = ['EUR 400', 'USD 401', 'YEN 402', 'YUAN 403', 'RUB 404']
    if cod1:
        if cod1==currency_cods[0]:
            if cod2==currency_cods[0]:
                print('К выдаче {0:0.2f} EUR'.format(EUR/EUR))
            elif cod2==currency_cods[1]:
                print('К выдаче {0:0.2f} USD'.format(EUR/USD))
            elif cod2==currency_cods[2]:
                print('К выдаче {0:0.2f} YEN'.format(EUR/YEN))
            elif cod2==currency_cods[3]:
                print('К выдаче {0:0.2f} YUAN'.format(EUR/YUAN))
            elif cod2==currency_cods[4]:
                print('К выдаче {0:0.2f} RUB'.format(EUR/RUB))
        elif cod1==currency_cods[1]:
            if cod2==currency_cods[0]:
                print('К выдаче {0:0.2f} EUR'.format(USD/EUR))
            elif cod2==currency_cods[1]:
                print('К выдаче {0:0.2f} USD'.format(USD/USD))
            elif cod2==currency_cods[2]:
                print('К выдаче {0:0.2f} YEN'.format(USD/YEN))
            elif cod2==currency_cods[3]:
                print('К выдаче {0:0.2f} YUAN'.format(USD/YUAN))
            elif cod2==currency_cods[4]:
                print('К выдаче {0:0.2f} RUB'.format(USD/RUB))
        elif cod1==currency_cods[2]:
            if cod2==currency_cods[0]:
                print('К выдаче {0:0.2f} EUR'.format(YEN/EUR))
            elif cod2==currency_cods[1]:
                print('К выдаче {0:0.2f} USD'.format(YEN/USD))
            elif cod2==currency_cods[2]:
                print('К выдаче {0:0.2f} YEN'.format(YEN/YEN))
            elif cod2==currency_cods[3]:
                print('К выдаче {0:0.2f} YUAN'.format(YEN/YUAN))
            elif cod2==currency_cods[4]:
                print('К выдаче {0:0.2f} RUB'.format(YEN/RUB))
        elif cod1==currency_cods[3]:
            if cod2==currency_cods[0]:
                print('К выдаче {0:0.2f} EUR'.format(YUAN/EUR))
            elif cod2==currency_cods[1]:
                print('К выдаче {0:0.2f} USD'.format(YUAN/USD))
            elif cod2==currency_cods[2]:
                print('К выдаче {0:0.2f} YEN'.format(YUAN/YEN))
            elif cod2==currency_cods[3]:
                print('К выдаче {0:0.2f} YUAN'.format(YUAN/YUAN))
            elif cod2==currency_cods[4]:
                print('К выдаче {0:0.2f} RUB'.format(YUAN/RUB))
        elif cod1==currency_cods[4]:
            if cod2==currency_cods[0]:
                print('К выдаче {0:0.2f} EUR'.format(RUB/EUR))
            elif cod2==currency_cods[1]:
                print('К выдаче {0:0.2f} USD'.format(RUB/USD))
            elif cod2==currency_cods[2]:
                print('К выдаче {0:0.2f} YEN'.format(RUB/YEN))
            elif cod2==currency_cods[3]:
                print('К выдаче {0:0.2f} YUAN'.format(RUB/YUAN))
            elif cod2==currency_cods[4]:
                print('К выдаче {0:0.2f} RUB'.format(RUB/RUB))
    

'''
def get_money():
      money=int(input('Введите сумму денег, которые вы хотите обменять: '))
      if money > 0:
          return money
      return 0
'''
'''
def main():
    EUR=87
    USD=73
    YEN=1.5
    YUAN=11
    RUB=1
    currency_cods = ['EUR 400', 'USD 401', 'YEN 402', 'YUAN 403', 'RUB 404']
    
    money = get_money()
    if not money:
        print('ERROR!')
        return

    cod =  get_first_money_cod(currency_cods)
    cod2 =  get_second_money_cod(currency_cods)
    if cod2:
        if cod2==currency_cods[0]:
            print('К выдаче {0:0.2f} EUR'.format(money/EUR))         
        elif cod2 == currency_cods[1]:
            print('К выдаче {0:0.2f} USD'.format(money/USD))
        elif cod2 == currency_cods[2]:
            print('К выдаче {0:0.2f} YEN'.format(money/YEN))
        elif cod2==currency_cods[3]:
            print('К выдаче {0:0.2f} YUAN'.format(money/YUAN))
    else:
        print('ERROR!')
'''

if __name__=='__main__':
    exchange_engine()







































