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
                # return data
            else:
                for key, val in data.items():
                    data[key] = self.__recursiveRename(val, key_name)
                    # return {key:  self.__recursiveRename(val, key_name)}  
        elif type(data) is list:
            for index in range(len(data)):
                data[index] = self.__recursiveRename(data[index], key_name)
        else:
            pass
            # return data

    def removeField(self, key_name:str)->dict:
        '''remove every occurence of a key with the key_name specified'''
        temp_data = self.map.copy()
        self.__recursiveRename(temp_data, key_name)
        return temp_data


if __name__ == '__main__':
    json_map = {"some": 23, "test": "some_test", "values": 32}
    json_data = json.dumps(json_map)
    api_refactor = ApiRefactor(json_data)
    result = api_refactor.removeField("test")
    print(json_data)
    print (api_refactor.map)
    print(result)