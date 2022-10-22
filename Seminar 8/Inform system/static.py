import BD

def stat_record():
    BD.cursor.execute('SELECT count(*) as cnt, max(salary) as max_sal, min(salary) as min_sal, avg(salary) as avg_sal FROM PERSONAL;')
    for one in BD.cursor.fetchmany():
        print(f'Кол-ва записей в таблице = {one[0]}, Максимальная зарплата = {one[1]}, Минимальная зарплата = {one[2]}, Средняя зарплата = {one[3]}')
