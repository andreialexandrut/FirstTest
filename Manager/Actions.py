from datetime import datetime
from time import sleep
from Validate import ValidateActions
from Persistence import DataPersistence


class ToDoList:

    def __init__(self):
        self.todo_list = DataPersistence.read_json()

    def __check_actual_id(self):
        return len(self.todo_list)

    @staticmethod
    def h():
        cmd = ["h", "ls", "a (params: title)", "e (params: id, title)",
               "d (params: id)", "t (params: id)", "s (params: il termine da cercare)"]
        for i in cmd:
            print(i)

    def ls(self):
        latest_datetime = []
        for i in range(len(self.todo_list)):
            extract_datetime = self.todo_list[i]
            if type(extract_datetime) is dict:
                latest_datetime.insert(i, extract_datetime["timestamp"])
            elif type(extract_datetime) is list: # Just for debug
                latest_datetime.insert(i, extract_datetime[2])
        if len(latest_datetime) > 1:
            latest_datetime.sort(reverse=True)
        if len(latest_datetime) > 0:
            for i in range(len(latest_datetime)):
                for j in range(len(self.todo_list)):
                    actual = self.todo_list[j]
                    if type(actual) is list: # Just for debug
                        if actual[2] == latest_datetime[i]:
                            print(actual)
                    elif type(actual) is dict:
                        if actual["timestamp"] == latest_datetime[i]:
                            print(actual)

    def a(self, title):
        if ValidateActions.check_title(title):
            actual_datetime = datetime.now()
            self.todo_list.insert(self.__check_actual_id(),
                                  [self.__check_actual_id(), title, actual_datetime.timestamp(), False])
            DataPersistence.write_json(self.todo_list)
            sleep(0.1)  # I must use a latency cause i may have some problems with the timestamps

    def e(self, todo_id, title):
        if self.__check_actual_id() > todo_id:  # I can't modify something that does not exist..
            if ValidateActions.check_title(title):
                actual_datetime = datetime.now()
                self.todo_list[todo_id] = [todo_id, title, actual_datetime.timestamp(), False]
                DataPersistence.write_json(self.todo_list)
                sleep(0.1)  # I must use a latency cause i may have some problems with the timestamps
        else:
            print("Wrong index")

    def d(self, todo_id):
        for i in range(len(self.todo_list)):
            actual = self.todo_list[i]
            if type(actual) is list:
                # That's just for debug
                if actual[0] == todo_id:
                    del self.todo_list[i]
                    DataPersistence.write_json(self.todo_list)
                    break
            elif type(actual) is dict:
                if actual["id"] == todo_id:
                    del self.todo_list[i]
                    DataPersistence.write_json(self.todo_list)
                    break

    def t(self, todo_id):
        if self.__check_actual_id() > todo_id:  # I can't modify something that does not exist..
            actual = self.todo_list[todo_id]
            if type(actual) is list:
                # That's just for debug
                if not actual[3]:
                    actual[3] = True
                    self.todo_list[todo_id] = actual
                    DataPersistence.write_json(self.todo_list)
            elif type(actual) is dict:
                if not actual["done"]:
                    actual["done"] = True
                    self.todo_list[todo_id] = actual
                    DataPersistence.write_json(self.todo_list)
        else:
            print("Wrong index")

    def s(self, title):
        equals = 0
        if len(self.todo_list) > 0:
            for i in range(len(self.todo_list)):
                actual = self.todo_list[i]
                # That's just for debug
                if type(actual) is list:
                    actual_title = [char for char in actual[1]]
                    title_searched = [char for char in title]
                    for j in range(len(title_searched)):
                        if j < len(actual_title) and j < len(title_searched):  # I don't want an overflow..
                            if actual_title[j] == title_searched[j]:
                                equals += 1
                                if equals == len(title_searched):
                                    print(actual)
                                    equals = 0
                elif type(actual) is dict:
                    actual_title = [char for char in actual["title"]]
                    title_searched = [char for char in title]
                    for j in range(len(title_searched)):
                        if j < len(actual_title) and j < len(title_searched):  # I don't want an overflow..
                            if actual_title[j] == title_searched[j]:
                                equals += 1
                                if equals == len(title_searched):
                                    print(actual)
                                    equals = 0
        else:  # empty file
            print([])
