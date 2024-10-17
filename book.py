class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = True  

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def borrow_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True

    def display_details(self):
        availability = "Available" if self.__available else "Borrowed"
        return f"{self.__title} by {self.__author}, Genre: {self.__genre}, Published: {self.__publication_date}, Status: {availability}"
    