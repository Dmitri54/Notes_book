
def userConsole():
    printMenuTitle("Главное меню\n         Книга заметок")
    print("1 - Добавить \n2 - Редактировать \n3 - Вывод всех заметок \n4 - Поиск по ID" 
          " \n5 - Поиск по дате \n6 - Удалить \n7 - Выход")
    printEmtyLine()
    print("Выберите пункт")



def printMenuTitle(textMenu):
    print("==============================")
    print("        ", textMenu)
    print("==============================")

def printEmtyLine():
    print("==============================")