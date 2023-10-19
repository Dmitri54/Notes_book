import Controller.commands as com
import UI.userMenu as ui

def start():
    while True:
        ui.userConsole()
        user_input = input()
        if user_input == '1':
            com.addNote()
        elif user_input == '2':
           break 
        elif user_input == '3':
            com.showNote("all")
        elif user_input == '4':
            com.showNote("ID")
        elif user_input == '5':
            com.showNote("date")
        elif user_input == '6':
            com.showNote("all")
            com.delNote()
        else:
            print("Программа завершина")