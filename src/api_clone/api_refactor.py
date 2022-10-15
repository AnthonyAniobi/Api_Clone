import json


class ApiRefactor:
    map:dict
    folder_name:str
    view_log:bool

    def __init__(self, response:str) -> None:
        self.map = json.loads(response)

    def __recursiveRemove(self, data:dict|list|str, key_name:str):
        if type(data) is dict:
            if key_name in data.keys():
                data.pop(key_name)
            else:
                for key, val in data.items():
                    data[key] = self.__recursiveRemove(val, key_name)
        elif type(data) is list:
            for index in range(len(data)):
                data[index] = self.__recursiveRemove(data[index], key_name)
        else:
            pass

    def removeField(self, key_name:str)->dict:
        '''remove every occurence of a key with the key_name specified'''
        temp_data = self.map.copy()
        self.__recursiveRemove(temp_data, key_name)
        return temp_data


if __name__ == '__main__':
    json_map = {"some": 23, "test": "some_test", "values": 32}
    json_data = json.dumps(json_map)
    api_refactor = ApiRefactor(json_data)
    result = api_refactor.removeField("test")
    print(json_data)
    print (api_refactor.map)
    print(result)