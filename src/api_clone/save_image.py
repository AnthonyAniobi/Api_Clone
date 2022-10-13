from io import BytesIO
from PIL import Image
import os

import requests

def saveImage(image_url:str, folder_name:str='images', image_format:ImageFormat=ImageFormat.JPG, view_log:bool=True, image_name:str|None=None)->str|None:
    '''Save an image from Url'''
    response = requests.get(image_url)
    
    if image_name is None:
        image_name = image_url.split('/')[-1]
        image_name = image_name.split('.')[0]
    
    if response.status_code == 200:
        if not os.path.isdir(folder_name):
            if view_log:
                print(f'creating folder => {folder_name}')
            os.mkdir(folder_name)
        img = Image.open(BytesIO(response.content))
        img.save(f'{folder_name}/{image_name}.{image_format}')
        if view_log:
            print(f'Saved image as => {image_name} !')
    else:
        if view_log:
            print(f'Couldn\'t get image \nCheck your internet connection!')