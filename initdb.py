import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )
    ''')
pervy_knigi = [
    ('Книга 1', 'Автор 1', 2000),
    ('Книга 2', 'Автор 2', 1999),
    ('Книга 3', 'Автор 3', 1998),
    ('Книга 4', 'Автор 4', 1997),
    ('Книга 5', 'Автор 5', 1996),
    ('Книга 6', 'Автор 6', 1995),
    ('Книга 7', 'Автор 7', 1994),
    ('Книга 8', 'Автор 8', 1993),
    ('Книга 9', 'Автор 9', 1992),
    ('Книга 10', 'Автор 10', 1991),
]

cursor.executemany('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', pervy_knigi)
conn.commit()
conn.close()

print("начальные данные успешно добавлены в базу данных.")
