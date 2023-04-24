from function import file_read, file_write
import time

now = time.strftime("%d-%m-%Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add ,show ,edit ,complete or exit:") or "exit"
    user_action = user_action.strip()

    if user_action.lower().startswith("add"):
        todo_list = file_read()
        todo = user_action[4:] + "\n"
        todo_list.append(todo.capitalize())
        file_write(todo_list)

    elif user_action.lower().startswith("show"):
        todo_list = file_read()
        list_for_show = [item.strip("\n") for item in todo_list]
        for i in range(0, len(list_for_show)):
             print(f"{i+1}) {list_for_show[i]}")

    elif user_action.lower().startswith("edit"):
        todo_list = file_read()
        try:
            edit = int(user_action[5:])-1
            new_todo = input("Edit to ").capitalize()
            todo_list[edit] = new_todo + "\n"
            file_write(todo_list)
        except ValueError and IndexError:
            print("Command is not valid")
            continue

    elif user_action.lower().startswith("complete"):
        todo_list = file_read()
        try:
            completed_todo = int(user_action[9:])-1
            removed_todo = todo_list.pop(completed_todo)
            removed_todo = removed_todo.strip("\n")
            print(f"Todo {removed_todo} was removed from the list")
            file_write(todo_list)
        except IndexError and ValueError:
            print("Command is not valid")
            continue

    elif user_action.lower().startswith("exit"):
        file_write(todo_list)
        break

    else:
        file_write(todo_list)
        break








