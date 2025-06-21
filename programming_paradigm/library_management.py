class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library():
    """Library managment system"""
    def __init__(self):
        self._books = [] #Private list of books to be added here

    def add_book(self, book):
        """Adding book to the library"""
        self._books.append(book)        

    def check_out_book(self, title):
        """Check out books from the library"""
        for book in self._books:
            if not book._Book__is_checked_out:
                if  book.title == title:
                    book._Book__is_checked_out = True
                    return book
             
    def return_book(self, title):
        """Return a book to the library"""
        for book in self._books:
            if book.title == title:
                if book._Book__is_checked_out:
                    book._Book__is_checked_out = False
                    return book
        return None

    def list_available_books(self):
        """List all available books in the library"""
        for book in self._books:
            if not book._Book__is_checked_out:
                print(book)
