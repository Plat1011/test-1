class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration



library = BookCollection()
library.add_book(Book("1984", "Джордж Оруэлл"))
library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков"))
library.add_book(Book("Преступление и наказание", "Фёдор Достоевский"))

print("Книги в библиотеке:")
for book in library:
    print(f"  - {book}")