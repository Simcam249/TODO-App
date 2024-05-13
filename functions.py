FILEPATH = "todos.txt"

def get_todos(file_path = FILEPATH):
    with open(file_path,mode="r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg,file_path=FILEPATH):
    with open(file_path,mode="w") as file:
        file.writelines(todos_arg)

