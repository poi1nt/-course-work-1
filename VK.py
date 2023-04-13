import requests
import datetime

class VK:
    def download_photos(tokenVK, id_user, count = '5'):
        url = 'https://api.vk.com/method/photos.getAll'
        params = {
            'owner_id': id_user,
            'extended': '1',
            'access_token': tokenVK,
            'v': '5.131',
            'photo_sizes': '1',
            'count': count
        }
        list_photo_name = []
        info = []
        dict_download_photo = {}
        res = requests.get(url, params).json()
        p = res['response']['items']
        for item in p:
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
                    dict_download_photo[str(photo_name)] = download_URL
        return info, dict_download_photo
    
    def user_name(tokenVK, id_user):
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': id_user,
            'name_case': 'nom',
            'access_token': tokenVK,
            'v': '5.131'
        }
        res = requests.get(url, params).json()
        users = res['response']
        for user in users:
            user_name = f'{user["first_name"]} {user["last_name"]}'
        return user_name