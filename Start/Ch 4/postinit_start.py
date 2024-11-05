# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # __price_per_page: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__

    def __post_init_(self):
        self.description =  f"{self.title} by {self.author}, {self.pages} pages, ${self.price}"
        # self.__price_per_page = self.price / self.pages
        # print(f"Book {self.title} initialized with description: {self.description}")
        
# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

print (b1.description)
print (b2.description)
# print(b1.__price_per_page)


# TODO: use the description attribute
