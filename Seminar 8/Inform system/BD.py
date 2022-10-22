import sqlite3
import delete_record
import add_record
import find_record
import preview_record
import update_record
import static
import more_salary


bd = sqlite3.connect("Data_base.db")

cursor = bd.cursor()

print("Подключен к SQLite3")

cursor.execute('''CREATE TABLE IF NOT EXISTS personal (
    id int primary key,
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT
    ) ''')

print("Таблица personal создана")



def inpute_choice():
    while True:
        print('Что желаем сделать:\n\
1 - посмотреть базу\n\
2 - добавить запись\n\
3 - удалить запись по фамилии и имени \n\
4 - Найти запись по ID \n\
5 - Изменить зарплату  \n\
6 - Посмотреть сотрудников, у кого зарплата выше указанной  \n\
7 - Вывести статистику по таблице  \n\
8 - выход')
        user_choise = input("Введите цифру: ")
        if int(user_choise) == 1:
            preview_record.preview_record()
        elif int(user_choise) == 2:
            add_record.add_record()
        elif int(user_choise) == 3:
            delete_record.del_record()
        elif int(user_choise) == 4:
            find_record.find_record()
        elif int(user_choise) == 5:
            update_record.update_record()
        elif int(user_choise) == 6:
            more_salary.more_salary()
        elif int(user_choise) == 7:
            static.stat_record()
        elif int(user_choise) == 8:
            print('Выход')
            break
        else:
            print('Не верно введен режим работы')

