from enum import Enum
import json

from .save_image import saveImage

class ApiDownloader:

    map:dict
    folder_name:str
    image_format:str
    view_log:bool=True

    def __init__(self, response:str, image_format:str='jpg', folder_name:str='images') -> None:
        self.map = json.loads(response)
        self.folder_name = folder_name
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
                    saveImage(data, self.folder_name, self.image_format, self.view_log)


    def __jsonRecurseImageDownloaderAtKey(self, data:dict|list|str, key_name:str):
        if type(data) is list:
            for val in data:
                self.__jsonRecurseImageDownloaderAtKey(val, key_name)
        elif type(data) is dict:
            if key_name in data.keys():
                if self.__isImage(data[key_name]):
                    saveImage(data[key_name], self.folder_name, self.image_format, self.view_log)
                else:
                    print(f'value of {key_name}: is not an image')
            else:
                for key, val in data.items():
                    self.__jsonRecurseImageDownloaderAtKey(val, key_name)
        else:
            pass

    def downloadImagesAtKey(self, key_name:str, folder_name:str|None=None):
        '''Scrape a json file and download all images with the key_name you specify'''
        if self.view_log:
            print('downloading all images in api')
        
        __localFolder:str
        if folder_name:
            __localFolder = self.folder_name #store initial value of folder
            self.folder_name = folder_name
        self.__jsonRecurseImageDownloaderAtKey(self.map, key_name)
        self.folder_name = __localFolder #return the folder to initial value
        if self.view_log:
            print('Completed!')


if __name__ == "__main__":
    json_data = {'name': 'Anthony', 'images':['www.something.jpg', 'www.another.jpg']}
    response = json.dumps(json_data)
    api_downloader = ApiDownloader(response)