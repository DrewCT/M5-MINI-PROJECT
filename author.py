class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
        self.__books = []

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def add_book(self, book):
        self.__books.append(book)

    def view_details(self):
        books_list = ', '.join([book.get_title() for book in self.__books])
        return f"Author: {self.__name}, Biography: {self.__biography}, Books: {books_list if self.__books else 'None'}"
    
    def view_details2(self):
        return f"Author: {self.__name}"