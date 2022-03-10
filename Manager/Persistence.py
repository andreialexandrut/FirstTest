import json


class DataPersistence:
    @staticmethod
    def write_json(todo_list):
        tmp_list = []
        for i in range(len(todo_list)):
            actual = todo_list[i]
            if type(actual) is dict:
                tmp_list.insert(i, actual)
            else:
                tmp_dict = {
                    "id": actual[0],
                    "title": actual[1],
                    "timestamp": actual[2],
                    "done": actual[3],
                }
                tmp_list.insert(i, tmp_dict)
        with open("TODO list.json", "w") as outpfile:
            json.dump(tmp_list, outpfile, indent=4)

    @staticmethod
    def read_json():
        try:
            with open("TODO list.json", "r") as inpfile:
                tmp_list = json.load(inpfile)
            return tmp_list
        except (KeyError, ValueError, FileNotFoundError):
            return []
