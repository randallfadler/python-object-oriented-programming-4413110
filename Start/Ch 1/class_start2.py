# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties

    # TODO: create instance methods


# TODO: create some book instances
b1 = Book("War and Peace",  "Leo Tolstoy", 1225, 15.99)

b2 = Book("The Catcher in the Rye",  "J.D. Salinger", 272, 12.99)


# TODO: print the price of book1


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
