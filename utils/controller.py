def get_user_info(users_data: list[dict]) -> None:
    for user in users_data:
        print(f'Twój znajomy: {user["Name"]} z: {user["Location"]} opublikował: {user["Posts"]}')


def add_user(user_data: list[dict]) -> None:
    tmp_Name: str = input('Podaj imię: ')
    tmp_Location: str = input('Podaj miejsce: ')
    tmp_Posts: int = int(input('Podaj liczbę postów: '))
    user_data.append({'Name': tmp_Name, 'Location': tmp_Location, 'Posts': int(tmp_Posts)})


def remove_user(users_data: list[dict]) -> None:
    user_Name = input('Podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['Name'] == user_Name:
            users_data.remove(user)


def update_user(users_data: list[dict]) -> None:
    user_Name = input('Podaj imię użytkownika do zmodyfikowania: ')
    for user in users_data:
        if user['Name'] == user_Name:
            user['Name'] = input('Podaj nowe imię: ')
            user['Location'] = input('Podaj nową lokalizację: ')
            user['Posts'] = input('Podaj nową liczbę postów: ')


def remove_user(users_data: list[dict]) -> None:
    user_Name = input('Podaj imię użytkownika do usunięcia: ')
    for user in users_data:
        if user['Name'] == user_Name:
            users_data.remove(user)


def get_coordinates(Location_name: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    adres_url: str = f'https://pl.wikipedia.org/wiki/{Location_name}'
    response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')

    return float(response_html.select('.latitude')[1].text.replace(',', '.')),
    [float(response_html.select('.longitude')[1].text.replace(',', '.')),

     ]


def get_map(users_data: list[dict]) -> None:
    import folium
    map = folium.Map(location=[52.3, ], zoom_start=6, tiles='OpenStreetMap')
    for user in users_data:
        print(get_coordinates(user['Location']))
        folium.Marker(
            location=get_coordinates(user['Location']),
            popup=f'<h5>{user['Location']}</h5><br/>{user['Name']}<br/>{user['Posts']}',
        ).add_to(map)
    map.save('Mapa.html')
