import PySimpleGUI as sg
from fns import get_todos, write_todos

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter TODO", key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window(title="My ToDo App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todos = get_todos()
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                index = todos.index(todo_to_edit)
                todos[index] = new_todo +'\n'
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select item first")
        case 'todos':
            print(values)
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
