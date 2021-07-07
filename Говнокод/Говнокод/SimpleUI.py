users = []
password1 = []


def add_new_user():
    print('Type your username: ')
    while 1:
        username = input()
        flag, user = compare_username(username)
        if not flag:
            break
        print('This Username Is Not Available! Try Again ')
    print('Type your password: ')
    password1 = input()
    while 1:
        print('Repeat password: ')
        password2 = input()
        if password1 == password2:
            print('User Added Succesfully!')
            break
        else: 
            print('Incorrect Password, ')

    users.append([username, password1])


def compare_username(username):
    for user in users:
        if username == user[0]:
            return 1, user
    return 0, 0
    

def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0

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
    print('Welcome back, {}!'.format(user[0]))
    while in_user(user):
        continue
        


def get_mod_number(mods):
    mod = input()
    if mod in mods:
        return mod
    else:
        return 0
        
def in_user(user):
    in_mods = {'1': change_username,
              '2': change_password,
              '3': exit_to_menu}

    print('1 - Change Username')
    print('2 - Change Password')
    print('3 - Exit to Menu')

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
    print('You have succesfully changed username!')
    user[0] = username 
    return 1


def change_password(user):
    while 1:
        print('Type new Password: ')
        password1 = input()
        if user[1] != password1:
            break
        else:
            print('You cannot set existing password! Try Again')
    print('You have succesfully changed password!')
    user[1] = password1
    return 1


def exit_to_menu(user):
    return 0


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
    main()