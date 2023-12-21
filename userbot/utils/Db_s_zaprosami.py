import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
teachername TEXT NOT NULL,
course TEXT NOT NULL,
date INTEGER,
time TEXT NOT NULL,
hometask TEXT NOT NULL
)
""")

newuser  = str(input())
newtime  = int(input())
newdate  = int(input())
hometask = str(input())
teachername = 'Lev'
course = 'EGA'
name_user = 'rigoriig'

#Как я предалагю хранить данные. С именами думаю понятно. Дата имеется ввиду день число месяца. Как вариант можем дописать еще хранение месяцав , но думаю, что больше чем на месяц планировать бессмысленно
#время занятие предлагаю хранитиь как четырехзначное число в строке первые две цифры часы вторые минуты.

# Пример добавления ученика 
cursor.execute('INSERT INTO Users (username, teachername, course, date, time, hometask) VALUES (?, ?, ?, ?, ?, ?)', (newuser, teachername, 'ega', newdate, newtime, hometask))
# Запрос на изменение даты и времени занятий 
# cursor.execute('UPDATE Users SET date = ?, time = ? WHERE username = ?', (newdate, newtime, newuser))
# Добавление домашки
# cursor.execute('UPDATE Users SET hometask = ? WHERE username = ?', (hometask, newuser))
# Cмена препа 
# newteacher = ' '
# cursor.execute('UPDATE Users SET teachername = ? WHERE username = ?', (newteacher, newuser))

#запрос преподавателем своего расписания на неделю 
# cursor.execute('SELECT username, date, time, teachername FROM Users  GROUP BY date HAVING teachername = ? ORDER BY time', (teachername,))
# results = cursor.fetchall()
# print
# for row in results:
#   print(row)

#Запрос пользователем даты времени и домашки/ 
# cursor.execute('SELECT hometask FROM Users WHERE username = ?', (name_user,))
# results = cursor.fetchall()

# for row in results:
#   print(row)

# #Удаление пользователя 
# deleteuser = ' '
# cursor.execute('DELETE FROM Users WHERE username = ?', (deleteuser,))


# # Сохраняем изменения и закрываем соединение
connection.commit()
# connection.close()