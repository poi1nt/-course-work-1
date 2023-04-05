import requests
import time
from pprint import pprint
import os

with open('info/token.txt', 'r') as file_object:
    token = file_object.read().strip()

def dounload_photos(id_user, token):
    url = 'https://api.vk.com/method/photos.getAll'
    params = {
        'owner_id': id_user,
        'extended': '1,likes',
        'access_token': token,
        'v': '5.131',
        'photo_sizes': '1'
    }
    res = requests.get(url, params).json()
    p = res['response']['items']
    for item in p:
        photo_name = item['likes']['count']
        for photo in item['sizes']:
            if photo['type'] == 'z':
                dounload_photo = requests.get(photo['url'], allow_redirects=True)
                open(f'{photo_name}.png', 'wb').write(dounload_photo.content)


dounload_photos('280602905', token)
