# import sqlite3
#
# db = sqlite3.connect("lesson.db")
#
# cursor = db.cursor()
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS user(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# last_name TEXT,
# age INTEGER
# )
#
# ''')
#
# cursor.execute('''
# INSERT INTO user(name, last_name,age)
# VALUES
# ('Muhammadali','Solijonov','14'),
# ('Qodirjon','Axmadjonov','15')
# ''')
#
# name = input("Ismingizni kiriting:")
# last_name = input("FAmilyangizni kiriting:")
# age = int(input("yoshingizni kiriting"))
#
# cursor.execute('''
# INSERT INTO user(name,last_name,age)
# VALUES(?,?,?),(name, last_name,age)''')


#
# import sqlite3
#
# conn = sqlite3.connect("users.db")
# cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     zavod TEXT,
#     yili TEXT,
#     rangi TEXT
# )
# """)
#
# cursor.execute("""
# INSERT INTO user(model, zavod, yili, rangi)
# VALUES
# ('G Class', 'MERS', '2022', 'White'),
# ('Cls','Mers','2023','Black'),
# ('M5','BMW','2024','Red')
# """)
#
# conn.commit()


# git
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS zds(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT,
# last_name TEXT,
# age INTEGER
# )
#
# ''')
#
# cursor.execute('''
# INSERT INTO zds(name, last_name,age)
# VALUES
# ('Muhammadali','Solijonov','14'),
# ('Qodirjon','Axmadjonov','15')
# ''')
#
# db.commit(db.close()

print("Alpha")
print("off_zds")
print("Game over")
print("+998886871020")