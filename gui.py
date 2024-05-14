import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.Input(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(),key="todos",
                      enable_events=True,size=(45,10))



window = sg.Window("My Todo App",
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=("Halvetica",20))
while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"] [0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"] [0])

        case sg.WIN_CLOSED:
            break




window.close()






