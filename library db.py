import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ur_pw",
            database="library_db"
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_to_db(self):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
            cursor.execute(query, (self.name, self.biography))
            conn.commit()
            cursor.close()
            conn.close()
            print("Author added successfully!")

    @staticmethod
    def display_authors():
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM authors")
            for (id, name, biography) in cursor.fetchall():
                print(f"ID: {id}, Name: {name}, Biography: {biography}")
            cursor.close()
            conn.close()

class Book:
    def __init__(self, title, author_id, publication_date, availability=True):
        self.title = title
        self.author_id = author_id
        self.publication_date = publication_date
        self.availability = availability

    def add_to_db(self):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author_id, publication_date, availability) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.title, self.author_id, self.publication_date, self.availability))
            conn.commit()
            cursor.close()
            conn.close()
            print("Book added successfully!")

    @staticmethod
    def display_books():
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            for (id, title, author_id, publication_date, availability) in cursor.fetchall():
                print(f"ID: {id}, Title: {title}, Author ID: {author_id}, Publication Date: {publication_date}, Available: {availability}")
            cursor.close()
            conn.close()

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    def add_to_db(self):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (self.name, self.library_id))
            conn.commit()
            cursor.close()
            conn.close()
            print("User added successfully!")

    @staticmethod
    def display_users():
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            for (id, name, library_id) in cursor.fetchall():
                print(f"ID: {id}, Name: {name}, Library ID: {library_id}")
            cursor.close()
            conn.close()

class BorrowedBook:
    def __init__(self, user_id, book_id, borrow_date, return_date=None):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def borrow_book(self):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.user_id, self.book_id, self.borrow_date, self.return_date))
            conn.commit()
            cursor.close()
            conn.close()
            print("Book borrowed successfully!")

    @staticmethod
    def return_book(book_id, return_date):
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL"
            cursor.execute(query, (return_date, book_id))
            conn.commit()
            cursor.close()
            conn.close()
            print("Book returned successfully!")


