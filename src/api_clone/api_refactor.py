import json


class ApiRefactor:
    map:dict
    folder_name:str
    view_log:bool

    def __init__(self, response:str) -> None:
        self.map = json.loads(response)