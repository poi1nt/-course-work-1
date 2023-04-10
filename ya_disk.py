import requests
import datetime

class YandexDisk:
    def __init__(self, tokenYA):
        self.tokenYA = tokenYA
        self.headers = {'Authorization': self.tokenYA}
        self.date = datetime.datetime.now()

    def upload_file_to_disk(self, file_name, download_URL, id_user):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': f'{id_user}/{self.date.strftime("%d-%m-%y %H.%M")}/{file_name}', 'url': download_URL}
        headers = self.headers
        response = requests.post(url, params=params, headers=headers)
        return response
    
    def new_folder(self, id_user):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': f'{id_user}/'}
        headers = self.headers
        requests.put(url, params=params, headers=headers)
        params = {'path': f'{id_user}/{self.date.strftime("%d-%m-%y %H.%M")}'}
        response = requests.put(url, params=params, headers=headers)
        return response
    
    def upload_json_to_disk(self, id_user):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        files = {'file': open('data.txt', 'rb')}
        params = {'path': f'{id_user}/{self.date.strftime("%d-%m-%y %H.%M")}/data.txt', 'overwrite': True}
        headers = self.headers
        href = requests.get(url, params=params, headers=headers).json()['href']
        response = requests.put(href, files=files)
        return response



    