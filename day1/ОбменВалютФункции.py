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

def get_first_money_cod(money_cods):
    for cod_m in money_cods:
        print(cod_m)    
    cod_m=int(input('Введите код валюты, которую хотите обменять: '))
    #TODO  сделать проверку на существование
    return cod_m


def get_second_money_cod(money_cods):
    for cod_m in money_cods:
        print(cod_m)    
    cod_m=int(input('Введите код валюты, которую хотите обменять: '))
    #TODO  сделать проверку на существование
    return cod_m

def exchange_engine(cod1, cod2):
    pass
#TODO доделать


def get_money():
      money=int(input('Введите сумму денег, которые вы хотите обменять: '))
      if money > 0:
          return money
      return 0


def main():
    EUR=87
    USD=73
    YEN=1.5
    YUAN=11
    currency_cods = ['EUR 400', 'USD 401', 'YEN 402', 'YUAN 403', 'RUB 404']
    
    money = get_money()
    if not money:
        print('ERROR!')
        return

    key1 =  get_first_money_cod(currency_cods)
    key2 =  get_second_money_cod(currency_cods)
    if key:
        if key==currency_cods[0]:
            print('К выдаче {0:0.2f} EUR'.format(money/EUR))         
        elif key == currency_cods[1]:
            print('К выдаче {0:0.2f} USD'.format(money/USD))
        elif key == currency_cods[2]:
            print('К выдаче {0:0.2f} YEN'.format(money/YEN))
        elif key==currency_cods[3]:
            print('К выдаче {0:0.2f} YUAN'.format(money/YUAN))
    else:
        print('ERROR!')


if __name__=='__main__':
    main()







































