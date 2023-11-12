import os

def get_todos(filepath='todos.txt'):
    if not os.path.exists("todos.txt"):
        with open(filepath, 'w') as file:
             pass
            
    with open(filepath) as file:
        todos = file.readlines()

    return todos

def write_todos(todos, filepath='todos.txt'):
    with open(filepath, 'w') as file:
            file.writelines(todos)