import sys
from Actions import ToDoList

todo_list_obj = ToDoList()

for i in range(1, len(sys.argv)):
    match sys.argv[i]:
        case "h":
            ToDoList.h()
        case "ls":
            todo_list_obj.ls()
        case "a":
            title = str(sys.argv[i + 1])
            todo_list_obj.a(title)
        case "e":
            idx = int(sys.argv[i + 1])
            title = str(sys.argv[i + 2])
            todo_list_obj.e(idx, title)
        case "d":
            idx = int(sys.argv[i + 1])
            todo_list_obj.d(idx)
        case "t":
            idx = int(sys.argv[i + 1])
            todo_list_obj.t(idx)
        case "s":
            title = str(sys.argv[i + 1])
            todo_list_obj.s(title)
