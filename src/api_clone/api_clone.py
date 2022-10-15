import json


class ApiClone:
    map:dict
    folder_name:str
    image_format:str
    view_log:bool=True

    def __init__(self, response:str) -> None:
        json.load(response)