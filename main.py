import requests
import datetime
from pprint import pprint
import json

with open('info/token.txt', 'r') as file_object:
    token = file_object.read().strip()

def register_info(photo_name, size):
    info = []
    info.append({'file_name': str(photo_name) + '.jpg', 'size': size})
    with open('data.txt', 'a') as file:
        json.dump(info, file, indent=4)

def dounload_photos(id_user, token):
    url = 'https://api.vk.com/method/photos.getAll'
    params = {
        'owner_id': id_user,
        'extended': '1,likes',
        'access_token': token,
        'v': '5.131',
        'photo_sizes': '1'
    }
    list_photo_name = []
    res = requests.get(url, params).json()
    p = res['response']['items']
    pprint(p)
    for item in p:
        photo_name = item['likes']['count']
        if photo_name in list_photo_name:
            date = datetime.date.fromtimestamp(item['date'])
            photo_name = f'{photo_name} ({date})'
        for photo in item['sizes']:
            size = photo['type']
            if size == 'o':
                list_photo_name.append(photo_name)
                register_info(photo_name, size)
                dounload_photo = requests.get(photo['url'], allow_redirects=True)
                open(f'{photo_name}.jpg', 'wb').write(dounload_photo.content)


dounload_photos('280602905', token)
