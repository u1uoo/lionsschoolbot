import aiosqlite

async def get_homeworks(login):
    async with aiosqlite.connect('..\my_database.db') as connection:
        data = await connection.execute('SELECT date, time, hometask FROM Users WHERE username = ?', (login,))
        rows = await data.fetchall()
        await connection.commit()
    return rows

async def add_homework(username,teachername,coursename,date,time,hometask):
    async with aiosqlite.connect('..\my_database.db') as connection:
        await connection.execute('INSERT INTO Users (username, teachername, course, date, time, hometask) VALUES (?, ?, ?, ?, ?, ?)',
                                        (username, teachername, coursename, date, time, hometask))
        await connection.commit()