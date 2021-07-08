users = []
password1 = []
#from Compare import *


def add_new_user():
    print('Create New Username: ')
    while 1:
        username = input()
        flag, user = compare_username(username)
        if not flag:
            break
        print('This Username Is Not Available! Try Again ')
    while 1:
        print('Create New Password: ')
        password1 = input()
        if len(password1) > 3:
            break 
        print('Password Is Too Short')
    while 1:
        print('Repeat password: ')
        password2 = input()
        if password1 == password2:
            print('User Added Succesfully!')
            break
        else: 
            print('Incorrect Password! ')

    users.append([username, password1])
    f = open('uidatabase.txt', 'w')
    for user in users:
        f.write('{} {}\n'.format(user[0], user[1]))
    f.close()


def enter():
    print('Type Your Username: ')
    while 1:
        flag, user = compare_username(input())
        if flag:
            break
        print('User Does Not Exist, Try Again')
    print('Type Your Password: ')
    while 1:
        if compare_password(input(), user):
            break
    print('Incorrect Password, Try Again')
    print('Welcome Back, {}!'.format(user[0]))
    while in_user(user):
        continue


def compare_username(username):
    for user in users:
        if username == user[0]:
            return 1, user
    return 0, 0


def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0
    

def calculator(user):    
    print('Welcome to Calculator! Type E to Exit.')
    print ('Type First Digit: ')
    a = input()
    if a.upper() == 'E':
        in_user(user)
    a = float(a)
    print('Type Action: ')
    sign = input()
    if sign.upper() == 'E':
        in_user(user)
    print('Type Second Digit: ')
    b = input()
    if b.upper() == 'E':
        in_user(user)
    b = float(b)
    if sign =='+':
        print('Sum Is ')
        print(a+b)
        calculator(user)
    elif sign =='-':
        print ('The Difference Is ')
        print(a-b)
        calculator(user)
    elif sign =='*' or 'x':
        if b==0:
            print ('You Cannot Divide By Zero!')
            calculator(user)
        if b>0 or b<0:
            print('Product Of Digits is ')
            print(a*b)
            calculator(user)
    elif sign ==':' or '//':
        print ('The Quotient Is ')
        print(a//b)
        calculator(user)


def get_mod_number(mods):
    mod = input()
    if mod in mods:
        return mod
    else:
        return 0
        

def delete_user(user):
    print('Are You Sure You Want To Delete This User? Type "yes" or "no".')
    confirm=input()
    if confirm.lower() == 'yes':
            f = open('uidatabase.txt', 'w')
            users.remove(user)
            for user in users:
                f.write('{} {}\n'.format(user[0], user[1]))
            f.close()
            print('User Has Been Removed.')
            return 0
    else:
        return 1
        

def in_user(user):
    in_mods = {'1': change_username,
              '2': change_password,
              '3': exit_to_menu,
              '4': calculator,
              '5': delete_user}

    print('1 - Change Username')
    print('2 - Change Password')
    print('3 - Exit to Menu')
    print('4 - Open Calculator')
    print('5 - Delete User')

    in_mod = get_mod_number(in_mods)
    if in_mod:
        return in_mods[in_mod](user)
    else:
        print('Wrong Number!')


def change_username(user):
    while 1:
        print('Choose New Username: ')
        username = input()
        flag, _ = compare_username(username)
        if not flag:
            break
    print('You Have Succesfully Changed Username!')
    user[0] = username 
    f = open('uidatabase.txt', 'w')
    for user in users:
        f.write('{} {}\n'.format(user[0], user[1]))
    f.close()
    return 1


def change_password(user):
    while 1:
        print('if You Want To Exit, Type "Y" or Anything Else To Skip: ')
        confirm = input()
        if confirm.upper() == 'Y':
            return 1
        print('Create New Password: ')
        password1 = input()
        if user[1] != password1:
            break
        print('You Cannot Set Existing Password! Try Again Or Type "Y" to Exit.')
    f = open('uidatabase.txt', 'w')
    user[1] = password1
    print('You Have Succesfully Changed Password!')
    for user in users:
        f.write('{} {}\n'.format(user[0], user[1]))
    f.close()
    return 1


def exit_to_menu(user):
    print('See You Again, {}!'.format(user[0]))
    menu()


def menu():
    mods = {'1': enter,
            '2': add_new_user,
            '3': exit}
            
    print('1 - Enter')
    print('2 - Add New User')
    print('3 - Exit')

    mod = get_mod_number(mods)
    if mod:
        mods[mod]()
    else:
        print('Wrong Number!')


def main():
    while 1:
        menu()


if __name__=='__main__':
    f = open('uidatabase.txt', 'r')
    users = f.read().split('\n')
    for i in range (len(users)):
        users[i] = users[i].split()
    users.pop(len(users) - 1)
    f.close()
    main()