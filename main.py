users: list[dict] = [
    {'Name': 'Kinga', 'Location': 'Kozienice', 'Posts': 500, },
    {'Name': 'Wika', 'Location': 'Radzyń', 'Posts': 400, },
    {'Name': 'Daria', 'Location': 'Łosice', 'Posts': 200, }
]


def get_user_info(users_data: list[dict])->None:
    for user in users:
        print(f'Twój znajomy: {user["Name"]} z: {user["Location"]} opublikował: {user["Posts"]}')

get_user_info(users)
