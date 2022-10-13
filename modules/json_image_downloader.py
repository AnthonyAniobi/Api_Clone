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
  

def jsonImageDownloader(json:dict, image_path:str='images', file_format:str='jpeg')->None:

    def __jsonScraper(data:dict|list|str|int):
        if data is dict:
            for key in data.keys:
                print('dict')
                __jsonScraper(data[key])
        elif data is list:
            print('list')
            for val in data:
                __jsonScraper(data)
        else:
            print('other')
            if data.split('.')[0].lower() in ('png', 'jpg', 'jpeg'):
                # imageDownloader(data, file_format, image_path)
                print(f'found in data: {data}')
            else:
                print(f'not found in data: {data}')


    if not os.path.isdir(image_path):
        os.mkdir(image_path)
    
    __jsonScraper(dict)



if __name__ == "__main__":

    test_result:dict = {
        'found': 123,
        'resulsts': [
            {
    "images":[
        "https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/x4cspjvzqn2qk76sjhiw.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768184/images/menus/ovni4qwzzxbufpsurlsg.jpg"
        ],"_id":"5f5eccf4e923d0aca3e7d442","menuname":"Pounded Yamm","description":"Yams that have been crushed or stirred to a creamy, dough - like consistency.Pounded yams are considered a fufu(a kind of starchy side dish) usually served with a stew or efo.","__v":0
        },{
    "images":[
        "https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/x4cspjvzqn2qk76sjhiw.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768184/images/menus/ovni4qwzzxbufpsurlsg.jpg"
        ],"_id":"5f5eccf4e923d0aca3e7d441","menuname":"Soup cream","description":"a soup prepared using cream, light cream, half and half or milk as a key ingredient. Sometimes the dairy product is added at the end of the cooking process, such as after a cream soup has been puréed.","__v":0
        },{
    "images":[
        "https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/x4cspjvzqn2qk76sjhiw.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768184/images/menus/ovni4qwzzxbufpsurlsg.jpg"
        ],"_id":"5f5eccf4e923d0aca3e7d445","menuname":"Egusi Soup","description":"A stew usually made with crayfish or other meat and thickened with ground melon seeds(egusi).","__v":0
        },{
    "images":[
        "https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/x4cspjvzqn2qk76sjhiw.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768184/images/menus/ovni4qwzzxbufpsurlsg.jpg"
        ],"_id":"5f5eccf4e923d0aca3e7d443","menuname":"Pepper Soups","description":"Light and spicy soup traditionally made with goat meat, but often with fish or other meat, as well as herbs and Nigerian spices.","__v":0
        },{
    "images":[
        "https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/x4cspjvzqn2qk76sjhiw.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768183/images/menus/xnurgo60mme1ewupfbin.jpg","https://res.cloudinary.com/jobizil/image/upload/v1602768184/images/menus/ovni4qwzzxbufpsurlsg.jpg"
        ],"_id":"5f5eccf4e923d0aca3e7d444","menuname":"Efo Riro","description":"A rich spinach stew usually made with spinach, scotch bonnets, and red bell peppers.","__v":0
        }
        ]
    }

    def jsonScraper(data:dict|list|str):
        if type(data) is dict:
            for key,value in data.items():
                jsonScraper(value)
        elif type(data) is list:
            for val in data:
                jsonScraper(val)
        else:
            if type(data) is str:
                if data.split('.')[-1].lower() in ('png', 'jpg', 'jpeg'):
                    # imageDownloader(data, file_format, image_path)
                    print(f'found in data: {data}')
                else:
                    print(f'not found in data: {data}')


    # jsonImageDownloader(test_result, 'test_images', '.png')
    jsonScraper(test_result)
    # print(type([1,2,3]))