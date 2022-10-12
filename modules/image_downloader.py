import os

from PIL import Image
import requests
from io import BytesIO

def imageDownloader(image_url:str, file_format:str='jpg', image_folder:str='images', image_name:str=None)->str|None:
    response = requests.get(image_url)
    if image_name is None:
        image_name = image_url.split('/')[-1]
        image_name = image_name.split('.')[0]
    
    if response.status_code == 200:
        if not os.path.isdir(image_folder):
            os.mkdir(image_folder)

        img = Image.open(BytesIO(response.content))
        img.save(f'{image_folder}/{image_name}.{file_format}')
        print(f'Saved image as => {image_name} !')
        return image_name

    else:
        print(f'could not download image {image_name} with url: {image_url}')
        


if __name__ == '__main__':
    imageDownloader('https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg');
