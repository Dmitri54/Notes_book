import Models.Note
import Storage.loadFromFile as lF
import Storage.writeToFile as wF


def addNote():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Models.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Models.Note.Note.get_id(note) == Models.Note.Note.get_id(i):
            Models.Note.Note.set_id(node)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена")

def showNote(txt):
    return

def delNote():
    return

