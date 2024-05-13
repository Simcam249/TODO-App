import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.Input(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")


window = sg.Window("My Todo App",
                   layout=[[label],[input_box,add_button,edit_button]],
                   font=("Halvetica",20))
while True:
    event,values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break



window.close()






