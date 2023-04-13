import os
import json
import datetime
from ya_disk import YandexDisk
from VK import VK

# tokenVK = ''
# tokenYA = ''

if __name__ == '__main__':
    date = datetime.datetime.now().strftime("%d-%m-%y %H.%M")
    tokenYA = input('Введите токен яндекс диска: ')
    ya = YandexDisk(tokenYA)
    id_user = input('Введите id пользователя: ')
    count = input('Введите число фотографий, которое хотите загрузить (по умолчанию 5): ')
    user_name = VK.user_name(tokenVK, id_user)
    YandexDisk.new_folder(ya, id_user, date, user_name)
    if count == '':
        info, dict_download_photo = VK.download_photos(tokenVK, id_user)
    else:
        info, dict_download_photo = VK.download_photos(tokenVK, id_user, count)
    YandexDisk.upload_file_to_disk(ya, date, id_user, dict_download_photo)

    os.remove('data.txt')
    with open('data.txt', 'a') as file:
        json.dump(info, file, indent=4)