import BD

sqllite_trucate_bd = """delete from personal"""

trucate = BD.cursor.execute(sqllite_trucate_bd)
print("Таблица personal очищена")

sqllite_insert_query = """INSERT INTO personal(id, name,last_name,position,salary,bonus)
                  VALUES
                  (1, "Олег", "Фролов", "Аналитик", 10000, 2000),
                  (2, "Иван", "Иванов", "Главный инженер", 50000, 10000),
                  (3, "Игорь", "Семенов", "Инженер", 20000, 8000),
                  (4, "Олег", "Петров", "Завхоз", 12000, 3000)
                  """

try:
    insert = BD.cursor.execute(sqllite_insert_query)
    BD.bd.commit()
    print("Записи успешно вставлены")
except:
    print("Данные уже есть")