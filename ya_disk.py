import requests
from tqdm import tqdm

class YandexDisk:
    def __init__(self, tokenYA):
        self.tokenYA = tokenYA
        self.headers = {'Authorization': self.tokenYA}

    def upload_file_to_disk(self, date, id_user, dict_download_photo):
        for photo_name, download_URL in tqdm(dict_download_photo.items()):
            url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {'path': f'{id_user}/{date}/{photo_name}', 'url': download_URL}
            headers = self.headers
            requests.post(url, params=params, headers=headers)
    
    def new_folder(self, id_user, date, user_name):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': f'{user_name}({id_user})/'}
        headers = self.headers
        requests.put(url, params=params, headers=headers)
        params = {'path': f'{user_name}({id_user})/{date}'}
        requests.put(url, params=params, headers=headers)
    