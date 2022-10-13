from io import BytesIO
from PIL import Image
import json
import os

import requests

class ApiDownloader:

    map:dict
    image_folder:str
    image_format:str
    view_log:bool=True

    def __init__(self, response:str, image_format:str='jpg', image_folder:str='images') -> None:
        self.map = json.loads(response)
        self.image_folder = image_folder
        self.image_format = image_format

    def __isImage(self, image:str)->bool:
        return image.split('.')[-1].lower() in ('png', 'jpg', 'jpeg')

    def __jsonRecursiveImageDownloader(self, data:dict|list|str):
        '''recursive function to loop through json and get all files'''
        if type(data) is dict:
            for key,value in data.items():
                self.__jsonRecursiveImageDownloader(value)
        elif type(data) is list:
            for val in data:
                self.__jsonRecursiveImageDownloader(val)
        else:
            if type(data) is str:
                if self.__isImage(data):
                    self.saveImage(data)

    def __jsonRecurseImageDownloaderAtKey(self, data:dict|list|str, key_name:str):
        if type(data) is list:
            for val in data:
                self.__jsonRecurseImageDownloaderAtKey(val, key_name)
        elif type(data) is dict:
            if key_name in data.keys():
                if self.__isImage(data[key_name]):
                    self.saveImage(data[key_name])
                else:
                    print(f'value of {key_name}: is not an image')
            else:
                for key, val in data.items():
                    self.__jsonRecurseImageDownloaderAtKey(val, key_name)
        else:
            pass

    def saveImage(self, image_url:str, image_name:str|None=None)->str|None:
        '''Save an image from Url'''
        response = requests.get(image_url)
        
        if image_name is None:
            image_name = image_url.split('/')[-1]
            image_name = image_name.split('.')[0]
        
        if response.status_code == 200:
            if not os.path.isdir(self.image_folder):
                if self.view_log:
                    print(f'creating folder => {self.image_folder}')
                os.mkdir(self.image_folder)
            img = Image.open(BytesIO(response.content))
            img.save(f'{self.image_folder}/{image_name}.{self.image_format}')
            if self.view_log:
                print(f'Saved image as => {image_name} !')
        else:
            if self.view_log:
                print(f'Couldn\'t get image \nCheck your internet connection!')

    def downloadAllImages(self, folder_name:str|None=None):
        '''Scrape a json file and download all images recursively'''
        if self.view_log:
            print('downloading all images in api')

        __localFolder:str
        if folder_name:
            __localFolder = self.image_folder #store initial value of folder
            self.image_folder = folder_name
        self.__jsonRecursiveImageDownloader(self.map)
        self.image_folder = __localFolder #return the folder to initial value
        if self.view_log:
            print('Completed!')

    def downloadImagesAtKey(self, key_name:str, folder_name:str|None=None):
        '''Scrape a json file and download all images with the key_name you specify'''
        if self.view_log:
            print('downloading all images in api')
        
        __localFolder:str
        if folder_name:
            __localFolder = self.image_folder #store initial value of folder
            self.image_folder = folder_name
        self.__jsonRecurseImageDownloaderAtKey(self.map, key_name)
        self.image_folder = __localFolder #return the folder to initial value
        if self.view_log:
            print('Completed!')

    
        