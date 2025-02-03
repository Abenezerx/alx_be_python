class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size):
        self.fie_size = file_size
        super().__init__(title, author)

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        super().__init__(title, author)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.list_books:
            print(book)