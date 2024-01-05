import tkinter as tk
from tkinter import ttk
import sqlite3

class Librarydb:
    def __init__(self, root):

        self.root = root
        self.root.title("Библиотека")

        #создание базы
        self.conn = sqlite3.connect('library.db')
        self.create_table()

        #создание интерфейса
        self.create_widgets()

        #отображение данных в интерфейсе
        self.refresh_books()
    def create_table(self):

        #создание таблицы если ее нет
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                year INTEGER
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        ttk.Label(self.root, text="Название книги:").grid(row=0, column=0, padx=5, pady=5)
        self.title_entry = ttk.Entry(self.root)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Автор:").grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = ttk.Entry(self.root)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Год издания:").grid(row=2, column=0, padx=5, pady=5)
        self.year_entry = ttk.Entry(self.root)
        self.year_entry.grid(row=2, column=1, padx=5, pady=5)

        #кнопки
        ttk.Button(self.root, text="Добавить книгу", command=self.add_book).grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Удалить книгу", command=self.delete_book).grid(row=4, column=0, columnspan=2, pady=10)
        ttk.Button(self.root, text="Обновить", command=self.refresh_books).grid(row=5, column=0, columnspan=2, pady=10)

        #таблица для отображения данных
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Название', 'Автор', 'Год'), show='headings')
        self.tree.grid(row=6, column=0, columnspan=3, pady=10)

        #установка заголовков столбцов
        self.tree.heading('ID', text='ID')
        self.tree.heading('Название', text='Название')
        self.tree.heading('Автор', text='Автор')
        self.tree.heading('Год', text='Год')

    def add_book(self):

        #добавление книги в базу данных
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()

        if title and author and year:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
            self.conn.commit()
            print("книга успешно добавлена в базу данных.")
            self.refresh_books()  #обновление данных в интерфейсе после добавления
        else:
            print("Пожалуйста, заполните все поля.")

    def delete_book(self):

        #удаление книги из базы данных
        selected_item = self.tree.selection()
        if selected_item:
            book_id = self.tree.item(selected_item, 'values')[0]
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
            self.conn.commit()
            print("книга успешно удалена.")
            self.refresh_books()  #обновление данных в интерфейсе после удаления
        else:
            print("выберите книгу для удаления.")
    def refresh_books(self):

        #отображение данных в интерфейсе
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

        #очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)

        #вставка новых данных
        for book in books:
            self.tree.insert('', 'end', values=book)


if __name__ == "__main__":
    root = tk.Tk()
    app = Librarydb(root)
    root.mainloop()
