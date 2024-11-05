# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__


# TODO: comparing two dataclasses - they implement __eq__


# TODO: change some fields
b1.title = "Anna Karenia"
b1.pages = 1234
print(b1.bookinfo())
# print (b2 == b3)
# print (b1 == b2)
