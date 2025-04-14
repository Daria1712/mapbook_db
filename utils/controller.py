def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy: {user["Name"]} z: {user["Location"]} opublikował: {user["Posts"]}')

def add_user(user_data: list[dict]) -> None:
    tmp_Name:str = input('Podaj imię: ')
    tmp_Location:str = input('Podaj miejsce: ')
    tmp_Posts:int = int(input('Podaj liczbę postów: '))
    user_data.append({'Name': tmp_Name, 'Location': tmp_Location, 'Posts': int(tmp_Posts)})

def remove_user(users_data: list[dict])-> None:
    user_Name=input('Podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['Name']==user_Name:
            users_data.remove(user)