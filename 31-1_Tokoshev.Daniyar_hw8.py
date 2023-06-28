import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL)
''')

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("INSERT INTO countries (title) VALUES ('Россия')")
cursor.execute("INSERT INTO countries (title) VALUES ('США')")
cursor.execute("INSERT INTO countries (title) VALUES ('Франция')")

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Создание таблицы cities
cursor.execute('''
    CREATE TABLE cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Москва', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Нью-Йорк', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Париж', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Лондон', 4)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Токио', 5)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Пекин', 6)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Мельбурн', 7)")

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Алексей', 'Сидоров', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Елена', 'Петрова', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ольга', 'Смирнова', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Мария', 'Ковалева', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Андрей', 'Иванов', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Сергей', 'Сидоров', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Наталья', 'Петрова', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Олег', 'Смирнов', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Екатерина', 'Ковалева', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Анна', 'Иванова', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Виктор', 'Сидоров', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Александр', 'Петров', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Дмитрий', 'Смирнов', 1)")

conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

print(
    "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

for city in cities:
    print(city[0], city[1])

city_id = int(input("Введите id города: "))

if city_id == 0:
    print("Программа завершена.")
else:
    cursor.execute('''
        SELECT employees.first_name, employees.last_name, countries.title, cities.title, cities.area
        FROM employees
        INNER JOIN cities ON employees.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))

    employees = cursor.fetchall()

    for employee in employees:
        print("Имя:", employee[0])
        print("Фамилия:", employee[1])
        print("Страна:", employee[2])
        print("Город проживания:", employee[3])
        print("Площадь города:", employee[4])
        print()

conn.close()
