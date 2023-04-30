import function
import PySimpleGUI as ui
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

ui.theme('Black')

clock = ui.Text('', key='clock')
label = ui.Text("Enter a todo:")
input_box = ui.InputText(tooltip="Type here", key="todo")
# add_button = ui.Button(size=4, image_filename="add.png", key='Add', tooltip="Add")
add_button = ui.Button(size=5, button_text="Add", key="Add")
list_box = ui.Listbox(values=function.file_read(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = ui.Button("Edit")
# complete_button = ui.Button(size=4, image_filename="complete.png", tooltip="Complete", key="Complete")
complete_button = ui.Button(size=8, key="Complete", button_text="Complete")
exit_button = ui.Button("Exit")

window = ui.Window("My-To do app",
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, value = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%d-%m-%Y %H:%M:%S"))
    # print(event)
    # print(value)
    # print(value['todos'])
    if event == "Add":
        todo_list = function.file_read()
        new_todo = value['todo']+"\n"
        todo_list.append(new_todo.capitalize())
        function.file_write(todo_list)
        window['todos'].update(values=function.file_read())

    if event == "Edit":
        try:
            selected_todo = value['todos'][0]
            edited_todo = value['todo']

            todos = function.file_read()
            index = todos.index(selected_todo)
            todos[index] = edited_todo.capitalize()+"\n"
            function.file_write(todos)
            window['todos'].update(values=todos)
        except IndexError:
            ui.popup("Please select the item first.",font=("Helvetica", 13))

    if event == 'todos':
        window['todo'].update(value=value['todos'][0])

    if event == 'Complete':
        try:
            selected_todo = value['todos'][0]
            todos = function.file_read()
            index = todos.index(selected_todo)
            todos.pop(index)
            function.file_write(todos)
            window['todos'].update(values=function.file_read())
            window['todo'].update(value='')
        except IndexError:
            ui.popup("Please select the item first.", font=("Helvetica", 13))

    if event == ui.WIN_CLOSED or event == 'Exit':
        break

window.close()
