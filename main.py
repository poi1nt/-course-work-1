import requests
import time

with open('info/token.txt', 'r') as file_object:
    token = file_object.read().strip()

url = 'https://api.vk.com/method/photos.getAll'





