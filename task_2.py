from pprint import pprint

import requests

TOKEN = ''


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
                   }
        return headers

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        pprint(response)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, path_filename):
        """Метод загружает файл filename на яндекс диск. disk_file_path -> путь до файла на yandex.disk """
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(path_filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return response.status_code


if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    uploader.upload_file_to_disk(disk_file_path="you_folder_on_yandex_disk/text.txt", path_filename="test.txt")