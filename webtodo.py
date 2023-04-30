import streamlit as st
import function

todo_list = function.file_read()


def add_todo():
    loc_todo = st.session_state['new_todo'].capitalize()+"\n"
    todo_list.append(loc_todo)
    function.file_write(todo_list)


st.title("My Todo App")
for index, todos in enumerate(todo_list):
    checkbox = st.checkbox(todos, key=todos)
    if checkbox:
        todo_list.pop(index)
        function.file_write(todo_list)
        del st.session_state[todos]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")