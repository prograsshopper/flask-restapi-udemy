import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# auto-increment 컬럼을 만들려면 int 가 아니라 반드시 INTEGER라고 명시해야함
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # real : Decimal
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()
connection.close()