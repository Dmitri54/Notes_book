
import Controller.controller as con


con.start()



# Задание
# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и 
# удалением заметок. 
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. 
# Сохранение заметок необходимо сделать в формате json или csv формат 
# (разделение полей рекомендуется делать через точку с запятой). 
# Реализацию пользовательского интерфейса студент может делать как ему удобнее, 
# можно делать как параметры запуска программы (команда, данные), 
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

# Решение
# 1) создам меню и сделаю вывод меню в консоль - DONE
# 2) создам класс Заметка, опешу его. Опешу функции Книги заметок
# Работа с фаилом txt (чтение, запись)
#