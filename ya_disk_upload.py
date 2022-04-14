from pprint import pprint
import requests
import pathlib
from pathlib import Path
import os


dir_path = pathlib.Path.cwd()
folder_name_in_python_project = 'folder_of_files' #папка внутри Питона, где все файлы на загрузку
path_to_folder = Path(dir_path, folder_name_in_python_project)
path=Path(dir_path, folder_name_in_python_project)
host = 'https://cloud-api.yandex.net:443/'
upload_salt = 'v1/disk/resources/upload'
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_list = os.listdir(path_to_folder)
        for file_name in file_list:
            value_for_OAuth = 'OAuth ' + token
            h = {'Authorization': value_for_OAuth}
            file_name_with_slash = '/' + file_name
            p = {'path': file_name_with_slash, 'overwrite': 'true'}
            y_url_to_upload = requests.get(host+upload_salt, params=p, headers=h)
            y_url_to_upload = y_url_to_upload.json()['href']
            file_name_with_path = Path(path, file_name)
            response = requests.put(y_url_to_upload, headers=h, data=open(file_name_with_path, 'rb'))
            if response.status_code == 201:
                print(f"Файл {file_name} - успешно загружен")
            # """Метод загружает файлы по списку file_list на яндекс диск"""

if __name__ == '__main__':
#     Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = path
    token = 'AQAAAAAFlDqEAADLW4n5l3U0cEaFpK4I9vcgDa0'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
