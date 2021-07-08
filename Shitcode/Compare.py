from SimpleUI import users

def compare_username(username):
    for user in users:
        if username == user[0]:
            return 1, user
    return 0, 0
    
def compare_password(pwd, user):
    if pwd == user[1]:
        return 1
    return 0

if __name__=='__main__':
    users.append(['test', 'test'])
    print(compare_username('New'))
    print(compare_username('test'))
