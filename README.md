## Project description

![issues](https://img.shields.io/github/issues/AnthonyAniobi/Api_Clone)
![forks](https://img.shields.io/github/forks/AnthonyAniobi/Api_Clone)
![stars](https://img.shields.io/github/stars/AnthonyAniobi/Api_Clone)
![license](https://img.shields.io/github/license/AnthonyAniobi/Api_Clone)

This is a utility project that helps you download files attached to an api response and save them locally. It also includes method for downloading network images to your local storage.

The `api_server.api_downloader` manages all downloads for images linked with any json response.

## Supported Input Types
The `api-clone` supports both json and normal python dictionaries for scraping api response. For downloading urls from url, a string would be required 

## Installation
The installation is simple:
```
pip install api-clone
```

## Usage
1. To download a single image from a url
```
from api_clone.api_downloader import saveImage

saveImage(image_url='url_of_image', folder_name='name of folder to save the image')
```

2. To save all images from a json response locally on your device
```
from api_clone.api_downloader import ApiDownloader

downloader = ApiDownloader(your_json_response_here)
downloader.downloadAllImages(folder_name='name of folder for saving images')
```

3. Save all images under a specific `key` in the json file. This method saves images with values having the same key as you specified.

```
from api_clone.api_downloader import ApiDownloader

downloader = ApiDownloader('json_response')
downloader.downloadImagesAtKey(key_name='name of image key', folder_name='folder name')
```

## Fields

| field | type | Default | description |
|-------|-------|-----|--------|
| map | `dict`| `None`| json response|
| folder_name | `str`|`images`| name of the folder where your images are saved|
| image_format | `ImageFormat`|`ImageFormat.jpg`| format to save the image ie. `png`, `jpg`, `jpeg`|

## Features
- Download all network images referenced from a json file
- Rename image json with names of local images on the pc