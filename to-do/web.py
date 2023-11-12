import streamlit as st
from fns import get_todos, write_todos

todos = get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    write_todos(todos)


st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label='New todo', 
              placeholder="Add new todo...", 
              key="new_todo", 
              on_change=add_todo,
              label_visibility='hidden')

st.session_state
