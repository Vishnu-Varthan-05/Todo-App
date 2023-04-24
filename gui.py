import function
import PySimpleGUI as ui

label = ui.Text("Enter a todo:")
input_box = ui.InputText(tooltip="Type here", key="todo")
add_button = ui.Button("Add")

window = ui.Window("My-To do app",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))
while True:
    event, value = window.read()
    print(event)
    print(value)
    if event == "Add":
        todo_list = function.file_read()
        new_todo = value['todo']+"\n"
        todo_list.append(new_todo.title())
        function.file_write(todo_list)
    elif ui.WIN_CLOSED == ui.WIN_CLOSED:
        break

window.close()


