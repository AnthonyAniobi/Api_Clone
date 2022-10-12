import os
from . import image_downloader, test_json
# from modules.image_downloader import imageDownloader
# from modules.test_json import map

def jsonImageDownloader(json:dict, image_path:str='images', file_format:str='jpeg')->None:
    
    if not os.path.isdir(image_path):
        os.mkdir(image_path)
    
    

    def __jsonScraper(data):
        if data is dict:
            for key in data.keys:
                __jsonScraper(data[key])
        elif data is list:
            for val in data:
                __jsonScraper(data)
        else:
            if data.split('.')[0].lower() in ('png', 'jpg', 'jpeg'):
                image_downloader.imageDownloader(data, file_format, image_path)


if __name__ == "__main__":
    jsonImageDownloader(test_json.map, 'test_images', '.png')