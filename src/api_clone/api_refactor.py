import json


class ApiRefactor:
    map:dict
    folder_name:str
    view_log:bool

    def __init__(self, response:str) -> None:
        self.map = json.loads(response)

    def __recursiveRename(self, data:dict|list|str, key_name:str):
        if type(data) is dict:
            if key_name in data.keys():
                data.pop(key_name)
                return data
            else:
                for key, val in data.items():
                    return self.__recursiveRename(val, key_name)  
        elif type(data) is list:
            for val in data:
                return self.__recursiveRename(val, key_name)
        else:
            return data

    def removeField(self, key_name:str)->dict:
        '''remove a key with name'''
        return self.__recursiveRename(map, key_name)


if __name__ == '__main__':
    json_map = {"some": 23, "test": "some test", "values": 32}
    json_data = json.dumps(json_map)
    api_refactor = ApiRefactor(json_data)
    result = api_refactor.removeField("test")
    print(json_data)