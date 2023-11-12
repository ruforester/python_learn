from fns import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
        
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}. {todo}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            index = int(user_action[5:])
            index = index - 1
            todos[index] = input("Enter new todo:") + '\n'
            write_todos(todos)
        except ValueError:
            print("Wrong command")
            continue

    elif user_action.startswith('complete'):
        try:
            with open('todos.txt') as file:
                todos = file.readlines()
            index = int(user_action[9:])
            index = index - 1
            todos.pop(index)
            write_todos(todos)
        except IndexError:
            print("Out of range")
            continue
        except ValueError:
            print("Wrong command")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Wrong command.")

print('Bye')
