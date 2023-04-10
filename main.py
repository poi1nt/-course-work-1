import requests
import datetime
import os
import json
from ya_disk import YandexDisk
from tqdm import tqdm

with open('info/tokenVK.txt', 'r') as file_object:
    tokenVK = file_object.read().strip()

with open('info/tokenYA.txt', 'r') as file_object:
    tokenYA = file_object.read().strip()

def download_photos(id_user, tokenVK):
    url = 'https://api.vk.com/method/photos.getAll'
    params = {
        'owner_id': id_user,
        'extended': '1,likes',
        'access_token': tokenVK,
        'v': '5.131',
        'photo_sizes': '1'
    }
    list_photo_name = []
    info = []
    res = requests.get(url, params).json()
    p = res['response']['items']
    for item in tqdm(p):
        photo_name = item['likes']['count']
        if photo_name in list_photo_name:
            date = datetime.date.fromtimestamp(item['date'])
            photo_name = f'{photo_name} ({date})'
        for photo in item['sizes']:
            size = photo['type']
            if size == 'z':
                list_photo_name.append(photo_name)
                info.append({'file_name': str(photo_name) + '.jpg', 'size': size})
                download_URL = photo['url']
                YandexDisk.upload_file_to_disk(ya, photo_name, download_URL, id_user)
    
    with open('data.txt', 'a') as file:
        json.dump(info, file, indent=4)

if __name__ == '__main__':
    ya = YandexDisk(tokenYA)
    # id_user = input('Введите id пользователя: ') #'280602905'
    id_user = '280602908'
    YandexDisk.new_folder(ya, id_user)
    download_photos(id_user, tokenVK)
    YandexDisk.upload_json_to_disk(ya, id_user)
    os.remove('data.txt')
    