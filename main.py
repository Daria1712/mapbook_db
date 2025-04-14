from utils.controller import get_user_info, add_user, remove_user
from utils.model import users



def main():
    while True:
        print('===================MENU==================')
        print('0 - Exit')
        print('1-Get user info')
        print('2 - Add user')
        print('3 - Remove user')
        print('=========================================')


        choice = input('Enter your choice:')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)

if __name__ == '__main__':
    main()
