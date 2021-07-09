#Simple User Interface
#Made by voooltexx

users = []
password1 = []

def add_new_user():
    print('Press "E" to Exit')
    print('Create Username: ')
    while 1:
        username = input()
        flag, user = compare_username(username)
        if username.upper() == 'E':
            return
        if not flag:
            break
        print('This Username Is Not Available! ')
    while 1:
        print('Create Password: ')
        password1 = input()
        if password1.upper() == 'E':
            return
        if len(password1) 3:
            break
        print('Password Must Have At Least 3 Symbols!')

    while 1:
        print('Repeat password: ')
        password2 = input()
        if password1.upper() == 'E':
            return
        if password1 == password2:
            print('User Added Succesfully!')
            break
        else: 
            print('Incorrect Password! ')

    users.append([username, password1, 0])
    f = open('uidatabase.txt', 'w')
    for user in users:
        f.write('{} {} {}\n'.format(user[0], user[1], 0))
    f.close()


def log_in():
    print('Available Users: ')
    f = open('uidatabase.txt', 'r')
    for user in users:
        print('{}'.format(user[0], '\n'))
    f.close()
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
        print('Incorrect Password, Try Again:')
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
    print('Available Actions: +, -, //, *')
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
    elif sign =='*':
        print ('The Product Of Digits Is ')
        print(a*b)
        calculator(user)
    elif sign =='//':
        if b==0:
            print ('You Cannot Divide By Zero!')
            calculator(user)
        if b>0 or b<0:
            print('The Quotient Is ')
            print(a//b)
            calculator(user)
    else:
        print('Wrong Action!')
        calculator(user)


def bank(user):
    print('Welcome To Bank App! Type E to Exit. ')
    print('Your Balance Is:')
    print('Choose User You Want Send Money To: ')
    f = open('uidatabase.txt', 'r')
    user2 = user
    while 1:
        for user in users:
            print('{}'.format(user[0], '\n'))
        choice = input()
        if choice.upper() == 'E':
            return 1
        elif choice == user2[0]:
            print('You Cannot Send Money To Yourself! ')
            continue
        elif choice == user[0]:
            print('Type 1 to Return.')
            print('Please, Type How Much Money You Want To Send: ')
            try:
                money=int(input())
            except:
                print('Wrong Number!')
                continue

        

def bank_balance():
    pass               



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
    in_mods = {'1': calculator,
               '2': bank,
               '3': change_username,
               '4': change_password,
               '5': exit_to_menu,
               '6': delete_user}

    print('1 - Open Calculator App')
    print('2 - Open Bank App')
    print('3 - Change Username')
    print('4 - Change Password')
    print('5 - Exit To Menu')
    print('6 - Delete User')

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
    print('If You Want To Exit, Type "E" ')
    while 1:
        print('Create New Password: ')
        password1 = input()
        if password1.upper() == 'E':
            return 1
        if user[1] != password1:
            f = open('uidatabase.txt', 'w')
            user[1] = password1
            print('You Have Succesfully Changed Password!')
            for user in users:
                f.write('{} {}\n'.format(user[0], user[1]))
            f.close()
            return 0
        print('You Cannot Set Existing Password!')
        change_password(user)


def exit_to_menu(user):
    print('Are You Sure You Want To Exit? Type "yes" or "no"')
    confirmation = input()
    if confirmation.lower() == 'yes':         
        print('See You Again, {}!'.format(user[0]))
        return 0
    if confirmation.lower() == 'no':
        in_user(user)
    else:
        print('Wrong Option!')
        exit_to_menu(user)


def menu():
    mods = {'1': log_in,
            '2': add_new_user,
            '3': exit}
            
    print('1 - Log In')
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
