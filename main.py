from utils.controller import get_user_info, add_user, remove_user, update_user, get_map, get_coordinates
from utils.model import users


def main():
    while True:
        print('===================MENU==================')
        print('0 - Exit')
        print('1-Get user info')
        print('2 - Add user')
        print('3 - Remove user')
        print('4 - Update user')
        print('5 - Prepare map')
        print('=========================================')

        choice = input('Enter your choice:')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)


if __name__ == '__main__':
    main()
