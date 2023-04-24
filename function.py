def file_write(todo_list):
    with open("todos.txt", "w") as file:
        file.writelines(todo_list)


def file_read():
    with open("todos.txt", "r") as file:
        local_todo_list = file.readlines()
        return local_todo_list


if __name__ == "__main__":
    print(__name__)
    print("hello")